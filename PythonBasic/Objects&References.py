a = "banana"
b = "banana"

print(a is b)

"""
The answer is True. This tells us that both a and b refer to the same object, and that it is the second 
of the two reference diagrams that describes the relationship. Python assigns every object a unique id and 
when we ask a is b what python is really doing is checking to see if id(a) == id(b).
"""