
class User:
    def __init__(self,userID,userName,email,password,profilepicture,biodata):
        self.userID = userID
        self.userName = userName
        self.email = email
        self.password = password
        self.profilepicture = profilepicture
        self.biodata = biodata

    def login(self):
        print("User "+self.userName+" is login")
class Jobseeker:



user_1 = User("82580","Harold","haroldhenry9903@gmail.com","harolH","pic","Good boy")

print(user_1.userID)
print(user_1.userName)
print(user_1.email)
print(user_1.password)
print(user_1.profilepicture)
print(user_1.biodata)

user_1.login()