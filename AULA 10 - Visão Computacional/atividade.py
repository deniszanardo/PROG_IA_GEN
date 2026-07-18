import streamlit as st
import nltk


#Exemplo da aula
# texto = "O serviço foi ruim"

# if "ruim" in texto:
#     print("Sentimento negativo")
# else:
#     print("Sentimento positivo")
    
#     # SIMLULAÇÃO DE ANALISE DE SENTIMENTO BASICA
    
#     # COM NLTK
    
# from nltk.tokenize import word_tokenize
# nltk.download('punkt_tab') # Recurso necessário para tokenização

# frase = "Instalar o NLTK é muito fácil!"
# palavras = nltk.word_tokenize(frase)

# texto = "IA está transformando o mundo"
# print(word_tokenize(texto))




# # ATIVIDADE 1

# PROBLEMÁTICA:

# Uma empresa recebe centenas de mensagens de clientes todos os dias. Ela precisa separar automaticamente o texto em palavras para facilitar a análise e organização das informações.

# TAREFA:

# Use tokenização para separar um texto em palavras individuais.
import nltk
from nltk.tokenize import word_tokenize

# Baixa os recursos necessários para a tokenização (apenas na primeira execução)
nltk.download('punkt')

# Exemplo de uma mensagem real de cliente
mensagem_cliente = "Olá! Gostaria de saber se o meu pedido #1024 já foi enviado? Aguardo retorno, obrigado."

# Aplicando a tokenização por palavras
palavras_tokenizadas = word_tokenize(mensagem_cliente, language='portuguese')

# Visualizando o resultado
print(palavras_tokenizadas)












# ---
# #_____________________________________________________________________________
# ATIVIDADE 2

# PROBLEMÁTICA:

# Um sistema de análise de dados precisa identificar quais palavras aparecem com mais frequência em avaliações de clientes para entender padrões de comportamento.

# TAREFA:

# Conte a frequência das palavras em um texto simples.

# ---
#_____________________________________________________________________________
# ATIVIDADE 3

# PROBLEMÁTICA:

# Uma empresa de atendimento quer detectar automaticamente mensagens com palavras negativas para priorizar o suporte ao cliente.

# TAREFA:

# Crie uma regra condicional para identificar palavras como “ruim”, “péssimo” ou “erro”.

# ---
#_____________________________________________________________________________
# ATIVIDADE 4

# PROBLEMÁTICA:

# Em uma análise de textos, palavras como “de”, “a”, “o”, “para” não ajudam na interpretação e precisam ser removidas para melhorar a análise.

# TAREFA:

# Remova stopwords de um texto em português.

# ---

#_____________________________________________________________________________# ATIVIDADE 5

# PROBLEMÁTICA:

# Uma equipe de marketing quer entender rapidamente se comentários de clientes são positivos ou negativos com base em palavras-chave.

# TAREFA:

# Crie um sistema simples de classificação de sentimento usando condicionais.

# ---

#_____________________________________________________________________________# ATIVIDADE 6

# PROBLEMÁTICA:

# Um chatbot precisa identificar palavras-chave dentro de uma frase para direcionar o cliente para o setor correto.

# TAREFA:

# Crie uma lógica que detecte palavras como “cancelar”, “erro” e “pagamento”.

# ---

#_____________________________________________________________________________# ATIVIDADE 7

# PROBLEMÁTICA:

# Um analista quer saber quais palavras mais aparecem em reclamações de clientes para melhorar o produto.

# TAREFA:

# Crie um código que identifique as palavras mais frequentes em um texto de reclamação.

# ---

#_____________________________________________________________________________# ATIVIDADE 8

# PROBLEMÁTICA:

# Uma empresa quer classificar mensagens automaticamente em “suporte técnico” ou “financeiro” com base em palavras específicas.

# TAREFA:

# Crie regras condicionais simples para classificar mensagens.

# ---

#_____________________________________________________________________________# ATIVIDADE 9

# PROBLEMÁTICA:

# Um sistema de IA precisa limpar textos removendo pontuação e deixando apenas palavras relevantes para análise.

# TAREFA:

# Remova pontuação e normalize um texto (letras minúsculas).

# ---

#_____________________________________________________________________________# ATIVIDADE 10

# PROBLEMÁTICA:

# Uma empresa quer entender o conteúdo de avaliações de produtos para identificar se os clientes estão satisfeitos ou insatisfeitos sem leitura manual.

# TAREFA:

# Combine tokenização + condicional para analisar sentimento básico de um texto