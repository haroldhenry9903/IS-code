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

        # Assuming there's a list of jobs available somewhere
        available_jobs = ["Software Engineer", "Data Analyst", "Project Manager", "Graphic Designer"]

        matching_jobs = [job for job in available_jobs if job_title.lower() in job.lower()]

        if matching_jobs:
            print("Available jobs matching your search:")
            for job in matching_jobs:
                print(f"- {job}")
        else:
            print("No jobs found with the specified title.")

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
        job_details = {
            'jobID': jobID,
            'jobName': jobName,
            'description': description,
            'applicationDeadline': applicationDeadline,
            'salary': salary,
            'skillsRequirement': skillsRequirement,
            'applications': []
        }
        self.joblistings.append(job_details)
        print(f"Job details filled for job: {jobName}")

    def postJob(self, job_details):
        self.joblistings.append(job_details)
        print(f"Job posted: {job_details['jobName']}")

    def reviewApplication(self, jobID, applicant):
        for job in self.joblistings:
            if job['jobID'] == jobID:
                job['applications'].append(applicant)
                print(f"Reviewed application for job '{job['jobName']}' from applicant '{applicant.userName}'.")
                return
        print(f"Job with ID {jobID} not found.")

    def contactApplicant(self, applicant, message):
        print(f"Contacting applicant '{applicant.userName}' with message: '{message}'")

    def editJobDetails(self, jobID, new_details):
        for job in self.joblistings:
            if job['jobID'] == jobID:
                job.update(new_details)
                print(f"Job details updated for job '{job['jobName']}'")
                return
        print(f"Job with ID {jobID} not found.")

    def cancelJobPosting(self, jobID):
        for job in self.joblistings:
            if job['jobID'] == jobID:
                self.joblistings.remove(job)
                print(f"Job posting for '{job['jobName']}' has been canceled.")
                return
        print(f"Job with ID {jobID} not found.")




#Artisan Class
class Artisan(User):
    def __init__(self, userID, userName, email, password, profilepicture, biodata, contactDetails, productlistings=None):
        super().__init__(userID, userName, email, password, profilepicture, biodata, contactDetails)
        self.productlistings = productlistings if productlistings else []

    def listProduct(self, productID, productName, description, price, image):
        product_details = {
            'productID': productID,
            'productName': productName,
            'description': description,
            'price': price,
            'image': image
        }
        self.productlistings.append(product_details)
        print(f"Product '{productName}' listed successfully.")

    def editProduct(self, productID, new_details):
        for product in self.productlistings:
            if product['productID'] == productID:
                old_product_name = product['productName']
                product.update(new_details)
                print(f"Product details updated for '{old_product_name}':")
                for key, value in new_details.items():
                    print(f"  {key}: {value}")
                return
        print(f"Product with ID {productID} not found.")

    def deleteProduct(self, productID):
        for product in self.productlistings:
            if product['productID'] == productID:
                self.productlistings.remove(product)
                print(f"Product '{product['productName']}' has been deleted.")
                return
        print(f"Product with ID {productID} not found.")

    def manageProduct(self):
        print(f"Products listed by {self.userName}:")
        for product in self.productlistings:
            print(f"Product ID: {product['productID']}")
            print(f"Product Name: {product['productName']}")
            print(f"Description: {product['description']}")
            print(f"Price: {product['price']}")
            print(f"Image: {product['image']}")
            print()

#Message and Notification Class
from datetime import datetime

class Message:
    def __init__(self, content, sender=None, recipient=None, timestamp=None):
        self.content = content
        self.sender = sender
        self.recipient = recipient
        self.timestamp = timestamp if timestamp else datetime.now()

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.content}"

class Notification:
    def __init__(self, message, sender=None, recipient=None):
        self.message = message
        self.sender = sender
        self.recipient = recipient

    def sendNotification(self):
        print(f"Notification sent to {self.recipient}: {self.message}")


