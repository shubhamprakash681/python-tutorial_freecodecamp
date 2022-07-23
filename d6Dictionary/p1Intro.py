# same as pair in c++

month_conversion = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

print(month_conversion['Jan'])
print(month_conversion.get('Dec'))
print(month_conversion.get('HUU'))  # returns None
print(month_conversion.get('HUU', 'Not a valid key'))   # returns 'Not a valid key' since 'HUU' is not present
