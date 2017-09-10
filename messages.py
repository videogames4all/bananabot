#For discord
import discord
import asyncio

#For random numbers
import random

commands = {"!help": "Print these help messages.",
            "!rule34": "Post a sexy image ;D",
            "!waifu": "Call someone's waifu shit.",
            "!banana": "Ooh! Banana!",
            "!penis, !dong, !dick, !schlong, !johnson, !bird, !weiner, !cock [<length>]": "PENIS!"}

penis_commands = ["!penis", "!dong", "!dick", "!schlong", "!johnson", "!bird", "!weiner", "!cock"]

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

    return

if __name__ == "__main__":
    #Don't run messages.py
    print("Not this file, ya dingus.")
