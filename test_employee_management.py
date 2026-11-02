import unittest
from employee_management import Person, Employee, Manager, Developer


class TestOOP(unittest.TestCase):
    def test_overloaded_constructors(self):
        self.assertEqual(Employee().get_employee_id(), "N/A")
        self.assertEqual(Employee("A", 30).age, 30)
        e = Employee("A", 30, "E1", 100)
        self.assertEqual((e.get_employee_id(), e.get_salary()), ("E1", 100.0))
        self.assertEqual(Employee.from_string("B,25,E2,500").get_salary(), 500.0)
        self.assertEqual(Employee.from_dict({"name": "C"}).name, "C")
        with self.assertRaises(TypeError):
            Employee(1, 2, 3, 4, 5)

    def test_encapsulation(self):
        e = Employee("A", 30, "E1", 100)
        self.assertFalse(hasattr(e, "salary"))
        e.set_salary(200)
        self.assertEqual(e.get_salary(), 200.0)
        with self.assertRaises(ValueError):
            e.set_salary(-1)

    def test_inheritance_and_issubclass(self):
        self.assertTrue(issubclass(Manager, Employee))
        self.assertTrue(issubclass(Developer, Employee))
        self.assertTrue(issubclass(Employee, Person))
        self.assertFalse(issubclass(Person, Employee))

    def test_overriding(self):
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            Manager("M", 40, "M1", 10, "HR").display()
            Developer("D", 22, "D1", 10, "Java").display()
        out = buf.getvalue()
        self.assertIn("Department: HR", out)
        self.assertIn("Programming Language: Java", out)


if __name__ == "__main__":
    unittest.main()
