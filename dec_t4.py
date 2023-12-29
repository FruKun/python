import time

def retry(max_tries, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            tries = 0
            times = 0 
            while tries < max_tries:
                result = func(*args, **kwargs)
                if result:
                    return result
                tries += 1
                times += delay * tries
                time.sleep(delay * tries)
            raise Exception("Function execution failed after " + str(tries) + " tries and " + str(times) + " seconds")
        return wrapper
    return decorator

@retry(max_tries=3, delay=2)
def some_function(b):
    if b:
        return True
    else:
        return False

result = some_function(False)
print(result)
