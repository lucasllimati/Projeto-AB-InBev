# Anotações

bees-breweries-case/
│
├── dags/                      # (para o Airflow)
│   └── pipeline.py
├── docker/
│   ├── Dockerfile
│   └── requirements.txt
├── logs/
├── src/
│   └── main.py                # seu script principal
├── tests/
│   └── test_pipeline.py       # testes unitários
├── data_lake/                 # persistência local
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── .env                       # variáveis sensíveis (email, senhas)
├── docker-compose.yml
└── README.md
