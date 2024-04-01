#first task
def generateArray(length:int,start:int):
    if isinstance(length,int) and isinstance(start,int):
        arr=[]
        for i in range(start,start+length):
            arr.append(i)
        return arr
    else:
        return "invalid data type" 
try:
    length = int(input("please input a value for length "))
    start = int (input ("enter the start point ") )
    print(generateArray(length, start))
except ValueError:
    print("Please enter valid number")


#second task
def divisibleBy3OR5(number):
    if isinstance(number,int):
        if number%3==0 and number%5==0:
            return "fizzbuzz"
        elif number%3==0:
            return "fizz"
        elif number%5==0:
            return "buzz"
        else:
            return "not divisible on 3 or 5"
    else:
        return "not valid datatype"
    
try:
    number = int(input("please enter the number"))
    print(divisibleBy3OR5(number))
except ValueError:
    print("please enter valid number")

#revsee a string form user 
def reverse_string():
    inpt = input("please enter your string ")
    reverse_string = inpt[::-1]
    return reverse_string

print(reverse_string());


####
import re

def validate_name(name):
    return len(name.strip()) > 0 and name.isalpha()
def validate_email(email):
    return re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email.strip()) is not None

def get_name():
    while True:
        name = input("pleas enter your name ").strip()
        if validate_name(name):
            return name
        else:
            print("invalid name please enter valid name")
def get_email():
    while True:
        email = input("please enter your email: ").strip()
        if validate_email(email):
            return email
        else:
            print("invalid email  please enter valid email.")

name = get_name()
email = get_email()
print(f"name: {name}\n email: {email}")

#####

def longestSubstring(inpt):
    inpt = inpt.lower()
    longest = ""
    current = inpt[0]
    for char in inpt[1:]:
        if ord(char) >= ord(current[-1]):
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = char

    return longest

input_str = input("pleas enter a string ")
longest_substring = longestSubstring(input_str)
print("the longest substring is :", longest_substring)

#####


sum = 0
count = 0

while True:
    inpt = input("please enter a number or done to exit the entering  ")
    if inpt.lower() == "done":
        break
    try:
        number = float(inpt)
        sum += number
        count += 1
    except ValueError:
        print("invalid input please enter a number or done ")

if count > 0:
    average = sum / count
    print(f"total: {sum}")
    print(f"count : {count}")
    print(f"average : {average}")
else:
    print("there is no numbers  ")

