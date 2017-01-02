from src.deenuxapi.Model import Model

class User(Model):

    def __init__(self, id, username, firstname, lastname, email):
        super(User, self).__init__(id)
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email