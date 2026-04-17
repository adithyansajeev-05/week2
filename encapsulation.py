class student:
    def __init__(self,name,id_number):
        self.name=name
        self.__id_number=id_number
    def get_id(self):
        return(self.__id_number)
    def set_id(self,new_id):
        if isinstance(new_id, int) and 1000 <= new_id <= 9999:
            self.__id_number = new_id
            print("ID updated successfully ",new_id)
        else:
            print("Invalid ID: must be a 4-digit number")
    def study(self,subject):
        print(f"{self.name} is studying {subject}.")
# -----------------class method-----------------------
    @classmethod
    def school_info(cls,obj,school):
        print(f"{obj.name} is stydying at {school}.")
obj=student("adil",100)
# print(obj.id_number)  //this is not possible because 
                        #private variables cannot be accesed using object referencing

print("first id is :",obj.get_id())
obj.set_id(4500)
obj.study("English")
student.school_info(obj,"ABC school")
obj2=student("mark",101)
print("the new id is :",obj2.get_id())
obj.set_id(2001)