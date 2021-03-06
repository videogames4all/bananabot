#Needed to work with Discord
import discord
import asyncio
#messages.py for where I put my stuff
import messages
#For fuck
import random
#For cross-posting between channels
import cross_post

#Super admin of bot
SUPER_ADMIN = "ZepLander#1497" #Das me

#Create a Client object
client = discord.Client()

#Get ready
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print('------')

#Anytime a message is added, check to see if it's important
@client.event
async def on_message(message):
    ch = message.channel
    #Make sure BananaBot isn't the one sending the message
    if (client.user != message.author):
        #If !quit, the bot will exit if the message author is the SUPER_ADMIN
        if message.content.startswith("!quit"):
            #Check to see if I'm the one that told it to quit
            if (str(message.author) == SUPER_ADMIN):
                await ch.send("Bye!")
                await client.logout()
                await client.close()
                return

            else:
                author = str(message.author).split("#")
                author = author[0]
                await ch.send("You can't make me quit, " + author)

        #Other commands go here
        elif message.content.startswith("!"):
            await messages.message_check(client, message) #Check messages.py for more detail

        #Eggplant emoji
        elif (message.content.lower() == "fuck"):
            chance = random.randint(1,10)
            if (chance == 1):
                await message.add_reaction("\U0001F3E9")
            else:
                await message.add_reaction("\U0001F346")

        #Oh shit, a rat
        elif (message.content.lower() == "oh shit"):
            await message.add_reaction("\U0001F400")

        #Banana by Toto
        elif ("toto" in message.content.lower()):
            author = str(message.author).split("#")
            author = author[0]
            await ch.send(str(message.author.mention) + " https://youtu.be/LEnVwL01qKo")

        #Cross-post check
        await cross_post.check(client, message)

#This part goes last to connect the bot to Discord
try:
    #Try to open the file with the token in it
    with open("token.txt", "r") as token:
        for line in token:
            token_str = line.strip("\n")
            break
    token.closed
    client.run(token_str)
except:
    print("Error opening token.txt, exiting.")
