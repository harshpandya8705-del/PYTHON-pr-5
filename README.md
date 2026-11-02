PYTHON OOP PROJECT: EMPLOYEE MANAGEMENT SYSTEM (OOP WRAPPER)

ABOUT THE PROJECT
This is a menu-driven console application written in Python. It models people and employees using Object-Oriented Programming concepts such as classes, inheritance, encapsulation, method overriding and method overloading.


PROJECT FILES
1. employee_management.py - main program with all classes and the menu (run this file)
2. test_employee_management.py - unit tests
3. generate_output_pdf.py - runs a demo and creates the output PDF
4. sample_output.txt - console output of a real run
5. Project_Output.pdf - program output in PDF format
6. README.md - this file


HOW TO RUN
1. Install Python 3.8 or higher.
2. Open a terminal in the project folder.
3. Start the program with: python employee_management.py
4. Run the tests with: python -m unittest -v
5. To regenerate the PDF (optional): pip install reportlab, then python generate_output_pdf.py


CLASS DESIGN
Person - has name and age.
Employee - inherits from Person. Adds private employee_id and private salary.
Manager - inherits from Employee. Adds department.
Developer - inherits from Employee. Adds programming_language.


FEATURES AND HOW EACH REQUIREMENT IS MET
1. Employee base class: Employee class has employee_id, name, age and salary.
2. Getters and setters: get_salary, set_salary, get_employee_id and set_employee_id are provided, with validation.
3. Constructor and destructor: __init__ creates the object and __del__ cleans up when it is deleted.
4. Use of self: used in all instance methods to refer to the object's own attributes.
5. Manager class: adds department and overrides display().
6. Developer class: adds programming_language and overrides display().
7. Method overloading: Python does not support true overloading, so the Employee constructor accepts 0 to 4 arguments, and extra constructors from_string() and from_dict() are provided.
8. Encapsulation: salary and employee_id are private and can only be accessed through getter and setter methods.
9. Inheritance and method overriding: Person -> Employee -> Manager / Developer, and each class overrides display().
10. super(): used in constructors and display() to call the parent class.
11. issubclass(): used in Show Details to check whether a class is a subclass of Employee.
12. User interface: a menu-driven interface with an Exit option.


MENU OPTIONS
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit


ASSUMPTIONS
1. Python has no true method overloading, so it is done using variable arguments and alternative constructors.
2. Person is the top class, because the sample output creates a Person with name and age, and Employee also needs name and age.
3. A "Create a Developer" option was added to the menu because the project requires a Developer class. Because of this, Show Details is option 5 and Exit is option 6.
4. Show Details displays the most recently created object of each type.
5. Salary cannot be negative, age must be a whole number between 0 and 120, and text fields cannot be empty. Wrong input asks the user again.
6. The project text mentions adding, updating and removing employees, but the sample interface only shows create, show and exit, so the interface follows the sample. Updating is possible in code through the setter methods.


SAMPLE OUTPUT
Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 3

Enter Name: Alice Johnson
Enter Age: 40
Enter Employee ID: M456
Enter Salary: 80000
Enter Department: Sales

Manager created with name: Alice Johnson, age: 40, ID: M456, salary: $80000.0, and department: Sales.

The full output is in sample_output.txt and Project_Output.pdf.


GITHUB SUBMISSION STEPS
1. git init
2. git add .
3. git commit -m "Employee Management System - OOP project"
4. git branch -M main
5. git remote add origin https://github.com/your-username/your-repo-name.git
6. git push -u origin main
7. Submit the GitHub repository link to your instructor.


ORIGINALITY
All code was written for this assignment. No code was copied from classmates.
