def next_birthday(date, birthdays):
    '''
    Find the next birthday after the given date.

    @param:
    date - a tuple of two integers specifying (month, day)
    birthdays - a dict mapping from date tuples to lists of names, for example,
      birthdays[(1,10)] = list of all people with birthdays on January 10.

    @return:
    birthday - the next day, after given date, on which somebody has a birthday
    list_of_names - list of all people with birthdays on that date
    '''
    later = [d for d in birthdays if d > date]
    if later:
        birthday = min(later)
    else:
        birthday = min(birthdays)  # wrap around to the start of next year
    list_of_names = birthdays[birthday]
    return birthday, list_of_names
