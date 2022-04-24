# Airman to Colonel: Cadet Promotions Calculator
# Code written by C/Col George Powell
# Version 1.0

import time, webbrowser
version = 1.0
print('Airman to Colonel: Cadet Promotions Calculator, version {}'.format(version))
print('Code written by C/Col George Powell')
print('This program will tell you if you have enough time in the Cadet Program to reach the Spaatz.')
print('\nBE ADVISED\nThis code is a work in progress, and is not guaranteed to be accurate.\nIf you notice any errors in the calculations, please email me.\nMy CAP email is george.powell@gawg.cap.gov (copy a senior member) and I will try to fix any issues.\nInclude the the name of this program (Airman to Colonel Cadet Promotions Calculator) in the subject line')
WhatToDo = 0
while not WhatToDo == 1 and not WhatToDo == 2:
    print('\nTo run the program, type a 1 and hit enter.\nIf you would like to access the FAQ page then type a 2 and hit enter.')
    addition = int(input('==> '))
    if not addition == "":
        WhatToDo = addition
    else:
        WhatToDo = 0

while WhatToDo == 1:
    print(' 1: C/AB \n 2: C/Amn \n 3: C/A1C \n 4: C/SrA \n 5: C/SSgt')
    print(' 6: C/TSgt \n 7: C/MSgt \n 8: C/SMSgt \n 9: C/CMSgt \n 10: C/CMSgt (1st Ghost)')
    print(' 11: C/2dLt \n 12: C/2dLt (1st Ghost) \n 13: C/1stLt \n 14: C/1stLt (1st Ghost)')
    print(' 15: C/Capt \n 16: C/Capt (1st Ghost) \n 17: C/Capt (2nd Ghost)')
    print(' 18: C/Maj \n 19: C/Maj (1st Ghost) \n 20: C/Maj (2nd Ghost)')
    print(' 21: C/LtCol \n 22: C/Col')
    print('Please enter the corresponding number for your CAP grade:')
    GradeNumber = int(input('==> '))
    print('Please enter your age')
    Age = int(input('==> '))
    if Age < 11 or Age > 21:
        print('Your age is not in the proper cadet age range')
        if Age < 11:
            Age = 12
    AgeInMonths = Age * 12
    PromotionsRemaining = 22 - GradeNumber
    MonthsPlusSpaatz = PromotionsRemaining * 2
    if MonthsPlusSpaatz >= 2:
        Months = MonthsPlusSpaatz -2
    else:
        Months = 0
    print('You have {} promotions remaining. That is about {} months of nonstop promoting.'.format(PromotionsRemaining, Months))
    if GradeNumber >= 22:
        print('But it looks like you have already earned your Spaatz. Congratulations!')
    elif Months < 216 - AgeInMonths:
        TimeLeft = 216 - AgeInMonths
        #print(TimeLeft)
        print('If you promote regularly may be able to reach C/Col by the time you are 18 years old.')
        #print('To reach your Spaatz before you turn 18, you should promote at least every {} months'.format(TimeLeft // Months))
    else:
        if Months < 252 - AgeInMonths:
            print('You cannot reach C/Col before you turn 18, but you can get your Spaatz before you turn 21.')
        else:
            print('Unfortunately, you will not have the time to become a Cadet Colonel before you age out of the program.')
            print('Although you will not be able to reach this milestone, this is only one of the opportunities that the CAP cadet program provides, and I encourage you to continue promoting to rise as high in the ranks as you can.')
    time.sleep(10)
    print('\n\n\n\n\n\n\n\n\n\n\n\nIf you found this program useful, please consider leaving a good review on HUBCAP!')
    time.sleep(5)
    z = input('\n\n\nPress enter to run this program again.')
    print('\n\n\n\n\n\n')

if WhatToDo == 2:
    print('\n\nAirman to Colonel Cadet Promotions Calculator Frequently Asked Questions: \n\nQ: The program stops and displays an error message. What went wrong?\nA: If the message started with [Traceback (most recent call last)] then an invalid character was probably entered. This program only accepts inputs of intergers. Anything else will probably result in an error message.')
    print('\nQ: Does this program store any of my information?\nA: This program does not record any information that you enter. After you close the program, all information is cleared.')
    print('\n \nThis FAQ page is a work in progress.\nPlease send any questions you have to george.powell@gawg.cap.gov and copy a senior member.\nBe sure to include the name of this project (Airman to Colonel Cadet Promotions Calcuator) in the subject line.')
    print('If you would prefer to submit your feedback via Google Forms, type 1 and press Enter')
    closeProgram = input('If you want to stop this program, just press Enter: ')
    if closeProgram == '1':
         webbrowser.open('https://forms.gle/ipTjo6Z89HdpU9p4A')
   
