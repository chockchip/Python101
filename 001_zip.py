# zip

"""
The zip() function returns a zip object, 
which is an iterator of tuples where the first 
item in each passed iterator is paired together, 
and then the second item in each passed iterator 
are paired together etc.
"""

a = ("John", "Charles", "Mike",)
b = ("Jenny", "Christy", "Monica", "vicky")
c = ("a", "b")

x = zip(a, b, c)
print(list(x))

# Remark
# 1. Size of zip data will be shortest size of interator that use to zip. 
# 2. Type of return data is zip. (We can convert it to other type)