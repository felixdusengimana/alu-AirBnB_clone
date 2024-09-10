#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # For a clean exit without an additional prompt
        return True

    def emptyline(self):
        """Overrides the emptyline method to do nothing."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
