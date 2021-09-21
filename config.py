class Config:
    
    TRAIN_RAW: str = "./raw.csv"
    TRAIN_PROCESSED: str = "./processed.csv"
    TRAIN_VECTORIZED: str = "./vectorized.parquet"
    TRAIN_VALID: str = "./vectorized_valid.parquet"
    TRAIN_MODEL: str = "model.pkl"
    
    TRAIN_RAW_2: str = "./raw2.csv"
    TRAIN_PROCESSED_2: str = "./processed2.csv"
    TRAIN_VECTORIZED_2: str = "./vectorized2.parquet"
    TRAIN_VALID_2: str = "./vectorized_valid2.parquet"
    TRAIN_MODEL_2: str = "model2.pkl"
    