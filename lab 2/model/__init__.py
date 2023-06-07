from dao_factory import factory


# from connection import get_pool


class User:
    id: int = None
    login: str
    password: str
    role: int = None  # 1- user, 2- admin, 3- master

    def __init__(self, id=None, login=None,  password=None, role=None):
        self.id = id
        self.login = login
        self.password = password
        self.role = role


class Illness:
    id: int
    illness_name: str = None
    illness_type: str = None
    illness_description: str = None
    status: str = None  # 'pending', 'accepted', 'rejected', 'healed'
    user_id: int = None
    price: float = None

    def __init__(self, name, type, description, status, user_id, price, request_id=None):
        self.id = request_id
        self.illness_name = name
        self.illness_type = type
        self.illness_description = description
        self.status = status
        self.user_id = user_id
        self.price = price


class Feedback:
    id: int
    request_id: int = None
    doctor_id: int = None
    text: str = None

    def __init__(self, id=None, request_id=None, master_id=None, text=None):
        self.id = id
        self.illness_id = request_id
        self.doctor_id = master_id
        self.text = text
