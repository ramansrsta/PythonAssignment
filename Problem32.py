n = int(input('Enter a number upto which you want to print '))
dictionary = {}
for x in range(1,n+1):
    dictionary[x] = x*x
        
print(dictionary)