# Restaurant Kitchen Service

Django project for managing cars and drivers in the Taxi Service

## Try it!

Use the following user to log in and check the functionality of the website: 

```shell
login: Admin
password: q123ewasd
```

## Installation 

Python3 must be already installed

```shell
git clone https://github.com/Vanya2389/restaurant-kitchen-service.git
cd restaurant-kitchen-service
python3 -m venv venv
source venv/bin/activate  # on macOS
venv\Scripts\activate  # on Windows 
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata data.json
python manage.py runserver #starts Django Server
```

## Features

* Authentication functionality for Cook/User
* Managing dishes, cooks & dish types directly from website interface
* Powerful admin panel for advanced managing

## Demo

![Website Interface](demo/home.png)
![Website Interface](demo/cook.png)
![Website Interface](demo/dish_list.png)
![Website Interface](demo/dish_update.png)
![Website Interface](demo/dish_delete.png)
