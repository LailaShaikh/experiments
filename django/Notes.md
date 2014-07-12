Django Db router:
================
`
 python manage.py syncdb --database=write_db

 python manage.py shell

 Entry.objects.create(title="post3",body="English language is modern language")
 Entry.objects.create(title="Post about english",body="English language is modern language",slug="english")

 In [10]: Entry.objects.using('write_db')
 Out[10]: [<Entry: <Entry:post2>>, <Entry: <Entry:Post about english>>]

 In [11]: Entry.objects.using('read_db')
 Out[11]: [<Entry: <Entry:test>>]
`