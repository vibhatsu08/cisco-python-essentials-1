# python program to "glue" two dictionaries together and create a new dictionary with that value.
dict1 = {
    "batman": "robert pattinson",
    "black adam": "dwayne johnson"
}
dict2 = {
    "ironman": "robert downey junior",
    "spiderman": "tom holland"
}
dict3 = {}

for item in (dict1, dict2) :
    dict3.update(item)    
    
print(dict3)