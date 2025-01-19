from .alias import Alias
from workabot.core.bot import Worka


async def setup(bot: Worka) -> None:
    await bot.add_cog(Alias(bot))
