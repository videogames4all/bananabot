import discord
import asyncio

commands = {"!help": "Print these help messages.",
            "!test": "Print a test message.",
            "!sleep": "Sleep for 5 seconds.",
            "!rule34": "Post a sexy image ;D",
            "!waifu": "Call someone's waifu shit.",
            "!banana": "Ooh! Banana!"}

async def message_check(client, message):
    #Print commands that this bot knows
    if (message.content.startswith("!help")):
        for key,value in commands.items():
            await client.send_message(message.channel, key + ": " + value)

    #Print a test message
    elif (message.content.startswith("!test")):
        await client.send_message(message.channel, "This has been a test of your local test bot.")

    #Have it sleep for 5 seconds
    elif (message.content.startswith("!sleep")):
        await asyncio.sleep(5)
        await client.send_message(message.channel, "Done sleeping.")

    #"Post porn", except just outright call the user a pervert
    elif (message.content.startswith("!rule34")):
        #Pull apart the author of the message
        author = str(message.author).split("#")
        author = author[0]
        #And call them a perv
        await client.send_message(message.channel, author + " is a fuckin' perv.", tts=True)

    #Your waifu is shit
    elif (message.content.startswith("!waifu")):
        await client.send_message(message.channel, ":poop: YOUR WAIFU IS SHIT! :poop:")
        await asyncio.sleep(2)
        await client.send_message(message.channel, "SHIIIIITTTTTT!")

    #Ooh! Banana!
    elif (message.content.startswith("!banana")):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=z8WvSGNEV24")

    return

if __name__ == "__main__":
    #Don't run messages.py
    print("Not this file, ya dingus.")
