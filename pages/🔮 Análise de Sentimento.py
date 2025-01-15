import streamlit as st
import pandas as pd
from LeIA import SentimentIntensityAnalyzer
import string
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Certifique-se de baixar os dados do NLTK, caso ainda não tenha feito
nltk.download('stopwords')

# Inicializa o analisador de sentimentos
analyzer = SentimentIntensityAnalyzer()

# Configurações iniciais do Streamlit
st.set_page_config(
    page_title="Predição de Satisfação do Cliente",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Define palavras de parada em português
STOP_WORDS = set(stopwords.words('portuguese'))

# Função para limpar e processar o texto


def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    # words = text.split()
    # filtered_words = [word for word in words if word not in STOP_WORDS]
    # return " ".join(filtered_words)
    return text

# Função para classificar o sentimento


def classify_sentiment(text):
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return 'Positivo'
    elif scores['compound'] <= -0.05:
        return 'Negativo'
    else:
        return 'Neutro'

# Função para gerar nuvem de palavras


def generate_wordcloud(text):
    wordcloud = WordCloud(width=400, height=400,
                          background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)


# Título principal
st.title("🔮 Predição da Satisfação do Cliente")

# Introdução
st.markdown("#### ℹ️ Sobre a Aplicação")
st.write(
    """
    Com o aumento das interações digitais, entender como os clientes percebem seus produtos ou serviços é essencial. Esta aplicação combina Processamento de Linguagem Natural (NLP) e Machine Learning para analisar avaliações e determinar o sentimento predominante nelas.
    """
)
st.info(
    """
    **Objetivos da aplicação**:
    - Identificar emoções expressas nas avaliações.
    - Auxiliar empresas na tomada de decisões estratégicas.
    - Entender os principais fatores que levam à satisfação ou insatisfação.
    """
)

# Orientações
st.markdown("#### 📖 Como Usar")
st.info(
    """
    **Para uma única avaliação:**
    - Insira ou cole uma avaliação no campo de texto abaixo.
    - Clique em **Prever Satisfação**.
    - Veja o resultado da análise, indicando o sentimento como Positivo, Negativo ou Neutro.
    
    **Para um arquivo CSV com várias avaliações:**
    - Certifique-se de que o arquivo contém uma coluna chamada **review**, onde cada linha representa uma avaliação.
    - Faça o upload do arquivo na seção Análise de Arquivo CSV.
    - A aplicação irá processar todas as avaliações, mostrando:
        - O sentimento de cada avaliação.
        - Um gráfico com a contagem de sentimentos positivos, negativos e neutros.
        - Nuvens de palavras para os sentimentos positivos e negativos.
    """
)

# Seção para análise individual
st.markdown("#### ✏️ Avaliação Individual")
with st.form(key='review_form'):
    review_text = st.text_area(
        label="Digite aqui a avaliação do cliente:",
        height=150,
    )
    submit_button = st.form_submit_button("Prever Satisfação")

    if submit_button:
        if review_text.strip():
            cleaned_text = clean_text(review_text)
            sentiment = classify_sentiment(cleaned_text)
            st.subheader("📊 Resultado da Análise de Sentimento")
            if sentiment == "Positivo":
                st.success(f"Satisfação Predita: {sentiment} 😊")
            elif sentiment == "Negativo":
                st.error(f"Satisfação Predita: {sentiment} 😔")
            else:
                st.warning(f"Satisfação Predita: {sentiment} 😐")
        else:
            st.warning(
                "⚠️ Por favor, digite uma avaliação antes de clicar no botão.")

# Seção para upload de arquivos CSV
st.markdown("#### 📂 Análise de Arquivo CSV")
uploaded_file = st.file_uploader(
    "Envie um arquivo CSV com uma coluna de avaliações", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    if 'review' in data.columns:
        data['cleaned_review'] = data['review'].apply(clean_text)
        data['sentiment'] = data['cleaned_review'].apply(classify_sentiment)
        st.write("📊 Resultados da Análise:")
        st.write(data[['review', 'sentiment']])

        # Contagem de sentimentos
        sentiment_counts = data['sentiment'].value_counts()
        st.bar_chart(sentiment_counts)

        # Nuvem de palavras para sentimentos positivos
        st.markdown("#### ☁️ Nuvem de Palavras - Sentimentos Positivos")
        positive_text = " ".join(
            data[data['sentiment'] == 'Positivo']['cleaned_review'])
        generate_wordcloud(positive_text)

        # Nuvem de palavras para sentimentos negativos
        st.markdown("#### ☁️ Nuvem de Palavras - Sentimentos Negativos")
        negative_text = " ".join(
            data[data['sentiment'] == 'Negativo']['cleaned_review'])
        generate_wordcloud(negative_text)
    else:
        st.warning("⚠️ O arquivo deve conter uma coluna chamada 'review'.")
