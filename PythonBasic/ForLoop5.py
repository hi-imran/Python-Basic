
addition_str = "2+5+10+20"
sum_val = 0
for num in addition_str.split("+"):
    sum_val += int(num)
print(sum_val)
