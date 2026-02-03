from __future__ import annotations

import datetime
import discord
import math
import random

from discord.ext import commands
from typing import TYPE_CHECKING
from utils.checks import is_staff
from utils.utils import KurisuCooldown

if TYPE_CHECKING:
    from kurisu import Kurisu
    from typing import Optional
    from utils.context import KurisuContext


class Memes(commands.Cog):
    """
    Meme commands
    """

    def __init__(self, bot: Kurisu):
        self.bot: Kurisu = bot
        self.bot.loop.create_task(self.init_memes())
        self.extras = bot.extras

        self.excluded = [self._listmemes]

        for command in self.walk_commands():
            if command not in self.excluded and not command.cooldown:
                command._buckets = commands.DynamicCooldownMapping(KurisuCooldown(1, 15.0), commands.BucketType.channel)

    async def cog_check(self, ctx: KurisuContext) -> bool:
        if ctx.guild is None or ctx.command in self.excluded or isinstance(ctx.author, discord.User):
            return True
        return not (ctx.channel in self.bot.assistance_channels)

    async def cog_command_error(self, ctx: KurisuContext, error: commands.CommandError):
        if isinstance(error, commands.CheckFailure) and ctx.channel.guild is not None:
            await ctx.message.delete()
            try:
                await ctx.author.send(
                    "Meme commands are disabled in this channel, or your privileges have been revoked.")
            except discord.Forbidden:
                await ctx.send(
                    f"{ctx.author.mention} Meme commands are disabled in this channel, or your privileges have been revoked.")

    async def init_memes(self):
        await self.bot.wait_until_all_ready()
        self.emoji = discord.utils.get(self.bot.guild.emojis, name='fug') or discord.PartialEmoji.from_str("⁉")
        self.wagu_emoji = discord.utils.get(self.bot.guild.emojis, name="wagu") or "⁉"
        self.waguspooky = discord.utils.get(self.bot.guild.emojis, name="waguspooky") or "⁉"
        self.waguxmas = discord.utils.get(self.bot.guild.emojis, name="waguxmas") or "⁉"
        self.waguspin = discord.utils.get(self.bot.guild.emojis, name="waguspin") or "⁉"
        self.waguspinaaa = discord.utils.get(self.bot.guild.emojis, name="waguspinaaa") or "⁉"
        self.waguwat = discord.utils.get(self.bot.guild.emojis, name="waguwat") or "⁉"
        self.waguwu = discord.utils.get(self.bot.guild.emojis, name="waguwu") or "⁉"
        self.waguw = discord.utils.get(self.bot.guild.emojis, name="waguw") or "⁉"
        self.hyperwagu = discord.utils.get(self.bot.guild.emojis, name="hyperwagu") or "⁉"
        self.wagupeek = discord.utils.get(self.bot.guild.emojis, name="wagupeek") or "⁉"
        self.poggu = discord.utils.get(self.bot.guild.emojis, name="poggu") or "⁉"
        self.waguburger = discord.utils.get(self.bot.guild.emojis, name="waguburger") or "⁉"
        self.wagucar = discord.utils.get(self.bot.guild.emojis, name="wagucar") or "⁉"
        self.shutwagu = discord.utils.get(self.bot.guild.emojis, name="shutwagu") or "⁉"
        self.waguboat = discord.utils.get(self.bot.guild.emojis, name="waguboat") or "⁉"
        self.wagutv = discord.utils.get(self.bot.guild.emojis, name="wagutv") or "⁉"
        self.ghostwagu = discord.utils.get(self.bot.guild.emojis, name="ghostwagu") or "⁉"
        self.flushedsquish = discord.utils.get(self.bot.guild.emojis, name="flushedsquish") or "⁉"
        self.flushedball = discord.utils.get(self.bot.guild.emojis, name="flushedball") or "⁉"
        self.flushedeyes = discord.utils.get(self.bot.guild.emojis, name="flushedeyes") or "⁉"
        self.plusher_flusher = discord.utils.get(self.bot.guild.emojis, name="plusher_flusher") or "⁉"
        self.isforme = discord.utils.get(self.bot.guild.emojis, name="isforme") or "⁉"
        self.flushedtriangle = discord.utils.get(self.bot.guild.emojis, name="flushedtriangle") or "⁉"
        self.flushedstuffed = discord.utils.get(self.bot.guild.emojis, name="flushedstuffed") or "⁉"
        self.flushedsquare = discord.utils.get(self.bot.guild.emojis, name="flushedsquare") or "⁉"
        self.flushedskull = discord.utils.get(self.bot.guild.emojis, name="flushedskull") or "⁉"
        self.flushedmoon = discord.utils.get(self.bot.guild.emojis, name="flushedmoon") or "⁉"
        self.flushedhot = discord.utils.get(self.bot.guild.emojis, name="flushedhot") or "⁉"
        self.flushedhand = discord.utils.get(self.bot.guild.emojis, name="flushedhand") or "⁉"
        self.flushedhalf = discord.utils.get(self.bot.guild.emojis, name="flushedhalf") or "⁉"
        self.flushedgoomba = discord.utils.get(self.bot.guild.emojis, name="flushedgoomba") or "⁉"
        self.flushedflat = discord.utils.get(self.bot.guild.emojis, name="flushedflat") or "⁉"
        self.flushedcowboy = discord.utils.get(self.bot.guild.emojis, name="flushedcowboy") or "⁉"
        self.flushedwater = discord.utils.get(self.bot.guild.emojis, name="flushedwater") or "⁉"
        self.flushedw = discord.utils.get(self.bot.guild.emojis, name="FlushedW") or "⁉"
        self.flushedhalf2 = discord.utils.get(self.bot.guild.emojis, name="flushedhalf2") or "⁉"
        self.flushedroulette = discord.utils.get(self.bot.guild.emojis, name="flushedroulette") or "⁉"
        self.flushedcushion = discord.utils.get(self.bot.guild.emojis, name="flushedcushion") or "⁉"
        self.flushedcrush = discord.utils.get(self.bot.guild.emojis, name="flushedcrush") or "⁉"
        self.isforme2 = discord.utils.get(self.bot.guild.emojis, name="isforme2") or "⁉"
        self.isforme3 = discord.utils.get(self.bot.guild.emojis, name="isforme3") or "⁉"
        self.flushed5 = discord.utils.get(self.bot.guild.emojis, name="flushed5") or "⁉"
        self.flushedbold = discord.utils.get(self.bot.guild.emojis, name="flushedbold") or "⁉"
        self.joyclap = discord.utils.get(self.bot.guild.emojis, name="joyclap") or "⁉"

    async def _meme(self, ctx: KurisuContext, msg, directed: bool = False, image_link: Optional[str] = None,
                    allowed_mentions: Optional[discord.AllowedMentions] = None):

        if image_link is not None:
            title = f"{self.bot.escape_text(ctx.author.display_name) + ':' if not directed else ''} {msg}"
            embed = discord.Embed(title=title, color=discord.Color.default())
            embed.set_image(url=image_link)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.bot.escape_text(ctx.author.display_name) + ':' if not directed else ''} {msg}",
                           allowed_mentions=allowed_mentions)

    # list memes
    @commands.command(name="listmemes")
    async def _listmemes(self, ctx: KurisuContext):
        """List meme commands."""
        cmds = ", ".join([x.name for x in self.get_commands()][1:])
        await self._meme(ctx, f"```{cmds}```")

    @is_staff("Moderator")
    @commands.guild_only()
    @commands.command(hidden=True, aliases=['🍰', 'cake'])
    async def birthday(self, ctx: KurisuContext, member: discord.Member):
        """Wishes a happy birthday. Do not abuse pls."""

        await ctx.message.delete()
        try:
            await member.add_roles(self.bot.roles['🍰'])
        except discord.Forbidden:
            return

        timestamp = datetime.datetime.now(self.bot.tz)
        delta = datetime.timedelta(seconds=86400)
        expiring_time = timestamp + delta

        await self.extras.add_timed_role(member, self.bot.roles['🍰'], expiring_time)
        await ctx.send(f"Happy birthday {member.mention}!")

    @commands.command(hidden=True)
    async def hru(self, ctx: KurisuContext):
        """Finally asking how Aurisu is."""
        feeling_list = ["AWFUL", "stfu", "alright", "I am a bot what the fuck do you think?", "DREAMING ABOUT OBTAINING XS00000003", "Look at the assistance channels for two minutes and tell me how **you** think I am."]
        await ctx.send(random.choice(feeling_list))

    @commands.command(hidden=True)
    async def rotate(self, ctx: KurisuContext, u: discord.Member, degrees: int = None):
        """Rotate a user 🌪️"""
        MAX_DEGREES = 10000

        base_degrees = random.randint(-1080, 1080)
        is_kurisu = (u.id == self.bot.user.id)  # are we Kurisu?

        if degrees is not None:
            if abs(degrees) > MAX_DEGREES:
                await ctx.send(f"That's too much rotation. Please keep it within ±{MAX_DEGREES} degrees.")
                return
            total_degrees = base_degrees + degrees
        else:
            total_degrees = base_degrees

        total_rotations = total_degrees / 360

        msg = f"{u.mention + ' has' if not is_kurisu else 'I have'} been rotated {base_degrees} degrees. "

        if degrees is not None:
            msg += f"This means {'the user is' if not is_kurisu else 'I am'} now at {total_degrees} degrees, which is"
        else:
            msg += "That is"  # lol

        if total_degrees < 0:  # directions update
            msg += f" {abs(total_rotations):.2f} leftward rotations."
        else:
            msg += f" {total_rotations:.2f} rightward rotations."

        await self._meme(ctx, msg, True)


async def setup(bot):
    await bot.add_cog(Memes(bot))
