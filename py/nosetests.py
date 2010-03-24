import os
from ConfigParser import SafeConfigParser
from nose.config import Config
from nose.core import TestProgram, collector
import tempfile

from envbuilder.command import Command
from envbuilder.sh import sh
from envbuilder.args import Arguments

class NoseTestCommand(Command):
    """
    Run nose tests (experimental).
    """
    name='py.nose'
    def run(self, args, config):
        for parcel in config.parcels:
            if not parcel.get('no-nose', False):
                nose_opts=parcel.get('nose', {})
                writer = SafeConfigParser()
                writer.add_section('nosetests')
                for key, value in nose_opts.iteritems():
                    if self.nose_has_option(key):
                        writer.set('nosetests', key, value)
                config_file = tempfile.NamedTemporaryFile(delete=False)
                try:
                    writer.write(config_file)
                finally:
                    config_file.close()
                try:
                    options = ['{BINDIR}/nosetests', '-c %s' % config_file.name]
                    options.extend(args.nose_arguments)
                    sh(' '.join(options), cwd=parcel['dir'])
                finally:
                    os.remove(config_file.name)

    def get_arg_parser(self):
        parser = self.get_base_arg_parser()
        parser.add_argument('nose_arguments',
                            help='arguments to pass to nose',
                            nargs='*')
        parser.add_argument('-k', '--keep-config-file',
                            action='store_true',
                            help='Keep the temporary config file when done')
        return parser

    def nose_has_option(self, optname):
        optname = '--' + optname
        nose_config = Config()
        parser = nose_config.getParser()
        return parser.get_option(optname) is not None
