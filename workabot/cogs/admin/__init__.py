from workabot.core.bot import Worka

from .admin import Admin


async def setup(bot: Worka) -> None:
    await bot.add_cog(Admin(bot))
