set -e

source /fmrm/venv/bin/activate
cd /fmrm/gimkana_festa_major
python3 manage.py loaddata gimkana/fixtures/qrs.yaml
