is_male = True
is_tall = False
if is_male and is_tall:
    print('You are a TALL MALE')
elif is_male and not is_tall:
    print('You are a SHORT MALE')
elif is_male or is_tall:
    print('You are either a male or tall')
else:
    print('You are NEITHER male NOR tall')
