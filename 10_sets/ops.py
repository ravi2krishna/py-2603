# Set Methods / Operations On Sets

# add(): add element to set
data = {10,20,30,40,50}
print(data)
data.add(60)
print(data)

# update(): add multiple elements to set i.e iterables
data = {10,20,30,40,50}
print(data)
data.update([60,70,80])
print(data)

# pop(): Removes arbitrary/random element
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): Removes element based on value 
data = {10,20,30,40,50}
print(data)
data.remove(30)
print(data)
# data.remove(90) # KeyError: 90
print(data)

# discard(): Removes element based on value, if value doesn't exist, No Error 
data = {10,20,30,40,50}
print(data)
data.discard(30)
print(data)
data.discard(90) 
print(data)

# clear(): empties set 
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)

# copy(): Makes a copy 
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)

# All above methods are like regular methods we used with lists and sets

# Below methods are specific to sets only 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): Combine Both Sets 
print(s1.union(s2))
print(s1 | s2) # | - pipe symbol

# intersection(): Get Common Elements From Sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection(s2))
print(s1 & s2) # & - ampersand symbol
print(s1)
print(s2)

# intersection_update(): Get Common Elements From Sets and update calling set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection_update(s2))
print(s1)
print(s2)

# Any _update does same i.e updates calling set 

# difference(): Removes common elements from the set and gives unique elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.difference(s2))
print(s2.difference(s1))

print(s1 - s2) 

print(s1)
print(s2)

# difference_update(): Removes common elements from the set and gives unique elements and update calling set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.difference_update(s2))

print(s1)
print(s2)

# symmetric_difference(): Removes common elements and takes combined elements from both sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.symmetric_difference(s2))

print(s1 ^ s2)

print(s1)
print(s2)

# symmetric_difference_update(): Removes common elements and takes combined elements from both sets and update calling set 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.symmetric_difference_update(s2))

print(s1)
print(s2)

# issubset(): checks if given set is subset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset(): checks if given set is superset of another set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s2.issuperset(s3))
print(s1.issuperset(s3))

# isdisjoint(): checks if sets have common elements 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))