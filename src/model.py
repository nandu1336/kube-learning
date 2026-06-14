from sqlalchemy import ( BigInteger, Column, String, MetaData)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base(metadata=MetaData(schema='dbo'))

class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key = True, autoincrement = True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username!r}, email={self.email!r})>"

    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("Invalid email address")
        return address.lower()


    @validates('username')
    def validate_username(self, key, name):
        if not name or len(name) > 100:
            raise ValueError("Invalid username")
        return name.strip()
