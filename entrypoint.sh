#!/bin/sh

# Espera o banco ficar disponível (simples polling)
echo "Esperando pelo banco de dados..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "Banco de dados disponível. Rodando migrations..."
python manage.py migrate

echo "Iniciando o servidor..."
exec "$@"
