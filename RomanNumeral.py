#! /usr/bin/python
import sys
import re
from StateMachine import StateMachine


class RomanNumeral:
    digits = { "i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000 }

    def __init__(self, s):
        if not re.match('^[ivxlcdm]+$', s, re.IGNORECASE):
            raise Exception("Not a Roman Numeral")

        self.state_machine = StateMachine(self.digits)

        for c in s:
            self.state_machine.char(c)

        self.value = self.state_machine.output()


    def get(self):
        return self.value



if __name__ == "__main__":
    n = RomanNumeral(sys.argv[1])
    print n.get()
