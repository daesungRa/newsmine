


class Users:
    def __init__(self):
        pass

    def get_by_username_or_id(self, id: str = None, username: str = None):
        return {
            'id': id and id or -1,
            'username': username and username or 'smpl_user',
        }

