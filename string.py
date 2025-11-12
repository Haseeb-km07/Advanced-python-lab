string1 = input("Enter a word:")
string2 = input("Enter a word:")

s1 = string1[0] + string2[1] + string1[2:]
s2 = string2[0] + string1[1] + string2[2:]

result = s1 +" " + s2

print(result)