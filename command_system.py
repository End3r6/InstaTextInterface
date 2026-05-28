import shlex
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class CommandContext:
    user_phone: str
    body: str
    args: list[str]
    options: dict[str, str]
    session: dict


@dataclass
class Command:
    name: str
    description: str
    handler: Callable[[CommandContext], str]

def parse_message(body: str):
    tokens = shlex.split(body)

    args = []
    options = {}

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.startswith("--"):
            key = token[2:]

            if i + 1 < len(tokens) and not tokens[i + 1].startswith("--"):
                options[key] = tokens[i + 1]
                i += 2
            else:
                options[key] = "true"
                i += 1
        else:
            args.append(token)
            i += 1

    return args, options