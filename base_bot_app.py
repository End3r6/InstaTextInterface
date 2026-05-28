from command_system import Command, CommandContext


class BaseBotApp:
    name = "base"
    description = "Base Bot App"

    def __init__(self):
        self.commands = {}
        self.register_commands()

    def execute(self, args, options):
        if not args:
            return self.help()

        command_name = args[0]

        if command_name == "help":
            return self.help()

        command = self.commands.get(command_name)

        if not command:
            return f"Unknown command: {command_name}\n\n{self.help()}"

        return command["handler"](args[1:], options)

    def register_commands(self):
        pass

    def add_command(self, name, handler, description=""):
        self.commands[name] = {
            "handler": handler,
            "description": description
        }

    def help(self):
        lines = [f"{self.name} commands:"]
        for name, command in self.commands.items():
            lines.append(f"- {name}: {command['description']}")
        return "\n".join(lines)