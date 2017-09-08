import discord
import asyncio

async def message_check(client, message):
    #Print a test message
    if (message.content.startswith("!test")):
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

    elif (message.content.startswith("!waifu")):
        await client.send_message(message.channel, ":poop: YOUR WAIFU IS SHIT! :poop:")
        await asyncio.sleep(2)
        await client.send_message(message.channel, "SHIIIIITTTTTT!")

    return

if __name__ == "__main__":
    #Don't run messages.py
    print("Not this file, ya dingus.")
