Example Django app created for Stack Overflow DevDays in Amsterdam

To try it out (make sure you have installed Django first):

$ ./manage.py syncdb
... create yourself a super user account ...

$ ./manage.py loaddata events < events.json 
Installing json fixture 'events' from absolute path.
Installed 22 object(s) from 1 fixture(s)

$ ./manage.py runserver 8000

Now visit:

http://localhost:8000/events/amsterdam/
http://localhost:8000/admin/
