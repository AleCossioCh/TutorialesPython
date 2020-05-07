myStr = "Hello World"
# print(dir(myStr))
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())

print(myStr.replace('Hello', 'bye').upper())

print(myStr.count('o'))
print(myStr.count(' '))

print(myStr.startswith('Hel'))
print(myStr.endswith('orld   '))

print(myStr.split())

print(myStr.find('l'))
print(len(myStr))
print(myStr.index('o'))
print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])

print("The string is " + myStr)
print(f"The string is {myStr}")