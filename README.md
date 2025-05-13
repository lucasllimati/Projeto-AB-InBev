# 🎯 Objetivo

Consumir dados de uma API, transformos dados e utilizando o data lake com a [arquitetura medallion](https://learn.microsoft.com/pt-br/azure/databricks/lakehouse/medallion).

---

## 📋 Instruções do Desafio

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

## Como executar a aplicação

### Software necessários

Para executar a aplição você irá precisar do [Docker Desktop](https://www.docker.com/), caso não tenha, favor instalar (Versão utilizada: 4.41.2).

Também é necessário uma IDE, no caso, sugiro o [VS Code](https://code.visualstudio.com/), que foi testado nesse desenvolvimento, mas as demais IDEs também devem funcionar, caso não tenha, favor instalar.

### Baixar repositório Git

Para baixar também é necessário ter o [Git](https://git-scm.com/downloads) instalado para conseguir baixar diretamente.

1. Abra o terminal CMD/Git
    - Também é possivel baixar diretamente no diretório, clique no botão "<> Code", depois Download ZIP. Extraia o arquivo para a pasta desejada e depois continue a partir do tópico 5.
  
2. Selecione o repositorio desejado.

    ```bash
    cd ~/Documentos
    ```

3. Clone o repositórioo com o comando:

    ```bash
    git clone https://github.com/lucasllimati/Projeto-AB-InBev.git
    ```

4. Entre na pasta

    ```bash
    cd Projeto-AB-InBev
    ```

5. Abra o VS Code como comando. Ou mesmo, abra o VS Code manualmente, vá em arquivo, abrir pasta e selecione a pasta onde baixou o arquivo.

    ```bash
      code .
    ```

6. Abra o terminal e execute o código (criação do container)

    ```bash
      docker-compose up -d
    ```

7. Quando terminar de instalar, abra o navegado e acesse o link [http://localhost:8080/](http://localhost:8080/)
    User: airflow
    Password: airflow

8. Quando abrir o Airflow, procure a DAG *brewery_pipeline* e do lado esquerdo, abaixo de actions clique em play.

9. Para acompanhar a execução, clice na *brewery_pipeline* edepois em Graph.

10. Quando todas as caixinhas ficarem verde escuro o processo foi executado com sucesso.

11. Para verificar os arquivos, abra a pasta data_lake e lá estará os arquivos atualizados do processo de extração da Open Brewery DB API.

12. Para finalizar, para a execução do container com o código abaixo

    ```bash
      docker-compose down
    ```

## Lógica do desenvolvimento

### Melhorias

## ✅ Checklist do Projeto

Checklist de acompanhamento:

### 🔄 API

- [x] Conectar à API Open Brewery DB  
- [x] Coletar e armazenar os dados brutos

### ⚙️ Orquestração

- [x] Escolher ferramenta (Airflow, Luigi, Mage, etc.)  
- [x] Implementar agendamento  
- [x] Implementar tentativas e tratamento de erros

### 🐍 Linguagem

- [x] Escolher linguagem (preferência: Python/PySpark)  
- [ ] Criar testes para o código

### 🐳 Containerização (opcional, mas recomendada)

- [x] Criar Dockerfile  
- [x] Executar aplicação em container

### 🏗️ Arquitetura Medallion

- [x] Bronze Layer: salvar dados brutos da API  
- [x] Silver Layer: transformar para parquet/delta  
- [x] Silver Layer: particionar por localização  
- [x] Gold Layer: criar agregação por tipo e localização

### 📡 Monitoramento e Alertas

- [ ] Definir abordagem para monitoramento de falhas e qualidade de dados

### 📁 Repositório GitHub

- [x] Subir projeto para repositório público  
- [x] Documentar decisões técnicas  
- [x] Incluir instruções de execução (README)

### ☁️ Serviços em Nuvem (se aplicável)

- [ ] Incluir instruções de configuração fora do repositório

### ⏱️ Prazos

- [x] Entregar em até 1 semana  
- [x] Compartilhar link do repositório GitHub com o time BEES
