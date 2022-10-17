# Task 1
def ValidateNum (num1) :
    if (0 <= num1 <= 100):
        Valid = True
    else:
        Valid = False
    return Valid

integer = int(input("Please enter a number between 0 & 100"))
print(ValidateNum(integer))

# Task 2
def CheckUpperLower(string) :
    Upper = 0
    Lower = 0
    for letter in string:
        if letter.isupper():
            Upper += 1
        elif letter.islower():
            Lower += 1
    print( "No. of Upper case characters : %s,No. of Lower case characters : %s" % (Upper,Lower))


Text = input("Please enter a string")
CheckUpperLower(Text)

# Task 3
def Greeting(Name) :
    print()
    NewName = ""
    for letter in Name:
        if (Name[0].isupper()):
            NewName = Name[0].upper() + Name[1:].lower()
        elif (Name[0].islower()):
            NewName = Name[0].upper() + Name[1:].lower()
    print("Hello! ", NewName)
Name = input("Please enter your name")
Greeting(Name)

# Task 4
def RemoveLast(string):
    print()
    NewString = string[:-1]
    return NewString

string = input("Enter a string")
print("Returned string: " + RemoveLast(string))

# Task 5
def ConvertDegrees(Celcius):
    fahrenheit = float((Celcius * 1.8) + 32)
    print(str(Celcius) + " converted into fahrenheit is " + str(fahrenheit))

def ConvertFahrenheit(Fahrenheit):
    celcius = float((Fahrenheit / 1.8) - 32)
    print(str(Fahrenheit) + " converted into celcius is " + str(celcius))

choice = input("Choose which to convert (C)elcius or (F)ahrenheit")
number = float(input("How much degrees/fahrenheit?"))
if choice == 'F':
    ConvertFahrenheit(number)
elif choice == 'C':
    ConvertDegrees(number)

# Task 6
def ConvertDegrees(Celcius):
    fahrenheit = float((Celcius * 1.8) + 32)
    print(str(Celcius) + "C converted into fahrenheit is " + str(fahrenheit))

number = float(input("How much degrees: "))
ConvertDegrees(number)