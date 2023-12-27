
import datetime

#class user
class User:

    def __init__(self,userID,userName,email,password,profilepicture,biodata,contactDetails):
        self.userID = userID
        self.userName = userName
        self.email = email
        self.password = password
        self.profilepicture = profilepicture
        self.biodata = biodata
        self.contactDetails = contactDetails


    def login(self):
        print("User "+self.userName+" is login\n")
#Customer Class
class Customer(User):

    def __init__(self, userID, userName, email, password, profilepicture, biodata , contactDetails, cart , orderHistory):
        User.__init__(self, userID, userName, email, password, profilepicture, biodata , contactDetails)
        self.cart = cart
        self.orderHistory = orderHistory

    def viewCart(self):
        print("Customer " + self.userName + " is Viewing cart\n")
#Jobseeker Class
class JobSeeker(User):
    def __init__(self, userID, userName, email, password, profilepicture, biodata , contactDetails):
        User.__init__(self, userID, userName, email, password, profilepicture, biodata , contactDetails)
    def SendResume(self):
        print("User is sending resume")

#JobProvider Class
class JobProvider(User):
    def __init__(self, userID, userName, email, password, profilepicture, biodata , contactDetails , company , joblistings ):
        User.__init__(self, userID, userName, email, password, profilepicture, biodata , contactDetails)
        self.company = company
        self.joblistings = joblistings

#Artisan Class
class Artisan(User):
    class Artisan(User):
        def __init__(self, userID, userName, email, password, profilepicture, biodata, contactDetails , productlistings):
            User.__init__(self, userID, userName, email, password, profilepicture, biodata, contactDetails)
            self.productlistings = productlistings



