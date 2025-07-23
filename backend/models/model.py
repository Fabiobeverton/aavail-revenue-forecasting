import os
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from datetime import datetime
import logging

MODEL_PATH = "models/model.joblib"
DATA_PATH = "data/revenue.csv"

# Setup logging
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO
)

def train_model():
    if not os.path.exists(DATA_PATH):
        logging.error(f"Arquivo de dados não encontrado: {DATA_PATH}")
        raise FileNotFoundError(f"Arquivo de dados não encontrado: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    if df.empty:
        logging.error("O arquivo de dados está vazio.")
        raise ValueError("O arquivo de dados está vazio.")

    # Validação básica dos dados
    required_columns = {"country", "date", "revenue"}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        logging.error(f"Colunas obrigatórias ausentes: {missing}")
        raise ValueError(f"Colunas obrigatórias ausentes: {missing}")

    try:
        df["date"] = pd.to_datetime(df["date"])
        df["dayofyear"] = df["date"].dt.dayofyear
    except Exception as e:
        logging.error(f"Erro ao converter datas: {e}")
        raise

    X = df[["country", "dayofyear"]]
    y = df["revenue"]

    preprocessor = ColumnTransformer([
        ("country_encoder", OneHotEncoder(handle_unknown='ignore'), ["country"])
    ], remainder='passthrough')

    pipeline = Pipeline([
        ("preprocessing", preprocessor),
        ("regression", LinearRegression())
    ])

    try:
        pipeline.fit(X, y)
        joblib.dump(pipeline, MODEL_PATH)
        logging.info(f"Modelo treinado e salvo em: {MODEL_PATH}")
    except Exception as e:
        logging.error(f"Erro ao treinar ou salvar o modelo: {e}")
        raise

def load_model():
    if not os.path.exists(MODEL_PATH):
        logging.error(f"Modelo não encontrado em: {MODEL_PATH}. Treine o modelo primeiro.")
        raise FileNotFoundError(f"Modelo não encontrado em: {MODEL_PATH}. Treine o modelo primeiro.")
    try:
        return joblib.load(MODEL_PATH)
    except Exception as e:
        logging.error(f"Erro ao carregar o modelo: {e}")
        raise

def predict(model, country: str, date: str):
    try:
        date_obj = pd.to_datetime(date)
        dayofyear = date_obj.dayofyear
        X_pred = pd.DataFrame([{"country": country, "dayofyear": dayofyear}])
        revenue = model.predict(X_pred)[0]
        return {
            "country": country,
            "target_date": date,
            "predicted_revenue": round(float(revenue), 2)
        }
    except Exception as e:
        logging.warning(f"Erro na previsão: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    try:
        train_model()
        logging.info("Treinamento concluído com sucesso.")
    except Exception as e:
        logging.error(f"Falha no treinamento do modelo: {e}")
