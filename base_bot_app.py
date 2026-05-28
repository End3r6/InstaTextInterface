from command_system import Command, CommandContext


class BaseBotApp:
    name = "base"
    description = "Base Bot App"

    def __init__(self):
        self.commands = {}
        pass

    def execute(self, args, options):
        pass

    def add_command(self, name, handler, description=""):
        self.commands[name] = {
            "handler": handler,
            "description": description
        }