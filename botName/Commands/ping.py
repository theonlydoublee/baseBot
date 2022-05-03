import hikari
import lightbulb

pingPL = lightbulb.Plugin("pingPL")


# region Ping Pong
@pingPL.command()
@lightbulb.command("ping", "Says 'pong!'")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_ping(ctx: lightbulb.context):
    # await pingPL.bot.rest.create_message(ctx.channel_id, "Create New Message")
    await ctx.respond('Pong!')
# endregion


def load(bot: lightbulb.BotApp):
    bot.add_plugin(pingPL)


def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(pingPL)

