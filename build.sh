# requirements.txt
django==5.0
django-crispy-forms==2.1
whitenoise==6.6.0
gunicorn==21.2.0

# vercel.json
{
    "builds": [
        {
            "src": "build.sh",
            "use": "@vercel/static-build",
            "config": {
                "distDir": "staticfiles"
            }
        }
    ],
    "routes": [
        {
            "src": "/static/(.*)",
            "dest": "/static/$1"
        },
        {
            "src": "/(.*)",
            "dest": "core/wsgi.py"
        }
    ]
}

# build.sh
#!/bin/bash
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput

# .gitignore
*.pyc
__pycache__
db.sqlite3
.DS_Store
*.pyo
*.pyd
.Python
env
pip-log.txt
.env
.venv
ENV/
staticfiles/
media/

