# Game designed for troubleshooting inconvenient rollback behavior associated with a CDS.

default MainChar = _("Protagonist!")
default SomeGuy = _("Some Guy")
default SomeChar = _("A Character")

define S = Character("[SomeGuy]", color="007FA4", image="someguy")
define C = Character("[SomeChar]", color="FF3974", image="somechar")
define MC = Character("[MainChar]", color="219D56", image="mc")

define tall_tags = []
define mid_tags = ["someguy"]
define small_tags = ["somechar"]

label start:

    scene outside

    "This game was made to test some weird rollback behavior."
    show someguy at right
    show somechar at closeleft
    S "Watch me have an idea."
    fx idea
    S "Check that out. Easy to type."
    "However, if you rollback one line from here, the idea WILL attempt escape. Fix it by rolling back two."
    fx dots
    C "You hate to see it..."
    "Rolling back one line from here will do the same thing to the dots. Rolling back TWO lines won't stop them, either."
    fx sparkle
    MC "This can't happen to me because I live in the textbox. :)"
    "Thank you for playing!"

    return
