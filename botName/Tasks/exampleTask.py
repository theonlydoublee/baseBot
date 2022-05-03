from lightbulb.ext import tasks
import lightbulb, hikari

plugin = lightbulb.Plugin("statusUpdater")


# @plugin.command
@tasks.task(s=30, auto_start=True)
async def statusUpdater():
    print('Task Ran')


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)
