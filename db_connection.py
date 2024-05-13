from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker
from immutabledict import immutabledict

# connection string format driver+postgresql://user:pass@host:port/dbname
engine = create_engine("postgresql+psycopg2://adm_recept:recept@localhost:5432/recept", echo=True) 
#, echo_pool="debug"


# url = URL(
#     drivername="postgresql+psycopg2",
#     username="adm_recept",
#     password="recept",
#     host="localhost",
#     port=5432,
#     database="recept",
#     query=immutabledict(),  # immutabledict({'alt_host': ('host1', 'host2'), 'ssl_cipher': '/path/to/crt'})
# )

# engine = create_engine(url, echo=True)

session_pool = sessionmaker(engine)


with session_pool() as session:
    # session.add(some_other_object)
    rezso = session.execute(text("SELECT NOW  ()"))

print(rezso.all())
    