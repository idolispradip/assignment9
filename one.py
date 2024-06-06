import functools
import time
from datetime import datetime

def log_execution(log_file_path):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper_log(*args, **kwargs):
            start_time = time.time()
            start_datetime = datetime.now()
            
            result = func(*args, **kwargs)
            
            end_time = time.time()
            end_datetime = datetime.now()
            time_spent = end_time - start_time
            
            log_entry = (
                f"Function: {func.__name__}\n"
                f"Start Time: {start_datetime}\n"
                f"End Time: {end_datetime}\n"
                f"Result: {result}\n"
                f"Time Spent: {time_spent:.4f} seconds\n"
                f"{'-'*40}\n"
            )
            
            with open(log_file_path, 'a') as log_file:
                log_file.write(log_entry)
            
            return result
        return wrapper_log
    return decorator_log

# Example usage
@log_execution('execution_log.txt')
def example_function(x, y):
    return x + y

# Call the function to test the logging
example_function(5, 10)
