name = "Sally"
greeting = "Nice to meet you"
s = "Hello, {}. {}."

print(s.format(name,greeting)) # will print Hello, Sally. Nice to meet you.

print(s.format(greeting,name)) # will print Hello, Nice to meet you. Sally.

print(s.format(name)) # 2 {}s, only one interpolation item! Not ideal.

"""
It is also important that you give format the same amount of arguments as there are {} waiting for 
interpolation in the string. If you have a {} in a string that you do not pass arguments for, you may 
not get an error, but you will see a weird undefined value you probably did not intend suddenly inserted 
into your string. You can see an example below.
"""