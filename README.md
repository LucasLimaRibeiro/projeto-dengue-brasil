# 🦟 Dashboard de Dengue no Brasil

## Projeto de Análise e Visualização de Dados com Python

Projeto acadêmico desenvolvido para análise dos casos de dengue no Brasil entre 2015 e 2024.

O projeto utiliza técnicas de análise exploratória, tratamento de dados, indicadores, visualização e dashboard interativo para identificar padrões temporais e regionais relacionados à ocorrência da dengue.

---

## 🎯 Objetivo

Analisar como os casos de dengue evoluíram no Brasil entre 2015 e 2024, identificando regiões, estados e períodos com maior concentração de casos e incidência.

Também são analisadas possíveis relações entre os casos de dengue e variáveis climáticas, como chuva e temperatura.

---

## 📊 Dados analisados

A base utilizada contém informações relacionadas a:

- Ano
- Mês
- Data
- Região
- Estado (UF)
- Município
- População
- Chuva em milímetros
- Temperatura média
- Casos de dengue
- Internações
- Óbitos
- Incidência por 100 mil habitantes
- Nível de alerta

---

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- GitHub

---

## 🔎 Análises realizadas

O projeto apresenta:

- Tratamento e preparação dos dados
- Análise exploratória
- Análise temporal
- Análise regional
- Análise por estado
- Indicadores de casos, internações e óbitos
- Análise de incidência
- Análise de níveis de alerta
- Análise de correlação
- Série temporal com média móvel
- Dashboard interativo

---

## 🚀 Recursos avançados

O projeto utiliza recursos avançados de análise de dados, incluindo:

### Análise de série temporal

Foi realizada uma análise mensal dos casos de dengue, incluindo média móvel de três meses e variação percentual.

### Análise de correlação

Foi analisada a relação entre variáveis como:

- Chuva e casos de dengue
- Temperatura e casos de dengue
- Casos de dengue e internações
- Casos de dengue e óbitos

É importante destacar que correlação estatística não significa causalidade.

---

## 📈 Dashboard

O dashboard foi desenvolvido utilizando Streamlit e permite realizar análises interativas por meio de filtros de:

- Ano
- Região
- Estado
- Nível de alerta

Também apresenta KPIs, gráficos, tabelas e interpretações dos resultados.

---

## 📁 Estrutura do projeto

```text
projeto-dengue-brasil/
│
├── app.py
├── requirements.txt
├── README.md
├── index.html
│
├── dados/
│   └── simulacao_dengue_brasil.csv
│
├── database/
│
├── notebooks/
│   └── analise_dengue.ipynb
│
└── imagens/