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
                product.update(new_details)
                print(f"Product details updated for '{product['productName']}'")
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

print("___________________________________________________________________________")
# Example usage of review class:
review1 = Review(1, 101, 201, 4, "This is a great product!")
review2 = Review(2, 102, 201, 5, "Excellent service!")
review1.displayReview()
review2.displayReview()
review1.leaveReview(5, "Fantastic product!")
review1.displayReview()
review2.editReview(4, "Very good service!")
review2.displayReview()
review1.deleteReview()
review1.displayReview()

print("_________________________________________________________________________________________________________________")
# Example usage of Job Class:
job1 = Job(1, "Software Developer", "Full-time software development position", "2023-01-31", "hr@company.com", 80000, "ABC Company", ["Python", "JavaScript", "SQL"])
job2 = Job(2, "Data Analyst", "Data analysis role", "2023-02-28", "hr@company.com", 70000, "XYZ Inc.", ["Excel", "Python", "Statistics"])
job1.getJobDetails()
job2.getJobDetails()
job1.closeApplication()
job2.closeApplication()

print("_________________________________________________________________________________________________________________")
#Example usage for Product class:
product1 = Product("Product 1", "Description for Product 1", 19.99, "product1.jpg")
product2 = Product("Product 2", "Description for Product 2", 29.99, "product2.jpg")
product_list = []
product1.displayProduct()
product2.displayProduct()
product1.updateProduct("Updated Product 1", "Updated Description for Product 1", 24.99, "updated_product1.jpg")
product1.displayProduct()
product1.addProduct(product_list, product1)
product1.addProduct(product_list, product2)
product2.removeProduct(product_list, "Product 2")
print("_________________________________________________________________________________________________________________")
# Example usage of User Class:
user1 = User("1", "Alice", "alice@example.com", "password123", "profile.jpg", "Bio: Alice", "Contact: 123-456-7890")
user1.login("password123")
user1.composeMessage("Bob", "Hello Bob, how are you?")
user1.composeMessage("Charlie", "Hi Charlie, let's meet up.")
user1.viewMessage(0)
user1.discardMessage(1)
user1.updateProfile("new_profile.jpg", "Updated bio", "Updated contact: 987-654-3210")
user1.logout()
print("_________________________________________________________________________________________________________________")
# Example usage Customer Class:
customer1 = Customer("s1", "Alice", "alice@example.com", "password123", "profile.jpg", "Bio: Alice", "Contact: 123-456-7890")
customer1.browseProducts()
customer1.purchaseProduct("Product A")
customer1.addToFavorite("Product B")
customer1.removeFromFavorite("Product A")
customer1.viewPurchaseHistory()
customer1.updatePaymentMethod("Credit Card ending in 1234")
customer1.contactArtisan("Artisan1", "Hello, can you make a custom item for me?")
customer1.leaveReview("Product C", 5, "Great product!")
customer1.updateProfile("new_profile.jpg", "Updated bio", "Updated contact: 987-654-3210")
print("_________________________________________________________________________________________________________________")
# Example usage Job seeker class:
job1 = Job(1, "Software Developer", "Full-time software development position", "2023-01-31", "hr@company.com", 80000, "ABC Company", ["Python", "JavaScript", "SQL"])
job2 = Job(2, "Data Analyst", "Data analysis role", "2023-02-28", "hr@company.com", 70000, "XYZ Inc.", ["Excel", "Python", "Statistics"])
job_seeker = JobSeeker(101, "John Doe", "john@example.com", "password123", "profile.jpg", "Bio: John", "Contact: 123-456-7890")
job_seeker.searchJob("Software Developer")
job_seeker.applyJobs(job1)
job_seeker.applyJobs(job1)  # Applying for the same job again to test duplication handling
job_seeker.viewJobDetails(job1)
job_seeker.filterJob("Python")
job_seeker.contactJobProvider(job2, "Is this position remote?")
required_skills_for_job = ["Python", "Data Analysis", "Machine Learning"]

# Set the skills for the JobSeeker
job_seeker.skills = ["Python", "Data Analysis", "Machine Learning"]

# Define some skills required for a job
required_skills_for_job = ["Python", "Data Analysis", "Machine Learning"]

# Check if the JobSeeker has the required skills for the job
job_seeker.checkSkillsForJob(required_skills_for_job)

print("_________________________________________________________________________________________________________________")
# Example usage of Artisan methods
# Create an Artisan instance
artisan = Artisan(
    userID=401,
    userName="CraftyArtisan",
    email="crafty@example.com",
    password="password123",
    profilepicture="artisan_profile.jpg",
    biodata="Artisan at Crafty Creations",
    contactDetails="Contact: 987-654-3210"
)

# List a product
artisan.listProduct(
    productID=1,
    productName="Handcrafted Necklace",
    description="Beautiful handcrafted necklace with gemstones",
    price=50.00,
    image="necklace_image.jpg"
)

# Edit a product
artisan.editProduct(
    productID=1,
    new_details={
        'description': "Exquisite handcrafted necklace with gemstones",
        'price': 75.00
    }
)
# Delete a product
artisan.deleteProduct(productID=1)
# Manage products
artisan.manageProduct()

print("_________________________________________________________________________________________________________________")
# Create a JobProvider instance
job_provider = JobProvider(
    userID="1",
    userName="CompanyABC",
    email="companyabc@example.com",
    password="password123",
    profilepicture="profile.jpg",
    biodata="Company ABC is a leading tech company.",
    contactDetails="123-456-7890",
    company="Company ABC",
    joblistings=[]
)

# Fill job details for a job listing
job_provider.fillJobDetails(
    jobID="101",
    jobName="Software Engineer",
    description="Looking for a software engineer with Python expertise.",
    applicationDeadline="2023-01-31",
    salary="$80,000 - $100,000 per year",
    skillsRequirement=["Python", "Django", "Web Development"]
)

# Post a job listing
job_details = {
    'jobID': "102",
    'jobName': "Data Analyst",
    'description': "Data analyst position for data-driven projects.",
    'applicationDeadline': "2023-02-15",
    'salary': "$70,000 - $90,000 per year",
    'skillsRequirement': ["Data Analysis", "SQL", "Statistics"]
}
job_provider.postJob(job_details)

# Review an applicant's application for a job listing
applicant = User(
    userID="2",
    userName="JohnDoe",
    email="johndoe@example.com",
    password="applicantpass",
    profilepicture="applicant.jpg",
    biodata="Experienced software engineer.",
    contactDetails="987-654-3210"
)
job_provider.reviewApplication(jobID="101", applicant=applicant)

# Contact an applicant
job_provider.contactApplicant(applicant, "You have been shortlisted for the Software Engineer position.")

# Edit job details
new_job_details = {
    'jobID': "101",
    'jobName': "Senior Software Engineer",
    'description': "Looking for a senior software engineer with 5+ years of experience.",
    'applicationDeadline': "2023-02-28",
    'salary': "$90,000 - $120,000 per year",
    'skillsRequirement': ["Python", "Django", "Web Development", "Leadership"]
}
job_provider.editJobDetails(jobID="101", new_details=new_job_details)

# Cancel a job posting
job_provider.cancelJobPosting(jobID="102")
