import os, sys
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','plantzaura.settings')  # adjust if your settings module differs
import django
django.setup()
from django.db import connection

sql = """
CREATE TABLE IF NOT EXISTS "App_userprofile" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "username" varchar(150) NULL,
    "email" varchar(254) NULL,
    "user_id" integer NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE("user_id")
);
"""

cur = connection.cursor()
cur.execute(sql)
cur.connection.commit()

# create index on user_id if not present (safe)
try:
    cur.execute('CREATE INDEX IF NOT EXISTS "App_userprofile_user_id_idx" ON "App_userprofile" ("user_id");')
    cur.connection.commit()
except Exception:
    pass

print("Ensured App_userprofile exists (with username,email,user_id).")
