"""
Scene bank for the pallowyn (Halloween/Spooky Seasonal) video pipeline.
Follows PALLOWYN_VIDEO_STYLE.md exactly -- cozy-spooky/whimsical, NOT
horror. 12 scenes, alternating has_people true/false 6/6 (same pattern
as dark-fantasy's scene_bank.py).
"""

SCENES = [
    {
        "title": "porch jack-o-lanterns",
        "has_people": False,
        "still_prompt": "A row of glowing carved jack-o'-lanterns lining a "
            "wooden porch step, warm candlelight flickering from within each "
            "one, small pumpkins and gourds scattered around, string lights "
            "overhead, deep purple-blue autumn night sky, drifting mist, "
            "whimsical dark-fantasy illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "candle flicker inside each jack-o'-lantern moves gently, cozy "
            "spooky Halloween atmosphere, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "lone witch silhouette",
        "has_people": True,
        "still_prompt": "A whimsical witch in a pointed hat and flowing cloak "
            "standing at the edge of a misty pumpkin patch, back turned to "
            "camera, warm jack-o'-lantern light glowing nearby, deep "
            "purple-blue autumn night sky, drifting mist, whimsical "
            "dark-fantasy illustration style, wide cinematic composition, "
            "9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "witch's cloak sways gently and mist drifts slowly, cozy spooky "
            "Halloween atmosphere, subtle ambient motion only, no camera "
            "movement, no zoom, no pan",
    },
    {
        "title": "haunted house on the hill",
        "has_people": False,
        "still_prompt": "A charming old Victorian house on a hill at night, "
            "warm orange light glowing from its windows, twisted bare trees "
            "framing it, a few jack-o'-lanterns lining the path up to the "
            "door, deep purple-blue autumn night sky, drifting mist, "
            "whimsical dark-fantasy illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "window light flickers softly and mist drifts across the hill, "
            "cozy spooky Halloween atmosphere, subtle ambient motion only, "
            "no camera movement, no zoom, no pan",
    },
    {
        "title": "trick-or-treaters on the lane",
        "has_people": True,
        "still_prompt": "A group of small trick-or-treaters in costume "
            "silhouettes walking down a leaf-covered lane at dusk, carrying "
            "glowing jack-o'-lantern buckets, warm porch lights glowing in "
            "the distance, deep purple-blue autumn sky, drifting mist, "
            "whimsical dark-fantasy illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only fallen "
            "leaves drift gently across the lane, cozy spooky Halloween "
            "atmosphere, subtle ambient motion only, no camera movement, no "
            "zoom, no pan",
    },
    {
        "title": "black cat on a fence",
        "has_people": False,
        "still_prompt": "A black cat with glowing amber eyes perched on an "
            "old wooden fence, a full moon rising behind it, pumpkins and "
            "cobwebs nearby, deep purple-blue autumn night sky, drifting "
            "mist, whimsical dark-fantasy illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "cat's tail flicks slowly and mist drifts behind it, cozy "
            "spooky Halloween atmosphere, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "pumpkin patch at dusk",
        "has_people": True,
        "still_prompt": "A whimsical scarecrow figure standing amid a "
            "sprawling pumpkin patch at dusk, warm amber sky fading to deep "
            "purple, rows of glowing jack-o'-lanterns scattered through the "
            "field, whimsical dark-fantasy illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "scarecrow's straw and nearby vines sway gently in the breeze, "
            "cozy spooky Halloween atmosphere, subtle ambient motion only, "
            "no camera movement, no zoom, no pan",
    },
    {
        "title": "candlelit graveyard gate",
        "has_people": False,
        "still_prompt": "An old wrought-iron cemetery gate draped in "
            "cobwebs, rows of whimsical tombstones beyond it lit by small "
            "candle lanterns, twisted bare trees overhead, deep purple-blue "
            "autumn night sky, drifting mist, whimsical dark-fantasy "
            "illustration style, wide cinematic composition, 9:16 vertical, "
            "highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "candle lanterns flicker and mist drifts between the "
            "tombstones, cozy spooky Halloween atmosphere, subtle ambient "
            "motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "children carving pumpkins",
        "has_people": True,
        "still_prompt": "Silhouettes of a family gathered around a table "
            "carving jack-o'-lanterns on a porch at night, warm string "
            "lights overhead, finished pumpkins glowing nearby, deep "
            "purple-blue autumn night sky, whimsical dark-fantasy "
            "illustration style, wide cinematic composition, 9:16 vertical, "
            "highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "string lights and candle flames flicker gently, cozy spooky "
            "Halloween atmosphere, subtle ambient motion only, no camera "
            "movement, no zoom, no pan",
    },
    {
        "title": "owl on a twisted branch",
        "has_people": False,
        "still_prompt": "A large owl perched on a gnarled, twisted tree "
            "branch silhouetted against a giant orange full moon, wisps of "
            "fog below, deep purple-blue autumn night sky, whimsical "
            "dark-fantasy illustration style, wide cinematic composition, "
            "9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "owl's feathers ruffle slightly and fog drifts below, cozy "
            "spooky Halloween atmosphere, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "costumed figure at the door",
        "has_people": True,
        "still_prompt": "A whimsical costumed figure -- a friendly ghost "
            "draped in a flowing white sheet -- standing at a warmly lit "
            "front door decorated with cobwebs and pumpkins, deep "
            "purple-blue autumn night sky behind, whimsical dark-fantasy "
            "illustration style, wide cinematic composition, 9:16 vertical, "
            "highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "ghost's sheet billows gently and the porch light flickers, "
            "cozy spooky Halloween atmosphere, subtle ambient motion only, "
            "no camera movement, no zoom, no pan",
    },
    {
        "title": "cobweb covered barn",
        "has_people": False,
        "still_prompt": "An old wooden barn draped in thick cobwebs, a "
            "single lantern glowing in the loft window, pumpkins stacked "
            "outside the door, deep purple-blue autumn night sky, drifting "
            "mist, whimsical dark-fantasy illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "lantern flickers and cobwebs sway faintly in the breeze, cozy "
            "spooky Halloween atmosphere, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "bonfire gathering",
        "has_people": True,
        "still_prompt": "Silhouetted figures in costume gathered around a "
            "crackling bonfire in a field at night, jack-o'-lanterns lined "
            "up nearby, sparks rising into the deep purple-blue autumn sky, "
            "whimsical dark-fantasy illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "bonfire flames flicker and sparks drift upward, cozy spooky "
            "Halloween atmosphere, subtle ambient motion only, no camera "
            "movement, no zoom, no pan",
    },
]
