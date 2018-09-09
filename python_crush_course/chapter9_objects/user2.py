class UserProfile():
    """ Attempt to model a User Profile object """

    def __init__(self, first, last, city, genre):
        self.first = first
        self.last = last
        self.city = city
        self.genre = genre
        self.login_attempts = 0

    def describe_user(self):
        print("\nName: {} {}\nGenre: {}\nCity: {}\nLogin Attempts: {}".format(self.last, self.first, self.genre,
                                                                              self.city, self.login_attempts))


    def greet_user(self):
        print("Welcome {} {}!".format(self.first, self.last))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
