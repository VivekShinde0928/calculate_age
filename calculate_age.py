"""
Author  : Vivek Shinde
Date    : 31/05/2020
purpose : Practice problem solving
code    : To calculate age after 100 years.Also what will be year as u complete 100 yrs taking age/year of yours as input

"""
#calculate age after 100yrs

while True:
    user_input = input('\nEnter Your age or year: ')
    if user_input.isalpha():
        print('please enter int')
        continue
    else:
        user_input=int(user_input)
        break

if user_input in range(1, 101):
    value1 = 100 - user_input
    value3 = 2020 - user_input
    print(f'\nyou will turn 100 years old after {value1} years in {value3 + 100} ')
elif user_input > 100 and user_input < 1900:
    print('\nyou seem to be the oldest person alive')
elif user_input < 1:
    print('\nyou are not born yet')
elif user_input in range(1900, 2021):
    value2 = user_input + 100
    print(f'\nyou will turn 100 years old in {value2} year')
elif user_input > 2020:
    print('\nyou are dreaming!')
else:
    print("\nsomething went wrong!")


