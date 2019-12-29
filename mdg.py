#Mulligan Dice Golf: A dice golf game that is luck based. Is fun tho. Originally made by those people, I'm just putting it in a bot.
#Work with discord
import discord

#Need RNG
import random

#6 dice, handle each differently
#Par 4/5 Tee-off Die
def black_die():
    shot = random.randint(1,10) #Returns 1-10. 1-6 = fairway, 7-8 = rough, 9-10 = hazard
    if (shot <= 6):
        return "fairway" #1 stroke

    elif (shot <= 8):
        return "rough" #2 strokes

    else:
        return "hazard" #3 strokes

#Par 4/5 Iron Die
def white_die():
    shot = random.randint(1,10) #Returns 1-10. 1-5 = green, 6-7 = chip, 8 = bunker, 9 = hazard, 10 = tap in
    if (shot <= 5):
        return "green" #1 stroke

    elif (shot <= 7):
        return "chip" #2 strokes

    elif (shot <= 8):
        return "bunker" #2 strokes

    elif (shot <= 9):
        return "hazard" #3 strokes

    else:
        return "tap-in" #2 strokes, ignore green_die()

#Par 5 Fairway Driver Die
def orange_die():
    shot = random.randint(1,10) #Returns 1-10. 1-3 = green, 4-8 = fairway, 9-10 = rough
    if (shot <= 3):
        return "green" #1 stroke, ignore white_die()

    elif (shot <= 8):
        return "fairway" #1 stroke

    else:
        return "rough" #2 strokes

#Par 3 Tee-off Die
def yellow_die():
    shot = random.randint(1,10) #Returns 1-10, 1-5 = green, 6-7 = chip, 8-9 = bunker, 10 = hazard
    if (shot <= 5):
        return "green" #1 stroke

    elif (shot <= 7):
        return "chip" #2 strokes

    elif (shot <= 9):
        return "bunker" #2 strokes

    else:
        return "hazard" #3 strokes

#Putting Die
def green_die():
    shot = random.randint(1,12) #Returns 1-12, 1-4 = one, 5-9 = two, 10-12 = three
    if (shot <= 4):
        return "one"

    elif (shot <= 9):
        return "two"

    else:
        return "three"

#Weather die
def blue_die():
    shot = random.randint(1,12) #Returns 1-12, 1 = sun, 2 = wind, 3-12 = nothing
    if (shot == 1):
        return "sun" #Minus 1 stroke

    elif (shot == 2):
        return "wind" #Plus 1 stroke

    else:
        return "nothing" #Nothing extra

#Dice for a hole
def hole(par_in=0):
    par = par_in
    if (par == 0):
        par = random.randint(3,5)

    if (par == 3):
        #Roll the yellow, green, and blue dies
        yellow = yellow_die()
        green = green_die()
        blue = blue_die()

        strokes = 0
        #Handle the yellow die
        if (yellow == "green"):
            strokes += 1

        elif (yellow == "chip"):
            strokes += 2

        elif (yellow == "bunker"):
            strokes += 2

        else:
            strokes += 3

        #Handle the green die
        if (green == "one"):
            strokes += 1

        elif (green == "two"):
            strokes += 2

        else:
            strokes += 3

        #Handle the blue die
        if (blue == "sun"):
            strokes -= 1

        elif (blue == "wind"):
            strokes += 1
            
        return "Par 3: " + str(strokes)

    elif (par == 4):
        #Roll the black, white, green, and blue dies
        black = black_die()
        white = white_die()
        green = green_die()
        blue = blue_die()

        strokes = 0
        #Handle the black die
        if (black == "fairway"):
            strokes += 1

        elif (black == "rough"):
            strokes += 2

        else:
            strokes += 3

        #Handle the white die
        ignore_green = False
        if (white == "green"):
            strokes += 1

        elif (white == "chip"):
            strokes += 2

        elif (white == "bunker"):
            strokes += 2

        elif (white == "hazard"):
            strokes += 3

        else:
            strokes += 2
            ignore_green = True #Tapped in!

        #Handle the green die
        if (ignore_green == False):
            if (green == "one"):
                strokes += 1

            elif (green == "two"):
                strokes += 2

            else:
                strokes += 3

        #Handle the blue die
        if (blue == "sun"):
            strokes -= 1

        elif (blue == "wind"):
            strokes += 1

        return "Par 4: " + str(strokes)

    elif (par == 5):
        #Roll the black, orange, white, green, and blue dies
        black = black_die()
        orange = orange_die()
        white = white_die()
        green = green_die()
        blue = blue_die()

        strokes = 0
        #Handle the black die
        if (black == "fairway"):
            strokes += 1

        elif (black == "rough"):
            strokes += 2

        else:
            strokes += 3

        #Handle the orange die
        ignore_white = False
        if (orange == "green"):
            strokes += 1
            ignore_white = True

        elif (orange == "fairway"):
            strokes += 1

        else:
            strokes += 2

        #Handle the white die
        ignore_green = False
        if (ignore_white == False):
            if (white == "green"):
                strokes += 1

            elif (white == "chip"):
                strokes += 2

            elif (white == "bunker"):
                strokes += 2

            elif (white == "hazard"):
                strokes += 3

            else:
                strokes += 2
                ignore_green = True #Tapped in!

        #Handle the green die
        if (ignore_green == False):
            if (green == "one"):
                strokes += 1

            elif (green == "two"):
                strokes += 2

            else:
                strokes += 3

        #Handle the blue die
        if (blue == "sun"):
            strokes -= 1

        elif (blue == "wind"):
            strokes += 1

        return "Par 5: " + str(strokes)

    else:
        return "bad par, 1-zillion stroke penalty"

#Play a hole of Mulligan Dice Golf
async def mdg_game(client, message):
    results = hole()
    ch = message.channel
    await ch.send(results)
