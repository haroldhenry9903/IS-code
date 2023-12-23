import datetime

class User:
    def __init__(self, userID, userName, email, password, profilepicture, biodata):
        self.userID = userID
        self.userName = userName
        self.email = email
        self.password = password
        self.profilepicture = profilepicture
        self.biodata = biodata
        self.notification_settings = NotificationSettings()

    def login(self):
        print("User " + self.userName + " is login")

class NotificationSettings:
    def __init__(self):
        self.email_notifications = False
        self.push_notifications = False

    def set_email_notifications(self, enabled):
        self.email_notifications = enabled

    def set_push_notifications(self, enabled):
        self.push_notifications = enabled

class Message:
    def __init__(self, content):
        self.content = content
        self.timestamp = datetime.datetime.now() # Current time
        self.is_read = False

    def send_message(self, recipient):
        print("Message sent to: ", recipient)

    def received_message(self, sender):
        self.is_read = False  # Mark message as unread
        print("Message recieved from: ", sender)

    def view_message(self):
        print("Message content: ", self.content)
        self.is_read = True  # Mark message as read

    def notif_message(self):
        print("New message from: ", self.sender)

user_1 = User("82580", "Harold", "haroldhenry9903@gmail.com", "harolH", "pic", "boy")

print(user_1.userID)
print(user_1.userName)
print(user_1.email)
print(user_1.password)
print(user_1.profilepicture)
print(user_1.biodata)

user_1.login()

message = Message("Hello, Merry Christmas Mr David.")
message.send_message("David Lee")
message.received_message("Trump")
message.view_message()
