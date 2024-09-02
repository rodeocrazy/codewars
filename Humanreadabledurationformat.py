def format_duration(seconds):
    end = ""

    if seconds == 0:
        return 'now'

    years, days, hours, minutes = 0, 0, 0, 0
    y, d, h, m, s = "", "", "", "", ""

    if (seconds // (60*60*24*365)) >= 1:
        years = seconds // (60*60*24*365)
        seconds -= years * (60*60*24*365)

    if (seconds // (60*60*24)) >= 1:
        days = seconds // (60*60*24)
        seconds -= days * (60*60*24)

    if (seconds // (60*60)) >= 1:
        hours = seconds // (60*60)
        seconds -= hours * (60*60)

    if (seconds // (60)) >= 1:
        minutes = seconds // (60)
        seconds -= minutes * (60)

    lst = [years, days, hours, minutes, seconds]

    if years >= 1:
        y = 'year'
        if years > 1:
            y = 'years'
        end += str(years) + " " + y
        if lst.count(0) == 3:
            end += ' and '
        if lst[2:].count(0) <= 2:
            end += ', '

    if days >= 1:
        d = 'day'
        if days > 1:
            d = 'days'
        end += str(days) + " " + d
        if lst[1:].count(0) == 2 and lst[:2].count(0) < 1:
            end += ' and '
        if lst[2:].count(0) <= 1:
            end += ', '

    if hours >= 1:
        h = 'hour'
        if hours > 1:
            h = 'hours'
        end += str(hours) + " " + h
        if lst[2:].count(0) == 1 and lst[:3].count(0) < 2:
            end += ' and '
        if lst[2:].count(0) == 0:
            end += ', '

    if minutes >= 1:
        m = 'minute'
        if minutes > 1:
            m = 'minutes'
        end += str(minutes) + " " + m
        if lst[3:].count(0) == 0:
            end += ' and '

    if seconds >= 1:
        s = 'second'
        if seconds > 1:
            s = 'seconds'
        end += str(seconds) + " " + s

    return end