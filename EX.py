lis = [5, 7, 233, 8, -1, 93, -4, 301]

min = lis[0]
for i in lis:
    if i < min:
        min = i

print(min)







lis = [5, 7, 233, 8, 301, -1, 93, -4]

max = lis[0]
sec_max = lis[0]
for i in lis:
    if i > max:
        sec_max = max
        max = i

print(sec_max)







lis = [5, 7, 4, 8, 9, 2]

sum = 0
for i in lis:
    sum += i

print(sum)






info = ["Some", 7, -2.33, 6, 0.01, "data"]

for el in info:
    print(el)

nums = [7, -2.33, 6, 0.01]

for num in nums:
    if num > 0:
        continue

    print(num)








students = {
    "physics": ["Bob", "Alex", "Micke"],
    "math": ["Bob", "Alex", "Micke"],
    "biology": ["Bob", "Alex", "Micke"],
}

print(students)
print(students['math'])





info = {"MainKey": "MainValue"}

for sym in info['MainKey']:
    print(sym)


info = {"Alex": 35, "Bob": 40, "Mike": 23}
info.pop('Bob')
info['Mike'] = 24

print(info.keys())
info.clear()
print(info)







tup = ("Hi", ", how are", " you?")

string = ""
for i in tup:
    string += i

print(string)

i = 4
while i <= 13:
    if i != 7 and i != 11:
        print(i ** 2)

    i += 1





nums = (7, 0, -4, 2, 9, -5)

sum = 0
for el in nums:
    if el > 0:
        sum += el

print(sum)






numbers = "5,7,8,2"

list = numbers.split(",")
for i in list:
    print(i)






lis = [
    ["Some", "cool", "data"],
    [54, 6],
    [-3, 0, 5.6, 4, 33, 19]
]

for firstList in lis:
    for el in firstList:
        print(el)





basket = [
    {
        'position': 'Book about python',
        'count': 1,
    },
    {
        'position': 'Mouse with cabel',
        'count': 12,
    }
]

count = 0
for element in basket:
    count += element['count']

print(count)







data = {
    'question': ['Why', 'are', 'not', 'all'],
    'animals': {
        'birds': [
            {'name': 'birds'}
        ],
        'others': [
            [
                {'name': 'flying'},
                {'name': 'the'},
                {'name': 'time'},
            ],
        ],
    },
    'parts': {
        'question': '?'
    }
}

why = data['question'][0]
birds = data['animals']['birds'][0]['name']
are = data['question'][1]
str_not = data['question'][2]
flying = data['animals']['others'][0][0]['name']
all = data['question'][3]
the = data['animals']['others'][0][1]['name']
time = data['animals']['others'][0][2]['name']
question = data['parts']['question']
string = why + " " + birds + " " + are + " " + str_not + " " + flying + " " + all + " " + the + " " + time + question
print(string)








l = [6, 9, 0, 12]
b = [5, 23]
l.extend(b)
l.append(9)
l.insert(3, 8)
l.remove(23)
l.sort()
print(l)
l.reverse()
print(l)





def square(a, b):
    res = a * b
    return res


print(square(5, 9))






def newList(lis):
    newOne = []
    newOne.append(lis[0])
    newOne.append(lis[-2])
    return newOne


lis = newList([5, 10, 15, 20, 25])
print(lis)





def some(*args):
    el = []
    for i in args:
        el.append(i)

    print(el)


some(5, 6, 8, 2, 122, 6, 245)




def find(lis, toFind):
    for el in lis:
        if el == toFind:
            return "Yes"
    return "No"

l = [2, 4, 6, 8, 10]
print(find(l, 4))