from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

    role = relationship('Role')


class Illness(Base):
    __tablename__ = 'illness'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(50), nullable=False)
    product_model = Column(String(50), nullable=False)
    problem_description = Column(Text, nullable=False)
    price = Column(Integer)
    status = Column(Enum('pending', 'accepted', 'rejected', 'in-process', 'healed'), nullable=False, default='pending')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

    user = relationship('User')


class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    request_id = Column(Integer, ForeignKey('illness.id'), nullable=False)
    master_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

    illness = relationship('Illness')
    master = relationship('User')
