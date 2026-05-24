from user import User

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for p in self.privileges:
            print(p)


class Admin(User):
    def __init__(self, first_name, last_name, age, email, password, phone_number):
        super().__init__(first_name, last_name, age, email, password, phone_number)
        self.priv = Privileges([
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users"
        ])


admin = Admin("Artem", "Lehotskyi", 18, "artemlehotskyi@gmail.com", 6969696969696, "0679560282")
admin.priv.show_privileges()