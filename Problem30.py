dicti = {1:10,2:20,3:30,4:40,5:50}

def keyFinder(key,dictionary):
    if key in dictionary:
        print('Key exists')
    else:
       print('key Doesnot exist')

keyFinder(1,dicti)
keyFinder(47,dicti)