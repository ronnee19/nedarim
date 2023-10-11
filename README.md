# nedarim

# Iron Sords - Finding missing persons
## Local development:
In order to run in your own local env, please run the following:

`git clone https://github.com/ronnee19/nedarim.git
cd nedarim
`
create virtual env:
https://docs.python.org/3/library/venv.html

For mac/unix OS:
```
python -m venv ./
source .venv/bin/activate
pip install -r requirements.txt
```
Every push to master will automatically deploy the app with the latest version.

## Run the application on the local env (Be carefull!!!):
The command to run the app locally:

`streamlit run ./main.py `

Link to production:
https://nedarim-icfb24kwtfz6vpz9bypp2z.streamlit.app/

# To configure postgress DB:

To switch connection into postgress database do the following:

Create a file: "[project dir]/.streamlit/secrets.toml"
put the following in the file

[connections.postgresql]
dialect = "postgresql"  
host = "localhost"  
port = "5432"  
database = "xxx"  
username = "xxx"  
password = "xxx"  

get creds/details from David Oz via secured way

make sure you turn the db on flag on python main.py file

