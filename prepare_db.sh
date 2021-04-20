set -e

source /fmrm/venv/bin/activate
cd /fmrm/gimkana_festa_major
rm db.sqlite3
python3 manage.py migrate
python3 manage.py loaddata gimkana/fixtures/users.json
python3 manage.py loaddata gimkana/fixtures/qrs.yaml

