"""
Scene bank for the pallowyn (Halloween/Spooky Seasonal) video pipeline.
Follows PALLOWYN_VIDEO_STYLE.md exactly -- cozy-spooky/whimsical, NOT
horror. 12 scenes, alternating has_people true/false 6/6 (same pattern
as dark-fantasy's scene_bank.py).

Rewritten with specific, named props and small narrative details in each
scene (not just generic "pumpkins and cobwebs") so every image reads as
a distinct, thought-out moment instead of an interchangeable template.
"""

SCENES = [
    {
        "title": "porch jack-o-lanterns",
        "has_people": False,
        "still_prompt": "A row of seven carved jack-o'-lanterns of "
            "different sizes lining a weathered wooden porch step, each "
            "with a different hand-carved face -- one toothy grin, one "
            "surprised O mouth, one lopsided wink -- warm candlelight "
            "flickering from within each, a wicker basket of small gourds "
            "and one striped candy corn spilling out beside them, string "
            "lights with tiny bat-shaped bulbs overhead, a hand-painted "
            "wooden sign reading 'BOO' leaning against the railing, deep "
            "purple-blue autumn night sky, drifting mist, whimsical "
            "dark-fantasy illustration style, wide cinematic composition, "
            "9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "candle flicker inside each jack-o'-lantern moves gently and "
            "the bat-shaped string lights blink faintly, cozy spooky "
            "Halloween atmosphere, subtle ambient motion only, no camera "
            "movement, no zoom, no pan",
    },
    {
        "title": "lone witch silhouette",
        "has_people": True,
        "still_prompt": "A whimsical witch in a patched pointed hat and a "
            "flowing cloak with a crooked broom slung over one shoulder, "
            "standing at the edge of a misty pumpkin patch with her black "
            "cat sitting at her feet, back turned to camera, a lantern "
            "made from a small hollowed pumpkin swinging from her free "
            "hand, warm jack-o'-lantern light glowing nearby, deep "
            "purple-blue autumn night sky, drifting mist, whimsical "
            "dark-fantasy illustration style, wide cinematic composition, "
            "9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "witch's cloak sways gently, her pumpkin lantern swings faintly, "
            "and mist drifts slowly across the patch, cozy spooky Halloween "
            "atmosphere, subtle ambient motion only, no camera movement, no "
            "zoom, no pan",
    },
    {
        "title": "haunted house on the hill",
        "has_people": False,
        "still_prompt": "A charming lopsided Victorian house on a hill at "
            "night, one shutter hanging slightly askew, warm orange light "
            "glowing from its round attic window and two front windows, "
            "twisted bare trees framing it with a tire swing hanging from "
            "one branch, a crooked line of nine jack-o'-lanterns of "
            "shrinking size lining the path up to the door, a broomstick "
            "leaning by the entrance, deep purple-blue autumn night sky, "
            "drifting mist, whimsical dark-fantasy illustration style, "
            "wide cinematic composition, 9:16 vertical, highly detailed, "
            "no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "window light flickers softly, the tire swing sways slightly "
            "in the breeze, and mist drifts across the hill, cozy spooky "
            "Halloween atmosphere, subtle ambient motion only, no camera "
            "movement, no zoom, no pan",
    },
    {
        "title": "trick-or-treaters on the lane",
        "has_people": True,
        "still_prompt": "A group of five small trick-or-treaters in "
            "costume silhouettes -- one with a pointed dinosaur tail, one "
            "carrying a glowing jack-o'-lantern bucket shaped like a cat, "
            "one dragging a cape that's a little too long -- walking down "
            "a leaf-covered lane at dusk in a loose uneven line, a string "
            "of paper bat decorations taped to a nearby mailbox, warm "
            "porch lights glowing in the distance, deep purple-blue "
            "autumn sky, drifting mist, whimsical dark-fantasy "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only "
            "fallen leaves drift gently across the lane and the paper bat "
            "decorations flutter slightly, cozy spooky Halloween "
            "atmosphere, subtle ambient motion only, no camera movement, "
            "no zoom, no pan",
    },
    {
        "title": "black cat on a fence",
        "has_people": False,
        "still_prompt": "A slender black cat with glowing amber eyes and "
            "one notched ear perched on an old leaning wooden fence post, "
            "its tail curled around a small carved pumpkin balanced beside "
            "it, a full moon rising behind it wreathed in wispy cloud, "
            "a scatter of fallen leaves and one abandoned trick-or-treat "
            "bag caught in the fence slats, cobwebs strung between the "
            "posts, deep purple-blue autumn night sky, drifting mist, "
            "whimsical dark-fantasy illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "cat's tail flicks slowly, its ear twitches once, and mist "
            "drifts behind it, cozy spooky Halloween atmosphere, subtle "
            "ambient motion only, no camera movement, no zoom, no pan",
    },
    {
        "title": "pumpkin patch at dusk",
        "has_people": True,
        "still_prompt": "A whimsical scarecrow in a patchwork flannel "
            "shirt and a straw hat with one button eye slightly higher "
            "than the other, standing on a single wooden post amid a "
            "sprawling pumpkin patch at dusk, a crow perched on its "
            "outstretched arm, warm amber sky fading to deep purple, rows "
            "of glowing jack-o'-lanterns of every size scattered through "
            "the field with one giant prize pumpkin left uncarved in the "
            "foreground, whimsical dark-fantasy illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "scarecrow's straw sleeves and the nearby vines sway gently in "
            "the breeze and the crow shifts its wings once, cozy spooky "
            "Halloween atmosphere, subtle ambient motion only, no camera "
            "movement, no zoom, no pan",
    },
    {
        "title": "candlelit graveyard gate",
        "has_people": False,
        "still_prompt": "An old wrought-iron cemetery gate draped in thick "
            "cobwebs with one gate hinge creaked slightly open, rows of "
            "whimsical rounded tombstones beyond it -- one reading 'R.I.P. "
            "MR. WHISKERS' with a small paw print carved below it -- each "
            "lit by a small candle lantern hung on a bent iron hook, "
            "twisted bare trees overhead with a paper skeleton decoration "
            "hanging from one branch, deep purple-blue autumn night sky, "
            "drifting mist, whimsical dark-fantasy illustration style, "
            "wide cinematic composition, 9:16 vertical, highly detailed, "
            "no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "candle lanterns flicker, the paper skeleton sways slightly, "
            "and mist drifts between the tombstones, cozy spooky Halloween "
            "atmosphere, subtle ambient motion only, no camera movement, "
            "no zoom, no pan",
    },
    {
        "title": "children carving pumpkins",
        "has_people": True,
        "still_prompt": "Silhouettes of a family of four gathered around a "
            "newspaper-covered table carving jack-o'-lanterns on a porch "
            "at night, pumpkin seeds and scraped-out pulp piled in a "
            "metal bowl, one small silhouette proudly holding up a "
            "finished carving with a crooked triangle nose, warm string "
            "lights overhead with a few bulbs burned out, finished "
            "pumpkins glowing in a row along the railing, deep "
            "purple-blue autumn night sky, whimsical dark-fantasy "
            "illustration style, wide cinematic composition, 9:16 "
            "vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "string lights and candle flames flicker gently and steam "
            "rises faintly from a nearby mug of cider, cozy spooky "
            "Halloween atmosphere, subtle ambient motion only, no camera "
            "movement, no zoom, no pan",
    },
    {
        "title": "owl on a twisted branch",
        "has_people": False,
        "still_prompt": "A large round-eyed owl with speckled feathers "
            "perched on a gnarled, twisted tree branch, one talon gripping "
            "a small carved pumpkin left wedged in the bark below it, "
            "silhouetted against a giant orange full moon crossed by a "
            "single line of migrating bats, wisps of fog below tangled "
            "around exposed roots, deep purple-blue autumn night sky, "
            "whimsical dark-fantasy illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "owl's feathers ruffle slightly, the distant bats continue "
            "their line across the moon, and fog drifts below, cozy "
            "spooky Halloween atmosphere, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "costumed figure at the door",
        "has_people": True,
        "still_prompt": "A whimsical costumed figure -- a friendly ghost "
            "draped in a flowing white sheet with two crooked eye holes cut "
            "slightly uneven -- standing at a warmly lit front door "
            "decorated with cobwebs, a wreath of black and orange ribbon, "
            "and a carved pumpkin on the welcome mat, a bowl of candy left "
            "on the porch rail with a hand-written note propped against it, "
            "deep purple-blue autumn night sky behind, whimsical "
            "dark-fantasy illustration style, wide cinematic composition, "
            "9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "ghost's sheet billows gently, the porch light flickers, and "
            "the ribbon wreath sways faintly, cozy spooky Halloween "
            "atmosphere, subtle ambient motion only, no camera movement, "
            "no zoom, no pan",
    },
    {
        "title": "cobweb covered barn",
        "has_people": False,
        "still_prompt": "An old wooden barn with a faded painted star on "
            "its door, draped in thick cobwebs strung between the eaves, "
            "a single lantern glowing in the loft window where a scarecrow "
            "prop is slumped against the sill, pumpkins stacked in a "
            "wheelbarrow just outside the door, a hand-lettered sign "
            "reading 'HAYRIDE' nailed crookedly to a post, deep "
            "purple-blue autumn night sky, drifting mist, whimsical "
            "dark-fantasy illustration style, wide cinematic composition, "
            "9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "lantern flickers and cobwebs sway faintly in the breeze, cozy "
            "spooky Halloween atmosphere, subtle ambient motion only, no "
            "camera movement, no zoom, no pan",
    },
    {
        "title": "bonfire gathering",
        "has_people": True,
        "still_prompt": "Silhouetted figures in costume -- one in a "
            "pointed witch hat, one wearing plastic vampire fangs visible "
            "in profile, one holding a long roasting stick with a "
            "marshmallow on the end -- gathered around a crackling bonfire "
            "in a field at night, a row of jack-o'-lanterns lined up on "
            "a nearby hay bale, a cooler and folded lawn chairs just "
            "outside the firelight, sparks rising into the deep "
            "purple-blue autumn sky, whimsical dark-fantasy illustration "
            "style, wide cinematic composition, 9:16 vertical, highly "
            "detailed, no text, no watermark",
        "animate_prompt": "Camera completely locked and static, only the "
            "bonfire flames flicker, sparks drift upward, and the "
            "marshmallow on the stick glows faintly, cozy spooky Halloween "
            "atmosphere, subtle ambient motion only, no camera movement, "
            "no zoom, no pan",
    },
]
