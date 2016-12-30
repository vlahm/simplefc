"""
simplefc (simple flash card)

Usage:
  simplefc create_set <setname>
  simplefc add_entry <setname> (-i <entry>... | -f <file>...)
  simplefc study [-tdbamfsr] <setname>
  simplefc view_set <setname>
  simplefc view_archive <setname>
  simplefc unarchive <setname> <ID>...
  simplefc delete_entry <setname> <ID>...
  simplefc list_sets
  simplefc delete_set <setname>
  simplefc [-h | --help]
  simplefc [-v | --version]

Options:
  -h --help  Show this page.
  -v --version  Show version.
  -a  Include all entries.
  -m  Include many entries, but exclude the easy ones. Useful
      after logging substantial study time.
  -f  Include few entries, only the hard ones. Useful after
      logging substantial study time.

Examples:
  simplefc -C 'biology 450 final'
  simplefc -a 'biology 450 final' -i 'xanthophyll~a yellow or brown carotenoid pigment found in plants; anthocyanin~a red flavonoid pigment found in plants'
  simplefc -S 'biology 450 final' -z

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/vlahm/simplefc
"""

from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION

def main():
    """Main CLI entrypoint."""
    import simplefc.commands
    options = docopt(__doc__, version=VERSION)

    for k, v in options.items():
        if hasattr(simplefc.commands, k) and v:
            module = getattr(simplefc.commands, k)
            simplefc.commands = getmembers(module, isclass)
            command = [command[1] for command in simplefc.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
