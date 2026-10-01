"""
Scene bank for the pallowyn (Halloween/Spooky Seasonal) video pipeline.
Follows PALLOWYN_VIDEO_STYLE.md exactly -- cozy-spooky/whimsical, NOT
horror. Uses Higgsfield Soul v2 for the still + Minimax Hailuo 2.3
image-to-video for the animate step, same as creepvale/dark-fantasy.

Third revision (2026-10-01), two changes based on direct feedback that
the videos "look like a still image with a tiny bit of flame movement"
and that posts "keep almost repeating themselves":

  1. Hailuo 2.3 has NO structural camera_fixed parameter -- camera
     behavior is driven entirely by animate_prompt wording. Every scene
     previously said "camera completely locked... no camera movement
     whatsoever", which directly told the model to barely move. That
     phrasing is gone -- every animate_prompt below now asks for a real,
     deliberate camera move (push-in, pull-back, pan, tilt, orbit, or
     dolly), varied scene to scene.
  2. Bank grew from 12 to 16 scenes to stretch the rotation cycle at 3
     posts/day from 4 days to a bit over 5, and the 4 new scenes add
     settings (a candy shop window, a hayride wagon, a front-porch
     greeter, a corn maze entrance) distinct from the existing
     porch/patch/graveyard set for more variety within the cycle.
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
        "animate_prompt": "Bring this image to life with a slow pan right "
            "along the row of jack-o'-lanterns, one face passing into "
            "view after another. Candle flicker moves inside each one, "
            "the bat-shaped string lights blink. Cozy spooky Halloween "
            "atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow push-in "
            "toward the witch and her cat, the pumpkin patch spreading "
            "wider at the edges of frame as the camera closes in. Her "
            "cloak sways, her pumpkin lantern swings, mist drifts. Cozy "
            "spooky Halloween atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow rising "
            "camera movement, craning up from the line of jack-o'-"
            "lanterns on the path to the glowing attic window. Window "
            "light flickers, the tire swing sways, mist drifts across the "
            "hill. Cozy spooky Halloween atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow pan left, "
            "following the uneven line of trick-or-treaters down the "
            "lane. Fallen leaves drift across the lane, the paper bats "
            "flutter. Cozy spooky Halloween atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow pull-back, "
            "widening from the cat to reveal the full moon rising behind "
            "it. The cat's tail flicks, its ear twitches once, mist "
            "drifts. Cozy spooky Halloween atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow dolly "
            "forward through the pumpkin patch toward the scarecrow. Its "
            "straw sleeves and the nearby vines sway, the crow shifts its "
            "wings once. Cozy spooky Halloween atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow push-in "
            "through the gate toward the 'MR. WHISKERS' tombstone. Candle "
            "lanterns flicker, the paper skeleton sways, mist drifts "
            "between the tombstones. Cozy spooky Halloween atmosphere, "
            "no text",
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
        "animate_prompt": "Bring this image to life with a slow tilt down "
            "from the string lights overhead to the table of carving "
            "pumpkins. String lights and candle flames flicker, steam "
            "rises from a nearby mug of cider. Cozy spooky Halloween "
            "atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow orbital "
            "drift to the right around the owl's branch. Its feathers "
            "ruffle, the bats continue their line across the moon, fog "
            "drifts below. Cozy spooky Halloween atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow push-in "
            "on the ghost figure at the door. The sheet billows, the "
            "porch light flickers, the ribbon wreath sways. Cozy spooky "
            "Halloween atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow pan left "
            "across the barn's front, from the wheelbarrow of pumpkins to "
            "the glowing loft window. The lantern flickers, cobwebs sway. "
            "Cozy spooky Halloween atmosphere, no text",
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
        "animate_prompt": "Bring this image to life with a slow pull-back "
            "from the bonfire, widening to reveal the full circle of "
            "figures. Flames flicker, sparks drift upward, the "
            "marshmallow glows faintly. Cozy spooky Halloween atmosphere, "
            "no text",
    },
    {
        "title": "candy shop window",
        "has_people": False,
        "still_prompt": "A cozy small-town candy shop window at night, "
            "displays packed with jars of candy corn, chocolate "
            "skeletons, and caramel apples wrapped in orange cellophane, "
            "a hand-painted 'TRICK OR TREAT' banner strung across the top "
            "of the glass, a cardboard black cat cutout taped crookedly "
            "inside, warm golden light spilling out onto the sidewalk, "
            "a small pile of fallen leaves swept against the shop's "
            "doorstep, deep purple-blue autumn night sky reflected faintly "
            "in the glass, whimsical dark-fantasy illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Bring this image to life with a slow push-in "
            "through the shop window toward the jars of candy. The "
            "banner stirs faintly, the warm light flickers gently, "
            "reflections shift in the glass. Cozy spooky Halloween "
            "atmosphere, no text",
    },
    {
        "title": "hayride wagon",
        "has_people": True,
        "still_prompt": "A wooden hayride wagon piled high with loose hay "
            "and pulled by a sturdy silhouetted draft horse, small "
            "costumed passengers sitting along the wagon's edges with "
            "legs dangling, a string of pumpkin-shaped lanterns strung "
            "along the wagon's rails, rolling farmland and a distant "
            "corn maze visible under a deep purple-blue autumn sky, a "
            "trail of loose hay wisps drifting off the back of the wagon, "
            "whimsical dark-fantasy illustration style, wide cinematic "
            "composition, 9:16 vertical, highly detailed, no text, no "
            "watermark",
        "animate_prompt": "Bring this image to life with a slow pan "
            "right, following the wagon as it moves across the farmland. "
            "The pumpkin lanterns swing gently, loose hay wisps drift off "
            "the back, the horse's mane shifts. Cozy spooky Halloween "
            "atmosphere, no text",
    },
    {
        "title": "front-porch greeter",
        "has_people": True,
        "still_prompt": "A life-sized animatronic-style skeleton dressed "
            "in a tophat and bowtie, propped jauntily in a rocking chair "
            "on a decorated front porch, one bony hand raised mid-wave, "
            "a bowl of candy balanced on its lap, jack-o'-lanterns lining "
            "the porch steps below, orange string lights looping along "
            "the railing, a small 'HAPPY HALLOWEEN' bunting sagging "
            "slightly in the middle, deep purple-blue autumn night sky "
            "behind, whimsical dark-fantasy illustration style, wide "
            "cinematic composition, 9:16 vertical, highly detailed, no "
            "text, no watermark",
        "animate_prompt": "Bring this image to life with a slow tilt up "
            "from the jack-o'-lanterns on the steps to the skeleton in "
            "the rocking chair. The chair rocks almost imperceptibly, the "
            "string lights blink, the bunting sways. Cozy spooky "
            "Halloween atmosphere, no text",
    },
    {
        "title": "corn maze entrance",
        "has_people": False,
        "still_prompt": "The entrance to a tall corn maze at dusk, a "
            "rustic wooden archway with a hand-painted sign reading "
            "'MAZE' hanging slightly crooked, two carved pumpkins "
            "flanking the entrance path, rows of dried cornstalks "
            "towering on either side disappearing into deep shadow, a "
            "scarecrow positioned just inside the entrance keeping watch, "
            "warm string lights looped along the archway, deep "
            "purple-blue autumn sky fading behind the stalks, whimsical "
            "dark-fantasy illustration style, wide cinematic composition, "
            "9:16 vertical, highly detailed, no text, no watermark",
        "animate_prompt": "Bring this image to life with a slow dolly "
            "forward through the archway into the maze entrance. The "
            "cornstalks rustle faintly, the string lights flicker, the "
            "scarecrow's sleeve stirs. Cozy spooky Halloween atmosphere, "
            "no text",
    },
]
