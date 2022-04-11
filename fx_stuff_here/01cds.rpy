python early:

    def parse_fx(lex):
        obj = []
        check_point = lex.checkpoint()
        lex_piece = None
        lex.advance()
        if lex.match("extend"):
            lex.unadvance()
            lex.unadvance()
            lex.unadvance()
            lex.advance()
            lex_piece = 0
            while str(lex.word()).upper() != str(lex.word()) or not lex.match("\"") and lex_piece < 10:
                lex_piece += 1
                lex.unadvance()
                lex.unadvance()
                lex.advance()
            if lex_piece == 10:
                print("why do you have so many things btwn your say and your extend. stop that.")
                return ["mc", test, 0]
            elif lex.match("\""):
                obj.append("mc")
            else:
                lex_piece = lex.name()
                obj.append(lex_piece)
        elif lex.match("show"):
            lex_piece = lex.word()
            obj.append(lex_piece)
        elif lex.match("\""):
            obj.append("mc")
        else:
            lex_piece = lex.name()
            obj.append(lex_piece)

        lex.revert(check_point)
        next_word = 0

        while not lex.eol():
            next_word = lex.word()
            obj.append(next_word) # Always an image tag or Character object.
            next_word = lex.word()
            if next_word is None:
                obj.append(0)
                break
            elif isinstance(next_word, basestring) or str(next_word.upper() == str(next_word)):
                obj.append(0)
                obj.append(next_word)
            else:
                obj.append(next_word)
                next_word = lex.word()
                if next_word is None:
                    break
                else:
                    obj.append(next_word)

        return obj

    def clear_fx_layer(obj):
        renpy.scene(layer="effects")
        return

    def execute_fx(obj):
        x = 0
        while True:
            try:
                whos_emoting = obj[0+x]
                fx_type = obj[1+x]
                fx_pos = obj[2+x]
                fx_display(whos_emoting, fx_type, fx_pos)
                x = x+3
            except:
                break
        return

    renpy.register_statement("fx", parse=parse_fx, execute=clear_fx_layer, post_execute=execute_fx)
