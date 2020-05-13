def coords(x,y,players,position,action,stack):
    if players == 2:
        if position == 1:
            if action == 1:
                # SB minraise HU
                posx, posy = chart_coords(x,y)
                chart = "BB defend vs minraise HU"
                chartpath = "Spin and Go Preflop Charts/Headsup Charts/BB defend vs minraise.PNG"
                return posx,posy,chart,chartpath
            elif action == 2:
                # SB shove HU
                posx, posy = shove_coords(x,y)
                chart = "BB defend vs shove HU"
                chartpath = "Spin and Go Preflop Charts/Headsup Charts/BB vs SB shove HU.png"
                return posx,posy,chart,chartpath

            elif action == 3:
                # SB limp, HU
                if stack >= 15:
                    # more than 15BB
                    posx, posy = chart_coords(x, y)
                    chart = "BB defend vs limp HU 15+ BB"
                    chartpath = "Spin and Go Preflop Charts/Headsup Charts/BB defend vs limp 15BB and more.PNG"
                    return posx, posy, chart, chartpath
                else:
                    # less than 15BB
                    posx, posy = chart_coords(x, y)
                    chart = "BB defend vs limp HU less than 15 BB"
                    chartpath = "Spin and Go Preflop Charts/Headsup Charts/BB defend vs limp 14BB and less.png"
                    return posx, posy, chart, chartpath


        elif position == 2:
            if action == 1:
                if stack >= 14:
                    # SB open 14+
                    posx, posy = chart_coords(x, y)
                    chart = "SB open HU 14+ BB"
                    chartpath = "Spin and Go Preflop Charts/Headsup Charts/SB HU 14BB and more.PNG"
                    return posx, posy, chart, chartpath
                elif stack >= 11:
                    # SB open 11-14
                    posx, posy = chart_coords(x, y)
                    chart = "SB open HU 11-13 BB"
                    chartpath = "Spin and Go Preflop Charts/Headsup Charts/11-13BB HU SB.PNG"
                    return posx, posy, chart, chartpath
                elif stack >= 7:
                    # SB open 7-10
                    posx, posy = chart_coords(x, y)
                    chart = "SB open HU 7-10 BB"
                    chartpath = "Spin and Go Preflop Charts/Headsup Charts/7-10BB HU.PNG"
                    return posx, posy, chart, chartpath
                else:
                    # nash push
                    posx, posy = nash_coords(x, y)
                    chart = "Nash Push"
                    chartpath = "Spin and Go Preflop Charts/Headsup Charts/nashpush.png"
                    return posx, posy, chart, chartpath
        elif position == 3:
            if action == 1:
                # nash push
                posx, posy = nash_coords(x,y)
                chart = "Nash Push"
                chartpath = "Spin and Go Preflop Charts/Headsup Charts/nashpush.png"
                return posx,posy,chart,chartpath
            elif action == 2:
                # nash call
                posx, posy = nash_coords(x, y)
                chart = "Nash Call"
                chartpath = "Spin and Go Preflop Charts/Headsup Charts/nashcall.png"
                return posx, posy, chart, chartpath

    elif players == 3:
        if position == 1:
            if action == 1:
                # BU minraise
                if stack >= 17:
                    # 17 and more
                    posx, posy = chart_coords(x, y)
                    chart = "BB vs BU minraise 17+ BB"
                    chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BB vs BU minraise 17BB and more.PNG"
                    return posx, posy, chart, chartpath
                else:
                    # 16 and less
                    posx, posy = chart_coords(x, y)
                    chart = "BB vs BU minraise 16 and less BB"
                    chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BB vs BU minraise 16BB and less.PNG"
                    return posx, posy, chart, chartpath
            elif action == 2:
                # BU shove
                posx, posy = shove_coords(x, y)
                chart = "BB vs BU shove 3-way"
                chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BB vs BU shove 3-way.png"
                return posx, posy, chart, chartpath

            elif action == 3:
                # BU limp
                posx, posy = altchart_coords(x, y)
                chart = "BB vs BU limp 3-way"
                chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BB vs BU limp.png"
                return posx, posy, chart, chartpath

            elif action == 4:
                # SB minraise
                posx, posy = chart_coords(x, y)
                chart = "BB vs SB minraise 3-way"
                chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BB vs SB minraise.PNG"
                return posx, posy, chart, chartpath

            elif action == 5:
                # SB 2.5x
                posx, posy = chart_coords(x, y)
                chart = "BB vs SB 2.5x raise 3-way"
                chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BB vs SB 2.5x.png"
                return posx, posy, chart, chartpath

            elif action == 6:
                # SB shove
                posx, posy = shove_coords(x, y)
                chart = "BB vs SB shove 3-way"
                chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BB vs SB shove 3-way.png"
                return posx, posy, chart, chartpath
            else:
                # SB limp
                posx, posy = chart_coords(x, y)
                chart = "BB vs SB limp 3-way"
                chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BB vs SB limp.png"
                return posx, posy, chart, chartpath


        elif position == 2:
            if action == 1:
                # BU minraise
                posx, posy = altchart_coords(x, y)
                chart = "SB vs BU minraise 3-way"
                chartpath = "Spin and Go Preflop Charts/3 Handed Charts/SB vs BU Raise 3-way.PNG"
                return posx, posy, chart, chartpath
            elif action == 2:
                # BU limp
                posx, posy = altchart_coords(x, y)
                chart = "SB vs BU limp 3-way"
                chartpath = "Spin and Go Preflop Charts/3 Handed Charts/SB vs BU limp.png"
                return posx, posy, chart, chartpath
            else:
                # BU fold/ SB open
                if stack >= 18:
                    # SB open 3 way 18+
                    posx, posy = chart_coords(x, y)
                    chart = "SB open 3-way 18+ BB"
                    chartpath = "Spin and Go Preflop Charts/3 Handed Charts/SB 3-way 18BB+ open.PNG"
                    return posx, posy, chart, chartpath
                elif stack >= 14:
                    # SB open 3 way 14-17
                    posx, posy = chart_coords(x, y)
                    chart = "SB open 3-way 14-17 BB"
                    chartpath = "Spin and Go Preflop Charts/3 Handed Charts/SB 3-way 14-17BB 3-way open.PNG"
                    return posx, posy, chart, chartpath
                else:
                    # nash push
                    posx, posy = nash_coords(x, y)
                    chart = "Nash Push"
                    chartpath = "Spin and Go Preflop Charts/Headsup Charts/nashpush.png"
                    return posx, posy, chart, chartpath
        elif position == 3:
            if action == 1:
                # BU open 3 way
                if stack >= 13:
                    # stack 13+
                    posx, posy = chart_coords(x, y)
                    chart = "BU open 3-way 13+ BB"
                    chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BU open 13+BB.PNG"
                    return posx, posy, chart, chartpath
                else:
                    # stack 12-
                    posx, posy = chart_coords(x, y)
                    chart = "BU open 3-way 12 or less BB"
                    chartpath = "Spin and Go Preflop Charts/3 Handed Charts/BU push 12BB or less.PNG"
                    return posx, posy, chart, chartpath


