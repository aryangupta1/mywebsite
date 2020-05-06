# mywebsite
My portfolio
HOW TO CLONE
1.Install and run virtual environment
--pip install virtualenv
--virtualenv 'envname'
--source 'envname'/bin/activate
2.Install requirements and dependencies
--pip install -r requirements.txt
3.Run server
--python manage.py runserver

If step3 does not work try:
--python manage.py makemigrations
--python manage.py migrate
--python manage.py runserver


--If you're getting an error with python, use python3 instead 
  -- e.g. python3 manage.py runserver
