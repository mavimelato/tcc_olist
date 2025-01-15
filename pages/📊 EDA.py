import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

sns.set_theme(style="whitegrid")

# Carregar os dados diretamente da URL com ?raw=true
df = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/df_preprocessed.csv')
order_items = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/olist_order_items_dataset.csv')
orders = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/olist_orders_dataset.csv')
payments = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/olist_order_payments_dataset.csv')
products = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/olist_products_dataset.csv')
customers = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/olist_customers_dataset.csv')
sellers = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/olist_sellers_dataset.csv')
product_category = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/product_category_name_translation.csv')
geolocation = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/olist_geolocation_dataset.csv')
reviews = pd.read_csv('https://raw.githubusercontent.com/mavimelato/tcc_olist/master/data/olist_order_reviews_dataset.csv')

st.title('📊 Análise Exploratória de Dados')
st.markdown("""
            A Análise Exploratória de Dados (EDA) tem como objetivo examinar e entender os dados de forma profunda, com a finalidade de identificar padrões, tendências e anomalias. No contexto de uma plataforma de e-commerce, buscamos compreender como os pedidos, clientes e produtos se comportam ao longo do tempo e em diferentes regiões. A análise envolve a exploração de múltiplas dimensões, incluindo temporalidade, localização geográfica, e o comportamento de compra dos clientes. 

            Além disso, a EDA investigou variáveis cruciais que influenciam o sucesso de um e-commerce, como a relação entre preço e frete, o tempo de entrega e o feedback dos clientes, fornecendo uma visão holística sobre o desempenho da plataforma e as necessidades dos consumidores.            
            
            #### Navegação 
            
            Nesta página de Análise Exploratória de Dados (EDA), você pode explorar diferentes áreas de análise de forma simples e interativa. A navegação é feita por meio de um select box, localizado no topo da página, onde você pode escolher entre os seguintes tópicos de análise:
            
            - **Pedidos:** a análise dos pedidos busca identificar padrões de compra, sazonalidade e o comportamento dos consumidores ao longo do tempo.
            - **Preços:** aqui, analisamos a variação de preços dos produtos e como esses preços afetam a demanda.
            - **Avaliações:** a análise de avaliações dos clientes oferece insights sobre a satisfação e a qualidade dos produtos. Ela ajuda a identificar produtos bem avaliados e aqueles que necessitam de melhorias, influenciando as decisões de compra e a lealdade dos clientes.
            - **Métricas:** analisa métricas-chave como receita mensal, clientes ativos, pedidos mensais e clientes recorrentes. Esses indicadores ajudam a monitorar o desempenho financeiro e a fidelização de clientes, além de fornecer insights sobre a saúde do negócio e a eficácia das estratégias de marketing.
            """)

# Selecionar seção da EDA
section = st.selectbox('Escolha uma seção da EDA:', [
                       'Pedidos', 'Preços', 'Avaliações', 'Métricas'])

