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
    ch = message.channel
    poke_num = None
    if (args == None):
        poke_num = str(random.randint(0, 807))

    else:
        poke_num = args[0]

    try:
        poke_string = ""

        if (poke_num == "0" or poke_num.lower() == "missingno"):
            #Add missingno
            poke_string = "0: MissingNo. - Bird/Normal type."

        else:
            pokemon = pokebase.pokemon(poke_num.lower())
            poke_string = str(pokemon.id) + ": " + pokemon.name.title() + " - "
            #See how many types there are for the pulled Pokemon, and append as needed.
            type_string = ""
            if (len(pokemon.types) == 2):
                type_string = str(pokemon.types[0].type).title() + "/" + str(pokemon.types[1].type).title() + " type."
            else:
                type_string = str(pokemon.types[0].type).title() + " type."

            #Add something for evolutionary line. pulls evolves_from_species and evolution_chain

            poke_string = poke_string + type_string

        #Send the message
        await ch.send(poke_string)

    except:
        traceback.print_exc()
        await ch.send(sys.exc_info()[0])
