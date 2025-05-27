# Aplicação de Técnicas de Aprendizado de Máquina na Predição de Satisfação do Cliente para E-commerce
---

## Sobre o Negócio

A Olist é a maior loja de departamentos nos marketplaces brasileiros, conectando pequenos comerciantes a diversos canais de vendas. A empresa gerencia um grande volume de dados de pedidos, abrangendo várias dimensões como status do pedido, preço, pagamento, desempenho do frete, localização dos clientes, atributos dos produtos e avaliações dos clientes.

Depois que um cliente compra o produto na Olist Store, um vendedor é notificado para atender a esse pedido. Uma vez que o cliente recebe o produto, ou a data de entrega estimada é devida, o cliente recebe uma pesquisa de satisfação por e-mail, onde ele pode dar uma nota para a experiência de compra e escrever alguns comentários.

A Olist enfrenta desafios em compreender as necessidades dos clientes e melhorar continuamente seus serviços e produtos, por isso é necessário uma análise detalhada dos dados para desenvolver estratégias para melhorar a experiência do cliente.

## Objetivos
- Analisar padrões de comportamento de compra e desempenho de vendas na Olist, incluindo variações por região, estado, categoria de produto e tipo de pagamento, para identificar tendências estratégicas.
- Explorar a relação entre métricas de entrega, como tempo e custo de frete, e a satisfação dos clientes, considerando variações regionais e estaduais.
- Investigar os fatores que influenciam a pontuação de avaliações dos clientes, como categoria de produto, tipo de pagamento e tempo de entrega, para entender as principais causas de satisfação e insatisfação.
- Desenvolver um modelo preditivo para classificar a satisfação do cliente para prever a probabilidade de um cliente estar satisfeito ou insatisfeito.
---

## Resumo dos Dados

<div align="center">


| Nome da Coluna                   | Descrição                                                                                      |
|----------------------------------|------------------------------------------------------------------------------------------------|
| `order_id`                         | Identificador único do pedido.                                                                 |
| `customer_id`                      | Chave para o conjunto de dados dos clientes. Cada pedido tem um customer_id único.            |
| `order_status`                     | Referência ao status do pedido (entregue, enviado, etc).                                        |
| `order_purchase_timestamp`         | Mostra o momento da compra.                                                                    |
| `order_approved_at`                | Mostra o momento da aprovação do pagamento.                                                    |
| `order_delivered_carrier_date`     | Mostra a data em que o pedido foi encaminhado ao parceiro logístico.                          |
| `order_delivered_customer_date`    | Mostra a data de entrega real do pedido ao cliente.                                            |
| `order_estimated_delivery_date`    | Mostra a data de entrega estimada que foi informada ao cliente no momento da compra.           |
| `customer_unique_id`               | Identificador único de um cliente.                                                             |
| `customer_zip_code_prefix`         | Os primeiros cinco dígitos do CEP do cliente.                                                  |
| `customer_city`                    | Nome da cidade do cliente.                                                                     |
| `customer_state`                   | Estado do cliente.                                                                             |
| `order_item_id`                    | Número sequencial que identifica o número de itens incluídos no mesmo pedido.                   |
| `product_id`                      | Identificador único do produto.                                                                |
| `seller_id`                        | Identificador único do vendedor.                                                               |
| `shipping_limit_date`              | Mostra a data limite de envio do vendedor para entregar o pedido ao parceiro logístico.        |
| `price`                            | Preço do item.                                                                                 |
| `freight_value`                    | Valor do frete do item (se um pedido tiver mais de um item, o valor do frete é dividido).      |
| `payment_sequential`               | Um cliente pode pagar um pedido com mais de um método de pagamento.                            |
| `payment_type`                     | Método de pagamento escolhido pelo cliente.                                                     |
| `payment_installments`             | Número de parcelas escolhidas pelo cliente.                                                     |
| `payment_value`                    | Valor da transação.                                                                           |
| `product_category_name`            | Categoria raiz do produto, em português.                                                        |
| `product_name_lenght`              | Número de caracteres extraídos do nome do produto.                                              |
| `product_description_lenght`       | Número de caracteres extraídos da descrição do produto.                                         |
| `product_photos_qty`               | Número de fotos publicadas do produto.                                                          |
| `product_weight_g`                 | Peso do produto medido em gramas.                                                              |
| `product_length_cm`                | Comprimento do produto medido em centímetros.                                                   |
| `product_height_cm`                | Altura do produto medida em centímetros.                                                        |
| `product_width_cm`                | Largura do produto medida em centímetros.                                                       |
| `seller_zip_code_prefix`          | Os primeiros 5 dígitos do CEP do vendedor.                                                      |
| `seller_city`                      | Nome da cidade do vendedor.                                                                    |
| `seller_state`                     | Estado do vendedor.                                                                            |
| `product_category_name_english`    | Nome da categoria em inglês.                                                                   |
| `review_id`                        | Identificador único da avaliação.                                                               |
| `review_score`                     | Nota variando de 1 a 5 dada pelo cliente em uma pesquisa de satisfação.                          |
| `review_comment_title`            | Título do comentário da avaliação deixada pelo cliente, em português.                          |
| `review_comment_message`          | Mensagem do comentário da avaliação deixada pelo cliente, em português.                        |
| `review_creation_date`            | Mostra a data em que a pesquisa de satisfação foi enviada ao cliente.                          |
| `review_answer_timestamp`         | Mostra o momento em que a pesquisa de satisfação foi respondida.                               |

