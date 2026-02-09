
import time
# https://docs.python.org/3/library/time.html#time.localtime                  .
# print("%s" % "ft_list")
# print("{:s}" % "ft_list")

time_0f = time.strftime('%B %-d, %Y', time.localtime(0))
print(f"Seconds since {time_0f}: {int(time.time()):,}", end="")
print(f" or {int(time.time()):.2e} in scientific notation")

print(time.strftime("%b %d %Y", time.localtime()))
