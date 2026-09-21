"""
Muxes the page's music track onto a silent generated video with ffmpeg.
Same pattern as dark-fantasy's mux_audio.py, but the track's real duration
is detected at runtime via ffprobe instead of being hardcoded -- this repo
doesn't know "Carnival of the Macabre.mp3"'s exact length ahead of time.

Requires `ffmpeg` and `ffprobe` on PATH (installed via apt in the workflow).
"""
import os
import json
import subprocess

CLIP_DURATION_SECONDS = 6.0  # matches Hailuo 2.3's duration=6 setting
FADE_SECONDS = 0.5


def get_audio_duration(audio_path):
    """Returns the audio file's duration in seconds via ffprobe."""
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", audio_path,
    ]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return float(result.stdout.strip())


def mux(video_path, audio_path, offset_seconds, out_path):
    """
    Cuts a CLIP_DURATION_SECONDS window out of audio_path starting at
    offset_seconds, fades it in/out, and muxes it onto video_path (video
    stream copied, not re-encoded).
    """
    fade_out_start = CLIP_DURATION_SECONDS - FADE_SECONDS
    filter_complex = (
        f"[1:a]afade=t=in:st=0:d={FADE_SECONDS},"
        f"afade=t=out:st={fade_out_start}:d={FADE_SECONDS}[a]"
    )
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-ss", str(offset_seconds), "-t", str(CLIP_DURATION_SECONDS), "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "0:v", "-map", "[a]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        out_path,
    ]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    return out_path


def next_offset(state, track_duration_seconds):
    """
    Steps the music offset forward by one clip length each run so
    consecutive posts don't reuse the exact same slice of the track, and
    wraps back to 0 once the track runs out.
    """
    offset = state.get("music_offset_seconds", 0.0)
    if offset + CLIP_DURATION_SECONDS >= track_duration_seconds:
        offset = 0.0
    return offset
