import random

n = 100
between = [0 for i in range(100)]
unload = [0 for i in range(100)]
arrive = [0 for i in range(100)]
start = [0 for i in range(100)]
idle = [0 for i in range(100)]
wait = [0 for i in range(100)]
finish = [0 for i in range(100)]
harbor = [0 for i in range(100)]

between[0] = random.randint(15, 145)
unload[0] = random.randint(45, 90)

arrive[0] = between[0]
HARTIME = unload[0]
MAXHAR = unload[0]
WAITIME = 0
MAXWAIT = 0
IDLETIME = arrive[0]

finish[0] = arrive[0] + unload[0]
for i in range(1, 100):
    between[i] = random.randint(15, 145)
    unload[i] = random.randint(45, 90)
    arrive[i] = arrive[i - 1] + between[i]
    timediff = arrive[i] - finish[i - 1]
    if timediff >= 0:
        idle[i] = timediff
        wait[i] = 0
    else:
        wait[i] = -timediff
        idle[i] = 0
    start[i] = arrive[i] + wait[i]
    finish[i] = start[i] + unload[i]
    harbor[i] = wait[i] + unload[i]
    HARTIME += harbor[i]
    if harbor[i] > MAXHAR:
        MAXHAR = harbor[i]
    WAITIME += wait[i]
    IDLETIME += idle[i]
    if wait[i] > MAXWAIT:
        MAXWAIT = wait[i]
HARTIME = HARTIME / n
WAITIME = WAITIME / n
IDLETIME = IDLETIME / finish[99]
print(HARTIME, MAXHAR, WAITIME, MAXWAIT, IDLETIME)
