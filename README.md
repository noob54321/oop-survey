# OOP-Survey
A project for CSC 0102, a simple rating-survey generation site.

# Requirements
- [python3](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [virtualenv](https://pypi.org/project/virtualenv/)

# Instructions
1. Clone the repository. [Guide](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
2. Setup the environment in the main directory
```
oop-survey/
    ... # some apps and file
    <target>
```
Command
```
    virtualenv venv
```
3. Activate the environment
```
    venv\bin\activate
```
Output
```
    (venv) <currentDirectory>
```
4. Install the requirements
```
    pip install -r requirements.txt
```
5. Create .env
```
    oop-survey/
        ... # otherfile
        .env
```
6. Copy the corresponding data in env.development if development mode else env.production to the .env

# Build
1. Run makemigrations
```
    python manage.py makemigrations
```
2. Run migrate
```
    python manage.py migrate
```

# Run Server
```
    python manage.py runserver # default 127.0.0.1:8000
```