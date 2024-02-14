# 1. Install requirements

## create and activate virtual environment: 
python -m venv venv
<br>
source venv/bin/activate
## Install requirements:
pip isntall -r requirements.txt


# 2. Start project
## For migrations: 
 python manage.py makemigrations
 <br>
 python manage.pt migrate
## After migrations are done use:
 python manage.py runserver
