#For discord
import discord
import asyncio

#For random numbers
import random

#For the pokeapi
import pokemon

#For Mulligan Dice Golf
import mdg

commands = {"!help": "Print these help messages.",
            "!rule34": "Post a sexy image ;D",
            "!waifu": "Call someone's waifu shit.",
            "!banana": "Ooh! Banana!",
            "!penis, !dong, !dick, !schlong, !johnson, !bird, !weiner, !cock [<length>]": "PENIS!",
            "!about": "Print some info about this bot.",
            "!doc_chicken": "IT'S TIME FOR DOC CHICKEN YA'LL!",
            "!groot": "I am Groot.",
            "!pokemon": "Get information on a Pokemon (still working on it)",
            "!mdg": "Play a hole of Mulligan Dice Golf (work in progress)"}

penis_commands = ["!penis", "!dong", "!dick", "!schlong", "!johnson", "!bird", "!weiner", "!cock"]

info_list = ["My name is Banana-Bot, and ZepLander is my papa.",
            "I'm still a work in progress.",
            "If you've got some ideas on what I should do, tell ZepLander, preferably by smoke signal.",
            "I like long walks on the beach, and romantic candle-lit dinners.",
            "I may just be a bot, but I know your waifu is shit.",
            "When in doubt, blame Scott.",
            "I... uhhh... forgot what I was going to say.",
            "A/S/L? Quite some time/bot/a laptop",
            "Surely you can think of more words to use for a penis that I can learn.",
            "How should I draw an ASCII vagina?",
            "There's a lot stored in memory for me, I should start storing things in files as I get bigger.",
            "There can be only one.",
            "...",
            "Traps aren't gay.",
            "Ayyy lmao!",
            "Like, comment, and subscribe for more crazy bot antics!",
            "On Tuesdays I sexually identify as an attack helicopter.",
            "Cuck",
            "Fuck this, fuck you, fuck me, and fuck it all."]

doc_chicken_urls = ["https://www.youtube.com/watch?v=J-hRvCUMtIU",
                    "https://www.youtube.com/watch?v=jT8F4wVxdCk"]

groot = ["I am Groot.",
        "I am Groot!",
        "I am GROOT!",
        "I, am Groot.",
        "We are Groot.",
        "i am groot",
        "1 4m Gr007"]

async def message_check(client, message):
    full_message = message.content.split(" ")
    command = full_message[0]
    args = None
    if (len(full_message) > 1):
        args = full_message[1:]

    #Print commands that this bot knows
    if (command == "!help"):
        for key,value in commands.items():
            await client.send_message(message.channel, key + ": " + value)

    #"Post porn", except just outright call the user a pervert
    elif (command == "!rule34"):
        #Pull apart the author of the message
        author = str(message.author).split("#")
        author = author[0]
        #And call them a perv
        await client.send_message(message.channel, author + " is a fuckin' perv.", tts=True)

    #Your waifu is shit
    elif (command == "!waifu"):
        await client.send_message(message.channel, ":poop: YOUR WAIFU IS SHIT! :poop:")
        await asyncio.sleep(2) #Wait 2 seconds for dramatic effect
        await client.send_message(message.channel, "SHIIIIITTTTTT!")

    #Ooh! Banana!
    elif (command == "!banana"):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=z8WvSGNEV24")

    #Share some info about this bot
    elif (command == "!about"):
        about_print = random.randint(0, len(info_list) -1)
        await client.send_message(message.channel, info_list[about_print])

    #Penis
    elif (command in penis_commands):
        #The most complicated command so far!
        if (args != None):
            #If there's an argument (just need the first one), see if we want a custom length
            if (args[0].isdigit() == False):
                #It's not a number, so just do the normal thaaang
                penis_length = random.randint(2,12)
                penis = "8" + "=" * penis_length + "D"
                await client.send_message(message.channel, penis)

            else:
                #It's a number, let's get a penis going!
                penis_length = args[0].split(".")
                penis_length = penis_length[0]
                penis_length = int(penis_length)
                if (penis_length < 1):
                    #At this point it's not even a penis
                    await client.send_message(message.channel, "You can't have a penis that has no length, you might as well not have a penis!")

                else:
                    #Print out the user's desired (oh baby!) penis
                    penis = "8" + "=" * penis_length + "D"
                    await client.send_message(message.channel, penis)
                    if (penis_length > 12):
                        #Assuming one "=" is one inch, this is getting absurd even for porn
                        await client.send_message(message.channel, "Good luck fitting that!")

        else:
            #Just a regular penis (is 12 inches still reasonable for porn?)
            penis_length = random.randint(2,12)
            penis = "8" + "=" * penis_length + "D"
            await client.send_message(message.channel, penis)

    #DOC CHICKEN!
    elif (command == "!doc_chicken"):
        doc_random = random.randint(0, len(doc_chicken_urls) - 1)
        await client.send_message(message.channel, "IT'S TIME FOR DOC CHICKEN YA'LL! " + doc_chicken_urls[doc_random])

    #I am Groot
    elif (command == "!groot"):
        groot_random = random.randint(0, len(groot) - 1)
        await client.send_message(message.channel, groot[groot_random], tts=True)

    #Gotta catch 'em all!
    elif (command == "!pokemon"):
        await pokemon.pokemon_get(client, message, args)

    #Play a round of Mulligan Dice Golf
    elif (command == "!mdg"):
        await mdg.mdg_game(client, message)

    return

if __name__ == "__main__":
    #Don't run messages.py
    print("Not this file, ya dingus.")
