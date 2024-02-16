#task 2
string = "abCBAaAAAAa"
def steps_to_convert(string):
    res = 0
    for x in string:
        if x.isupper():
            res += 1
    return res
print(steps_to_convert(string))


# task 3

txt = "How to ace BC Calculus in 5 Easy Steps"
def prevent_distractions(txt):
    lst = ("anime", "meme", "vines", "roasts", "Danny DeVito")
    for x in lst:
        if x in txt:
            return "NO!"

    return "Safe watching!"

print(prevent_distractions(txt))


# task 4
lst = [3, 6, 12, 36]
def factor_chain(lst):
    lst1 = []
    for x in lst:
        if lst[-1] % x == 0:
            lst1.append(x)
    return len(lst) == len(lst1)

print(factor_chain(lst))


# task 4
lst = [3, 6, 12, 36]
def factor_chain(lst):
    lst1 = []
    for x in lst:
        if lst[-1] % x == 0:
            lst1.append(x)
    return len(lst) == len(lst1)

print(factor_chain(lst))

# task 7
dates = ["Sept 22", "Sept 21", "Oct 15"]
month = input("Month: ")
def upload_count(dates,month):
    l = len(month)
    res = 0
    for i in dates:
        if i[:l] == month:
            res += 1
    return res

print(upload_count(dates,month))