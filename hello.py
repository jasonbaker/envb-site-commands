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

class helloweb(Command):
    """
    Run a webserver that prints hello world
    """
    name='helloweb'
    py_dependencies=['cherrypy']
    def run(self, args, config):
        import cherrypy
        class HelloWorld(object):
            def index(self):
                return 'Hello, world!'
            index.exposed=True
        cherrypy.quickstart(HelloWorld())

class named_hello(Command):
    """
    Prints hello to a specified user.
    """
    name = 'named_hello'
    def get_arg_parser(self):
        parser = self.get_base_arg_parser()
        parser.add_argument('--name', default='world',
                            help='Specify who we are greeting')
        return parser

    def run(self, args, config):
        notify('Hello, %s!' % args.name)
