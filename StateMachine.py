class StateMachine:
    '''state can be one of the following:
        - None: initialising
        - prefix: values that will subtract from the result
        - remainder: values that add to the result
    '''
    prefix = 1
    remainder = 2

    def __init__(self, d):
        self.value = 0
        self.previous = None
        self.digits = d
        ## self.current_string = ""


    def char(self, c):
        if self.previous and self.digits[c] > self.digits[self.previous]:
            # digit is larger, so previous character is now the prefix
            # (subtract twice the digit's value from the total because it's a
            # prefix digit not a remainder digit, so undo the previous addition as well)
            self.value -= self.digits[self.previous] * 2
        self.value += self.digits[c]

        self.previous = c


    def output(self):
        return self.value
