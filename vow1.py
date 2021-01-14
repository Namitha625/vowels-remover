string = input("enter a string")

for i in range(0,len(string)):
  if string[i]not in ['A','E','I','O''U','a','e','i','o','u']:
    print(string[i], end="")
