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
    
    #initializing a generator starting at input number or zero
    def __init__(self, start=0):
        self.start = start
        self.next = start
     
    #incrementing up by one each time called
    def generate(self):     
        self.next += 1
        return self.next - 1
    
    #resetting back to start
    def reset(self):
        self.next = self.start
    

