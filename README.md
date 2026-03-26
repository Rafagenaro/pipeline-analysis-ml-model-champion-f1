# 🏎️ Previsão do Campeonato Mundial de F1 2025 com Data Science + MLOps

Projeto de Data Science e MLOps aplicado à Fórmula 1 com o objetivo de prever o campeão da temporada 2025 a partir de dados históricos de corrida, features de desempenho e modelagem preditiva.

O modelo indicou **Lando Norris** como campeão da temporada.

---

## 📌 Objetivo

Este projeto foi desenvolvido para unir minha paixão pela **Fórmula 1** com meus estudos em **Ciência de Dados** e **Engenharia/MLOps**.

A proposta foi construir uma pipeline de dados em camadas, tratar informações da API **OpenF1**, criar variáveis relevantes de desempenho e treinar um modelo de machine learning capaz de estimar a posição final dos pilotos na última corrida da temporada — e, a partir disso, prever o campeão mundial.

---

## 🚀 Tecnologias utilizadas

- **Python**
- **Pandas**
- **XGBoost**
- **Scikit-learn**
- **Terraform**
- **Azure Storage Account**
- **OpenF1 API**

---

## 🏗️ Arquitetura do projeto

A infraestrutura foi provisionada com **Terraform** na **Azure**, seguindo uma abordagem em camadas para organização e maturidade dos dados:

- **raw** → dados brutos extraídos da API OpenF1  
- **silver** → dados tratados, limpos e padronizados  
- **gold** → dataset final com features prontas para modelagem  

Essa separação facilita manutenção, rastreabilidade e escalabilidade do pipeline.

---

## 📊 Fonte de dados

Os dados foram obtidos a partir da **OpenF1 API**, contendo informações relacionadas a corridas, posições, pilotos e desempenho ao longo da temporada.

---

## 🧠 Feature Engineering

Para melhorar a capacidade preditiva do modelo, foram criadas algumas variáveis derivadas importantes:

- **driver_avg_position** → média de posição do piloto
- **team_avg_position** → média de posição da equipe
- **driver_track_avg** → média de desempenho do piloto em determinado circuito
- **driver_form_last3** → desempenho recente considerando as últimas 3 corridas

Essas features ajudaram o modelo a capturar tanto o histórico geral quanto o momento recente de cada piloto.

---

## 🤖 Modelagem

Foi utilizado um modelo de **regressão com XGBoost** para prever a posição final dos pilotos.

### Métricas obtidas
- **MAE:** 0,50
- **R²:** 0,76

Os resultados mostraram uma performance consistente para o objetivo proposto.

---

## 🏁 Resultado da previsão

Após o ranqueamento final gerado pelo modelo, o projeto apontou:

# **Lando Norris como campeão mundial de F1 2025**

Mesmo com bom desempenho do modelo, houve um **empate técnico entre os três pilotos analisados**, já que o dataset continha apenas competidores muito próximos em performance.

Na prática, a diferença final foi influenciada pelo histórico acumulado de Norris ao longo da temporada.

---

## ⚠️ Limitações do projeto

Um dos principais pontos observados foi a **baixa variância da amostra**.

Como o modelo foi treinado apenas com dados dos **três pilotos que disputavam o título**, as variáveis mais importantes, como:

- `points`
- `driver_avg_position`

acabaram ficando muito semelhantes entre si, dificultando a diferenciação real entre **P1, P2 e P3**.

Isso fez com que o modelo gerasse scores contínuos muito próximos.

### Principal aprendizado
Para melhorar o poder de discriminação do modelo, o ideal seria incluir **todos os pilotos do grid** no dataset, aumentando a variabilidade dos dados e permitindo identificar diferenças mais sutis de desempenho.

---

## 📚 Principais aprendizados

Este projeto trouxe aprendizados importantes em diferentes frentes:

- **Data Science:** criação de features, modelagem preditiva e interpretação de métricas
- **Engenharia de Dados:** organização do pipeline em camadas
- **MLOps/Cloud:** provisionamento de infraestrutura com Terraform na Azure
- **Análise crítica:** entendimento de como baixa variância impacta diretamente a capacidade do modelo em diferenciar observações muito parecidas

Além disso, foi uma ótima oportunidade de aplicar teoria em um contexto que me motiva de verdade: **Fórmula 1**.

---

## 📂 Estrutura sugerida do projeto

```bash
.
├── data/
│   ├── raw/
│   ├── silver/
│   └── gold/
├── notebooks/
│   ├── 01_extracao.ipynb
│   ├── 02_tratamento.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_modelagem.ipynb
├── src/
│   ├── ingestion/
│   ├── processing/
│   ├── features/
│   └── modeling/
├── terraform/
│   └── main.tf
├── requirements.txt
└── README.md