if section == 'Pedidos':
    # Pergunta em Markdown
    st.markdown(
        "### 1. Como o número de pedidos muda ao longo do tempo? Qual dia teve o maior número de pedidos?")

    # Manipulação de Dados - Criando um DataFrame agrupado
    df_aux = df[['day_month_year', 'order_id']].groupby(
        ['day_month_year']).count().reset_index()

    # Criando o gráfico interativo
    fig_11 = px.bar(df_aux, x='day_month_year', y='order_id')

    # Personalizando o gráfico usando Plotly
    fig_11.update_layout(
        title='Número de Pedidos por Dia',       # Título do gráfico
        xaxis_title='Dia',                        # Rótulo do eixo X
        yaxis_title='Número de Pedidos',          # Rótulo do eixo Y
        title_x=0.3,                               # Centraliza o título do gráfico
        # Ajuste das margens (esquerda, direita, superior, inferior)
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico interativo no Streamlit
    st.plotly_chart(fig_11)

    # Resposta em Markdown
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                    Para analisar o comportamento do número de pedidos ao longo do tempo, foi criada uma visualização que mostra a quantidade de pedidos por dia. A análise do número de pedidos ao longo do tempo, ilustrada no gráfico acima, revelou um pico em 24 de novembro de 2017, data da Black Friday. 
                    
                    Esse aumento reflete o impacto significativo de datas promocionais no comércio eletrônico, destacando sua relevância para o aumento de transações na plataforma.""")

    # Pergunta em Markdown
    st.markdown(
        "### 2. Qual é a distribuição do número de pedidos por tipo de pagamento e qual método é o mais utilizado?")

    # Manipulação de Dados - Criando um DataFrame agrupado
    df_aux = df[['payment_type', 'order_id']].groupby(
        ['payment_type']).count().reset_index()
    df_aux.sort_values('order_id', ascending=False, inplace=True)

    # Criando o gráfico interativo
    fig_13 = px.bar(df_aux, x='payment_type', y='order_id',
                    text_auto=True, color='payment_type')

    # Personalizando o gráfico
    fig_13.update_layout(
        title='Número de Pedidos por Tipo de Pagamento',  # Título do gráfico
        xaxis_title='Tipo de Pagamento',                  # Rótulo do eixo X
        yaxis_title='Número de Pedidos',                  # Rótulo do eixo Y
        title_x=0.5,                                     # Centraliza o título do gráfico
        # Inclina os rótulos do eixo X para melhor leitura
        xaxis_tickangle=-45,
        # Margens personalizadas
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_13)

    # Resposta em Markdown
    with st.expander("Detalhes da Análise"):
        st.markdown(""" O gráfico apresentado mostra a distribuição do número de pedidos por tipo de pagamento. A análise revelou que o cartão de crédito é o método de pagamento mais utilizado, seguido pelo boleto, que representa cerca de 25% do volume de pagamentos feitos com cartão de crédito. O vale e o cartão de débito ocupam, respectivamente, a terceira e quarta posições no ranking de pagamentos """)

    # Pergunta em Markdown
    st.markdown("### 3. Como o número de pedidos varia por região? Existe alguma região que tenha mais pedidos em um determinado período?")

    # Manipulação de Dados - Criando um DataFrame agrupado
    df_aux = df[['day_month_year', 'order_id', 'customer_region']].groupby(
        ['day_month_year', 'customer_region']).count().reset_index()

    # Selecionando dados de 2018
    df_aux = df_aux.loc[df_aux['day_month_year'] >= '2018-01-01']

    # Criando o gráfico interativo de linha
    fig_12 = px.line(df_aux, x='day_month_year', y='order_id',
                     color='customer_region', title='Número de Pedidos por Região')

    # Personalizando o gráfico usando Plotly
    fig_12.update_layout(
        xaxis_title='Dia',                         # Rótulo do eixo X
        yaxis_title='Número de Pedidos',           # Rótulo do eixo Y
        title_x=0.3,                               # Centraliza o título do gráfico
        # Ajuste das margens (esquerda, direita, superior, inferior)
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico interativo no Streamlit
    st.plotly_chart(fig_12, use_container_width=True)

    # Resposta em Markdown
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                    Foi gerada uma visualização para analisar a variação do número de pedidos por região ao longo do tempo, destacando a quantidade de pedidos por dia em diferentes regiões. 
                    
                    A análise dos dados de 2018 revelou que a região Sudeste se manteve como a líder em número de pedidos durante todo o ano, com uma proporção consistente em relação às demais regiões. Apesar da variação no volume total de pedidos ao longo do tempo, a proporção entre as regiões permaneceu praticamente inalterada.
                    
                    Esse comportamento sugere uma estabilidade nas preferências regionais, com a região Sudeste liderando, mas sem grandes flutuações ao longo do ano.""")

    # Pergunta 5: Como é a distribuição semanal dos pedidos não entregues?
    st.markdown(
        "### 4. Como é a distribuição semanal dos pedidos não entregues?")

    # Manipulação de Dados - Criando um DataFrame agrupado
    df_aux = df.loc[(df['day_month_year'] >= '2018-01-01') &
                    (df['order_status'] != 'delivered'), :]
    df_aux = df_aux[['weekofyear', 'order_id', 'order_status']].groupby(
        ['weekofyear', 'order_status']).count().reset_index()

    # Criando o gráfico interativo
    fig_14 = px.bar(df_aux, x='weekofyear', y='order_id', color='order_status',
                    title='Número de Pedidos Não Entregues por Semana (2018)',
                    labels={'weekofyear': 'Semana', 'order_id': 'Número de Pedidos'})

    fig_14.update_layout(
        title='Número de Pedidos Não Entregues por Semana (2018)',
        xaxis_title='Semana',
        yaxis_title='Número de Pedidos',
        title_x=0.3,
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico
    st.plotly_chart(fig_14)

    # Resultado observado no gráfico
    with st.expander("Detalhes da Análise"):
        st.markdown("""
    A análise da distribuição semanal dos pedidos não entregues em 2018 revela padrões interessantes. Observa-se um pico no número de pedidos cancelados entre as semanas 4 e 9, seguido por outro aumento em torno da 30ª semana. 
    
    Esses picos podem indicar sazonalidade ou fatores específicos que influenciam o comportamento dos pedidos ao longo do ano. 
    
    ### Recomendação 
    - Investigar se esses padrões se repetem em outros anos
    - Identificar causas subjacentes e propor estratégias para diminuir esses eventos.
    """)

    # Pergunta 6: Isso é um padrão anual?
    st.markdown("#### 4.1 Isso é um padrão anual?")

    # Manipulação de Dados - Criando um DataFrame agrupado para 2017
    df_aux = df.loc[(df['day_month_year'] >= '2017-01-01') & (df['day_month_year']
                                                              <= '2017-12-31') & (df['order_status'] != 'delivered'), :]
    df_aux = df_aux[['weekofyear', 'order_id', 'order_status']].groupby(
        ['weekofyear', 'order_status']).count().reset_index()

    # Criando o gráfico interativo
    fig_141 = px.bar(df_aux, x='weekofyear', y='order_id', color='order_status',
                     title='Número de Pedidos Não Entregues por Semana (2017)',
                     labels={'weekofyear': 'Semana', 'order_id': 'Número de Pedidos'})

    fig_141.update_layout(
        title='Número de Pedidos Não Entregues por Semana (2017)',
        xaxis_title='Semana',
        yaxis_title='Número de Pedidos',
        title_x=0.3,
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico
    st.plotly_chart(fig_141)

    # Resultado observado no gráfico
    with st.expander("Detalhes da Análise"):
        st.markdown("""
    A análise dos dados de 2017 não revela um padrão anual semelhante ao observado em 2018. Contudo, destaca-se que, assim como em 2018, o número de pedidos cancelados é maior entre as semanas 30 e 33.
    """)

    # Pergunta 7: Números de pedidos por categoria
    st.markdown(
        "### 5. Quais categorias de produtos têm o maior volume de vendas?")

    # Manipulação de Dados - Agrupando por categoria
    df_aux1 = df[['product_category_name', 'order_id']].groupby(
        ['product_category_name']).count().reset_index()
    df_aux1 = df_aux1.sort_values('order_id', ascending=False).head(20)

    # Criando o gráfico interativo
    fig_21 = px.bar(df_aux1, x='product_category_name',
                    y='order_id', text_auto=True)
    fig_21.update_layout(
        title='Número de Pedidos por Categoria',
        xaxis_title='Categoria',
        yaxis_title='Número de Pedidos',
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico
    st.plotly_chart(fig_21)

    # Resultado observado no gráfico
    with st.expander("Detalhes da Análise"):
        st.markdown("""
    A análise dos números de pedidos por categoria revela que as categorias com maior volume de vendas incluem cama, mesa e banho, beleza e saúde, esporte e lazer, móveis de decoração e informática e acessórios. Por outro lado, categorias como seguros e serviços e CDs e DVDs musicais apresentam um desempenho abaixo do esperado.
    
    ### Recomendação 
    - Reavaliar a estratégia em relação a esses produtos, uma vez que o mercado digital tem se distanciado dessas áreas.
    """)

    # Pergunta 5: Os clientes compram mais no começo do mês?
    st.markdown(
        "### 6. Os clientes tendem a fazer mais compras no início ou no final do mês?")

    # Manipulação de Dados
    df_aux = df[['order_id', 'day']].groupby(['day']).count().reset_index()
    df_aux.sort_values('order_id', ascending=False, inplace=True)

    # Criando o gráfico
    fig_17 = px.bar(df_aux, x='day', y='order_id', text_auto=True,
                    title='Número de Pedidos por Dia do Mês',
                    labels={'day': 'Dia', 'order_id': 'Número de Pedidos'},
                    color='order_id', color_continuous_scale='magma')

    # Personalizando o gráfico
    fig_17.update_layout(
        title_x=0.3,
        xaxis_title='Dia do Mês',
        yaxis_title='Número de Pedidos',
        xaxis=dict(tickmode='linear'),
        yaxis=dict(title='Número de Pedidos'),
        xaxis_tickangle=-45,
        margin=dict(l=20, r=20, t=50, b=50)
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_17)

    # Resultados do gráfico
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                O gráfico mostra que não há um padrão claro de compras mais frequentes no início do mês, mas é possível notar uma queda significativa no número de pedidos a partir do 28º dia.
                
                Esse comportamento pode indicar que os consumidores reduzem suas compras conforme o mês avança, talvez devido ao esgotamento do orçamento ou outras prioridades. 
                
                ### Recomendação 
                - Ajustar as estratégias de vendas, oferecendo promoções no final do mês, visando impulsionar as compras nesse período.
                """)

    # Pergunta 6: Número de Pedidos por Dia da Semana
    st.markdown("### 7. Qual dia da semana tem o maior número de pedidos?")

    # Manipulação dos dados
    df_aux1 = df[['order_id', 'name_dayofweek']].groupby(
        ['name_dayofweek']).count().reset_index()
    df_aux1.sort_values('order_id', ascending=False, inplace=True)

    # Criando o gráfico
    fig_18 = px.bar(df_aux1, x='name_dayofweek', y='order_id', text_auto=True, color='name_dayofweek',
                    labels={'name_dayofweek': 'Dia da Semana', 'order_id': 'Número de Pedidos'})

    # Personalizando o gráfico
    fig_18.update_layout(
        title='Número de Pedidos por Dia da Semana',
        xaxis_title='Dia da Semana',
        yaxis_title='Número de Pedidos',
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_18)

    # Pergunta 7: Valor Médio de Pagamento por Dia da Semana
    st.markdown("### 8. Em qual dia da semana os consumidores gastam mais?")

    # Manipulação dos dados
    df_aux2 = df[['payment_value', 'name_dayofweek']].groupby(
        ['name_dayofweek']).mean().reset_index()
    df_aux2.sort_values('payment_value', ascending=False, inplace=True)

    # Criando o gráfico
    fig_19 = px.bar(df_aux2, x='name_dayofweek', y='payment_value', text_auto=True, color='name_dayofweek',
                    labels={'name_dayofweek': 'Dia da Semana', 'payment_value': 'Valor Médio do Pagamento'})

    # Personalizando o gráfico
    fig_19.update_layout(
        title='Valor Médio de Pagamento por Dia da Semana',
        xaxis_title='Dia da Semana',
        yaxis_title='Valor Médio do Pagamento',
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_19)

    # Resultados do gráfico
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                    A análise dos gráficos mostra que a segunda-feira tem o maior número de pedidos, o que pode ser aproveitado com promoções nesse dia. Já a sexta-feira, embora com menos pedidos, apresenta o maior valor médio de pagamento, indicando que os consumidores gastam mais próximo ao fim da semana.
                    
                    ### Recomendação 
                    - Explorar ofertas e descontos direcionados para aumentar o ticket médio nas sextas-feiras. 
                    -  O fim de semana, com menor volume de pedidos e valores, pode ser uma oportunidade para otimizar campanhas e engajar mais consumidores.
                    """)

    # Pergunta 8: Quais são as 5 cidades com mais pedidos?
    st.markdown(
        "### 9. Quais são as cinco cidades com o maior número de pedidos?")

    # Manipulação dos dados de geolocalização (assumindo que você tem as tabelas de geolocalização e clientes)
    # Cria dados de ponto representativo a partir do código postal dos dados geográficos
    geo_data = pd.DataFrame(dict(rep_lat=geolocation.groupby("geolocation_zip_code_prefix").geolocation_lat.mean(),
                                 rep_long=geolocation.groupby("geolocation_zip_code_prefix").geolocation_lng.mean())).reset_index()

    # Mesclar os dados de geolocalização nos dados de clientes
    geo_customers = customers.merge(
        geo_data, left_on="customer_zip_code_prefix", right_on="geolocation_zip_code_prefix")

    # Focar em customer_unique_id porque customer_id é distribuído por pedido
    grouped_geo_customers = geo_customers.groupby("customer_unique_id")[
        ["rep_lat", "rep_long"]].mean().reset_index()

    # Ajuste conforme sua necessidade
    top_5_cities = df['customer_city'].value_counts().head(5).reset_index()
    top_5_cities.columns = ['Cidade', 'Número de Pedidos']

    # Criando o gráfico
    fig_52 = px.bar(top_5_cities, x='Cidade', y='Número de Pedidos',
                    title='Top 5 Cidades com Mais Pedidos',
                    labels={'Cidade': 'Cidade',
                            'Número de Pedidos': 'Número de Pedidos'},
                    color='Cidade')

    # Atualizando layout
    fig_52.update_layout(
        xaxis_title='Cidade',
        yaxis_title='Número de Pedidos',
        width=800,
        height=400,
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_52)

    # Resultados do gráfico
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                    As cinco cidades com o maior número de pedidos são, respectivamente, São Paulo, Rio de Janeiro, Belo Horizonte, Brasília e Curitiba. Esse padrão reflete a forte concentração de consumo nas capitais e grandes centros urbanos.
                    
                    ### Recomendação 
                    - Focar esforços logísticos e de marketing nessas cidades para atender à alta demanda com eficiência.""")

    # Pergunta 4: Número de Pedidos por Estado
    st.markdown("### 10. Quais estados têm o maior volume de pedidos?")

    # Manipulação de Dados
    df_aux = df[['customer_state', 'order_id']].groupby(
        ['customer_state']).count().reset_index()
    df_aux.sort_values('order_id', ascending=False, inplace=True)

    # Criando o gráfico
    fig_16 = px.bar(df_aux, x='customer_state', y='order_id', text='order_id',
                    title='Número de Pedidos por Estado',
                    labels={'customer_state': 'Estado', 'order_id': 'Número de Pedidos'})

    # Personalizando o gráfico
    fig_16.update_layout(
        title='Número de Pedidos por Estado',
        xaxis_title='Estado',
        yaxis_title='Número de Pedidos',
        height=600,
        width=1000,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        title_x=0.3,
        xaxis_tickangle=-45,
        margin=dict(l=50, r=50, t=50, b=50)
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_16)

    # Resultados do gráfico
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                    A análise do gráfico mostra que São Paulo lidera em número de pedidos, seguido por Rio de Janeiro e Minas Gerais, ambos da Região Sudeste, um importante polo de consumo e logística. 
                    
                    Já os estados do Norte têm volumes bem menores, sugerindo desafios logísticos ou um alcance limitado do e-commerce na região. 
                    
                    ### Recomendação 
                    - Ajustar as estratégias para melhorar a presença e a logística no Norte.""")

elif section == 'Preços':
    # Pergunta em Markdown
    st.markdown(
        "### 1. Como é a distribuição dos preços nas 10 categorias de produtos mais vendidas?")

    # Manipulação de Dados - Agrupando por categoria de produto
    df_aux1 = df[['product_category_name', 'order_id']].groupby(
        ['product_category_name']).count().reset_index()
    df_aux1.sort_values('order_id', ascending=False, inplace=True)

    # Selecionando as 10 categorias mais vendidas
    most_sold_categories = df_aux1.product_category_name.head(10).tolist()
    df_aux2 = df[df['product_category_name'].isin(most_sold_categories)]

    # Criando o gráfico de caixa (box plot) com uma paleta de cores categórica
    fig_31 = px.box(df_aux2, x='product_category_name', y='price',
                    title='Distribuição de Preços nas 10 Categorias Mais Vendidas',
                    labels={'product_category_name': 'Categoria',
                            'price': 'Preço'},
                    color='product_category_name',
                    color_discrete_sequence=px.colors.qualitative.Plotly)

    # Personalizando o layout do gráfico
    fig_31.update_layout(
        title_x=0.3,                   # Centraliza o título
        xaxis_title='Categoria',       # Rótulo do eixo X
        yaxis_title='Preço',           # Rótulo do eixo Y
        xaxis_showgrid=False,          # Remove a grade do eixo X
        yaxis=dict(title='Preço'),     # Define o título do eixo Y
        xaxis_tickangle=-45,           # Inclina os rótulos do eixo X para melhor legibilidade
        # height=600,                    # Aumenta a altura do gráfico
        # Ajusta as margens para dar mais espaço aos rótulos
        margin=dict(l=40, r=40, t=80, b=150),
        xaxis_tickfont_size=10         # Diminui o tamanho da fonte dos rótulos do eixo X
    )

    # Exibindo o gráfico interativo
    st.plotly_chart(fig_31)

    # Resposta em Markdown
    with st.expander("Detalhes da Análise"):
        st.markdown("""
    A análise das 10 categorias mais vendidas revelou que algumas categorias, como "relógios_presentes", possuem preços mais altos, indicando um potencial para estratégias focadas em produtos premium. Por outro lado, "telefonia" e "utilidades_domesticas" apresentam preços médios baixos e alta demanda, tornando-se atrativas para consumidores sensíveis ao preço. Além disso, categorias como "beleza_saude" e "cama_mesa_banho" mostram uma diversidade de preços, o que sugere a possibilidade de segmentação de mercado.

    ### Recomendação 
    - Focar em estratégias premium para categorias como "relógios_presentes", destacando o valor agregado e a exclusividade dos produtos.
    - Atração de consumidores sensíveis ao preço com promoções e descontos em categorias como "telefonia" e "utilidades_domesticas", para aproveitar a alta demanda.
    - Segmentação de mercado nas categorias "beleza_saude" e "cama_mesa_banho", criando campanhas personalizadas para diferentes perfis de clientes, aproveitando a diversidade de preços.
    """)

    # Manipulação de Dados - Agrupando por categoria de produto e aplicando filtro de preço
    df_aux2 = df[(df['product_category_name'].isin(
        most_sold_categories)) & (df['price'] <= 1000)]

    # Criando o gráfico de caixa (box plot)
    fig_32 = px.box(df_aux2, x='product_category_name', y='price',
                    title='Distribuição de Preços nas 10 Categorias Mais Vendidas (Abaixo de R$1.000)',
                    labels={'product_category_name': 'Categoria',
                            'price': 'Preço'},
                    color='product_category_name',
                    color_discrete_sequence=px.colors.qualitative.Plotly)

    # Personalizando o layout do gráfico
    fig_32.update_layout(
        title_x=0.3,                   # Centraliza o título
        xaxis_title='Categoria',       # Rótulo do eixo X
        yaxis_title='Preço',           # Rótulo do eixo Y
        xaxis_showgrid=False,          # Remove a grade do eixo X
        xaxis_tickangle=-45         # Inclina os rótulos do eixo X para melhor legibilidade
        # height=650                     # Define a altura do gráfico
    )

    # Exibindo o gráfico interativo
    st.plotly_chart(fig_32)

    # Resposta em Markdown
    with st.expander("Detalhes da Análise"):
        st.markdown("""
        Ao filtrar produtos abaixo de R$1.000 nas 10 categorias mais vendidas revela preços médios acessíveis, indicando oportunidades para ampliar a oferta nessa faixa, atrair mais consumidores e aumentar o volume de vendas.
    """)

    # Pergunta em Markdown
    st.markdown(
        "### 2. Como varia o preço médio dos produtos entre os diferentes estados e regiões do Brasil?")

    # Manipulação de Dados - Criando o dataframe agrupado
    df_aux = df[['customer_state', 'price', 'customer_region']].groupby(
        ['customer_state', 'customer_region']).mean().reset_index()
    df_aux.sort_values('price', ascending=False, inplace=True)

    # Criando o gráfico de barras
    fig_33 = px.bar(df_aux, x='customer_state', y='price', color='customer_region', text_auto=True,
                    title='Preço Médio dos Produtos por Estado e Região',
                    labels={'customer_state': 'Estado', 'price': 'Preço Médio', 'customer_region': 'Região'})

    # Personalizando o layout do gráfico
    fig_33.update_layout(
        title_x=0.5,                   # Centraliza o título
        xaxis_title='Estado',          # Rótulo do eixo X
        yaxis_title='Preço Médio',     # Rótulo do eixo Y
        xaxis_showgrid=False,          # Remove a grade do eixo X
        yaxis=dict(title='Preço Médio'),  # Define o título do eixo Y
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_33, use_container_width=True)

    # Resposta em Markdown
    with st.expander("Detalhes da Análise"):
        st.markdown("""
        Os resultados apresentados indicam variações significativas no preço médio dos produtos entre os estados e regiões do Brasil. Estados da região Norte e Nordeste, como PB, AC e AL, apresentam preços mais altos, enquanto as regiões Sul e Sudeste registram valores mais baixos, com destaque para SP. 
        
        ### Recomendação
        - Explorar estratégias de preço diferenciadas, levando em consideração as particularidades regionais, como custos de distribuição e perfil de consumo.
    """)

    # Pergunta em Markdown
    st.markdown(
        "### 3. Qual é a diferença no preço médio do frete entre os estados e como isso varia por região?")

    # Manipulação de Dados - Criando o dataframe agrupado
    df_aux = df[['customer_state', 'freight_value', 'customer_region']].groupby(
        ['customer_state', 'customer_region']).mean().reset_index()
    df_aux.sort_values('freight_value', ascending=False, inplace=True)

    # Criando o gráfico de barras
    fig_34 = px.bar(
        df_aux,
        x='customer_state',
        y='freight_value',
        color='customer_region',
        text_auto=True,
        title='Preço Médio do Frete por Estado e Região',
        labels={'customer_state': 'Estado',
                'freight_value': 'Preço Médio do Frete', 'customer_region': 'Região'}
    )

    # Personalizando o layout do gráfico
    fig_34.update_layout(
        title_x=0.3,                   # Centraliza o título
        xaxis_title='Estado',          # Rótulo do eixo X
        yaxis_title='Preço Médio do Frete',  # Rótulo do eixo Y
        xaxis_showgrid=False,          # Remove a grade do eixo X
        # Define o título do eixo Y
        yaxis=dict(title='Preço Médio do Frete')
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_34)

    # Texto explicativo no Streamlit
    with st.expander("Detalhes da Análise"):
        st.markdown("""
        Os resultados apresentados no gráfico indicam que os clientes da Região Norte e Nordeste enfrentam custos elevados de frete, além de preços médios mais altos para os produtos, como observado na análise anterior. 
        
        ### Recomendação
        - Revisar as estratégias logísticas para essa região, como buscar alternativas de transporte mais econômicas ou oferecer promoções para compensar os custos elevados.
        - Avaliar a possibilidade de precificação diferenciada e segmentação de produtos, ajustando a oferta para tornar as compras mais acessíveis nesse mercado.
        """)

elif section == 'Avaliações':
    # Pergunta
    st.markdown(
        "#### 1. Quais categorias de produtos apresentam as melhores e piores avaliações?")

    # Criando o dataframe com as médias de avaliação por categoria
    category_reviews = df.groupby('product_category_name')[
        'review_score'].mean().reset_index()

    # Ordenando os resultados pela média das avaliações
    category_reviews = category_reviews.sort_values(
        by='review_score', ascending=False)

    # Criando o gráfico de barras no Streamlit
    fig, ax = plt.subplots(figsize=(12, 14))  # Aumentando o tamanho da figura
    sns.barplot(x='review_score', y='product_category_name',
                data=category_reviews, palette='magma', ax=ax)
    ax.set_title('Média de Avaliações por Categoria de Produto', fontsize=16)
    ax.set_xlabel('Média da Avaliação', fontsize=14)
    ax.set_ylabel('Categoria de Produto', fontsize=14)

    # Ajustando os rótulos do eixo Y
    ax.tick_params(axis='y', labelsize=10)  # Reduzindo o tamanho dos rótulos
    plt.tight_layout()  # Garantindo que os rótulos não sejam cortados

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)

    with st.expander("Detalhes da Análise"):
        st.markdown(""" 
                    Os resultados apresentados no gráfico indicam que as categorias **CDs e DVDs** e **roupa infanto juvenil** possuem as médias de avaliação mais altas, enquanto **seguros** apresenta uma das médias mais baixas. Essa categoria também foi identificada em uma análise anterior como a que tem o menor número de pedidos. Isso sugere que tanto a avaliação negativa quanto a baixa demanda podem estar relacionadas a problemas específicos nessa área. 
                    
                    ### Recomendação
                    - Investigar as causas dessas avaliações baixas e o baixo volume de vendas, buscando: **otimizar a experiência do cliente**, **melhorar o atendimento** e **ajustar a oferta de produtos**. 
                    - Implementar estratégias de marketing voltadas para aumentar a visibilidade e a confiança nessa categoria podem contribuir para melhorar tanto as avaliações quanto o número de pedidos.""")

    # Pergunta
    st.markdown(
        "#### 2. Como a pontuação média da avaliação dos produtos se relaciona com o tempo de entrega em diferentes regiões?")

    # Manipulação de Dados
    df_aux = df[['review_score', 'payment_value', 'customer_state', 'customer_region',
                 'delivery_time_in_hours']].groupby(['customer_state', 'customer_region']).mean().reset_index()

    # Criando o gráfico
    fig_44 = px.scatter(
        df_aux,
        x='delivery_time_in_hours',
        y='review_score',
        color='customer_region',
        size='payment_value',
        trendline='ols',
        trendline_scope='overall',
        trendline_color_override='white',
        title='Pontuação Média da Avaliação vs. Delta de Tempo (Regiões)',
        labels={
            'delivery_time_in_hours': 'Tempo de entrega (horas)',
            'review_score': 'Pontuação da Avaliação'
        }
    )

    # Customizando o layout do gráfico
    fig_44.update_layout(
        title='Pontuação Média da Avaliação vs. Tempo de entrega (Regiões)',
        xaxis_title='Tempo de entrega (horas)',
        yaxis_title='Pontuação da Avaliação',
        # height=650
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_44, use_container_width=True)

    # Selecionando apenas as colunas numéricas
    df_numerico = df.select_dtypes(include=['number'])

    # Calculando a matriz de correlação
    correlation_matrix = df_numerico.corr()

    # Criando o mapa de calor
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='RdBu',
                fmt='.2f', linewidths=0.5, ax=ax)
    ax.set_title('Matriz de Correlação')

    # Exibindo o mapa de calor no Streamlit
    st.pyplot(fig)

    with st.expander("Detalhes da Análise"):
        st.markdown("""
    A pontuação de avaliação dos produtos está fortemente relacionada ao tempo de entrega. Entregas rápidas geralmente resultam em avaliações mais positivas, enquanto entregas demoradas impactam negativamente as avaliações. Regiões com infraestrutura logística melhor tendem a ter tempos de entrega mais rápidos e, consequentemente, avaliações mais altas, enquanto áreas com desafios logísticos enfrentam pontuações mais baixas.

    ### Recomendação
    - Investir em infraestrutura logística nas regiões com tempos de entrega mais longos.
    - Melhorar a eficiência no transporte por meio de parcerias com transportadoras locais ou otimização de rotas de entrega.
    - Desenvolver uma comunicação mais transparente com os clientes sobre o status da entrega, para melhorar a experiência geral, mesmo em áreas de entrega mais demorada.

    """)

    # Pergunta
    st.markdown(
        "#### 3. Qual é a relação entre a pontuação média de avaliação dos clientes e o tempo de entrega dos produtos em diferentes estados?")

    # Manipulação de Dados - Criando o DataFrame agrupado
    df_aux = df[['review_score', 'payment_value', 'customer_state',
                 'delivery_time_in_hours']].groupby(['customer_state']).mean().reset_index()

    # Criando o gráfico
    fig_45 = px.scatter(df_aux, x='delivery_time_in_hours', y='review_score', color='customer_state', size='payment_value',
                        trendline='ols', trendline_scope='overall', trendline_color_override='white',
                        title='Pontuação Média da Avaliação vs. Delta de Tempo (Estados)',
                        labels={'delivery_time_in_hours': 'Tempo de entrega (horas)', 'review_score': 'Pontuação da Avaliação'})

    # Customizando o gráfico
    fig_45.update_layout(
        title='Pontuação Média da Avaliação vs. Tempo de entrega (Estados)',
        xaxis_title='Tempo de entrega (horas)',
        yaxis_title='Pontuação da Avaliação',
        height=650
    )

    # Mostrando o gráfico no Streamlit
    st.plotly_chart(fig_45)

    with st.expander("Detalhes da Análise"):
        st.markdown("""
    Os dados mostram que **estados com tempos de entrega mais rápidos**, como **SP** e **PR**, tendem a ter pontuações de avaliação mais altas, enquanto estados com entregas mais lentas, como **RR** e **AM**, apresentam pontuações mais baixas. 
    
    #### Recomendação:
    - Para melhorar a satisfação do cliente, a empresa pode focar em otimizar a logística nos estados com tempos de entrega mais longo
    - Investir em soluções de transporte mais eficientes, parcerias com transportadoras locais ou até mesmo reavaliar a distribuição de estoque nessas regiões pode resultar em uma melhoria significativa nas avaliações.
    """)

    # Pergunta
    st.markdown(
        "#### 3. Qual é a distribuição das avaliações dos clientes do e-commerce?")

    print("review_score == 5: %d" % len(df[df['review_score'] == 5]))
    print("review_score == 4: %d" % len(df[df['review_score'] == 4]))
    print("review_score == 3: %d" % len(df[df['review_score'] == 3]))
    print("review_score == 2: %d" % len(df[df['review_score'] == 2]))
    print("review_score == 1: %d" % len(df[df['review_score'] == 1]))
    score_list = [len(df[df['review_score'] == 1]),
                  len(df[df['review_score'] == 2]),
                  len(df[df['review_score'] == 3]),
                  len(df[df['review_score'] == 4]),
                  len(df[df['review_score'] == 5])]

    # Definindo as cores
    colors = ['#001C5B', '#E64E36', '#ff82cd', '#0A4EE4', '#779E3D']

    # Criando o gráfico de barras no Plotly
    fig_47 = go.Figure(data=[go.Bar(
        x=[1, 2, 3, 4, 5],
        y=score_list,
        marker_color=colors,
        text=score_list,  # Adiciona os rótulos com os valores de quantidade
        textposition='inside',  # Coloca os rótulos dentro das barras
    )])

    # Configurações do gráfico
    fig_47.update_layout(
        title="Distribuição das Avaliações dos Clientes",
        xaxis_title="Pontuação da Avaliação",
        yaxis_title="Quantidade",
        width=1100,
        height=600
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_47)

    # Texto explicativo usando st.expander
    with st.expander("Detalhes da Análise"):
        st.markdown("""
        A **maioria das avaliações** é positiva, com  56.55% com nota 5 e 19% com nota 4. Isso indica uma experiência **geralmente satisfatória** para os clientes do e-commerce.

        Contudo, também existem **áreas de melhoria**, com 12.58% de nota 1 e  3.48% de nota 2.
        Essas notas mais baixas sugerem que, embora a experiência de compra seja amplamente positiva, há um segmento de clientes que está insatisfeito com aspectos específicos do serviço.

        #### Recomendação:
        - A empresa pode se concentrar em **identificar os pontos críticos** que geram insatisfação (como atrasos ou problemas no atendimento) e implementar **ações corretivas**.
        - Melhorias nas áreas mais criticadas podem **aumentar ainda mais a satisfação** e ajudar a transformar avaliações negativas em positivas.
        """)

