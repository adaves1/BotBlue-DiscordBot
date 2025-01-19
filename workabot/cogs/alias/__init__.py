from .alias import Alias
from workabot.core.bot import Red


async def setup(bot: Red) -> None:
    await bot.add_cog(Alias(bot))
