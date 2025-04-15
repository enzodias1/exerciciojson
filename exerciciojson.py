#!/usr/bin/env python
# coding: utf-8

# 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

# In[6]:


# 🔧 Instalar a biblioteca openai (é compatível com a API do OpenRouter)


# In[7]:


# 📦 Configurar API Key da OpenRouter
import openai
import getpass

api_key = getpass.getpass("Cole sua chave da OpenRouter API (começa com org-): ")

openai.api_key = api_key
openai.api_base = "https://openrouter.ai/api/v1"


# In[8]:


# 📤 Upload do documento técnico
nome_arquivo = 'documento_tecnico.txt'  # Altere conforme necessário

with open(nome_arquivo, 'r', encoding='utf-8') as f:
    texto_tecnico = f.read()


# In[13]:


from openai import OpenAI
import json

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def extrair_info(texto):
    prompt = f"""
Você é um assistente técnico. Extraia do seguinte texto técnico:

- Componentes mencionados
- Especificações técnicas
- Problemas relatados
- Ações realizadas (ações que já foram executadas)
- Ações recomendadas (ações que ainda precisam ser feitas)
- Informações ambíguas ou incompletas

Organize as informações no seguinte formato JSON:
{{
  "componentes_mencionados": [...],
  "especificacoes_tecnicas": [...],
  "problemas_relatados": [...],
  "acoes_realizadas": [...],
  "acoes_recomendadas": [...],
  "observacoes_ambiguas_ou_incompletas": [...]
}}

Texto técnico:
\"\"\"{texto}\"\"\"
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("⚠️ O modelo retornou um conteúdo fora do padrão JSON. Exibindo como texto:")
        return content



# In[14]:


# 🚀 Executar extração e visualizar resultado
resultado = extrair_info(texto_tecnico)

import pprint
pprint.pprint(resultado)

