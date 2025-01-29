import signal, threading
from contextlib import contextmanager

def timeout_handler(signum, frame):
    raise TimeoutError("Execution timed out!")

# TODO: fix this, still failing
def timeout_windows(seconds):
    timer = threading.Timer(seconds, lambda: (_ for _ in ()).throw(TimeoutError("Execution timed out!")))
    timer.start()
    return timer

@contextmanager
def timeout(seconds):
    if hasattr(signal, 'SIGALRM'):  # Unix-like systems
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(seconds)
        try:
            yield
        finally:
            signal.alarm(0)
    else:  # Windows
        timer = timeout_windows(seconds)
        try:
            yield
        finally:
            timer.cancel()