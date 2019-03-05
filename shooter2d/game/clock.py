import time


def clocked_function(func):
    func.last_called = time.time()

    def wrapper(*args, **kwargs):
        now = time.time()
        response = func(*args, **kwargs, dt=(now - func.last_called))
        func.last_called = now
        return response
    return wrapper
