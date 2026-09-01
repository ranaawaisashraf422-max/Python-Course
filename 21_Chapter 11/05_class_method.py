class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

object = Employee()
object.a = 45

object.show()