def nash_coords(y,x):
    nashmap = [[(28, 57), (60, 57), (95, 57), (130, 57), (165, 57), (200, 57), (235, 57), (270, 57), (305, 57), (340, 57), (375, 57), (410, 57), (445, 57)],
               [(28, 85), (60, 85), (95, 85), (130, 85), (165, 85), (200, 85), (235, 85), (270, 85), (305, 85), (340, 85), (375, 85), (410, 85), (445, 85)],
               [(28, 113), (60, 113), (95, 113), (130, 113), (165, 113), (200, 113), (235, 113), (270, 113), (305, 113), (340, 113), (375, 113), (410, 113), (445, 113)],
               [(28, 141), (60, 141), (95, 141), (130, 141), (165, 141), (200, 141), (235, 141), (270, 141), (305, 141), (340, 141), (375, 141), (410, 141), (445, 141)],
               [(28, 169), (60, 169), (95, 169), (130, 169), (165, 169), (200, 169), (235, 169), (270, 169), (305, 169), (340, 169), (375, 169), (410, 169), (445, 169)],
               [(28, 197), (60, 197), (95, 197), (130, 197), (165, 197), (200, 197), (235, 197), (270, 197), (305, 197), (340, 197), (375, 197), (410, 197), (445, 197)],
               [(28, 225), (60, 225), (95, 225), (130, 225), (165, 225), (200, 225), (235, 225), (270, 225), (305, 225), (340, 225), (375, 225), (410, 225), (445, 225)],
               [(28, 253), (60, 253), (95, 253), (130, 253), (165, 253), (200, 253), (235, 253), (270, 253), (305, 253), (340, 253), (375, 253), (410, 253), (445, 253)],
               [(28, 281), (60, 281), (95, 281), (130, 281), (165, 281), (200, 281), (235, 281), (270, 281), (305, 281), (340, 281), (375, 281), (410, 281), (445, 281)],
               [(28, 309), (60, 309), (95, 309), (130, 309), (165, 309), (200, 309), (235, 309), (270, 309), (305, 309), (340, 309), (375, 309), (410, 309), (445, 309)],
               [(28, 337), (60, 337), (95, 337), (130, 337), (165, 337), (200, 337), (235, 337), (270, 337), (305, 337), (340, 337), (375, 337), (410, 337), (445, 337)],
               [(28, 365), (60, 365), (95, 365), (130, 365), (165, 365), (200, 365), (235, 365), (270, 365), (305, 365), (340, 365), (375, 365), (410, 365), (445, 365)],
               [(28, 393), (60, 393), (95, 393), (130, 393), (165, 393), (200, 393), (235, 393), (270, 393), (305, 393), (340, 393), (375, 393), (410, 393), (445, 393)]]


    return(nashmap[x][y])

