#For discord
import discord
import asyncio

#Pull a random Pokemon if no args are passed
import random

#Pokeapi just got a lot easier
import pokebase

#Look at the info passed and grab info on the Pokemon wanted
async def pokemon_get(client, message, args):
    poke_num = None
    if (args == None):
        poke_num = random.randint(1, 802)

    else:
        poke_num = args[0]

    pokemon = pokebase.pokemon(poke_num)
    await client.send_message(message.channel, pokemon.name)
