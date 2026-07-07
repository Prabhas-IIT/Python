def add_time(start, duration, day=''):

    #Conversion to 24 hr time format
    pmam = start[-2:]
    col_pos = start.index(':')
    minutes = int(start[col_pos+1:col_pos+3])
    if pmam == 'PM':
        hr = int(start[:col_pos]) + 12
    else:
        hr = int(start[:col_pos])

    #scraping time to be added
    hradd = int(duration[:duration.index(':')])
    minadd = int(duration[-2:])
    
    #adding time and tracking days added
    days = 0
    minutes += minadd
    if minutes >= 60:
        hr += 1
        minutes = minutes % 60
    hr += hradd
    if hr > 24:
        days += hr // 24
        hr = 24 if hr%24 == 0 else hr % 24    

    #Conversion of time back to 12hr format
    if hr >= 12 and hr != 24:
        pmam = 'PM'
        hr = 12 if hr == 12 else hr % 12
    else:
        pmam = 'AM'
        hr = 12 if hr == 24 else hr

    #days passed
    if days == 0:
        days_passed = ''
    elif days == 1:
        days_passed = ' (next day)'
    else:
        days_passed = f' ({days} days later)'

    #which day
    if day:
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']    
        for week_day in week:
            if week_day.lower() == day.lower():
                day_index = week.index(week_day)
        day_index += days
        day = week[day_index % 7]
        day = f', {day}'
    
    #final time
    new_time = f'{hr}:{str(minutes).zfill(2)} {pmam}{day}{days_passed}'

    return new_time
