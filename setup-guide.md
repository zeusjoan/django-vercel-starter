# Instrukcja konfiguracji środowiska deweloperskiego dla Django + Vercel

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że masz zainstalowane:
- MacOS (instrukcja dedykowana dla MacOS)
- Terminal
- Homebrew (jeśli nie, zainstaluj: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`)

## Krok 1: Instalacja podstawowych narzędzi

```bash
# Instalacja Python i Git przez Homebrew
brew install python3 git

# Instalacja VS Code
brew install --cask visual-studio-code
```

## Krok 2: Przygotowanie projektu

```bash
# Utworzenie katalogu projektu
mkdir django-vercel-starter
cd django-vercel-starter

# Utworzenie i aktywacja środowiska wirtualnego
python3 -m venv venv
source venv/bin/activate

# Instalacja wymaganych pakietów Python
pip install django django-crispy-forms whitenoise gunicorn
pip install autopep8 pylint pylint-django

# Utworzenie projektu Django
django-admin startproject core .
python3 manage.py startapp main

# Utworzenie podstawowej struktury katalogów
mkdir -p static/css static/js static/img
mkdir -p media templates/main
```

## Krok 3: Konfiguracja VS Code

1. Instalacja wymaganych rozszerzeń VS Code:
```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension batisteo.vscode-django
code --install-extension ms-python.debugpy
```

2. Utworzenie i konfiguracja katalogu .vscode:
```bash
mkdir -p .vscode
```

3. Utworzenie pliku `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.autoImportCompletions": true,
    
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--django-settings-module=core.settings"
    ],
    
    "editor.formatOnSave": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": true,
        "editor.rulers": [79, 120]
    },
    
    "files.associations": {
        "**/*.html": "html",
        "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt"
    },
    
    "files.exclude": {
        "**/*.pyc": true,
        "**/__pycache__": true,
        ".pytest_cache": true
    },

    "terminal.integrated.env.osx": {
        "DJANGO_SETTINGS_MODULE": "core.settings"
    }
}
```

4. Utworzenie pliku `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver"
            ],
            "django": true,
            "justMyCode": true
        }
    ]
}
```

## Krok 4: Konfiguracja Vercel

1. Utworzenie pliku `vercel.json`:
```json
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
```

2. Utworzenie pliku `build.sh`:
```bash
#!/bin/bash
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
```

3. Nadanie uprawnień dla build.sh:
```bash
chmod +x build.sh
```

4. Utworzenie pliku `requirements.txt`:
```
django==5.0
django-crispy-forms==2.1
whitenoise==6.6.0
gunicorn==21.2.0
```

## Krok 5: Konfiguracja Git

1. Utworzenie pliku `.gitignore`:
```
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
venv/
ENV/
staticfiles/
media/
```

## Weryfikacja instalacji

1. Sprawdzenie czy Django jest zainstalowane:
```bash
python3 -c "import django; print(django.get_version())"
```

2. Wykonanie migracji Django:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

3. Uruchomienie serwera deweloperskiego:
```bash
python3 manage.py runserver
```

## Skróty klawiszowe VS Code

- `F5` - uruchomienie debuggera Django
- `Cmd + Shift + P` - paleta poleceń
- `Cmd + Shift + X` - rozszerzenia
- `Cmd + Shift + E` - eksplorator plików
- `Cmd + `` - terminal

## Ważne przypomnienie

Za każdym razem gdy pracujesz nad projektem, aktywuj środowisko wirtualne:
```bash
source venv/bin/activate
```

## Rozwiązywanie problemów

Jeśli napotkasz problemy z:

1. Interpreterem Python w VS Code:
   - Użyj `Cmd + Shift + P`
   - Wpisz "Python: Select Interpreter"
   - Wybierz interpreter z venv

2. Brakującymi pakietami:
   ```bash
   pip install -r requirements.txt
   ```

3. Prawami dostępu do build.sh:
   ```bash
   chmod +x build.sh
   ```
