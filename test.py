""" test.py docstring """

import bacli

bacli.setDescription(__doc__)


@bacli.command
def run():
    print("Running")