</div>

---
## Metodologia

O projeto seguiu uma abordagem estruturada que combinou Análise Exploratória de Dados (EDA), Processamento de Linguagem Natural (NLP) e Machine Learning. Inicialmente, foram analisados dados de pedidos, clientes, avaliações, pagamentos e entregas de um e-commerce para extrair padrões de comportamento e identificar fatores que influenciam a satisfação dos clientes. Em seguida, as avaliações textuais foram tratadas com técnicas de NLP e classificadas em sentimentos (positivo, negativo ou neutro) utilizando vetorização com TF-IDF e modelos como Random Forest, SVM e Logistic Regression.

O modelo final foi integrado em uma aplicação com Streamlit, que permite a visualização dos insights da análise exploratória e a predição de sentimentos em tempo real com base em novos comentários inseridos pelo usuário.

---


## Principais Insights

#### 📍 Análise Regional e Geográfica

- Em 2018, a região Sudeste liderou em número de pedidos, com destaque para SP, RJ e MG. A distribuição regional se manteve estável ao longo do ano, reforçando seu papel como polo logístico e consumidor.
- Estados do Norte e Nordeste têm menos pedidos e enfrentam maiores custos de frete e preços médios. Recomenda-se revisar estratégias logísticas e de precificação para melhorar a acessibilidade.

#### 📈 Comportamento de Compra ao Longo do Tempo

- Segunda-feira tem o maior número de pedidos; sexta-feira, embora tenha menos pedidos, possui o maior ticket médio. Isso sugere oportunidades de campanhas específicas para cada dia.
- Há queda significativa nos pedidos após o dia 28, sugerindo restrição orçamentária dos consumidores. Ofertas no fim do mês podem ajudar a manter o ritmo de vendas.
- A Black Friday gerou um pico expressivo de pedidos, confirmando sua importância estratégica. A recomendação é preparar campanhas e logística com antecedência para aproveitar o alto volume.

#### 🚚 Entregas e Avaliação

- A análise revela uma relação direta entre o tempo de entrega e a avaliação dos clientes. Estados com entregas mais rápidas, como São Paulo e Paraná, apresentam avaliações mais altas, enquanto regiões com maior tempo de entrega, como Roraima e Amazonas, registram notas mais baixas. Isso evidencia o impacto da eficiência logística na percepção de qualidade do serviço.
- Para melhorar a satisfação dos clientes, é recomendável investir na otimização das rotas de entrega, ampliar centros de distribuição em regiões críticas e aprimorar a comunicação sobre prazos. Essas ações podem reduzir o tempo de espera e, consequentemente, elevar as avaliações recebidas pelos pedidos.

#### 📈 Desempenho e Retenção

- Estados com entregas mais rápidas (ex: SP, PR) têm avaliações mais altas. Onde o tempo é maior (ex: RR, AM), as notas caem. Melhorias logísticas e comunicação clara são essenciais.
---

## **Conclusões**

**1. Importância da Eficiência Logística:** Regiões com entregas rápidas apresentam avaliações mais positivas, reforçando a necessidade de otimizar rotas e ampliar a infraestrutura logística para reduzir o tempo de entrega e aumentar a satisfação do cliente.

**2. Estratégias Regionais de Preço e Frete:** Diferenças significativas nos preços e custos de frete entre regiões indicam a necessidade de adotar políticas de precificação diferenciadas, considerando o perfil de consumo e os custos logísticos para melhorar a competitividade nas regiões Norte e Nordeste.

**3. Promoções e Campanhas Sazonais:** Eventos como Black Friday têm impacto direto no volume de pedidos. Além disso, dias da semana e final de mês apresentam variações no comportamento de compra que podem ser exploradas com promoções específicas para aumentar as vendas e o ticket médio.

**4. Foco na Retenção de Clientes:** Apesar do alto número de novos clientes, a baixa taxa de conversão em clientes recorrentes indica a necessidade de desenvolver programas de fidelização e melhorar a experiência pós-compra para reduzir o churn.

**5. Aproveitamento dos Dados para Decisões Estratégicas:** A análise integrada dos dados de pedidos, avaliações e logística permite identificar pontos fortes e gargalos operacionais, apoiando a tomada de decisões mais assertivas e orientadas por dados.

**6. Personalização de Ofertas:** Entender os padrões regionais e temporais de compra possibilita criar campanhas personalizadas que aumentem o engajamento do cliente e a eficiência das ações de marketing.

---

## **Aplicação para Predição de Satisfação**

Para tornar os resultados acessíveis e interativos, foi desenvolvida uma aplicação em Streamlit que permite a predição do sentimento das avaliações dos clientes. Nela, o usuário pode inserir um texto de avaliação e obter instantaneamente a classificação do sentimento como “Positivo”, “Negativo” ou “Neutro”. A aplicação também oferece visualizações da análise exploratória dos dados.

O link para acesso à aplicação está disponível [aqui](https://sentiment-analysis-olist.streamlit.app).

---
## Documentação Completa

Toda a análise detalhada, metodologia e resultados estão documentados no arquivo **TCC_Olist** que acompanha o projeto. Este arquivo contém a documentação completa e serve como suporte para consultas e aprofundamentos.
