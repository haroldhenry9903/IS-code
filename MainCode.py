
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
    pass

class NotificationSettings:
    def __init__(self):
        self.email_notifications = False
        self.push_notifications = False

    def set_email_notifications(self, enabled):
        self.email_notifications = enabled

    def set_push_notifications(self, enabled):
        self.push_notifications = enabled

class Message:
    def __init__(self, content, timestamp):
        self.content = content
        self.timestamp = timestamp
        self.is_read = False

    def send_message(self, recipient):
        # Send message to recipient                             LATER
        pass

    def received_message(self, sender):
        # Mark message as received                   LATER      
        pass

    def view_message(self, message):
        # Display message content                      LATER            
        pass

    def notif_message(self, message):
        # Display message notification                     LATER
        pass

user_1 = User("82580","Harold","haroldhenry9903@gmail.com","harolH","pic","boy")

print(user_1.userID)
print(user_1.userName)
print(user_1.email)
print(user_1.password)
print(user_1.profilepicture)
print(user_1.biodata)

user_1.login()
