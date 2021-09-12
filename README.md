# DVC_CML_sanbox
Here you can find basic ML pipeline that can be used to configure you DVC-CML infrastructure
reqs:

Do:
- git clone https://github.com/sergeychuvakin/DVC_CML_sandbox
- cd DVC_CML_sandbox
- pythob -m venv env 
- source env/bin/activate
- pip install -r requirements.txt

TRY: 
- dvc dag
- dvc repro
- dvc metrics --show
- dvc metrics --diff
