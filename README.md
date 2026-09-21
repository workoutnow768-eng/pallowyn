# pallowyn

Fully autonomous daily video pipeline for the @pallowyn Halloween/Spooky
Seasonal account. Sister repo to dark-fantasy, creepvale, chromeage,
voidcrete and vaporune -- same architecture (Higgsfield still -> Minimax
Hailuo 2.3 animate -> ffmpeg music mux -> Buffer GraphQL schedule), but a
cozy-spooky Halloween visual identity. See PALLOWYN_VIDEO_STYLE.md for
the full style lock.

## What one run does

1. Generate (scripts/main.py generate): picks the next scene(s) from
   scripts/scene_bank.py's rotation, for each one:
   - generates a still image (Higgsfield Soul v2, 1080p, 9:16)
   - animates it into a 6s silent video (Minimax Hailuo 2.3)
   - downloads the music track and detects its real duration via ffprobe
   - mixes in the music (ffmpeg, fading in/out, stepping through the
     track so consecutive posts don't reuse the same slice)
   - writes a manifest of the finished .mp4 paths + scheduled times
2. Commit + push those .mp4 files (Buffer needs a public URL to fetch
   from).
3. Schedule (scripts/main.py schedule): reads the manifest, creates
   one Buffer post per video per channel, then updates the rotation state
   and removes the manifest.

Runs daily at 17:23 UTC via the scheduled workflow, or on demand from the
Actions tab.

## One-time setup checklist

- [x] Repo is public (required for raw.githubusercontent.com fetches)
- [x] HIGGSFIELD_API_KEY secret set
- [x] MUSIC_TRACK_URL secret set (Carnival of the Macabre.mp3)
- [x] BUFFER_API secret set
- [ ] Confirm Instagram/YouTube channels are connected in Buffer if used
- [ ] Test with a manual run from the Actions tab before relying on the
      schedule

## Rotation state

state/pallowyn_state.json tracks which scene is next
(last_scene_index), the next open posting slot (scheduled_up_to), and
where in the music track the next mux should start
(music_offset_seconds). The bot owns these fields -- don't hand-edit
them while the scheduled workflow is active.

posts_per_day starts at 1 for the first test run (same testing process
dark-fantasy went through) -- bump to 3 once a run succeeds end-to-end.
