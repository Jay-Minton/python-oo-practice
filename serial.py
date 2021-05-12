"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """Creates the machine and sets the inital value"""
        self.start = start
        self.current = start
    
    def generate(self):
        """Increments the machine by one"""
        print(self.current)
        self.current += 1

    def reset(self):
        """Resets the machine back to it's inital value"""
        self.current = self.start
