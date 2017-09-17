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

    if (args == None):
        poke_random = random.randint(1, 802)
        url = "http://pokeapi.co/api/v2/pokemon/" + str(poke_random) + "/"
        payload = ""
        response = requests.request("GET", url, data=payload)
        data = response.json()
        print(data['forms'][0]['name'])

        await client.send_message(message.channel, data['forms'][0]['name'])

    else:
        await client.send_message(message.channel, "Still need to add argument support")

    conn.close()
