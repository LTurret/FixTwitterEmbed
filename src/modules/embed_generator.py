from time import time

from interactions import Embed


def embed_generator(content: dict, media: str | None = None, tweetId: str | None = None) -> Embed:
    embed: Embed = Embed(description=content["full_text"], color=0x1DA0F2, timestamp=time(), url="https://discord.com")
    embed.set_author(
        name=f"{content['author']} (@{content['screen_name']})",
        url=f"https://twitter.com/{content['screen_name']}",
        icon_url=content["icon_url"],
    )
    embed.set_footer(
        text="Twitter",
        icon_url="https://abs.twimg.com/icons/apple-touch-icon-192x192.png",
    )
    embed.add_field(name="Likes", value=content["favorite_count"], inline=True)
    embed.add_field(name="Retweets", value=content["retweet_count"], inline=True)
    embed.add_field(name="Tweet Portal", value=f"[Click me!](https://x.com/i/status/{tweetId})", inline=False)

    if media:
        embed.set_image(media)

    return embed
