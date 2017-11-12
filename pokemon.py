#For discord
import discord
import asyncio

#Pull a random Pokemon if no args are passed
import random

#Pokeapi just got a lot easier
import pokebase

#For exceptions
import traceback
import sys

#Look at the info passed and grab info on the Pokemon wanted
async def pokemon_get(client, message, args):
    poke_num = None
    if (args == None):
        poke_num = str(random.randint(1, 802))

    else:
        poke_num = args[0]

    try:
        pokemon = pokebase.pokemon(poke_num.lower())
        poke_string = str(pokemon.id) + ": " + pokemon.name.title() + " - "
        #See how many types there are for the pulled Pokemon, and append as needed.
        type_string = ""
        if (len(pokemon.types) == 2):
            type_string = str(pokemon.types[0].type).title() + "/" + str(pokemon.types[1].type).title() + " type."
        else:
            type_string = str(pokemon.types[0].type).title() + " type."

        poke_string = poke_string + type_string

        #Send the message
        await client.send_message(message.channel, poke_string)

    except:
        traceback.print_exc()
        await client.send_message(message.channel, sys.exc_info()[0])
