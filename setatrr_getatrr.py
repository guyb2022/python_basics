class Person:
    pass

person = Person()

# # creating attributes:
person.first = "doode"
person.last = 'Lebowski'
print(f"{person.first} {person.last}")
# output: doode Lebowski

# Creating attributes with setattr
setattr(person, 'first', 'doode')

# Also can take a value of an a variable
first_key = 'first'
first_val = 'Doode'
setattr(person, first_key, first_val)

# To get the value we use the getattr
# It will take the proper value according to the key
att = getattr(person, first_key)

print(att)
