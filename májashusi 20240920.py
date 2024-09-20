# dictionary = {
#     "szia" : "hi",
#     "alma" : "apple",
#     "csend" : "silence",
#     "probléma" : "problem"
# }
# empty_dict = dict()

#print(dictionary)
#print(empty_dict)

#print(dictionary["alma"])

#words = ["szia", "csend", "oroszlán", "alma"]
#for word in words:
#    if word in dictionary:
#        print(word, "->", dictionary[word])
#   else:
#        print(word, "nincs benne")

#for key in dictionary.keys():
#    print(key, "->", dictionary[key])

# print(dictionary.items())
# for magyar, angol in dictionary.items():
#     print(magyar, "->", angol)

# for value in dictionary.values():
#     print(value)

# animals = {
#     "cat" : "Sanyi",
#     "dog" : "Janusz",
#     "lion" : "Lajos"
# }

# animals["cat"] = "Zénó"
# print(animals)
# animals["mouse"] = "Jerry"
# print(animals)
# animals.update({
#     "goat" : "simulator",
#     "mammuth" : "Manny"
#     })
# print(animals)

# del animals["mouse"]
# print(animals)

# animals.popitem()
# print(animals)

# food = {
#     "pancake" : "pan",
#     "watermelon" : "nigeria",
#     "pasta" : "italy"
# }
# food["pasta"] = "chao"
# print(food)
# food["grapefruit"] = "grape"
# print(food)
# food.update({
#     "grapes" : "hihihaaa",
#     "passionfruit" : "why"
#     })
# print(food)

# del food["grapes"]
# print(food)

# food.popitem()
# print(food)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}

# Elégséges megoldás (fúúúúúúúúúúúújj)
# dic4.update(dic1)
# dic4.update(dic2)
# dic4.update(dic3)
# print(dic4)

# Jó megoldás
# for d in (dic1, dic2, dic3):
#     dic4.update(d)

# print(dic4)

students = {}
while True:
    name = input("Kérek egy nevet: ")
    if name == "":
       break
    score = int(input("Kérek egy pontszámot: "))
    if name not in students:
        students[name] = (score,)
    else:
        students[name] += (score,)

for name in sorted(students.keys()):
    add = 0
    counter = 0
    for score in students[name]:
        add += score
        counter += 1
    print(name, ":", add / counter)
