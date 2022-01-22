# Given 3 lists of strings, returns the words that occur in all 3 lists.
# You can assume all 3 input lists are the same size.
# You can assume each input list does not contain any duplicates.
#
# Example 1:
# Input - ["hi", "bye"], ["why", "lie"], ["try", "cry"]
# Output - []
#
# Example 2:
# Input - ["hi", "bye"], [ "bye", "lie" ], ["try", "cry"]
# Output - []
#
# Example 3:
# Input - ["hi", "bye"], ["bye", "lie"], ["bye", "cry"]
# Output - ["bye”]
#
# Return words that occur in 2 or more lists
# Example:
# Input - ["hi", "bye"], ["bye", "lie"], ["try", "cry"]
# Output - [“bye”]
#
# Assume input lists can have duplicate words. Return words that occur in 2 or more lists.
# Example:
# Input - ["hi", "hi"], ["bye", "dry"], ["try", "fly"]
# Output - []

def search(a, b, c):
    d = {}
    res = []
    a = set(a)
    b = set(b)
    c = set(c)
    for i in a:
        d[i] = 1 + d.get(i, 0)
    for i in b:
        d[i] = 1 + d.get(i, 0)
    for i in c:
        d[i] = 1 + d.get(i, 0)
    for i in d:
        if d[i] >= 2:
            res.append(i)
    return res


print(search(["hi", "bye"], ["why", "lie"], ["try", "cry"]))
print(search(["hi", "bye"], ["bye", "lie"], ["try", "cry"]))
print(search(["hi", "bye"], ["bye", "lie"], ["bye", "cry"]))

print(search(["hi", "bye"], ["bye", "lie"], ["try", "cry"]))

print(search(["hi", "hi"], ["bye", "dry"], ["try", "fly"]))
