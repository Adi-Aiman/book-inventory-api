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

# Notes:
- Update this document as the project evolves.
- Use the Issues and Projects tabs in the repository to track progress and tasks.

# Start:
-Received the task on Dec, 21 2023 at 6:41PM
