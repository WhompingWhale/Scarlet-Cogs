# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks

__author__ = "ScarletRav3n"

b = False


class Grammar:
    """Fix those mistakes"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.admin_or_permissions(administrator=True)
    async def grammar(self, on_off: str):
        """Toggle carrots"""
        f = on_off.lower()
        global b
        if f == "on":
            await self.bot.say("Deleting carrots is now ON. \n`Make sure I have the 'manage_messages' permission`")
            b = True
        elif f == "off":
            await self.bot.say("Deleting carrots is now OFF.")
            b = False
        else:
            await self.bot.say("I need an ON or OFF state.")

    async def on_message(self, m):
        k = m.content.lower()
        for x in self.bot.command_prefix:
            if x in m.content:
                # print("nothing")
                return
            elif "your a " in k:
                p = "you're*"
            elif "your an " in k:
                p = "you're*"
            elif "its not" in k:
                p = "it's*"
            elif "their not" in k:
                p = "they're*"
            elif "their a " in k:
                p = "they're*"
            elif "tommorrow" in k:
                p = "tomorrow*"
            elif "begining" in k:
                p = "beginning*"
            elif "^" in m.content:
                if b is True:
                    await self.bot.delete_message(m)
                return
            await self.bot.send_message(m.channel, p)


def setup(bot):
    n = Grammar(bot)
    bot.add_cog(n)