import os
# install base libraries, comment out the os.system lines after running
# os.system('powershell pip install hikari, hikari-lightbulb, python-dotenv, tasks')
# os.system('cls')
import hikari
from lightbulb.ext import tasks
from dotenv import load_dotenv
import lightbulb

rootFile = next(i for i in os.listdir(os.getcwd()) if 'bot' in i.lower())

def create_bot() -> lightbulb.BotApp:
    # load TOKEN and GUILDS from .env file
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

    bot = lightbulb.BotApp(
        token=TOKEN,
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

    bot.load_extensions_from(f"./{rootFile}/Commands")
    # bot.load_extensions_from("./{rootFile}/Tasks")
    bot.load_extensions_from(f"./{rootFile}/Listeners")

    # Loads tasks and autostart tasks will start
    tasks.load(bot)
    return bot


if __name__ == "__main__":
    create_bot().run()
