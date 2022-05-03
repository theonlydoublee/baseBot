import hikari
from lightbulb.ext import tasks
from dotenv import load_dotenv
import lightbulb, os

# https://github.com/parafoxia/hikari-intro/blob/main/lightbulb_bot/__main__.py

# Create a new message
# await pluginName.bot.rest.create_message(ctx.channel_id, "Create New Message")


def create_bot() -> lightbulb.BotApp:
    # load TOKEN and GUILDS from .env file
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    # GUILDS = (int(os.getenv("GUILD1")),
    #           # int(os.getenv("GUILD2"))
    #           )

    bot = lightbulb.BotApp(
        token=TOKEN,
        # default_enabled_guilds=GUILDS,
        help_slash_command=True,
    )

    @bot.command()
    @lightbulb.command('reload', 'reload plugins')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def cmd_reload(ctx: lightbulb.context.Context) -> None:
        plugins = []

        for e in bot.extensions:
            plugins.append(e)

        for c in plugins:
            # print(c)
            bot.reload_extensions(c)
        await ctx.respond(content='Reloaded the plugins', flags=hikari.MessageFlag.EPHEMERAL)

        # bot.reload_extensions('TestBot.Music.Commands')

    bot.load_extensions_from("./TestBot/Commands")
    # bot.load_extensions_from("./TestBot/Tasks")
    bot.load_extensions_from("./TestBot/Listeners")

    # Loads tasks and autostart tasks will start
    tasks.load(bot)
    return bot


if __name__ == "__main__":
    create_bot().run()
