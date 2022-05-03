import lightbulb, hikari

plError = lightbulb.Plugin("Error Listener")


# region ERROR HANDLERS
@plError.listener(lightbulb.CommandErrorEvent)
async def errorEvent(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Something went wrong with the command `{event.context.command.name}`.", flags=hikari.MessageFlag.EPHEMERAL)
        raise event.exception

    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("You are not the owner of this bot.", flags=hikari.MessageFlag.EPHEMERAL)

    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"This command is on cooldown. Try again in `{exception.retry_after:.0f}` seconds.", flags=hikari.MessageFlag.EPHEMERAL)

    else:
        raise exception

# endregion


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plError)


def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plError)