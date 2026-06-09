# 📊 Motor de Análise Macroeconômica — Integração Typebot + FastAPI + Groq (Llama 3.3)

Este repositório contém a documentação e os arquivos de configuração para o **Motor de Análise Macroeconômica**, uma solução inteligente desenvolvida para automatizar e enriquecer o atendimento ao cliente focado no mercado financeiro e na B3.

O sistema recebe um cenário econômico enviado pelo usuário (ex: "dólar em alta", "queda da Selic"), processa essa informação através de um modelo avançado de Inteligência Artificial e devolve uma recomendação estratégica humanizada e setorial direto no chat.

---

## 📸 Demonstração do Projeto

### ⚙️ Fluxo de Construção no Typebot
<img width="1036" height="540" alt="image" src="https://github.com/user-attachments/assets/a193dcff-a289-4088-a415-dd68a36b8ffb" />



### 🌐 Link do Chat
[Clique aqui para acessar o Motor de Análise Macroeconômica](https://typebot.co/macro-scenario-engine-ayae11f)

---

## 🛠️ Tecnologias e Stack Utilizadas

*   **Front-end / Interface:** [Typebot](https://typebot.io) — Construção da jornada do usuário, captura de dados personalizados (como o nome do usuário) e exibição das análises.
*   **Back-end / API:** [FastAPI (Python)](https://fastapi.tiangolo.com) — Criação do endpoint seguro `/analisar` para receber os dados do Typebot e gerenciar as chamadas de IA.
*   **Motor de IA:** [Groq Cloud API](https://groq.com) — Processamento de linguagem natural utilizando o modelo estável e ultraveloz **`llama-3.3-70b-versatile`**.
*   **Estilização:** CSS Customizado para uma experiência de interface no modo escuro (*Dark Mode*), alinhada com a identidade visual de mercado corporativo e financeiro.

---

## 🧠 Recursos Implementados

1.  **Acolhimento Humanizado:** O bot inicia solicitando o nome do usuário, salvando-o dinamicamente em variáveis (`{nome}`) para personalizar todas as mensagens seguintes da conversa.
2.  **Análise Macroeconômica em Tempo Real:** Conexão direta com o modelo Llama 3.3 via Groq, fornecendo insights detalhados sobre setores beneficiados (commodities, exportadoras) e setores que exigem cautela (varejo, empresas endividadas em moeda estrangeira).
3.  **Tratamento de Erros Resiliente (`Try/Except`):** Caso ocorra qualquer instabilidade de conexão ou expiração de modelos, a API captura o erro amigavelmente e evita o travamento do fluxo do cliente.
4.  **Interface Limpa:** Aplicação de CSS avançado para remover caixas duplicadas (*containers*) do Typebot, deixando os balões flutuantes, legíveis e com alto contraste.

---

## 🚀 Como Executar o Back-end

1.  **Instale as dependências necessárias:**
```bash
    pip install fastapi uvicorn groq pydantic
    ```

2.  **Configure sua Chave de API:**
    No arquivo principal do servidor, substitua a variável correspondente pela sua credencial gerada no painel da Groq:
```python
    client = Groq(api_key="SUA_CHAVE_AQUI")
    ```

3.  **Inicie o servidor localmente:**
```bash
    uvicorn main:app --reload
    ```
    O servidor estará rodando e pronto para receber requisições HTTP POST do seu Typebot no endereço `http://127.0.0.1:8000/analisar`.

---

## 🎨 Paleta de Cores Aplicada (CSS)

O chat foi customizado utilizando CSS injetado nas configurações avançadas do Typebot, trazendo as seguintes especificações:
*   **Fundo do Chat:** Azul Escuro Corporativo (`#0b1a24`)
*   **Balões do Robô:** Fundo Branco Puro (`#ffffff`) com Fonte Escura (`#1a202c`) para máxima legibilidade.
*   **Balões do Usuário:** Azul/Verde Piscina Vibrante (`#00b4d8`) com texto em branco, combinando com gráficos de alta de mercado.

```
---
## Contato

Desenvolvido por Patricia. Conecte-se comigo profissionalmente:

* [LinkedIn](https://www.linkedin.com/in/savarezi/)



