import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly as plt
import plotly.express as px
from IPython.display import Image
from scipy.stats import skew
import plotly.figure_factory as ff
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Home', page_icon='🎲')

# Título
st.markdown('# Análise de Satisfação do Cliente para E-commerce')

# Texto
st.markdown("""
    
    Este estudo teve como objetivo prever a satisfação dos clientes da Olist, uma das maiores plataformas de e-commerce do Brasil, utilizando aprendizado de máquina. A satisfação do cliente é um diferencial competitivo crucial no e-commerce, sendo influenciada por fatores como qualidade do produto, logística e atendimento. Poucas pesquisas combinaram aprendizado de máquina e análise de linguagem natural (NLP) para prever a satisfação em plataformas de grande escala como a Olist, o que justifica a realização deste estudo.
    
    ### Sobre a Olist
    
    A Olist é uma das maiores plataformas de e-commerce do Brasil, conectando pequenos e médios vendedores a milhões de consumidores em todo o país. Fundada em 2015, a Olist se destaca por facilitar o processo de venda online, permitindo que lojistas de diferentes setores tenham acesso a grandes marketplaces como Mercado Livre, B2W e Amazon, além de oferecer uma plataforma própria para a gestão de vendas.

    ### Resumo dos Dados 
    O dataset consiste em informações sobre 100k pedidos realizados entre 2016 e 2018 no Olist, abrangendo diversos marketplaces no Brasil. Ele inclui informações variadas sobre os pedidos, o que permite analisá-los sob diferentes perspectivas: status do pedido, preço, desempenho do pagamento e do frete, localização dos clientes, atributos dos produtos e até mesmo as avaliações dos clientes sobre suas compras.

    A seguir, detalho os principais datasets que compõem o conjunto de dados.

    - **olist_customers_dataset (clientes):** contém dados dos clientes, como *customer_id*, *customer_unique_id* e localização, ajudando a associar pedidos aos clientes e a entender seu comportamento de compra.
    - **olist_geolocation_dataset (geolocalização):** apresenta informações sobre códigos postais do Brasil e suas coordenadas geográficas, útil para mapear a localização de clientes e vendedores e calcular distâncias entre eles.
    - **olist_order_items_dataset (itens do pedido):** inclui informações detalhadas sobre os itens comprados em cada pedido, como o ID do produto, quantidade e preço. 
    - **olist_order_payments_dataset (pagamentos):** contém detalhes sobre as formas de pagamento usadas pelos clientes, como o tipo de pagamento, o valor pago e o número de parcelas.
    - **olist_order_reviews_dataset (avaliações):** dados sobre as avaliações dos clientes após o recebimento dos produtos, incluindo notas e comentários. 
    - **olist_orders_dataset (pedidos):** o dataset principal, contendo informações sobre cada pedido, como status do pedido, preço total, data do pedido, entre outros. Relaciona-se com os outros datasets para fornecer um quadro completo de cada transação.
    - **olist_products_dataset (produtos):** contém informações sobre os produtos vendidos no Olist, incluindo o product_id, nome, descrição e preço. 
    - **olist_sellers_dataset (vendedores):** inclui dados sobre os vendedores que enviaram os produtos para os clientes, como *seller_id*, localização e outros atributos.
    
    ### Data Schema 
    
    O Data Schema do dataset organiza os dados de forma estruturada, permitindo uma análise fácil e intuitiva. Ele detalha as relações entre os diferentes conjuntos de dados, como a correspondência entre pedidos e itens do pedido, entre clientes e suas avaliações, entre vendedores e os produtos que venderam, etc. O schema fornece uma visão clara das tabelas, campos e como elas se conectam, facilitando a realização de consultas complexas e análises de dados.""")

st.image('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/assets/dataschema.png', caption='Data Schema')

st.markdown("""---""")

st.markdown("""
    
    ### Navegação no Streamlit
    
    A aplicação foi dividida em três páginas principais para facilitar a navegação e a interação com os dados e modelos. Abaixo está a descrição de cada uma das páginas e suas funcionalidades:
    
    #### Home 
    Na página Home, os usuários terão uma visão geral do projeto e das funcionalidades disponíveis. Aqui, será apresentada uma explicação sobre os objetivos do trabalho e a metodologia adotada. Além disso, o usuário poderá entender o processo de análise de dados, desde a exploração até a construção do modelo preditivo.     
    
    #### Análise Exploratória de Dados  
    A página EDA (Análise Exploratória de Dados) será o espaço para explorar os insights obtidos dos datasets. Aqui, você encontrará todas as perguntas respondidas com os dados, junto com os gráficos e resultados que ilustram as conclusões da análise.     
    
    #### Predição da Satisfação
    A página de Predição da Satisfação permitirá que os usuários insiram dados sobre um pedido (como informações de compra e entrega) para prever a satisfação do cliente com base nos modelos de Machine Learning construídos. O usuário poderá inserir informações como o tipo de pagamento, preço, tempo de entrega e outros dados relevantes, e o modelo fará uma previsão sobre a satisfação do cliente, classificando-a como "Positiva", "Negativa" ou "Neutra". Isso ajudará a demonstrar como o modelo pode ser aplicado para prever a experiência do cliente com base nos dados históricos.    
    
    """)

st.markdown("""---""")
