# Libraries
import math

print("Hello, World!")

# Area Calculator
print('=================================')
print('Area Calculator by Carlos Corona')
print('=================================')


# Menu
print('1) Triangle')
print('2) Rectangle')
print('3) Circle')
print('4) Square')
print('5) Quit')


# User choice
choice = input('Which shape: ')

if choice == '1':
    base = int(input('base: '))
    height = int(input('height: '))
    area = (height * base) / 2
    print('The area is', area)
elif choice == '2':
    length = int(input('length: '))
    width = int(input('width: '))
    area = length * width
    print('The area is', area)
elif choice == '3':
    radius = int(input('radius: '))
    area = math.pi * radius ** 2
    print('The area is', area)
elif choice == '4':
    side = int(input('side: '))
    area = side ** 2
    print('The area is', area)
elif choice == '5':
    print('Try again later')