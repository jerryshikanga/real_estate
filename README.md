# real_estate
####To run this program :
Requirements 
* Python 3.5 or newer version
* Mysql database
---
Navigate into the root folder and run the following commands
1. pip install -r requirement.txt
2. python manage,py collectstatic
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py shell
>>In the shell propmt enter the following code
---
'''import init_script'''
---
'''init_script.main()'''

In settings.py
* look for allowed hosts an add your host name/ip
* change database settings to yours

