Task Overview:
To proceed to the next stage, we ask you to demonstrate your technical abilities by completing a set of tasks designed to assess your coding and  problem-solving skills. The detailed instructions are attached to this email.

Deadline:
Please note that the task must be completed within 5 days from the receipt of this email.

Version Control:
As part of this task, we would like you to demonstrate your version control skills. Please use Git to manage and document the changes you make during the task. This will help us understand your proficiency with essential tools and your approach to code management.

Questions or Concerns:
Should you have any questions or require further clarification about the task, please do not hesitate to reach out. We are here to support you through this process.

Submission:
Upon completion, please submit your work via email and share with us your git repositories. Ensure that your submission clearly demonstrates the progression and version control of your work.

We recognize the effort and time that goes into this task and want to assure you that this is a valuable step in getting to know you and your capabilities better. We are eagerly looking forward to your innovative solutions and approach.

Best of luck, and we hope you find this task both challenging and enjoyable!



# Book Inventory API Project Plan

## Introduction
This document outlines the plan for developing a simple yet functional Book Inventory API using Python Flask. The API will enable users to manage a book inventory by adding new books, retrieving book details, updating book information, and removing books from the inventory. Initial data will be seeded from a provided CSV file.

## Objectives
- Develop a RESTful API using Flask.
- Seed the database with initial data from a CSV file.
- Implement CRUD operations for book management.
- Document the API using Swagger.
- Deploy the API to a free hosting service.

## Development Plan

### Setup and Pre-requisites
- **Python Environment:** Ensure Python and pip are installed.
- **Virtual Environment:** Set up a virtual environment for the project.
- **Flask Installation:** Install Flask and any other necessary libraries.
- **Hosting Account:** Set up an account on a free hosting service suitable for Flask applications.

### Database Design
- **Models:** Define a `Book` model with fields such as `id`, `title`, `author`, and `year_published`.
- **Database Initialization:** Configure Flask-SQLAlchemy for database management.

### API Development
#### 1. Seeding Data
- **CSV Parsing:** Write a script to read initial book data from the provided CSV file.
- **Database Seeding:** Insert parsed data into the database as initial records.

#### 2. CRUD Operations
- **Create (POST):** Endpoint to add a new book to the inventory.
- **Read (GET):** Endpoints to retrieve all books and single book details.
- **Update (PUT/PATCH):** Endpoint to update an existing book's information.
- **Delete (DELETE):** Endpoint to remove a book from the inventory.

### API Documentation
- **Swagger Setup:** Integrate Swagger with Flask to document each endpoint, including its purpose, parameters, and expected responses.

### Testing
- Outline a basic strategy for testing each endpoint, ensuring that all CRUD operations perform as expected.

### Deployment
- **Deployment Process:** Detail the steps to deploy the API to the chosen free hosting service.
- **Environment Setup:** Ensure the environment is properly configured with all necessary dependencies.

## Conclusion
Summarize the goals and expected outcomes of the project.

## Appendix
- **References:** Any references or resources to be used.

https://www.fullstackpython.com/flask.html

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

HTTP status code for CRUD

https://www.moesif.com/blog/technical/api-design/Which-HTTP-Status-Code-To-Use-For-Every-CRUD-App/


# Notes:
- Update this document as the project evolves.
- Use the Issues and Projects tabs in the repository to track progress and tasks.

# Start:
-Received the task on Dec, 21 2023 at 6:41PM

END of Day 1, Able to tackle all Tasks, and able to deploy the service on Render.com
Even though the service able to run, the code base for this web api can still be improved.
Main concern is about the database URL, I will look into it and find solution for it.

old link : https://book-inventory-api.onrender.com


END of Day 2, Deploy the api through docker on render.com.
Get the swagger/openapi to work with the web api

working link on day 2 : https://docker-book-inventory-api.onrender.com

might take 2 mins in order for service to restart

END of Day 3, Realise that I have made a mistake regarding the book table, on day 1, in the midst of chasing the goal to tackle all the tasks and deploy on a hosting website. I somehow overlook the fact that, even though ISBN number are unique to each book, it is possible for a book not have ISBN number if it was not officially published, hence it cant be a primary key.

Its like I wore my developer hat, but forgot to put on my database designer glasses :dizzy:

After fixing the book table, I fix the status code for Create method, then update the web api swagger doc accordingly.

Also patch the database url leak by using .env variable.

END of day 4,

Decided to change the code structure, instead of monolithic, changed to modular.

Also improve the seed script and automate the seeding procedure at the start of service

Also delve in deeper into proper status code handling. The code can still be improved regarding that matter.

END of TASK <><><><>

Add the student table, And implement the one to many relationship between student and book,

Updated the openapi/swagger doc to match the current implementation.

# Task Conclusion and Review
The tasks is about developing a restful API for a book inventory, which also store the information about the student that borrowed books.

To me it was an engaging tasks, I am able to learn new things regarding building a restful API using flask framework, it also open up new knowledge for me especially regarding the status code handling.

Its clear to me that, I have a long road ahead of me in order to fully grasp the knowledge of building the restful API with flask.

To Summarize

API development :

1. Seeding Data:

I am able to create a seed script for adding initial values when a book table was newly created. I make use of sqlalchemy lib to complete the task.

2. CRUD Operations:

Able to successfully implement the CRUD operations for book and student table. And also implement one to many relationship between them.

API Documentation:

API documentation was succefully created using flask_swagger_ui library. Users can also interact with the API by using the swagger documentation.

Testing:

I tested the API through 3 medium, using the web browser, insomnia application, and swagger documentation. By testing, it also help me in status code handling process.

Deployment:

I deployed the API and the Postgresql Database on Render.com . The deployment is straight forward, it start by creating an account, then select the service to deploy, then put in the necessary information such and environment variable for postgresql URL.




