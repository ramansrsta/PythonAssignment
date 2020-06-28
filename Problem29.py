dictionary1={1:10, 2:20}
dictionary2={3:30, 4:40}
dictionary3={5:50,6:60}
dictionary4 = {}
for data in (dictionary1, dictionary2, dictionary3): 
    dictionary4.update(data)
print(dictionary4)

