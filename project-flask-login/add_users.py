from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///database.db', echo=True)

Session = sessionmaker(bind=engine)
s = Session()
    
usuario = User(username="admin", password="admin")
s.add(usuario)
s.commit()