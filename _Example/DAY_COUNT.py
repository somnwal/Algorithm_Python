import datetime

# 오늘 일자
today = datetime.datetime.now()
target = "2023-11-30"

holiday = ["2023-01-01",
           "2023-01-21",
           "2023-01-22",
           "2023-01-23",
           "2023-01-24",
           "2023-03-01",
           "2023-05-05"]

count = 0
count_except_holiday = 0

while today.strftime("%Y-%m-%d") <= target:
    today = today + datetime.timedelta(days=1)

    if today.strftime("%Y-%m-%d") not in holiday:
        if today.weekday() not in [5, 6]:
            count_except_holiday += 1
    count += 1


print("휴일 제외 : ", count_except_holiday)
print("휴일 포함 : ", count)