def chart_coords(y,x):
    chartmap = [[(1, 1), (40, 1), (79, 1), (118, 1), (157, 1), (196, 1), (235, 1), (274, 1), (313, 1), (352, 1), (391, 1), (430, 1), (469, 1)],
                [(1, 40), (40, 40), (79, 40), (118, 40), (157, 40), (196, 40), (235, 40), (274, 40), (313, 40), (352, 40), (391, 40), (430, 40), (469, 40)],
                [(1, 79), (40, 79), (79, 79), (118, 79), (157, 79), (196, 79), (235, 79), (274, 79), (313, 79), (352, 79), (391, 79), (430, 79), (469, 79)],
                [(1, 118), (40, 118), (79, 118), (118, 118), (157, 118), (196, 118), (235, 118), (274, 118), (313, 118), (352, 118), (391, 118), (430, 118), (469, 118)],
                [(1, 157), (40, 157), (79, 157), (118, 157), (157, 157), (196, 157), (235, 157), (274, 157), (313, 157), (352, 157), (391, 157), (430, 157), (469, 157)],
                [(1, 196), (40, 196), (79, 196), (118, 196), (157, 196), (196, 196), (235, 196), (274, 196), (313, 196), (352, 196), (391, 196), (430, 196), (469, 196)],
                [(1, 235), (40, 235), (79, 235), (118, 235), (157, 235), (196, 235), (235, 235), (274, 235), (313, 235), (352, 235), (391, 235), (430, 235), (469, 235)],
                [(1, 274), (40, 274), (79, 274), (118, 274), (157, 274), (196, 274), (235, 274), (274, 274), (313, 274), (352, 274), (391, 274), (430, 274), (469, 274)],
                [(1, 313), (40, 313), (79, 313), (118, 313), (157, 313), (196, 313), (235, 313), (274, 313), (313, 313), (352, 313), (391, 313), (430, 313), (469, 313)],
                [(1, 352), (40, 352), (79, 352), (118, 352), (157, 352), (196, 352), (235, 352), (274, 352), (313, 352), (352, 352), (391, 352), (430, 352), (469, 352)],
                [(1, 391), (40, 391), (79, 391), (118, 391), (157, 391), (196, 391), (235, 391), (274, 391), (313, 391), (352, 391), (391, 391), (430, 391), (469, 391)],
                [(1, 430), (40, 430), (79, 430), (118, 430), (157, 430), (196, 430), (235, 430), (274, 430), (313, 430), (352, 430), (391, 430), (430, 430), (469, 430)],
                [(1, 469), (40, 469), (79, 469), (118, 469), (157, 469), (196, 469), (235, 469), (274, 469), (313, 469), (352, 469), (391, 469), (430, 469), (469, 469)]]

    return(chartmap[x][y])

