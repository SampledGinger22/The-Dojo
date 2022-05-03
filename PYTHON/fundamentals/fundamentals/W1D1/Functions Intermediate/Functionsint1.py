# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

#Update Values in Dictionaries and Lists

# x[1][0] = 15
# print(x)


# students[0]["last_name"] = "Bryant"
# print(students)


# sports_directory['soccer'][0]="Andres"
# print(sports_directory)


# z[0]['x']= 30
# print(z)



#Iterate Through a List of Dictionaries


# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(val):
#     for i in range(0,4,1):
#         print ("first_name - " + val[i]["first_name"] + ",","last_name - " + val[i]["last_name"])

# iterateDictionary(students)




#Get Values From a List of Dictionaries
# students = [
#     {"first_name" : "Michael", "last_name" : "Jordan"},
#     {"first_name" : "John", "last_name" : "Rosales"},
#     {"first_name" : "Mark", "last_name" : "Guillen"},
#     {"first_name" : "KB", "last_name" : "Tonel"},
# ]

# def iterateDictionary2(key_name, some_list):
#     for i in range(0,4,1):
#         print (some_list[i][key_name])

# iterateDictionary2("last_name", students)



#Iterate Through a Dictionary with List Values

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(some_dict):
#     for z in some_dict:
#         print(len(some_dict[z]), z.upper())
#         for j in range(0,len(some_dict[z])):
#             print(some_dict[z][j])

# printInfo(dojo)


