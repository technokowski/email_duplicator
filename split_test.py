

email = ['abcd1234@natomas.org', 'abcd12345@natomas.org', 'bbjjdd34566@natomas.org', 'uuiidd4455@natomas.org']

# for i in email:
#     first_split = i.split('@')
#     second_split = first_split[0].split('1')
#     print(second_split)

for i in email:
    count = 0
    temp = list(i)
    for item in temp:
        if (item.isdigit()):
            count = count + 1
        else:
            pass
    if count == 5:
        print("*" * 15)
        print('Wrong Email')
        print(i)
        print("*" * 15)
    elif count == 4:
        print('Correct Email')
    else:
        print('oopsy')
