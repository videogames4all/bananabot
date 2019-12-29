import discord
import asyncio

channels_cross_post = [543551098783268866, 475718359401365511]
#Order: meet-up-coordination, nm-meetup
#channels_cross_post = [183744219297480705, 338792653384581122]
#Order: My bot-testing, [NMT]'s bot-testing

async def check(client, message):
    ch = message.channel
    #Check that the message was in a certain channel in a certain server
    if (message.channel.id in channels_cross_post):
        print(message.content)
        #Need to clean the message first, remove hyperlinks, and preface with who said what.
        link_less = remove_hyperlinks(str(message.content))
        #But don't send the message if there's nothing but a link in it
        if (link_less != " <link removed> ") and (link_less != ""):
            new_msg = str(message.author) + " said:\n" + link_less
            for xpost in channels_cross_post:
                if (xpost != message.channel.id):
                    dest_channel = client.get_channel(xpost)
                    await dest_channel.send(new_msg)

def remove_hyperlinks(message_sent):
    split_message = message_sent.split(" ")
    new_message = ""
    for split in split_message:
        if (split.startswith("https")) or (split.startswith("http")):
            new_message += " <link removed> "

        else:
            new_message += split + " "

    return new_message
