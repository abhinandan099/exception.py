'''     WAP to declare a list and write those content into file at end of the file only open that file in read mode
    and read 5th line from the file.'''

l1=["this","is","python","class"]
for i in l1:
f1=open("C:/Users/HP/Desktop/cse.txt","r")
    f1=open("C:/Users/HP/Desktop/a1.txt","a+")
    f1.write(i)
print(f1.readline(5))
f1.close()
f1=open("C:/Users/HP/Desktop/a1.txt","a")

'''     WAP to create a user define class which is using arithmatic division operation,
    define a class with a exception base class. Inside this class use init construction with self and message.
    now define a new class user exception;start the try block and take a and b input from user; if b=0 then raise
     our exception with message that is b>0 otherwise do division operation '''

class OurException(Exception):
    def __init__ (self,message):
        self.message=message
class usingException:
    try:
        a=int(input("a: "))
        b=int(input("b: "))
        if b==0:
            raise OurException("b should be grater than 0")
        d = a/b
        print("division operation successful with result:",d)
    except OurException as err:
        print("user defined exception:",err.message)


'''     WAP to create a dictionary to open a file in a binary mode make use of pickle.dum() to write data
 stream into the file. Make use of pickle.load() to load the data stream from file and print on the console.  '''

import pickle
animalDict={'ccat':2,'dog':7,'lion':4,'tiger':6,'leopard':12,'Bear':8,'elephant':19}
outfile=open('animal','wb')
pickle.dump(animalDict,outfile)
outfile.close()
fst=open("animal","rb")
data=pickle.load(fst)
try:
    while(True):
        print(data)
        data=pickle.load(fst)
except:
    print("Bye")
