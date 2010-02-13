from envbuilder.command import Command
from envbuilder.sh import notify

class hello(Command):
    """
    Print hello world.
    """
    def run(self, args, config):
        notify('Hello, world!')