def shove_coords(y, x):
    shovemap = [[(3, 1), (41, 1), (80, 1), (119, 1), (158, 1), (196, 1), (235, 1), (274, 1), (312, 1), (351, 1), (389, 1), (428, 1), (467, 1)],
                [(3, 39), (41, 39), (80, 39), (119, 39), (158, 39), (196, 39), (235, 39), (274, 39), (312, 39), (351, 39), (389, 39), (428, 39), (467, 39)],
                [(3, 78), (41, 78), (80, 78), (119, 78), (158, 78), (196, 78), (235, 78), (274, 78), (312, 78), (351, 78), (389, 78), (428, 78), (467, 78)],
                [(3, 117), (41, 117), (80, 117), (119, 117), (158, 117), (196, 117), (235, 117), (274, 117), (312, 117), (351, 117), (389, 117), (428, 117), (467, 117)],
                [(3, 156), (41, 156), (80, 156), (119, 156), (158, 156), (196, 156), (235, 156), (274, 156), (312, 156), (351, 156), (389, 156), (428, 156), (467, 156)],
                [(3, 194), (41, 194), (80, 194), (119, 194), (158, 194), (196, 194), (235, 194), (274, 194), (312, 194), (351, 194), (389, 194), (428, 194), (467, 194)],
                [(3, 233), (41, 233), (80, 233), (119, 233), (158, 233), (196, 233), (235, 233), (274, 233), (312, 233), (351, 233), (389, 233), (428, 233), (467, 233)],
                [(3, 271), (41, 271), (80, 271), (119, 271), (158, 271), (196, 271), (235, 271), (274, 271), (312, 271), (351, 271), (389, 271), (428, 271), (467, 271)],
                [(3, 310), (41, 310), (80, 310), (119, 310), (158, 310), (196, 310), (235, 310), (274, 310), (312, 310), (351, 310), (389, 310), (428, 310), (467, 310)],
                [(3, 349), (41, 349), (80, 349), (119, 349), (158, 349), (196, 349), (235, 349), (274, 349), (312, 349), (351, 349), (389, 349), (428, 349), (467, 349)],
                [(3, 387), (41, 387), (80, 387), (119, 387), (158, 387), (196, 387), (235, 387), (274, 387), (312, 387), (351, 387), (389, 387), (428, 387), (467, 387)],
                [(3, 426), (41, 426), (80, 426), (119, 426), (158, 426), (196, 426), (235, 426), (274, 426), (312, 426), (351, 426), (389, 426), (428, 426), (467, 426)],
                [(3, 465), (41, 465), (80, 465), (119, 465), (158, 465), (196, 465), (235, 465), (274, 465), (312, 465), (351, 465), (389, 465), (428, 465), (467, 465)]]
    return(shovemap[x][y])

def altchart_coords(y,x):
    altmap = [[(1, 0), (40, 0), (79, 0), (117, 0), (156, 0), (195, 0), (233, 0), (272, 0), (311, 0), (349, 0), (388, 0), (427, 0), (464, 0)],
              [(1, 38), (40, 38), (79, 38), (117, 38), (156, 38), (195, 38), (233, 38), (272, 38), (311, 38), (349, 38), (388, 38), (427, 38), (464, 38)],
              [(1, 77), (40, 77), (79, 77), (117, 77), (156, 77), (195, 77), (233, 77), (272, 77), (311, 77), (349, 77), (388, 77), (427, 77), (464, 77)],
              [(1, 115), (40, 115), (79, 115), (117, 115), (156, 115), (195, 115), (233, 115), (272, 115), (311, 115), (349, 115), (388, 115), (427, 115), (464, 115)],
              [(1, 154), (40, 154), (79, 154), (117, 154), (156, 154), (195, 154), (233, 154), (272, 154), (311, 154), (349, 154), (388, 154), (427, 154), (464, 154)],
              [(1, 193), (40, 193), (79, 193), (117, 193), (156, 193), (195, 193), (233, 193), (272, 193), (311, 193), (349, 193), (388, 193), (427, 193), (464, 193)],
              [(1, 231), (40, 231), (79, 231), (117, 231), (156, 231), (195, 231), (233, 231), (272, 231), (311, 231), (349, 231), (388, 231), (427, 231), (464, 231)],
              [(1, 270), (40, 270), (79, 270), (117, 270), (156, 270), (195, 270), (233, 270), (272, 270), (311, 270), (349, 270), (388, 270), (427, 270), (464, 270)],
              [(1, 309), (40, 309), (79, 309), (117, 309), (156, 309), (195, 309), (233, 309), (272, 309), (311, 309), (349, 309), (388, 309), (427, 309), (464, 309)],
              [(1, 348), (40, 348), (79, 348), (117, 348), (156, 348), (195, 348), (233, 348), (272, 348), (311, 348), (349, 348), (388, 348), (427, 348), (464, 348)],
              [(1, 386), (40, 386), (79, 386), (117, 386), (156, 386), (195, 386), (233, 386), (272, 386), (311, 386), (349, 386), (388, 386), (427, 386), (464, 386)],
              [(1, 425), (40, 425), (79, 425), (117, 425), (156, 425), (195, 425), (233, 425), (272, 425), (311, 425), (349, 425), (388, 425), (427, 425), (464, 425)],
              [(1, 463), (40, 463), (79, 463), (117, 463), (156, 463), (195, 463), (233, 463), (272, 463), (311, 463), (349, 463), (388, 463), (427, 463), (464, 463)]]
    return(altmap[x][y])
