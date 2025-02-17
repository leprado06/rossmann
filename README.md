# Previsão de faturamento Rossmann (Rede de farmacias na Europa)


## Descrição

A Rossmann é uma das maiores redes de drogarias da Europa. Nesse contexto de negócio, O CFO da empresa solicitou uma previsão das vendas das lojas para as próximas 6 semanas, o problema que o CFO está enfrentando é que atualmente as previsões de vendas são feitas pelos próprios gerentes de loja, o que resulta em divergências e dados inconfiáveis. Por isso o CFO quer ter uma noção clara e assertiva do orçamento disponível para planejar as reformas das lojas da Rossmann.

## Objetivo

Gerar predições de vendas por loja com eficiencia e de forma assertiva

## Planejamento da solução

Meu planejamento é aplicar o método cíclico CROSS-INDUSTRY PROCESS-DATA SCIENCE (CRISP-DS) que tem o objetivo de terminar o primeiro ciclo end-to-end de maneira rápida com os dados disponíveis para mapear todos os problemas que podem estar em diferentes etapas do projeto e entregar valor rápido para os stakeholders.


## Dicionário dos Dados

| Coluna	| Descrição |
| --------|-----------|
| Id | Identificador que representa um (Store, Date) duplo dentro do conjunto de teste |
| Store | Identificador exclusivo para cada loja |
| Sales | Volume de vendas de um determinado dia |
| Customers | Número de clientes em um determinado dia |
| Open | Indicador para saber se a loja estava aberta: 0 = fechada, 1 = aberta |
| StateHoliday | Indica um feriado estadual. Normalmente, todas as lojas, com poucas exceções, fecham em feriados estaduais. a = feriado, b = Páscoa, c = Natal, 0 = Nenhum |
| SchoolHoliday | Indica um feriado escolar |
| StoreType | Modelos de loja: a, b, c, d |
| Assortment | Descreve o sortimento da loja: a = básico, b = extra, c = estendido |
| CompetitionDistance | Distância em metros até a loja concorrente mais próxima |
| CompetitionOpenSince[Month/Year] | Ano e mês aproximados da abertura do concorrente mais próximo | 
| Promo | Indica se a loja está realizando uma promoção naquele dia |
| Promo2 | Indica uma promoção contínua e consecutiva para algumas lojas: 0 = loja não está participando, 1 = loja está participando |
| Promo2Since[Year/Week] | Ano e semana do calendário em que a loja começou a participar do Promo2 |
| PromoInterval | Descreve os intervalos consecutivos em que o Promo2 é iniciado, nomeando os meses em que a promoção é iniciada novamente. Por exemplo, "fev, mai, ago, nov" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para aquela loja|

## Ferramentas utilizadas

### Análise de Dados
Python 3.9.19: Linguagem de programação utilizada para desenvolvimento de scripts e análise de dados.
Estatística Descritiva: Método utilizado para resumir e interpretar os dados.
Exploratory Data Analysis (EDA): Processo de investigação inicial dos dados para descobrir padrões, entender melhor o negócio e testar hipóteses.

## Desenvolvimento
### Estratégia da solução
Para o objetivo de ensaiar os algoritmos de Machine Learning, escreverei os códigos utilizando a linguagem Python. Para treinar cada um dos algoritmos, vou variar seus principais parâmetros de ajuste afim de evitar o underfitting ou overfitting e elevar a métrica final. O conjunto de valores que fizerem os algoritmos alcançarem a melhor performance, serão aqueles escolhidos para o treinamento final do algoritmo.

### Modelagem de Dados e treinamento de algoritmos

Scikit-learn: Biblioteca de machine learning em Python usada para pré processamento de dados e implementação de algoritmos de aprendizado supervisionado e não supervisionado.
Boruta: Ferramenta utilizada para seleção de features, ajudando a identificar as variáveis mais importantes para modelos preditivos.
Random Forest Regressor: Implementação avançada do algoritmo RandomForest, otimizada para problemas de regressão, conhecida pela alta precisão e eficiência.
Random Search: Técnica usada para otimizar hiperparâmetros em modelos de machine learning através da geração aleatória de combinações.

## Top 3 Insights

### Insight 1


### Insight 2


### Insight 3


## Conclusão


## Próximos passos
