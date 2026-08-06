hour = float(input("starting time (hour)"))
minute = float(input("starting time (minute)"))
duration = float(input("starting time (duration)"))
minute = minute + duration 
hour = hour = duration
minute = minute % 60 
hour = hour % 60
print(hour, ",", minute, sep="")