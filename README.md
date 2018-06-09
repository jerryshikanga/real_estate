# real_estate
To run this program :
Navigate into the root folder
Run :
pip install -r requirement.txt
python manage,py collectstatic
python manage.py makemigrations
python manage.py migrate

In settings.py :
 look for allowed hosts an add your host name/ip
 change database settings to yours


python manage.py shell
Here do
import init_script
init_script.main()