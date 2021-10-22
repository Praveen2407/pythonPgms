# Find the number of occurances of each character in a given string

print("Enter the string")
hash = {}

for char in (str(input())):
	if char in hash:
		hash[char] = hash[char] + 1
	else:
		hash[char]=1
		
print(hash)