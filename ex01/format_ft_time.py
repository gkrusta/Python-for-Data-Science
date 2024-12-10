import time

curr_time = time.time()
print(f"Seconds since January 1, 1970: {curr_time} or {curr_time:.2e} in scientific notation")

formated_fate = time.strftime("%b %d %Y")
print(formated_fate)