from user2 import UserProfile


class Privileges():
    """ An attempt to define Users Privileges"""

    def __init__(self):
        """ Initialize Privileges Class """
        self.privileges = {}

    def add_privileges(self):
        """ Creates Roles and Tasks to be assigned """
        privilege_name = ""
        while privilege_name != "n":
            privilege_name = input("Role ('n' to quit): ")
            if privilege_name == "n":
                break
            else:
                privilege_description = input("Tasks: ")
                self.privileges[privilege_name] = privilege_description

    def show_privileges(self):
        """ List Roles and Tasks that conform the Privileges"""
        print("User's Privileges: ")
        for name in self.privileges:
            print(name + ": " + self.privileges[name])

class Admin(UserProfile):
    """ Defines a special type of User: Admin"""

    def __init__(self, name, lastname, city, genre):
        super().__init__(name, lastname, city, genre)
        """
        Initialize attributes of the parent class
        Then initialize attributes of the specific class Admin
        """
        self.privileges = Privileges()

    def admin_add_privileges(self):
        """ Add Admin Privileges """
        self.privileges.add_privileges()

    def admin_show_privileges(self):
        """ Show Admins Privileges on the system"""
        super().describe_user()
        self.privileges.show_privileges()
