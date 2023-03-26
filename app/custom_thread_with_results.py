import threading


class CustomThreadWithResult(threading.Thread):
    """
        Here we are overriding the parent class because we want data to be returned from the thread when is finish job.
    """
    result = None

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.result = target(*args, **kwargs)

        super().__init__(group=group, target=function, name=name, daemon=daemon)
