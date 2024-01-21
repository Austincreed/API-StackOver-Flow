This Repo contains Backend code for API that
1. LOADS all data from StackOverFlow API to Local Database.
2. Now On the Local Databse the API allows to perform GET, POST, PUT, PATCH, DELETE operations.

This API has been built using flask, so to run this API on the teminal you have to follow the steps:-
1.  .\venv\Scripts\activate  ---> to activate flask environment
2. $env:FLASK_APP="app"
3. $env:FLASK_ENV="development"  ---> turing the environment into ddevelopment mode
4. $env:FLASK_DEBUG=1  ---> to turning on the DEBUG MODE
5. .$env:PYTHONDONTWRITEBYTECODE=1  ---> To restrict the environment for auto creation of pycache folder
