# nedarim

To switch connecton into postgress database do the following:

Create a file: "[project dir]/.streamlit/secrets.toml"
put the following in the file:

# .streamlit/secrets.toml

[connections.postgresql]
dialect = "postgresql"
host = "localhost"
port = "5432"
database = "xxx"
username = "xxx"
password = "xxx"


get credd/details from David Oz via secured way
