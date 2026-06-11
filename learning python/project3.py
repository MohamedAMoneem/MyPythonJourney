# this project transforms
# given time in seconds into hours, minutes, and seconds

# before i learnt how to simplify code:

# seconds = input("insert seconds : \n")
# int_seconds = int(seconds)
# hours = int_seconds // 3600
# rest = hours % 3600
# minutes = rest // 60
# second = rest % 60
# print("time is : hours: " + str(hours) + " minutes: " + str(minutes) + "  seconds: " + str(second))

# after:

time = int(input("enter duration: "))
print (f"time is: hours: {time // 3600} minutes: {(time % 3600) // 60} seconds: {(time % 3600) % 60}")