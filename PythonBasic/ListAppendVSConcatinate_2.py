origlist = [45,32,88]
aliaslist = origlist
origlist += ["cat"]
origlist = origlist + ["cow"]
print(origlist)
print(aliaslist)
"""
origlist += ["cat"] and origlist = origlist + ["cow"] is different in case of List.
origlist += ["cat"] will add value in same List. i.e [45, 32, 88, 'cat']
origlist = origlist + ["cow"]  will create new List and add value to it. i.e [45, 32, 88, 'cat', 'cow']
"""