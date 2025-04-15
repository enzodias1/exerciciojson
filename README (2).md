
# 💬 Extração de Informações Técnicas com Python e OpenRouter

Este é um projeto simples em Python que realiza **análise automatizada de relatórios técnicos**.  
A partir de um arquivo `.txt`, o programa utiliza uma API de linguagem natural para extrair informações estruturadas em formato JSON.

---

## 📌 Funcionalidades

- Leitura de relatório técnico salvo como `.txt`
- Extração automática dos seguintes dados:
  - ✅ Componentes mencionados
  - ✅ Especificações técnicas
  - ✅ Problemas relatados
  - ✅ Ações realizadas
  - ✅ Ações recomendadas
  - ✅ Observações ambíguas ou incompletas
- Impressão formatada da resposta no terminal

---

## 🚀 Como rodar o projeto localmente

### 1. Faça o download do projeto

📥 Clone ou baixe este repositório:  
[https://github.com/enzodias1/exerciciojson](https://github.com/enzodias1/exerciciojson)

Ou baixe diretamente em .zip:  
[Download do ZIP](https://github.com/enzodias1/exerciciojson/archive/refs/heads/main.zip)

---

### 2. Acesse a pasta do projeto no terminal

```bash
cd caminho/para/exerciciojson
```

---

### 3. Crie e ative um ambiente virtual (opcional, mas recomendado)

#### 🪟 Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 Linux / 🍎 macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Instale as dependências

```bash
pip install openai
```

---

### 5. Insira sua chave de API da OpenRouter

> Quando executar o script, ele solicitará sua chave de API (você pode obter gratuitamente em [https://openrouter.ai](https://openrouter.ai)).

---

### 6. Execute o script principal

```bash
python exerciciojson.py
```

---

### 7. Exemplo de arquivo `documento_tecnico.txt`

Certifique-se de ter um arquivo `.txt` com o conteúdo do relatório técnico.  
Este repositório já contém um exemplo pronto: `documento_tecnico.txt`.

📄 Trecho do exemplo:

```
RELATÓRIO DE MANUTENÇÃO - SISTEMA DE REFRIGERAÇÃO INDUSTRIAL
Data: 15/03/2025
Técnico: João Silva

EQUIPAMENTO: Chiller modelo CR-420, fabricante CoolTech
...
```

---

## 🧪 Exemplo de saída (resumo)

```json
{
  "componentes_mencionados": ["Chiller modelo CR-420", "compressor secundário", "..."],
  "problemas_relatados": ["Queda de eficiência de 30%", "Aumento no ruído", "..."],
  "acoes_realizadas": ["Substituição das válvulas", "..."],
  "acoes_recomendadas": ["Substituir compressor em 60 dias", "..."],
  "especificacoes_tecnicas": ["Modelo: CR-420", "Fabricante: CoolTech"],
  "observacoes_ambiguas_ou_incompletas": []
}
```

---

## 🛠 Tecnologias utilizadas

- Python 3
- Biblioteca `openai` (via OpenRouter)
- API de linguagem natural (LLM)
- Leitura e escrita de arquivos `.txt` e `.json`

---

## 👤 Autor

Desenvolvido por [@enzodias1](https://github.com/enzodias1)  
Sinta-se à vontade para abrir *issues* ou sugerir melhorias!
