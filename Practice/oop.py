class x: ...
class y: ...
class z: ...

class User:
    name = ''
    email = ''
    phone = ''

    def register(self):
        print("This is a register method")

    def login(self):
        print("This is a login method")

        john_obj = User()
        john_obj.name = "John Doe"
        john_obj.email = "john@example.com"
        john_obj.phone = "123-456-7890"

        sheila_obj = User()
        sheila_obj.name = "Sheila Smith"
        sheila_obj.email = "sheila@example.com"
        sheila_obj.phone = "098-765-4321"

        print(john_obj.name)
        print(sheila_obj.phone)


user = User()
user.login()


class Customer:
    name = ''
    email = ''
    phone = ''

    def sign_up(self):
        print("This is a sign up method")

    def authenticate(self):
        print("This is an authenticate method")

        alice_obj = Customer()
        alice_obj.name = "Alice Johnson"
        alice_obj.email = "alice@example.com"
        alice_obj.phone = "111-222-3333"

        bob_obj = Customer()
        bob_obj.name = "Bob Wilson"
        bob_obj.email = "bob@example.com"
        bob_obj.phone = "444-555-6666"

        print(alice_obj.name)
        print(bob_obj.phone)


customer = Customer()
customer.sign_up()
customer.authenticate()
