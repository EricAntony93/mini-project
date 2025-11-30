import os, sys
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','plantzaura.settings')
import django
django.setup()
from django.db import connection

cur = connection.cursor()
tables = connection.introspection.table_names()
print("Existing tables:", tables)

# drop leftover temporary migration tables
temp_tables = [t for t in tables if t.startswith("new__App_")]
if not temp_tables:
    print("No temp new__App_ tables found.")
else:
    for t in temp_tables:
        print("Dropping temp table:", t)
        cur.execute(f'DROP TABLE IF EXISTS "{t}"')
    cur.connection.commit()
    print("Dropped temp tables. New table list:", connection.introspection.table_names())
