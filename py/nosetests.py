from nose.config import Config
from nose.core import TestProgram, collector

from envbuilder.command import Command

class NoseTestCommand(Command):
    """
    Run nose tests (experimental).
    """
    name='py.nosetests'
    def run(self, args, config):
        for parcel in config.parcels:
            nose_opts=parcel.get('nose', {})
            tester = TestProgram(exit=False, env=nose_opts, argv=args.nose_arguments)
            tester.runTests()

    def get_arg_parser(self):
        parser = self.get_base_arg_parser()
        parser.add_argument('nose_arguments',
                            help='arguments to pass to nose',
                            nargs='*')
        
        return parser