elif section == 'Métricas':
    # Pergunta
    st.markdown(
        "#### 1. Receita Recorrente Mensal (MRR)")

    col = ['customer_unique_id', 'price',
           'order_item_id', 'order_purchase_timestamp']
    orders = df[col]

    orders['order_purchase_timestamp'] = pd.to_datetime(
        orders['order_purchase_timestamp'])

    orders['InvoiceYearMonth'] = orders['order_purchase_timestamp'].map(
        lambda date: 100*date.year + date.month)

    orders['Revenue'] = orders['price'] * orders['order_item_id']
    orders_revenue = orders.groupby(['InvoiceYearMonth'])[
        'Revenue'].sum().reset_index()

    # Dados do gráfico
    plot_data = [
        go.Scatter(
            x=orders_revenue['InvoiceYearMonth'],  # Eixo X: Mês e Ano
            y=orders_revenue['Revenue'],  # Eixo Y: Receita
            mode='lines+markers',  # Exibe tanto as linhas quanto os marcadores
            marker=dict(color='blue'),  # Define a cor dos marcadores
            line=dict(color='blue')  # Define a cor da linha
        )
    ]

    # Layout do gráfico
    plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='Receita Mensal',
        width=900,
        height=500
    )

    # Criando a figura
    fig_401 = go.Figure(data=plot_data, layout=plot_layout)

    # Exibindo no Streamlit
    st.plotly_chart(fig_401, use_container_width=True)

    # Texto explicativo usando st.expander
    with st.expander("Detalhes da Análise"):
        st.markdown("""
        A receita mensal do e-commerce cresceu de forma contínua até agosto de 2018, com destaque para o período a partir de março de 2017, quando superou R$ 400 mil mensais, alcançando mais de R$ 1 milhão por mês. O pico foi em novembro de 2017, possivelmente impulsionado pela Black Friday, o que representou o maior volume de vendas do ano. 

        Em 2018, a receita se manteve estável, acima de R$ 1 milhão por mês, mostrando um desempenho consistente, embora o crescimento tenha sido menos expressivo em comparação a 2017.
        """)

    # Pergunta
    st.markdown(
        "##### 1.1 Análise de Flutuações na Receita Mensal")

    # Verificando a contagem de registros por mês
    orders['InvoiceYearMonth'] = pd.to_datetime(
        orders['InvoiceYearMonth'], format='%Y%m')
    orders_count = orders.groupby(orders['InvoiceYearMonth'].dt.to_period(
        'M')).size().reset_index(name='Registros')

    # Renomeando as colunas para uma exibição mais clara
    orders_count.columns = ['InvoiceYearMonth', 'Registros']

    # Criando a tabela usando plotly
    fig_table = go.Figure(go.Table(
        header=dict(values=['InvoiceYearMonth', 'Registros']),
        cells=dict(values=[orders_count['InvoiceYearMonth'].astype(
            str), orders_count['Registros']])
    ))

    # Ajustando o layout para reduzir a margem
    fig_table.update_layout(
        margin=dict(l=10, r=10, t=10, b=10)
    )
    # Exibindo a tabela no Streamlit
    st.plotly_chart(fig_table, use_container_width=False)

    # Texto explicativo usando st.expander
    with st.expander("Detalhes da Análise"):
        st.markdown("""A variação na receita no final de 2016 e 2018 foi analisada para entender se era causada por flutuações reais ou pela falta de dados. Identificou-se que, nesses períodos, especialmente a partir de agosto de 2018, houve ausência de registros completos, explicando a discrepância na receita.
                    """)

    # Pergunta
    st.markdown(
        "#### 2. Taxa de Crescimento Mensal (MoM)")

    # usando a função pct_change() para ver a variação percentual mensal
    orders_revenue['MonthlyGrowth'] = orders_revenue['Revenue'].pct_change()

    '''
        A função pct_change() no Pandas calcula a variação percentual entre os valores consecutivos de uma coluna de um DataFrame. 
        Essencialmente, ela mostra quanto o valor atual mudou em relação ao valor anterior, como uma porcentagem.
        '''

    # Filtrando os dados para exibir apenas a partir de janeiro de 2017
    filtered_data = orders_revenue.query("InvoiceYearMonth > 201701")

    # Criando o gráfico de taxa de crescimento mensal
    plot_data = [
        go.Scatter(
            x=filtered_data['InvoiceYearMonth'],  # Eixo X: Mês e Ano
            # Eixo Y: Taxa de Crescimento Mensal
            y=filtered_data['MonthlyGrowth'],
            mode='lines+markers'  # Exibe linhas com marcadores
        )
    ]

    plot_layout = go.Layout(
        xaxis={"type": "category"},  # Eixo X categórico
        title='Taxa de Crescimento Mensal', width=1000, height=500
    )

    # Criando a figura combinando os dados e o layout
    fig_402 = go.Figure(data=plot_data, layout=plot_layout)

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_402, use_container_width=True)

    # Texto explicativo usando st.expander
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                    A análise da Taxa de Crescimento Mensal (MoM), destacada no gráfico, evidencia flutuações significativas no desempenho da empresa. Alguns destaques incluem:

                    - **Altas expressivas**: Fevereiro de 2017 apresentou um crescimento de **+83,7%**.
                    - **Quedas acentuadas**: Dezembro de 2017 registrou uma redução de **-31,9%**.

                    Esses padrões sugerem **sazonalidade** e possíveis impactos de promoções ou desafios operacionais. 

                    ##### Recomendação:
                    - Replicar estratégias de sucesso utilizadas nos meses de maior crescimento.
                    - Ajustar campanhas e estoques para mitigar impactos em períodos de baixa.
                    - Tomar decisões baseadas em dados para promover um crescimento mais consistente ao longo do tempo.
                    """)

     # Pergunta
    st.markdown(
        "#### 3. Clientes Ativos Mensais (MAU)")

    # criando um dataframe de clientes ativos mensais contando os Customer IDs únicos
    orders_monthly_active = orders.groupby('InvoiceYearMonth')[
        'customer_unique_id'].nunique().reset_index()

    # Criando o gráfico de barras para clientes ativos mensais
    plot_data = [
        go.Bar(
            x=orders_monthly_active['InvoiceYearMonth'],  # Eixo X: Ano e Mês
            # Eixo Y: Clientes únicos ativos
            y=orders_monthly_active['customer_unique_id'],
        )
    ]

    # Layout do gráfico
    plot_layout = go.Layout(
        xaxis={"type": "category"},  # Eixo X categórico
        title='Clientes Ativos Mensais',  # Título do gráfico
        width=900,
        height=500
    )

    # Combinando os dados e o layout para criar a figura
    fig_403 = go.Figure(data=plot_data, layout=plot_layout)

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_403)

    # Texto explicativo usando st.expander
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                    Entre janeiro de 2017 e agosto de 2018, o número de Clientes Ativos Mensais (MAU) cresceu 134%, saindo de 735 em janeiro de 2017 para 6.352 em agosto de 2018. O pico registrado em novembro de 2017 representou um aumento de 63% em relação à média dos três meses anteriores, possivelmente influenciado pela Black Friday, conforme observado em análises anteriores.

                    Após o pico, houve uma queda de 25% em dezembro de 2017, seguida por um período de estabilização. Essa estabilização destaca a necessidade de estratégias para manter o engajamento após eventos sazonais.

                    #### Recomendação
                    - Campanhas de fidelização para reforçar a lealdade do cliente.
                    - Incentivos regulares, como promoções e ofertas, para estimular compras em períodos de menor movimento.
                    """)

    # Pergunta
    st.markdown(
        "#### 4. Pedidos Mensais")

    # Criar um novo dataframe para o número de pedidos utilizando o campo 'quantidade'
    orders_monthly_sales = orders.groupby('InvoiceYearMonth')[
        'order_item_id'].sum().reset_index()

    # Plotando o gráfico
    plot_data = [
        go.Bar(
            # Eixo X: mês e ano da fatura
            x=orders_monthly_sales['InvoiceYearMonth'],
            # Eixo Y: número total de itens do pedido
            y=orders_monthly_sales['order_item_id'],
        )
    ]

    plot_layout = go.Layout(
        xaxis={"type": "category"},  # Tipo do eixo X definido como categoria
        title='Número Total de Pedidos por Mês',  # Título do gráfico
        width=900,  # Largura do gráfico
        height=500  # Altura do gráfico
    )

    # Cria a figura com os dados e o layout do gráfico
    fig_404 = go.Figure(data=plot_data, layout=plot_layout)

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig_404)

    # Texto explicativo usando st.expander
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                    A análise dos pedidos mostra um crescimento constante, com picos em novembro e dezembro, provavelmente devido à Black Friday. A Olist pode explorar esses períodos com campanhas promocionais direcionadas.

                    No entanto, a partir de junho de 2018, houve um declínio no número de pedidos, o que indica menor engajamento. Para revitalizar o interesse e manter o engajamento dos clientes, a empresa pode investir em ofertas especiais, lançamento de novos produtos ou campanhas de fidelização.
                    """)

    # Pergunta
    st.markdown(
        "#### 5. Variação de Clientes Novos e Existentes por Mês")

    # Cria um DataFrame contendo o ID do cliente e a data da primeira compra
    orders_min_purchase = orders.groupby(
        'customer_unique_id').order_purchase_timestamp.min().reset_index()
    orders_min_purchase.columns = ['customer_unique_id', 'MinPurchaseDate']
    orders_min_purchase['MinPurchaseYearMonth'] = orders_min_purchase['MinPurchaseDate'].map(
        lambda date: 100*date.year + date.month)

    # Mescla a coluna da primeira data de compra com nosso DataFrame principal
    orders = pd.merge(orders, orders_min_purchase, on='customer_unique_id')

    orders['order_purchase_timestamp'] = pd.to_datetime(
        orders['order_purchase_timestamp'])

    orders['InvoiceYearMonth'] = orders['order_purchase_timestamp'].dt.to_period(
        'M')

    # Vamos usar a coluna 'MinPurchaseDate' e garantir que seja a primeira compra de cada cliente
    orders_min_purchase = orders.groupby('customer_unique_id')[
        'MinPurchaseDate'].min().reset_index()
    orders_min_purchase.columns = ['customer_unique_id', 'FirstPurchaseDate']

    orders_min_purchase['FirstPurchaseYearMonth'] = orders_min_purchase['FirstPurchaseDate'].dt.to_period(
        'M')

    orders = pd.merge(orders, orders_min_purchase[[
                      'customer_unique_id', 'FirstPurchaseYearMonth']], on='customer_unique_id', how='left')

    # Inicialmente, marcamos todos como 'Existing'
    orders['UserType'] = 'Existing'
    orders.loc[orders['InvoiceYearMonth'] ==
               orders['FirstPurchaseYearMonth'], 'UserType'] = 'New'

    # Passo 1: Converter 'InvoiceYearMonth' para string
    orders['InvoiceYearMonth'] = orders['InvoiceYearMonth'].astype(str)

    # Passo 2: Agrupar os dados por mês e tipo de cliente (New ou Existing)
    customer_counts = orders.groupby(['InvoiceYearMonth', 'UserType'])[
        'customer_unique_id'].nunique().reset_index()

    # Passo 3: Criar o gráfico com Plotly
    fig = px.line(customer_counts,
                  x='InvoiceYearMonth',
                  y='customer_unique_id',
                  color='UserType',
                  title='Variação de Clientes Novos e Existentes ao Longo do Tempo',
                  labels={'InvoiceYearMonth': 'Mês da Compra',
                          'customer_unique_id': 'Número de Clientes'},
                  markers=True)

    # Passo 4: Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

    # Texto explicativo usando st.expander
    with st.expander("Detalhes da Análise"):
        st.markdown("""
                    A análise mostra que, embora a empresa esteja atraindo um grande número de clientes novos, a conversão desses clientes em recorrentes é limitada. Isso pode indicar uma alta taxa de churn (desistência), o que é preocupante, pois o custo de adquirir novos clientes é geralmente mais alto do que reter os existentes. Esse padrão sugere que a experiência pós-compra pode não ser otimizada ou que não há iniciativas suficientes de fidelização para garantir que os clientes retornem.

                    #### Recomendação 
                    - Implementar programas de fidelidade que incentivem a recompra e aumentem o engajamento com os clientes existentes. 
                    - Analisar os padrões de churn e ajustar as estratégias de marketing e de atendimento, garantindo que a experiência do cliente seja positiva após a compra. 
                    - Monitorar a retenção de clientes ao longo do tempo também é essencial para maximizar o valor de longo prazo dos clientes (LTV).
                    """)
