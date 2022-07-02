import time

current_time = time.time()
print(f"Current time: {current_time}")

def speed_calc_decorator(function):
    def wrapper_function():
        starting_time = time.time()
        function()
        ending_time = time.time()
        print(f"{function.__name__} run speed: {ending_time - starting_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()

