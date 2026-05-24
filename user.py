class User:
    def __init__(self, first_name, last_name, age, email, password, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.password = password
        self.phone_number = phone_number
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")

    def greetings_user(self):
        print(f"Greetings, {self.first_name} {self.last_name}!")


user_1 = User("Artem", "Lehotskyi", 18, "artemlehotskyi@gmail.com", 6969696969696, "0679560282")
user_1.describe_user()
user_1.greetings_user()
print("--------------------------------")

user_2 = User("Anna", "Smith", 25, "anna@gmail.com", 12345, "0991234567")
user_2.describe_user()
user_2.greetings_user()
print("--------------------------------")
user_3 = User("Ivan", "Petrenko", 30, "ivan@gmail.com", 99999, "0671112233")
user_3.describe_user()
user_3.greetings_user()
print("--------------------------------")


user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)