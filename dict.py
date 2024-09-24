#Question 1: Create an empty dictionary
'''d={}
print(type(d))

#Question 2: Create a dictionary with key-value pairs for a person's name and age.

d={"name":"Wasiq","age":29}
print(d)

#Question 3: Access the value associated with the key "age" in the person dictionary.
d={"name":"Wasiq","age":29}
print(d.values())

#: Check if a key exists in the person dictionary.
d={"name":"Wasiq","age":29}

print(d.get("name"))

#Question 5: Add a new key-value pair "city" with the value "New York" to the person dictionary.
d={"name":"Wasiq","age":29}

d.update({"city":"New Yourk"})
print(d)

#Question 6: Remove the key-value pair with the key "age" from the person dictionary.
d={'name': 'Wasiq', 'age': 29, 'city': 'New Yourk'}
d.pop("age")
print(d)


#Question 7: Iterate through the keys in the person dictionary.
d={'name': 'Wasiq', 'age': 29, 'city': 'New Yourk'}
it= iter(d)
print(next(it))
print(next(it))
print(next(it))

#Question 8: Iterate through the values in the person dictionary.

d={'name': 'Wasiq', 'age': 29, 'city': 'New Yourk'}

for value in d.values():
    print(value)
    

#Question 8: Iterate through the keys in the person dictionary.
d={'name': 'Wasiq', 'age': 29, 'city': 'New Yourk'}
for key in d.keys():
    print(key)
    


#Question 9: Iterate through both keys and values in the person dictionary.
d={'name': 'Wasiq', 'age': 29, 'city': 'New Yourk'}
for key,value in d.items():
    print(f"key:{key}.value:{value}")


#Question 10: Create a dictionary with default values using the dict.fromkeys() method.
seq =("a","b","c","d")
print(dict.fromkeys(seq,None))


#Question 11: Get the value associated with a key using the dict.get() method with a default value.

d={'name': 'Wasiq', 'age': 29, 'city': 'New Yourk'}
print(d.get("name"))


#Question 13: Merge two dictionaries.

d={'name': 'Wasiq', 'age': 29, 'city': 'New Yourk'}
e={"Sajid":28,"rizwan":27}

d.update(e)
print(d)

#Question 14: Create a dictionary where the values are squares of the keys
d={}
for i in range(1,10):
    d[i]=i**2
print(d)


#Question 15: Find the key with the maximum value in a dictionary.

d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
keymax=max(d,key=lambda x : d[x])
print(keymax)


#Question 16: Sort a dictionary by its keys.
d={'b': 2, 'a': 1, 'c': 3}

sorted_dict=dict(sorted(d.items()))
print(sorted_dict)


#Question 17: Check if two dictionaries are equal.
d={'b': 2, 'a': 1, 'c': 3}
e={'b': 2, 'a': 1, 'c': 3}
print(d==e)


#Question 18: Remove all elements from a dictionary.
d={'b': 2, 'a': 1, 'c': 3}

d.clear()
print(d)
'''

