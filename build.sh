
#!/usr/bin/env bash

echo "Construyendo aplicación..."
python3 -m pip install -r requirements.txt


echo "Recopilando archivos estáticos..."
python3 manage.py collectstatic --noinput
