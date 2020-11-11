def get_hour_angle(h,m):
    #angel independent of minute hand
    hour_angle=h*30
    if hour_angle==360:
        hour_angle=0
    #angel depending on minute hand
    hour_angle+=((m/60)*30)
    return hour_angle

def calcAngle(h, m):
    hour_angle=get_hour_angle(h,m)
    minute_angle=m*6
    return abs(minute_angle-hour_angle)

print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165