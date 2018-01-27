'''
parms1:每小时薪水
parms2:每周正常工作时间
parms3:每周加班工作时间
return:总周薪
1
'''


def getMoney(hour_my, routine_work_date, overtime_date):
    money = hour_my(routine_work_date + 1.5 * overtime_date)
    return money
