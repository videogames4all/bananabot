#For discord
import discord
import asyncio

#Pull from pokeapi.co
import http.client
import json
import requests

#Pull a random Pokemon if no args are passed
import random

#Look at the info passed and grab info on the Pokemon wanted
async def pokemon_get(client, message, args):
    #Open a connection to pokeapi.co
    conn = http.client.HTTPConnection("pokeapi.co")
    payload = ""
    conn.request("GET", "/api/v2/pokemon/bulbasaur/", payload)
    res = conn.getresponse()
    data = res.read()
    obj = json.loads(data.decode("utf-8"))

    pokemon = None
    if (args == None):
        pokemon = random.randint(1, 802)

    else:
        pokemon = args[0]

    url = "http://pokeapi.co/api/v2/pokemon/" + str(pokemon) + "/"
    response = requests.request("GET", url, data=payload)
    data = response.json()
    print(data['name'].title())
    await client.send_message(message.channel, data['name'].title())

    conn.close()
