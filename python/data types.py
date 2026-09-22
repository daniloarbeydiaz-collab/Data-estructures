print ("Hello. Welcome to data structures class")

#Numeric data types
number1 = 10
print(f"Var number1 is: {type(number1)}")
gravity = 9.8
print(f"Var gravity is: {type(gravity)}")
numberx = 8j
print(f"Var numberx is: {type(numberx)}")

#string data types
my_name = "Danilo"
fullname = "Danilo Diaz"
#descriptio
"Hello, hows it going?"


# list
personal_info = [
    "danilo", 
    "diaz", 
    25, 
    True, 
    "pasto",
["juli", 10]
]
print(type(personal_info))
# father age and city
print(f"Father age: {personal_info[2]}")
print(f"Father city: {personal_info[4]}")
# daugther name and age
print(f"Daughter name: {personal_info[5][0]}")
print(f"Daughter age: {personal_info[5][1]}")
#update father age
new_age = input("please, type new father age: ")
personal_info[2] = new_age
#print(f"new father age is: {personal_info[2]}")
# add new information
personal_info.append("Malala")

#tuple
user_data = ("Benazir", "Bhutto", 25, "Pakistan")
print(user_data)
print(user_data[0])
new_age = 40
#user_data[2] = new_age
#dictionaries
countries_info = {
    "country_name": "colombia",
    "capital": "bogota",
    "abbrev" : "co",
    "code" : 57
}
print(countries_info["country_name"])
