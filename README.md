# 🍺 BEES Data Engineering – Breweries Case

## ✅ Tradução

Tradução da documentação recebida com os requisitos.

### 🎯 Objetivo

Avaliar suas habilidades em consumir dados de uma API, transformá-los e persistí-los em um data lake utilizando a arquitetura *medallion* (com três camadas: raw, curated e analytical).

---

### 📋 Instruções

- **API:** Use a Open Brewery DB API para buscar os dados de cervejarias.  
  👉 [https://www.openbrewerydb.org/](https://www.openbrewerydb.org/)

- **Orquestração:** Utilize uma ferramenta de orquestração de sua preferência (Airflow, Luigi, Mage etc.) para construir o pipeline de dados, incluindo agendamento, tentativas e tratamento de erros.

- **Linguagem:** Use a linguagem de sua escolha para consumir e transformar os dados. Inclua testes no seu código.  
  *Python e PySpark são preferidas.*

- **Containerização:** O uso de Docker ou Kubernetes conta pontos extras.

- **Arquitetura do Data Lake (Medallion):**
  - **Camada Bronze:** Armazene os dados brutos da API no formato nativo (JSON, CSV, etc.)
  - **Camada Prata:** Transforme os dados para um formato colunar (parquet ou delta) e particione por localização da cervejaria.
  - **Camada Ouro:** Crie uma visão agregada com a quantidade de cervejarias por tipo e localização.

- **Monitoramento e Alertas:** Descreva como você implementaria o monitoramento e alertas (falhas no pipeline, problemas de qualidade de dados etc.)

- **Repositório:** Crie um repositório público no GitHub com sua solução, explicando decisões de projeto e instruções para execução.

- **Serviços de Nuvem:** Caso utilize serviços em nuvem, forneça instruções de configuração separadamente (não poste no repositório público).

---

## 📊 Tabela Explicativa por Tópico

| Tópico                    | Descrição                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| **API**                  | Open Brewery DB - fornece informações sobre cervejarias nos EUA.         |
| **Orquestração**         | Airflow, Luigi, Mage, etc. (mostrar agendamento, tentativas e erros)     |
| **Linguagem**            | Qualquer linguagem (preferência: Python + PySpark) com testes incluídos  |
| **Containerização**      | Uso de Docker ou Kubernetes é opcional, mas agrega pontos                |
| **Bronze Layer**         | Dados crus da API, sem transformação (JSON, CSV, etc.)                   |
| **Silver Layer**         | Dados transformados em parquet/delta, particionados por localização      |
| **Gold Layer**           | Dados agregados: número de cervejarias por tipo e localização            |
| **Monitoramento/Alertas**| Estratégia para capturar falhas e problemas de qualidade no pipeline     |
| **Repositório GitHub**   | Código + documentação clara e instruções para executar                   |
| **Serviços em Nuvem**    | Instruções de configuração separadas (caso usados)                       |

---

## ✅ Checklist do Projeto

Checklist de acompanhamento:

### 🔄 API

- [x] Conectar à API Open Brewery DB  
- [x] Coletar e armazenar os dados brutos

### ⚙️ Orquestração

- [ ] Escolher ferramenta (Airflow, Luigi, Mage, etc.)  
- [ ] Implementar agendamento  
- [ ] Implementar tentativas e tratamento de erros

### 🐍 Linguagem

- [x] Escolher linguagem (preferência: Python/PySpark)  
- [ ] Criar testes para o código

### 🐳 Containerização (opcional, mas recomendada)

- [ ] Criar Dockerfile  
- [ ] Executar aplicação em container

### 🏗️ Arquitetura Medallion

- [x] Bronze Layer: salvar dados brutos da API  
- [ ] Silver Layer: transformar para parquet/delta  
- [ ] Silver Layer: particionar por localização  
- [ ] Gold Layer: criar agregação por tipo e localização

### 📡 Monitoramento e Alertas

- [ ] Definir abordagem para monitoramento de falhas e qualidade de dados

### 📁 Repositório GitHub

- [ ] Subir projeto para repositório público  
- [ ] Documentar decisões técnicas  
- [ ] Incluir instruções de execução (README)

### ☁️ Serviços em Nuvem (se aplicável)

- [ ] Incluir instruções de configuração fora do repositório

### ⏱️ Prazos

- [ ] Entregar em até 1 semana  
- [ ] Compartilhar link do repositório GitHub com o time BEES
