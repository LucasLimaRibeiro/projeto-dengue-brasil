# ============================================================
# PROJETO ACADÊMICO
# Disciplina: Linguagem de Programação — Análise e Visualização de Dados com Python
# Professor: Alexandre Neves Louzada
# Aluno: Lucas Lima Ribeiro
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Dashboard de Dengue no Brasil",
    page_icon="🦟",
    layout="wide"
)
st.markdown(
    "**Aluno:** Lucas Lima Ribeiro \n"
    "**Professor:** Alexandre Louzada \n"
    "**Materia:** Linguagens de programação \n"
)
st.divider()

# ============================================================
# CARREGAMENTO DOS DADOS
# ============================================================

@st.cache_data
def carregar_dados():
    return pd.read_csv("dados/simulacao_dengue_brasil.csv")


df = carregar_dados()


# ============================================================
# TÍTULO DO PROJETO
# ============================================================

st.title("🦟 Dashboard de Dengue no Brasil")

st.markdown(
    """
    ### Análise epidemiológica da dengue entre 2015 e 2024

    Este dashboard apresenta uma análise dos casos de dengue no Brasil,
    permitindo observar a evolução temporal da doença, sua distribuição
    regional e os principais indicadores relacionados aos casos.
    """
)


# ============================================================
# SIDEBAR — FILTROS
# ============================================================

st.sidebar.header("🔎 Filtros")

# Filtro de ano
anos = sorted(df["ano"].unique())

ano_selecionado = st.sidebar.selectbox(
    "Ano",
    ["Todos"] + anos
)

# Filtro de região
regioes = sorted(df["regiao"].unique())

regiao_selecionada = st.sidebar.selectbox(
    "Região",
    ["Todas"] + regioes
)

# Filtro de estado
ufs = sorted(df["uf"].unique())

uf_selecionada = st.sidebar.selectbox(
    "Estado (UF)",
    ["Todos"] + ufs
)

# Filtro de nível de alerta
alertas = sorted(df["nivel_alerta"].unique())

alerta_selecionado = st.sidebar.selectbox(
    "Nível de alerta",
    ["Todos"] + alertas
)


# ============================================================
# APLICAÇÃO DOS FILTROS
# ============================================================

df_filtrado = df.copy()

if ano_selecionado != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["ano"] == ano_selecionado
    ]

if regiao_selecionada != "Todas":
    df_filtrado = df_filtrado[
        df_filtrado["regiao"] == regiao_selecionada
    ]

if uf_selecionada != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["uf"] == uf_selecionada
    ]

if alerta_selecionado != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["nivel_alerta"] == alerta_selecionado
    ]


# ============================================================
# VERIFICAÇÃO DOS DADOS
# ============================================================

if df_filtrado.empty:

    st.warning(
        "Nenhum registro encontrado para os filtros selecionados."
    )

    st.stop()


# ============================================================
# KPIs
# ============================================================

total_casos = df_filtrado["casos_dengue"].sum()

total_internacoes = df_filtrado["internacoes"].sum()

total_obitos = df_filtrado["obitos"].sum()

media_incidencia = df_filtrado["incidencia_100k"].mean()


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🦟 Casos de dengue",
        f"{total_casos:,.0f}".replace(",", ".")
    )


with col2:

    st.metric(
        "🏥 Internações",
        f"{total_internacoes:,.0f}".replace(",", ".")
    )


with col3:

    st.metric(
        "⚠️ Óbitos",
        f"{total_obitos:,.0f}".replace(",", ".")
    )


with col4:

    st.metric(
        "📈 Incidência média",
        f"{media_incidencia:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )


# ============================================================
# EVOLUÇÃO TEMPORAL
# ============================================================

st.subheader("📈 Evolução dos casos de dengue")

casos_por_ano = (
    df_filtrado
    .groupby("ano")["casos_dengue"]
    .sum()
    .reset_index()
)


fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    casos_por_ano["ano"],
    casos_por_ano["casos_dengue"],
    marker="o"
)

ax.set_title("Evolução dos casos de dengue por ano")

ax.set_xlabel("Ano")

ax.set_ylabel("Número de casos")

ax.grid(True, alpha=0.3)

plt.tight_layout()

st.pyplot(fig)


# ============================================================
# CASOS POR REGIÃO
# ============================================================

st.subheader("🗺️ Casos de dengue por região")

casos_regiao = (
    df_filtrado
    .groupby("regiao")["casos_dengue"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(casos_regiao)


# ============================================================
# RANKING POR ESTADO
# ============================================================

st.subheader("🏆 Ranking de casos por estado")

casos_uf = (
    df_filtrado
    .groupby("uf")["casos_dengue"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(casos_uf)


# ============================================================
# INCIDÊNCIA POR REGIÃO
# ============================================================

st.subheader("📊 Incidência média por região")

incidencia_regiao = (
    df_filtrado
    .groupby("regiao")["incidencia_100k"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(incidencia_regiao)


# ============================================================
# CASOS X INTERNAÇÕES
# ============================================================

st.subheader("🏥 Casos de dengue e internações")

comparacao = (
    df_filtrado
    .groupby("ano")[["casos_dengue", "internacoes"]]
    .sum()
)

st.line_chart(comparacao)


# ============================================================
# NÍVEIS DE ALERTA
# ============================================================

st.subheader("🚨 Distribuição dos níveis de alerta")

distribuicao_alerta = (
    df_filtrado["nivel_alerta"]
    .value_counts()
)

st.bar_chart(distribuicao_alerta)


# ============================================================
# PRINCIPAIS INSIGHTS
# ============================================================

st.subheader("💡 Principais insights")

regiao_maior = (
    df_filtrado
    .groupby("regiao")["casos_dengue"]
    .sum()
    .idxmax()
)

uf_maior = (
    df_filtrado
    .groupby("uf")["casos_dengue"]
    .sum()
    .idxmax()
)

ano_maior = (
    df_filtrado
    .groupby("ano")["casos_dengue"]
    .sum()
    .idxmax()
)

st.write(
    f"• A região com maior quantidade de casos no período filtrado foi **{regiao_maior}**."
)

st.write(
    f"• O estado com maior quantidade de casos foi **{uf_maior}**."
)

st.write(
    f"• O ano com maior quantidade de casos foi **{ano_maior}**."
)

st.write(
    f"• A incidência média observada foi de "
    f"**{media_incidencia:.2f} casos por 100 mil habitantes**."
)


# ============================================================
# TABELA DE DADOS
# ============================================================

st.subheader("📋 Dados utilizados na análise")

st.dataframe(
    df_filtrado,
    use_container_width=True
)


# ============================================================
# CONCLUSÃO EXECUTIVA
# ============================================================

st.subheader("🎯 Conclusão executiva")

st.markdown(
    """
    A análise dos dados permite observar que a dengue apresenta
    comportamento variável ao longo dos anos e distribuição desigual
    entre as regiões e estados brasileiros.

    Os filtros disponíveis permitem analisar diferentes períodos,
    regiões, estados e níveis de alerta, facilitando a identificação
    de períodos e localidades com maior concentração de casos.

    Os indicadores e gráficos apresentados neste dashboard permitem
    transformar os dados epidemiológicos em informações mais claras
    para apoiar a interpretação dos padrões observados na base analisada.
    """
)
