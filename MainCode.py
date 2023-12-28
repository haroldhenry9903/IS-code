import datetime

#class user
class User:
    def __init__(self, userID, userName, email, password, profilepicture, biodata, contactDetails):
        self.userID = userID
        self.userName = userName
        self.email = email
        self.password = password
        self.profilepicture = profilepicture
        self.biodata = biodata
        self.contactDetails = contactDetails
        self.logged_in = False
        self.messages = []

    def login(self, entered_password):
        if self.password == entered_password:
            self.logged_in = True
            print("Login successful.")
        else:
            print("Login failed. Incorrect password.")

    def logout(self):
        self.logged_in = False
        print("Logged out successfully.")

    def viewMessage(self, message_index):
        if self.logged_in:
            if 0 <= message_index < len(self.messages):
                print("Message:", self.messages[message_index])
            else:
                print("Invalid message index.")
        else:
            print("You must be logged in to view messages.")

    def composeMessage(self, recipient, message_content):
        if self.logged_in:
            message = f"From: {self.userName}\nTo: {recipient}\nContent: {message_content}"
            self.messages.append(message)
            print("Message sent successfully.")
        else:
            print("You must be logged in to compose messages.")

    def discardMessage(self, message_index):
        if self.logged_in:
            if 0 <= message_index < len(self.messages):
                del self.messages[message_index]
                print("Message discarded successfully.")
            else:
                print("Invalid message index.")
        else:
            print("You must be logged in to discard messages.")

    def updateProfile(self, new_profilepicture, new_biodata, new_contactDetails):
        if self.logged_in:
            self.profilepicture = new_profilepicture
            self.biodata = new_biodata
            self.contactDetails = new_contactDetails
            print("Profile updated successfully.")
        else:
            print("You must be logged in to update your profile.")


#Customer Class
class Customer(User):
    def __init__(self, userID, userName, email, password, profilepicture, biodata, contactDetails,
                 favorite=None, purchaseHistory=None, paymentMethod=None, cart=None, orderHistory=None):
        super().__init__(userID, userName, email, password, profilepicture, biodata, contactDetails)
        self.favorite = favorite if favorite else []
        self.purchaseHistory = purchaseHistory if purchaseHistory else []
        self.paymentMethod = paymentMethod if paymentMethod else []
        self.cart = cart if cart else []
        self.orderHistory = orderHistory if orderHistory else []

    def browseProducts(self):
        print("Browsing available products...")

    def viewPurchaseDetails(self, orderID):
        for order in self.orderHistory:
            if order['orderID'] == orderID:
                print("Order Details:", order)
                return
        print("Order not found.")

    def addToFavorite(self, product):
        self.favorite.append(product)
        print(f"'{product}' added to favorites.")

    def removeFromFavorite(self, product):
        if product in self.favorite:
            self.favorite.remove(product)
            print(f"'{product}' removed from favorites.")
        else:
            print(f"'{product}' is not in your favorites.")

    def purchaseProduct(self, product):
        self.cart.append(product)
        print(f"'{product}' added to your cart.")

    def viewPurchaseHistory(self):
        print("Viewing purchase history...")
        for order in self.purchaseHistory:
            print("Order ID:", order['orderID'])
            print("Date:", order['date'])
            print("Products:", order['products'])
            print("Total Amount:", order['totalAmount'])
            print()

    def updatePaymentMethod(self, payment_info):
        self.paymentMethod = payment_info
        print("Payment method updated successfully.")

    def contactArtisan(self, artisan, message):
        print(f"Contacting artisan '{artisan}' with message: '{message}'")

    def leaveReview(self, product, rating, comment):
        print(f"Leaving a review for '{product}' with rating {rating} and comment: '{comment}'")

    # Overriding the updateProfile method from the User class
    def updateProfile(self, new_profilepicture, new_biodata, new_contactDetails):
        super().updateProfile(new_profilepicture, new_biodata, new_contactDetails)
        print("Customer profile updated successfully.")


#JobSeeker Class
class JobSeeker(User):
    def __init__(self, userID, userName, email, password, profilepicture, biodata, contactDetails):
        super().__init__(userID, userName, email, password, profilepicture, biodata, contactDetails)
        self.applied_jobs = []
        self.skills = []

    def searchJob(self, job_title):
        print(f"Searching for jobs with title: {job_title}...")

    def applyJobs(self, job):
        if job not in self.applied_jobs:
            self.applied_jobs.append(job)
            print(f"Applied for job: {job.jobName}")
        else:
            print("You have already applied for this job.")

    def viewJobDetails(self, job):
        print(f"Job Details for {job.jobName}:")
        job.getJobDetails()

    def filterJob(self, keyword):
        print(f"Filtering jobs with keyword: {keyword}...")

    def contactJobProvider(self, job, message):
        print(f"Contacting job provider for job '{job.jobName}' with message: '{message}'")

    def checkSkillsForJob(self, required_skills_for_job):
        if all(skill in self.skills for skill in required_skills_for_job):
            print("JobSeeker has the required skills for the job.")
            return True
        else:
            print("JobSeeker does not have all the required skills for the job.")
            return False


#JobProvider Class
class JobProvider(User):
    def __init__(self, userID, userName, email, password, profilepicture, biodata, contactDetails, company, joblistings=None):
        super().__init__(userID, userName, email, password, profilepicture, biodata, contactDetails)
        self.company = company
        self.joblistings = joblistings if joblistings else []

    def fillJobDetails(self, jobID, jobName, description, applicationDeadline, salary, skillsRequirement):
     
