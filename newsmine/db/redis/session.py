

class Session:  # TODO: Implement after installing redis
    def __init__(self, username):
        self.name = f'session_{username}'
        self.username = username

