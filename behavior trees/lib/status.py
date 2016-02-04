class Status:
    value = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        if self.value is None:
            return 'Running'
        elif self.value is False:
            return 'Failure'
        elif self.value is True:
            return 'Success'

    def __str__(self):
        if self.value is None:
            return '(running)'
        elif self.value is False:
            return '(failure)'
        elif self.value is True:
            return '(success)'

Success = Status(True)
Running = Status(None)
Failure = Status(False)

__all__ = ['Success', 'Failure', 'Running']
