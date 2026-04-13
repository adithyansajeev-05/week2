print("-------GREETINGS-------")
def greet_user(name):
    print(f"hello {name}! Good morning")
name=input("enter your name :")
greet_user(name)

print("------ADDITION---------")
def add(x,y):
    sum=x+y
    return(sum)
x=int(input("enter first number :"))
y=int(input("enter second number :"))
result=add(x,y)
print("sum is :",result)

print("-----DEFAULT ARGUEMENTS-----")
def describe_pet(pet_name,animal_type="dog"):
    print(f"the pet name is {pet_name}.the  animal type is {animal_type}")
print("with arguement_______")
describe_pet("rocky","dog")
print("without arguement____")
describe_pet("kiser",)

print("-------*ARGS-----------")
def sum_all(*args):
    sum=0
    for i in args:
        sum+=i
    return(sum)
print("the sum of 5 number is :",sum_all(1,2,3,4,5))
print("the sum of 10 number is :",sum_all(1,2,3,4,5,6,7,8,9,10))

print("--------*KWARGS---------")
def build_profile(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
build_profile(first_name="john",last_name="mathew",location="india",job="developer")

print("----------SCOPE------------")
count=0
print("before changes count = ",count)
def change():
    global count
    print("after global keyword count = ",count+10)
change()

""" without 'global' keyword,the changes to 'count' is not possible 
    because it is local inside function. """