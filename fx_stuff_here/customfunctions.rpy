init python:

    def fx_display(whos_emoting, fx_type, fx_pos):

        hold_this = None

        if str(whos_emoting).upper() == str(whos_emoting):
            hold_this = eval(whos_emoting).image_tag
            whos_emoting = hold_this

        if fx_pos == 0:
            if whos_emoting == MC.image_tag:
                fx_pos = [mc_fx_pos]
            elif not renpy.showing(whos_emoting):
                fx_pos = [side_fx_pos]

            else:
                fx_pos = renpy.get_at_list(whos_emoting)

                if whos_emoting in tall_tags:
                    if right in fx_pos:
                        fx_pos.append(fx_right_tall)
                    else:
                        fx_pos.append(fx_tall)
                elif whos_emoting in small_tags:
                    if right in fx_pos:
                        fx_pos.append(fx_right_small)
                    else:
                        fx_pos.append(fx_small)
                else:
                    if right in fx_pos:
                        fx_pos.append(fx_right_mid)
                    else:
                        fx_pos.append(fx_mid)

        else:
            hold_this = fx_pos
            fx_pos = renpy.get_at_list(whos_emoting)
            fx_pos.append(hold_this)

        renpy.show(fx_type, at_list=fx_pos, layer="effects")
        return
