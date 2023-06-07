from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


def get_session():
    load_dotenv()
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE = os.getenv('DATABASE')
    HOST = os.getenv('HOST')

    # Create a database connection URL
    db_url = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"

    # Create an SQLAlchemy engine
    engine = create_engine(db_url)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    return session
