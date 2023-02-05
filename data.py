import calendar

def work_days_calendar():
    work_days_calendar = []
    years = (2021, 2022)
    free_days = {
        2021: {
            1: (1,6),
            2: (0,0),
            3: (0,0),
            4: (4,5),
            5: (1,3,23),
            6: (3,0),
            7: (0,0),
            8: (15,0),
            9: (0,0),
            10: (0,0),
            11: (1,11),
            12: (25,26)
        },
    
        2022: {
            1: (1,6),
            2: (0,0),
            3: (0,0),
            4: (17,18),
            5: (1,3),
            6: (5,16),
            7: (0,0),
            8: (15,0),
            9: (0,0),
            10: (0,0),
            11: (1,11),
            12: (25,26)
        }
    }
    for year in years:
        for month in range(1, 13):
            for data in calendar.Calendar().itermonthdates(year,month):
                if data.month == month:
                    if data.isoweekday() < 6:
                        try:
                            if data.day not in free_days[year][month]:
                                work_days_calendar.append(str(data.year % 2000) + 
                                (('0' + str(data.month)) if data.month < 10 else str(data.month)) + 
                                (('0' + str(data.day)) if data.day < 10 else str(data.day)))
                        except KeyError:
                            continue
    work_days_calender_t = tuple(work_days_calendar)

    return work_days_calender_t
