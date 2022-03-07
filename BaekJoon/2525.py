hour, minute = map(int, input().split())
ovenTime = int(input())
minute += ovenTime
newHour = 0

if minute >= 60:
    newHour += minute // 60
    hour += newHour
    minute -= newHour * 60
    if hour >= 24:
        hour -= 24

print(hour, minute)
