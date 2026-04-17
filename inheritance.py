class user:
    def __init__(self,username,email):
        self.username=username
        self.email=email
    def login(self):
        print(f"{self.username} is logged in.")
class admin(user):
    def __init__(self,username,email,permission):
        super().__init__(username,email)
        self.permission=permission
    def login(self):
        print(f"Admin {self.username} is logged in with full access.")
    def delete_user(self):
        print("User deleted!")
admin1=admin("dony","dony@gmail.com","full access")
print("usernamme :",admin1.username)
print("email :",admin1.email)
print("permission :",admin1.permission)

print("--------POLYMORPHISM--------")
user_obj=user("jack","jack@gmail.com")
ls=[user_obj,admin1]
for i in ls:
    i.login()

print("--------SPECIALIZATION----------")
#  user_obj.delete_user() --------------------->not possible because 
                                                # user class have'nt contains delete_user()!
admin1.delete_user()
