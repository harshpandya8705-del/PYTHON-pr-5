"""
Python OOP Project: Employee Management System ("OOP Wrapper")

Concepts demonstrated
---------------------
* Classes & objects, constructors (__init__) and destructors (__del__)
* Inheritance      : Person -> Employee -> Manager / Developer
* Encapsulation    : private employee_id and salary with getters/setters
* Method overriding: display() overridden in every derived class
* Method overloading (Python style): default/variable arguments + classmethods
* super() and issubclass()
* Menu-driven console user interface
"""


# --------------------------------------------------------------------------
# Base class: Person
# --------------------------------------------------------------------------
class Person:
    """A generic person with a name and an age."""

    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# --------------------------------------------------------------------------
# Employee (derived from Person)
# --------------------------------------------------------------------------
class Employee(Person):
    """Employee with encapsulated (private) employee_id and salary."""

    _count = 0  # number of live Employee-type objects

    def __init__(self, *args):
        """
        Method overloading via variable arguments. Supported call styles:
            Employee()                                  -> all defaults
            Employee(name)                              -> name only
            Employee(name, age)                         -> name + age
            Employee(name, age, employee_id)            -> + id
            Employee(name, age, employee_id, salary)    -> full details
        """
        if len(args) > 4:
            raise TypeError("Employee() takes at most 4 arguments "
                            f"({len(args)} given)")
        name, age, emp_id, salary = (list(args) + ["Unknown", 0, "N/A", 0.0][len(args):])
        super().__init__(name, age)          # call parent constructor
        self.__employee_id = emp_id          # private attribute
        self.__salary = 0.0                  # private attribute
        self.set_salary(salary)              # validated through setter
        Employee._count += 1

    # ---- alternative "constructors" (more overloading) -------------------
    @classmethod
    def from_string(cls, text):
        """Create from 'name,age,id,salary' string."""
        name, age, emp_id, salary = [p.strip() for p in text.split(",")]
        return cls(name, int(age), emp_id, float(salary))

    @classmethod
    def from_dict(cls, data):
        """Create from a dictionary."""
        return cls(data.get("name", "Unknown"), data.get("age", 0),
                   data.get("employee_id", "N/A"), data.get("salary", 0.0))

    # ---- encapsulation: getters & setters --------------------------------
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, emp_id):
        if not str(emp_id).strip():
            raise ValueError("Employee ID cannot be empty.")
        self.__employee_id = str(emp_id).strip()

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        salary = float(salary)
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = salary

    # ---- behaviour --------------------------------------------------------
    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)
        print("Salary: ${}".format(self.__salary))

    def __del__(self):
        # Destructor: release resources / update the live-object counter.
        Employee._count -= 1

    @classmethod
    def live_count(cls):
        return cls._count


# --------------------------------------------------------------------------
# Manager (derived from Employee)
# --------------------------------------------------------------------------
class Manager(Employee):
    def __init__(self, name="Unknown", age=0, emp_id="N/A", salary=0.0,
                 department="General"):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):                       # method overriding
        super().display()
        print("Department:", self.department)


# --------------------------------------------------------------------------
# Developer (derived from Employee)
# --------------------------------------------------------------------------
class Developer(Employee):
    def __init__(self, name="Unknown", age=0, emp_id="N/A", salary=0.0,
                 programming_language="Python"):
        super().__init__(name, age, emp_id, salary)
        self.programming_language = programming_language

    def display(self):                       # method overriding
        super().display()
        print("Programming Language:", self.programming_language)


# --------------------------------------------------------------------------
# User-interface helpers
# --------------------------------------------------------------------------
def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty. Please try again.")


def read_int(prompt, minimum=0, maximum=120):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"  Please enter a number between {minimum} and {maximum}.")
        except ValueError:
            print("  Invalid input. Please enter a whole number.")


def read_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("  Salary cannot be negative.")
        except ValueError:
            print("  Invalid input. Please enter a number.")


def show_menu():
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Exit")


def create_person(store):
    name = read_text("\nEnter Name: ")
    age = read_int("Enter Age: ")
    store["person"] = Person(name, age)
    print(f"\nPerson created with name: {name} and age: {age}.")


def create_employee(store):
    name = read_text("\nEnter Name: ")
    age = read_int("Enter Age: ")
    emp_id = read_text("Enter Employee ID: ")
    salary = read_float("Enter Salary: ")
    emp = Employee(name, age, emp_id, salary)
    store["employee"] = emp
    print(f"\nEmployee created with name: {name}, age: {age}, "
          f"ID: {emp_id}, and salary: ${emp.get_salary()}.")


def create_manager(store):
    name = read_text("\nEnter Name: ")
    age = read_int("Enter Age: ")
    emp_id = read_text("Enter Employee ID: ")
    salary = read_float("Enter Salary: ")
    dept = read_text("Enter Department: ")
    mgr = Manager(name, age, emp_id, salary, dept)
    store["manager"] = mgr
    print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, "
          f"salary: ${mgr.get_salary()}, and department: {dept}.")


def create_developer(store):
    name = read_text("\nEnter Name: ")
    age = read_int("Enter Age: ")
    emp_id = read_text("Enter Employee ID: ")
    salary = read_float("Enter Salary: ")
    lang = read_text("Enter Programming Language: ")
    dev = Developer(name, age, emp_id, salary, lang)
    store["developer"] = dev
    print(f"\nDeveloper created with name: {name}, age: {age}, ID: {emp_id}, "
          f"salary: ${dev.get_salary()}, and language: {lang}.")


def show_details(store):
    print("\nChoose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    print("4. Developer")
    choice = input("Enter your choice: ").strip()

    options = {"1": ("person", "Person"), "2": ("employee", "Employee"),
               "3": ("manager", "Manager"), "4": ("developer", "Developer")}
    if choice not in options:
        print("\nInvalid choice. Returning to main menu.")
        return
    key, label = options[choice]
    obj = store.get(key)
    if obj is None:
        print(f"\nNo {label} has been created yet. Please create one first.")
        return

    print(f"\n{label} Details:")
    obj.display()
    # issubclass() demonstration
    cls = type(obj)
    print(f"\n[issubclass] {cls.__name__} is a subclass of Employee? "
          f"{issubclass(cls, Employee)}")


def main():
    print("--- Python OOP Project: Employee Management System ---")
    store = {}
    actions = {"1": create_person, "2": create_employee,
               "3": create_manager, "4": create_developer,
               "5": show_details}
    first = True
    while True:
        if not first:
            print("\n--- Choose another operation ---")
        first = False
        show_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == "6":
            store.clear()                    # destructors run here
            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!")
            break
        action = actions.get(choice)
        if action:
            action(store)
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
