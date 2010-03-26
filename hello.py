from envbuilder.command import Command
from envbuilder.sh import notify, sh

class hello(Command):
    """
    Print hello world.
    """
    name = 'hello'
    def run(self, args, config):
        notify('Hello, world!')

class hellosh(Command):
    """
    Print hello world.
    """
    name = 'hello'
    def run(self, args, config):
        sh("echo 'Hello, world!'")
