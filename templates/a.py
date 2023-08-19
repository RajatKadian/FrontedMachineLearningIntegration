
############ 1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# dict = {}
#
# for i in range(len(keys)):
#     dict[keys[i]] = values[i]
#
# print(dict)


############ 2

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# dict3 = dict1.copy()
# dict3.update(dict2)
#
# print(dict3)

######### 3

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
#
# print(sampleDict["class"]["student"]["marks"]["history"])

######### 4

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
#
# dict1 = {}
# for i in range(2):
#     dict1[employees[i]] = defaults
#     dict1[employees[i]] = defaults
#
# print(dict1)


######### 5


# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
#
# # Keys to extract
# keys = ["name", "salary"]
#
# dict1 = {}
#
# for i in keys:
#     if i in sample_dict:
#         dict1[i] = sample_dict[i]
#
# print(dict1)


########### 6

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# # Keys to remove
# keys = ["name", "salary"]
#
# sample_dict.pop("name","salary")
#
# print(sample_dict)

######## 7

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
#
# for i in sample_dict:
#     if sample_dict[i] == 200:
#         print("yes present")


######### 8

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# sample_dict['location'] = sample_dict.pop('city')
#
# print(sample_dict)

########## 9

# sample_dict = {
#     'Physics': 82,
#     'Math': 65,
#     'history': 75
# }
#
# print(min(sample_dict))

######## 10

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }


####
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

# exp = [2200, 2350, 2600, 2130, 2198]
#
#
# print("In feb this much extra was spent compared to jan:",exp[1]-exp[0]) # 150
#
# # 2. Find out your total expense in first quarter (first three months) of the year
# print("Expense for first quarter:",exp[0]+exp[1]+exp[2]) # 7150
#
# # 3. Find out if you spent exactly 2000 dollars in any month
# print("Did I spent 2000$ in any month? ", 2000 in exp) # False
#
# # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# exp.append(1980)
# print("Expenses at the end of June:",exp) # [2200, 2350, 2600, 2130, 2190, 1980]
#
# # 5. You returned an item that you bought in a month of April and
# # got a refund of 200$. Make a correction to your monthly expense list
# # based on this
# exp[3] = exp[3] - 200
# print("Expenses after 200$ return in April:",exp) # [2200, 2350, 2600, 1930, 2190, 1980]


heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append("black panther")
print(heros)

heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)

heros.remove(heros[1])
heros.remove(heros[1])
print(heros)

heros.sort()
print(heros)