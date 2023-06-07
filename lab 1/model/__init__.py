import datetime


class User:
    id: int = None
    login: str
    password: str
    role: int  # 1- patient, 2- doctor, 3- admin

    def __str__(self):
        return f"User id: {self.id}, login: {self.login}, password_hash: {self.password}," \
               f"user's role: {self.role} "


class Illness:
    id: int
    illness_name: str = None
    illness_type: str = None
    illness_description: str = None
    status: str = None  # 'pending', 'accepted', 'rejected', 'healed'
    user_id: int = None
    created_at: datetime = None
    price: float = None

    def __str__(self):
        return None


class Feedback:
    id: int
    illness_id: int = None
    doctor_id: int = None
    text: str = None
    created_at: datetime = None

    def __str__(self):
        return f"Healing id: {self.id}, healing year {self.year}," \
               f"is it healed {self.is_healed}, price: {self.price}"