#Product Class
class Product:
    def __init__(self, product_title, description, price, image):
        self.product_title = product_title
        self.description = description
        self.price = price
        self.image = image

    def validateDetails(self):
        # You can add validation logic here if needed
        return True  # Return True for simplicity

    def displayProduct(self):
        print("Product Title:", self.product_title)
        print("Description:", self.description)
        print("Price:", self.price)
        print("Image:", self.image)

    def updateProduct(self, product_title, description, price, image):
        self.product_title = product_title
        self.description = description
        self.price = price
        self.image = image

    def addProduct(self, product_list, new_product):
        if new_product.validateDetails():
            product_list.append(new_product)
            print("Product added successfully.")
        else:
            print("Invalid product details. Product not added.")

    def removeProduct(self, product_list, product_title):
        for product in product_list:
            if product.product_title == product_title:
                product_list.remove(product)
                print(f"Product '{product_title}' removed successfully.")
                break
        else:
            print(f"Product '{product_title}' not found in the list.")
# Cart Class
# Cart Class
class Cart:
    def __init__(self, cart_name="MyCart"):
        self.cart_name = cart_name
        self.items = []       # List to store Product objects
        self.total_price = 0.0  # Total price of all items in the cart

    def calculateTotalPrice(self):
        # Calculate the total price based on the items in the cart
        self.total_price = sum(product.price for product in self.items)

    def addProductToCart(self, product):
        self.items.append(product)
        print(f"Product '{product.product_title}' added to the cart.")

    def removeProductFromCart(self, product_title):
        for product in self.items:
            if product.product_title == product_title:
                self.items.remove(product)
                print(f"Product '{product_title}' removed from the cart.")
                break
        else:
            print(f"Product '{product_title}' not found in the cart.")

    def displayCart(self):
        print(f"{self.cart_name}'s Cart Contents:")
        for product in self.items:
            print("- " + product.product_title)

#Job Class
class Job:
    def __init__(self, jobID, jobName, description, applicationDeadline, contactDetails, salary, company, skillsRequirement):
        self.jobID = jobID
        self.jobName = jobName
        self.description = description
        self.applicationDeadline = applicationDeadline
        self.contactDetails = contactDetails
        self.salary = salary
        self.company = company
        self.skillsRequirement = skillsRequirement
        self.applications = []

    def getJobDetails(self):
        print("Job ID:", self.jobID)
        print("Job Name:", self.jobName)
        print("Description:", self.description)
        print("Application Deadline:", self.applicationDeadline)
        print("Contact Details:", self.contactDetails)
        print("Salary:", self.salary)
        print("Company:", self.company)
        print("Skills Requirement:", self.skillsRequirement)

    def updateJobDetails(self, jobName, description, applicationDeadline, contactDetails, salary, company, skillsRequirement):
        self.jobName = jobName
        self.description = description
        self.applicationDeadline = applicationDeadline
        self.contactDetails = contactDetails
        self.salary = salary
        self.company = company
        self.skillsRequirement = skillsRequirement

    def closeApplication(self):
        self.applicationDeadline = "Closed"
        print(f"Applications for job '{self.jobName}' are now closed.")

#Review Class
class Review:
    def __init__(self, reviewID, authorID, subjectID, rating, comment):
        self.reviewID = reviewID
        self.authorID = authorID
        self.subjectID = subjectID
        self.rating = rating
        self.comment = comment

    def leaveReview(self, rating, comment):
        self.rating = rating
        self.comment = comment
        print("Review submitted successfully.")

    def editReview(self, rating, comment):
        self.rating = rating
        self.comment = comment
        print("Review edited successfully.")

    def deleteReview(self):
        self.rating = None
        self.comment = None
        print("Review deleted successfully.")

    def displayReview(self):
        print("Review ID:", self.reviewID)
        print("Author ID:", self.authorID)
        print("Subject ID:", self.subjectID)
        print("Rating:", self.rating)
        print("Comment:", self.comment)
