class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, experssion, message):
        self.experssion = experssion
        self.message = message

class TransitionError(Error):
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
