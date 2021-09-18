# wapp to read marks from the user 
# and find the lowest and highest marks

marks = []
res = input(" do u want to enter some marks y/n ")
while res == "y":
	m = int(input("enter marks "))
	marks.append(m)
	res = input("do u want to enter more y/n ")
marks.sort()
print(marks)

#logic 1
low = marks[0]
high = marks[len(marks) - 1]

print("low = ", low)
print("high = ", high)

# logic 2
print("low = ", min(marks))
print("high = ", max(marks))





