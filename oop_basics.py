print("-------CLASS---------")
class course:
    def __init__(self,name,price,seats):
        self.name=name
        self.price=price
        self.seats=seats
    def display_info(self):
        print(f"course :{self.name} ,cost :{self.price}")
    def enroll_student(self):
        if(self.seats>0):
            self.seats-=1
            print(f"Sats left :{self.seats}")
        else:
            print("No Seats Available!")
    def status_logic(self):
        if(self.seats>0):
            return("ACTIVE")
        else:
            return("FULL !")
        
course1=course("Full Stack Masterclass",200000,45)
course2=course("Generative AI and LLM",150000,35)
course3=course("Advanced system Design",750000,30)

print("--------DISPLAY INFO-------")
course1.display_info()
course2.display_info()
course3.display_info()

print("--------STSTUS LOGIC---------")
status1=course("Full Stack Masterclass",200000,3)
status2=course("Generative AI and LLM",150000,0)
print(status1.status_logic())
print(status2.status_logic())