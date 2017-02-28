import hashlib
# class WrongDataForm(Exception):
#     pass


# class UsernameAlreadyExists(Exception):
#
#     def __init__(self):
#         if self.username in self.usernames and self.password != self.usernames[self.username]:


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False
        # while True:
        #     print("Hello, user. Here you can sign in/up.")
        #     try:
        #         self.username = input("Enter your username(at least 3 characters long): ")
        #         self.password = input("Enter your password(at least 8 characters long): ")
        #     except UsernameAlreadyExists:
        #
        #     if len(self.username) >= 3 and len(self.password) >= 8:
        #         if len(self.usernames) != 0 and self.usernames[self.username] == self.password:
        #             print("Welcome back, {}.".format(self.username))
        #         elif self.username in self.usernames and self.password != self.usernames[self.username]:
        #             raise UsernameAlreadyExists("this username is already taken")
        #         else:
        #             self.usernames[self.username] = self.password
        #         break
        #     else:
        #         raise WrongDataForm("username and/or password too short")
        # # print("wrong username. get out")
        # print(self.username, self.password)

    def _encrypt_pw(self, password):
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class MyException(Exception):
    def __init__(self, username):
        super().__init__(username)
        self.username = username


class UsernameAlreadyExists(MyException):
    pass


class PasswordTooShort(MyException):
    pass


class UsernameTooShort(MyException):
    pass


class UsernameNonexistent(MyException):
    pass

class PasswordIncorrect(MyException):
    pass


class PermissionError(Exception):
    pass


class NotLoggedInError(MyException):
    pass


class NotPermittedError(MyException):
    pass


class Authenticator:

    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(username) < 3:
            raise UsernameTooShort
        if len(password) < 8:
            raise PasswordTooShort
        self.users[username] = User(username, password)

    def log_in(self, username, password):
        try:
            logged_user = self.users[username]
        except KeyError:
            raise UsernameNonexistent
        if logged_user.check_password(password):
            logged_user.is_logged_in = True
            return True
        else:
            raise PasswordIncorrect

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False


authenticator = Authenticator()


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        '''Create a new permission that users
        can be added to'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        '''Grant the given permission to the user'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True



authenticator = Authenticator()
authenticator.register_user("lukatriska", "1999triska")
print(authenticator.users)
authorizor = Authorizor(authenticator)

print(authenticator)
print(authorizor)

