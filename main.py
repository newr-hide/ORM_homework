import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock

DSN = 'postgresql://postgres:root@localhost:5432/ORM_db_test'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# publisher = Publisher(name='Толстой')
# session.add(publisher)
# session.commit()

#





session.close()