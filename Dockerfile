# # Usando uma imagem base Python
# FROM python:3.10-slim

# # Definir o diretório de trabalho
# WORKDIR /app

# # Copiar o arquivo requirements
# COPY requirements.txt .

# # Instalar dependências
# RUN pip install --no-cache-dir -r requirements.txt

# # Copiar os arquivos necessários
# COPY . .

# # Definir a entrada do container
# CMD ["python", "main.py"]

# # Expor a porta 8080
# EXPOSE 8080

FROM apache/airflow:2.9.1-python3.10

USER root

# # Instala o Java 17
# RUN apt-get update && \
#     apt-get install -y openjdk-17-jdk-headless && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# ENV SPARK_HOME=/opt/spark
# ENV PATH=$PATH:$SPARK_HOME/bin

RUN pip install --upgrade pip
RUN pip install requests pandas pyarrow

# Copia os requisitos antes de mudar para o usuário airflow
# COPY requirements.txt /requirements.txt
COPY requirements.txt .

# Volta para o usuário airflow antes de rodar o pip
USER airflow

# # Agora sim, instale as dependências como usuário correto
RUN pip install --no-cache-dir -r /requirements.txt

# Copia os arquivos
COPY dags /opt/airflow/dags
COPY main.py /opt/airflow/main.py

