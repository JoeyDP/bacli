""" example.py: This file serves as a demonstration of the bacli functionality. """

import bacli


with bacli.cli(__doc__) as cli:

    @cli.command
    def run():
        """ Run the model. """
        print("Running")


    @cli.command
    def train(iterations: int, batch_size: int=32):
        """ Train the model. """
        print("Training model")
        print("{} iterations".format(iterations))
        print("batch size of {}".format(batch_size))
