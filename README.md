# 📊 Motor de Análise Macroeconômica — Typebot + FastAPI + Groq (Llama 3.3)

<img width="671" height="311" alt="image" src="https://github.com/user-attachments/assets/97182659-4ac3-4492-8292-a09e4e26fe5d" />


## 📌 Visão Geral

O **Motor de Análise Macroeconômica** é uma solução baseada em Inteligência Artificial desenvolvida para interpretar cenários econômicos e gerar recomendações estratégicas sobre setores e oportunidades de investimento na B3.

A aplicação integra **Typebot**, **FastAPI** e **Groq Cloud**, permitindo que usuários enviem cenários econômicos em linguagem natural e recebam análises rápidas, objetivas e humanizadas diretamente pelo chat.

---

## 📸 Demonstração do Projeto

### ⚙️ Fluxo Construído no Typebot

<img width="1131" height="544" alt="Fluxo Typebot" src="https://github.com/user-attachments/assets/6cac4554-54c7-4d92-b3fb-05c629ef3e4c" />

### 🌐 Acesso ao Chat

🔗 https://typebot.co/macro-scenario-engine-ayae11f

---

## 🏗️ Arquitetura da Solução

```text
Usuário
   ↓
Typebot
   ↓
Webhook HTTP
   ↓
FastAPI
   ↓
Groq Cloud (Llama 3.3 70B)
   ↓
Análise Macroeconômica
   ↓
Resposta Personalizada
```

---

## 🧠 Prompt Utilizado

O sistema utiliza o seguinte prompt para interpretar cenários econômicos e gerar recomendações:

```python
prompt = f"""
Você é um especialista em análise macroeconômica para o mercado financeiro brasileiro.

Analise o seguinte cenário enviado pelo usuário e traga uma recomendação estratégica clara, humanizada e direta de quais setores ou investimentos na B3 podem se beneficiar ou exigir cautela.

Cenário: {texto_recebido}

Traga uma resposta direta, sem introduções longas, ideal para leitura em um chat de suporte.
"""
```

### Objetivos do Prompt

- Interpretar cenários macroeconômicos.
- Identificar oportunidades de investimento.
- Sugerir setores favorecidos pela conjuntura.
- Alertar sobre riscos e pontos de atenção.
- Gerar respostas objetivas e de fácil leitura.
<img width="685" height="366" alt="image" src="https://github.com/user-attachments/assets/d855e4d8-6e9e-4113-865a-b404e00edee8" />

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Typebot | Interface conversacional |
| FastAPI | API REST para processamento |
| Python | Lógica de negócio |
| Groq Cloud | Infraestrutura de IA |
| Llama 3.3 70B Versatile | Modelo de linguagem |
| HTML/CSS | Customização visual |
| JSON | Troca de dados entre sistemas |

---

## 📂 Estrutura do Projeto

📁 Projeto

- 📄 [`Documentacao_Macro_Scenario_Engine.pdf`](./Documentacao_Macro_Scenario_Engine.pdf)
- 📄 [`README.md`](./README.md)
- 📄 [`main.py`](./main.py)
- 📄 [`requirements.txt`](./requirements.txt)
- 📄 [`vercel.json`](./vercel.json)
---

## 🚀 Recursos Implementados

### ✅ Atendimento Personalizado

Solicita o nome do usuário e utiliza variáveis dinâmicas para personalizar toda a conversa.

### ✅ Integração com Inteligência Artificial

Conexão direta com o modelo Llama 3.3 hospedado na Groq Cloud.

### ✅ Análise Macroeconômica

Identificação automática de:

- Setores beneficiados;
- Setores com maior risco;
- Possíveis impactos econômicos;
- Oportunidades na B3.

### ✅ Tratamento de Erros

Implementação de blocos `try/except` para garantir estabilidade da aplicação.

### ✅ Interface Moderna

Customização completa do Typebot com visual Dark Mode inspirado em plataformas financeiras.

---

## ⚙️ Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/macro-scenario-engine.git
```

### 2. Acesse a pasta

```bash
cd macro-scenario-engine
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure sua chave Groq

```python
client = Groq(api_key="SUA_CHAVE_AQUI")
```

### 5. Execute a aplicação

```bash
uvicorn main:app --reload
```

Servidor disponível em:

```text
http://127.0.0.1:8000
```

---

## 📡 Endpoint Disponível

### POST /analisar

Recebe um cenário econômico e retorna uma análise estratégica.

### Exemplo de Entrada

```json
{
  "texto": "Dólar em forte alta e expectativa de aumento da inflação."
}
```

### Exemplo de Resposta

```json
{
  "analise": "Exportadoras e empresas ligadas a commodities podem se beneficiar. Setores dependentes de importação exigem cautela."
}
```

---

## 🎨 Customização Visual

### Paleta Utilizada

| Elemento | Cor |
|-----------|------|
| Fundo Principal | #0b1a24 |
| Balão do Bot | #ffffff |
| Texto do Bot | #1a202c |
| Balão do Usuário | #00b4d8 |
| Texto do Usuário | #ffffff |

---

## 📈 Possíveis Evoluções

- Integração com APIs de mercado em tempo real;
- Histórico de consultas;
- Dashboard analítico;
- Recomendações por perfil de investidor;
- Integração com dados da B3;
- Geração de relatórios em PDF.

---

## 👩‍💻 Desenvolvedora

**Patricia Oliveira**

Analista e Desenvolvedora de Software.

### LinkedIn

https://www.linkedin.com/in/savarezi/

---

## 📄 Licença

Projeto desenvolvido para fins educacionais, demonstração técnica e portfólio profissional.
