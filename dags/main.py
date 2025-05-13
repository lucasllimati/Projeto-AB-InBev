# ====================================
# 📦 Importações de bibliotecas
# ====================================
import os
import json
import requests
import pandas as pd
import logging
from unidecode import unidecode

# ====================================
# Configuração de Logs
# ====================================
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ====================================
# Definição dos caminhos dos arquivos
# ====================================
# Caminho onde os dados brutos em JSON serão armazenados
BRONZE_PATH = "data_lake/bronze/breweries_raw.json"
# Caminho onde os dados brutos convertidos para CSV serão salvos
BRONZE_CSV_PATH = "data_lake/bronze/breweries_raw_converted.csv"
# Caminho para salvar os dados limpos (transformados), particionados por estado
SILVER_PATH = "data_lake/silver/"
# Caminho para salvar os dados agregados no formato parquet
GOLD_PATH = "data_lake/gold/breweries_final.parquet"

# ====================================
# 1.0 Etapa de Extração
# ====================================
def extrair_dados_breweries():
    # Extrai dados da API Open Brewery DB paginadamente e salva como JSON na camada bronze.
    try:
        url = "https://api.openbrewerydb.org/v1/breweries"
        all_data = []
        page = 1
        per_page = 50  # Número de registros por página

        while True:
        # while page <= 5:
            response = requests.get(url, params={"page": page, "per_page": per_page})
            response.raise_for_status()
            data = response.json()

            if not data:
                break

            all_data.extend(data)
            logging.info(f"📥 Pagina {page} extraida com {len(data)} registros")
            page += 1

        os.makedirs(os.path.dirname(BRONZE_PATH), exist_ok=True)
        with open(BRONZE_PATH, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=2, ensure_ascii=False)

        logging.info(f"✅ Dados extraidos e salvos em {BRONZE_PATH}")
    except Exception as e:
        logging.error(f"❌ Erro na extracao de dados: {e}")

# ====================================
# 1.1 Conversão JSON para CSV
# ====================================
def converter_json_para_csv():
    # Converte o JSON extraído para CSV usando Pandas.
    try:
        with open(BRONZE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        df = pd.DataFrame(data)
        df.to_csv(BRONZE_CSV_PATH, index=False, encoding="utf-8-sig")
        logging.info(f"✅ Dados convertidos para CSV em {BRONZE_CSV_PATH}")
    except Exception as e:
        logging.error(f"❌ Erro na conversao para CSV: {e}")

# ====================================
# 2️ Etapa de Transformação
# ====================================
def transformar_dados():
    # Limpa os dados, normaliza textos e salva particionado por estado no formato parquet.
    try:
        df = pd.read_csv(BRONZE_CSV_PATH, encoding="utf-8-sig")

        # Espaços em branco removidos
        espacos = df.select_dtypes(include="object").stack().str.contains(r"^\s+|\s+$").sum()
        df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
        logging.info(f"🔍 {espacos} valores com espacos removidos.")

        # brewery_type ausente
        antes = len(df)
        df = df[df["brewery_type"].notna()]
        logging.info(f"🧹 {antes - len(df)} linhas com 'brewery_type' ausente removidas.")

        # Duplicados por ID
        antes = len(df)
        df = df.drop_duplicates(subset=["id"])
        logging.info(f"🧹 {antes - len(df)} duplicatas removidas com base no 'id'.")

        # Preenchimento de website_url
        if "website_url" in df.columns:
            nulos = df["website_url"].isna().sum()
            df["website_url"] = df["website_url"].fillna("N/A")
            logging.info(f"🔧 {nulos} 'website_url' preenchidos com 'N/A'.")

        # Normalização do name
        antes = df["name"].copy()
        df["name"] = df["name"].str.replace(r"\s+", " ", regex=True).str.strip().str.replace('"', '')
        logging.info(f"✏️ {(antes != df['name']).sum()} nomes ajustados.")

        # Normalização de texto
        for col in ["state", "city", "country"]:
            if col in df.columns:
                df[col] = df[col].astype(str).str.lower().str.strip().apply(unidecode)

        # Localizações válidas
        if "latitude" in df.columns and "longitude" in df.columns:
            antes = len(df)
            df = df[df["latitude"].between(-90, 90) & df["longitude"].between(-180, 180)]
            logging.info(f"📍 {antes - len(df)} linhas com coordenadas invalidas removidas.")

        os.makedirs(SILVER_PATH, exist_ok=True)
        for state, df_state in df.groupby("state"):
            nome = unidecode(state).lower().replace(" ", "_")
            df_state.to_parquet(os.path.join(SILVER_PATH, f"{nome}.parquet"), index=False)

        logging.info(f"✅ Dados salvos em {SILVER_PATH} por estado.")
    except Exception as e:
        logging.error(f"❌ Erro: {e}")

# ====================================
# 3️ Etapa de Agregação
# ====================================
def agregar_dados():
    # Lê os arquivos parquet da camada silver, agrega por tipo e estado e salva o resultado final.
    try:
        dfs = []
        for file in os.listdir(SILVER_PATH):
            if file.endswith(".parquet"):
                df = pd.read_parquet(os.path.join(SILVER_PATH, file))
                dfs.append(df)

        if dfs:
            df_all = pd.concat(dfs)
            df_agg = df_all.groupby(["brewery_type", "state"]).size().reset_index(name="brewery_count")

            os.makedirs(os.path.dirname(GOLD_PATH), exist_ok=True)
            df_agg.to_parquet(GOLD_PATH, index=False)

            logging.info(f"✅ Dados agregados salvos em {GOLD_PATH}")
        else:
            logging.warning("⚠️ Nenhum dado encontrado na silver para agregar.")
    except Exception as e:
        logging.error(f"❌ Erro na agregação dos dados: {e}")

# ====================================
# 4️ Consulta Específica (opcional)
# ====================================
def obter_cervejaria_por_id(brewery_id: str):
    # [Utilizada somente para testes] Consulta e imprime dados de uma cervejaria específica a partir da API usando seu ID.
    try:
        url = f"https://api.openbrewerydb.org/v1/breweries/{brewery_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            logging.info("✅ Cervejaria encontrada:")
            for key, value in data.items():
                print(f"{key}: {value}")
        else:
            logging.warning(f"❌ Cervejaria nao encontrada. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"❌ Erro na consulta da cervejaria: {e}")

# ====================================
# 5 Execução do Pipeline
# ====================================
if __name__ == "__main__":
    logging.info("Iniciando processo...")
    extrair_dados_breweries()       # 1. Extração da API
    converter_json_para_csv()       # 1.1 Conversão JSON -> CSV
    transformar_dados()             # 2. Limpeza e transformação
    agregar_dados()                 # 3. Agregação final
    # obter_cervejaria_por_id("dfa3f8fc-21cf-443d-ba8d-8adfc6873852")  # 4. Consulta específica (opcional)
    logging.info("✅ Pipeline executado com sucesso.")
