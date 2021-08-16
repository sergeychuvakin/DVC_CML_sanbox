# DVC_CML_sanbox
Here you can find basic ML pipeline that can be used to configure you DVC-CML infrastructure
reqs:
pandas swifter stopwords nltk numpy sklearn spacy pyarrow fastparquet

1) git ignore manually 
*.pkl
*.parquet
*.csv
output.txt
2) git ignore auto 
/metrics.txt
/metrics.json
3) git dvc.lock
dvc metrics diff > output.txt

4) metrics should be in git