
# Transforms for positioning fx. Problem occurs at both default portrait positions
# like left/right and my own custom ones, so I left in the "right" variants
# (which account for "right"'s non-0.5 xanchor) and the logic in fx_display that
# selects them where appropriate, to make that easy to see!

transform mc_fx_pos: # <-- this one is used
    anchor (0.5, 0.5)
    pos (0.17, 0.84)

transform side_fx_pos:
    anchor (0.5, 0.5)
    pos (0.14, 0.78)

transform fx_tall:
    yanchor 0.0
    ypos 100
    xoffset 150

transform fx_mid:
    yanchor 0.0
    ypos 150
    xoffset 150

transform fx_small: # <-- this one is used
    yanchor 0.0
    ypos 250
    xoffset 150

transform fx_right_tall:
    yanchor 0.0
    ypos 100
    xoffset -150

transform fx_right_mid: # <-- this one is used
    yanchor 0.0
    ypos 150
    xoffset -150

transform fx_right_small:
    yanchor 0.0
    ypos 250
    xoffset -150


# Custom transforms for positioning characters onscreen below.

transform closeleft: # <-- this one is used
    anchor (0.5, 1.0)
    pos (0.4, 1.0)

transform closeright:
    anchor (0.5, 1.0)
    pos (0.6, 1.0)
