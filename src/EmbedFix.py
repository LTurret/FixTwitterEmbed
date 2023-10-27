from re import search

from interactions import events
from interactions import listen
from interactions import AllowedMentions
from interactions import Embed
from interactions import Extension

from modules.embed_generator import embed_generator
from modules.fetch_tweet import fetch_tweet
from modules.get_contents import get_contents


class twitterFix(Extension):
    def __init__(self, bot):
        self.bot: any = bot
        self.pattern: str = r"https\:\/\/[x|twitter]+\.com\/.+\/(\d+)"

        print(f" ↳ Creating {__name__}")

    @listen()
    async def on_message_create(self, event: events.MessageCreate):
        if event.message.author != self.bot.user:
            if search(rf"{self.pattern}", event.message.content):
                await event.message.add_reaction("✨")

    @listen()
    async def on_message_react(self, event: events.MessageReactionAdd):
        if event.reaction.count > 1 and event.reaction.me:
            # Clear reactions
            await event.reaction.remove()

            # Find keyword
            if search(rf"{self.pattern}", event.message.content):
                tweetId: str = search(rf"{self.pattern}", event.message.content).group(1)
                api_callback: dict = await fetch_tweet(tweetId)

                content: dict = {**(await get_contents(api_callback))}
                embeds: list[Embed] = []

                if content["images"]:
                    for image in content["images"]:
                        # Embeds composer - Compose multiple picture in to one array
                        embeds.append(embed_generator(content, image, tweetId=tweetId))

                else:
                    embeds.append(embed_generator(content, tweetId=tweetId))

                # Send embed
                if content["videos"] is not None:
                    await event.message.channel.send(
                        files=content["videos"],
                        embeds=embeds,
                        reply_to=event.message,
                        allowed_mentions=AllowedMentions.none(),
                        silent=True,
                    )
                else:
                    await event.message.channel.send(
                        embeds=embeds,
                        reply_to=event.message,
                        allowed_mentions=AllowedMentions.none(),
                        silent=True,
                    )


def setup(bot):
    twitterFix(bot)
