source ../../venv/gimkana/bin/activate
source ../venv/bin/activate

python3 manage.py loaddata gimkana/fixtures/users.json
python3 manage.py loaddata gimkana/fixtures/qrs.yaml
python3 manage.py loaddata gimkana/fixtures/shops.yaml
