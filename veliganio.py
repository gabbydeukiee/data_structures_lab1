firstNum = int(input('Enter first Number: '))
secNum = int(input('Enter second Number: '))

if firstNum < secNum:
    print(f"{firstNum} 'is Less than' {secNum}")
elif firstNum > secNum:
    print(f"{firstNum} 'is Greater than' {secNum}")
elif firstNum == secNum:
    print(f"{firstNum} 'is equal to' {secNum}")
else:
    print('Invalid input')

cm1 = input("Enter classmate name 1: ")
cm2 = input("Enter classmate name 2: ")
cm3 = input("Enter classmate name 3: ")

print('Your classmates are: ', cm1,',', cm2,',', cm3)