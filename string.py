# task 1

word = input("enter word")
def wo(soz):

    y = soz[0]
    x = soz[1]
    print(f"{y}{x}... {y}{x}... {soz}?")
wo(word)


# task 2

name = input("Enter name: ")
person = {
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother in law",
    "R2D2": "droid"
}
def find_relatives(ism, inson):
    for people in inson.keys():
        if ism == people:
            print(f"Luke i'm your {inson[people]}")
            break
    else:
        print("Nope")
find_relatives(name, person)



# task 3


mood = input("enter feel:")
def feeling(kayfiyat):
    if kayfiyat != "":
        print(f"Today,i am feeling {kayfiyat}")

    else:
        print("Today I am feeling neutral")

feeling(mood)



# task 4



word = input("enter words:")
vowels = "aouie"
result = 0
def vow(soz,unli,res):
    for x in soz:
        if x in unli:
            res = res + 1
    print(res)

vow(word,vowels,result)
# loop task 4
lst = [3, 6, 12, 36]
def factor_chain(lst):
    lst1 = []
    for x in lst:
        if lst[-1] % x == 0:
            lst1.append(x)
    return len(lst) == len(lst1)

print(factor_chain(lst))



# task 6



string = "the aardvark"

vowel = ["a","e","i","o","u"]
def replace_vowels(string,vowel):
    for x in string:
        if x in vowel:
            string = string.replace(x,"#")
    return string



print(replace_vowels(string,vowel))




# task 7



number = "1234123456785678"
str = ""
for x in number[:12]:
    number = number.replace(x, "*")
print(number+"5678")



# task 8


input = input("Enter string:")

def task(input):
    x = input.count("x")
    o = input.count("o")
    if x == o:
        print(True)
    elif x <= o or x >= o:
        print(False)
    else:
        print(True)

task(input)

# task 9


name = input("enter:")
x = name.split(" ")
y = x[0]
s = x[1]
print(f"{s} {y}")



# task 10



string = "abcde"
string1 = "abcwf"

def uniwue(string, string1):
    i  = 0
    for x in string:
        for y in string1:
            if x==y:
                i+=1
    print(len(string)-i)

uniwue(string, string1)