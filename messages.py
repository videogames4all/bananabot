#For discord
import discord
import asyncio

#For random numbers
import random

commands = {"!help": "Print these help messages.",
            "!test": "Print a test message.",
            "!sleep": "Sleep for 5 seconds.",
            "!rule34": "Post a sexy image ;D",
            "!waifu": "Call someone's waifu shit.",
            "!banana": "Ooh! Banana!",
            "!penis, !dong, !dick, !schlong, !johnson, !bird, !weiner, !cock": "PENIS!"}

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

    #Print a test message
    elif (command == "!test"):
        await client.send_message(message.channel, "This has been a test of your local test bot.")

    #Have it sleep for 5 seconds
    elif (command == "!sleep"):
        await asyncio.sleep(5)
        await client.send_message(message.channel, "Done sleeping.")

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
        await asyncio.sleep(2)
        await client.send_message(message.channel, "SHIIIIITTTTTT!")

    #Ooh! Banana!
    elif (command == "!banana"):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=z8WvSGNEV24")

    #Penis
    elif (command in penis_commands):
        penis_length = random.randint(2,20)
        penis = "8" + "=" * penis_length + "D"
        await client.send_message(message.channel, penis)

    return

if __name__ == "__main__":
    #Don't run messages.py
    print("Not this file, ya dingus.")
