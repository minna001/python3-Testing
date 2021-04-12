myname = "Mike"
Age = 26
occupation = "BA"
print(f'Name: {myname} Age: {Age} Occupation: {occupation}')

if Age > 18:
    print("Older then 18")
else:
    print("younger then 18")

def hello(name,age):
    print("hello {} you are {} years old".format(name,age))


hello("mark",17)

dognames = ["luna","Sean","Sally"]
print(dognames)

for x in range(1,10):
    print(x)

age=0   
while age <18:
    print(age)
    age +=1


dogdict = {"fido":"pit","Sean":"golden"}

print(dogdict["fido"])

class Dog:
    def __init__(self,name,age,fur):
        self.name = name
        self.age = age
        self.fur = fur
    def bark(self):
        print("BARK")

mydog = Dog("fido",13,"long")
mydog.bark()
print(mydog.name)