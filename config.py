class Config:
    TRAIN_RAW: str = "./raw.csv"
    TRAIN_PROCESSED: str = "./processed.csv"
    TRAIN_VECTORIZED: str = "./vectorized.parquet"
    TRAIN_VALID: str = "./vectorized_valid.parquet"
    TRAIN_MODEL: str = "model.pkl"
    CONNECTION_STRING = "mysql+pymysql://serge:passpass@localhost:3306/mlflow_models"
    # CONNECTION_STRING = pos
    #<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>