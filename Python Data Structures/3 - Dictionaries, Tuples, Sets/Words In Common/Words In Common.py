s1 = input()
s2 = input()
l1 = s1.split()
l2 = s2.split()
print(len(set(l1)&set(l2)))