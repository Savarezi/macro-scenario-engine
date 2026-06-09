import os
import requests  # <-- Mudamos para requisição HTTP direta, que a Vercel aceita sem travar
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from mangum import Mangum

if os.path.exists("./.env"):
    load_dotenv(dotenv_path="./.env")

app = FastAPI()
handler = Mangum(app)

class CenarioInput(BaseModel):
    cenario: str

@app.post("/analisar")
def analisar_cenario(dados: CenarioInput):
    texto_recebido = dados.cenario
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        return {
            "status": "erro",
            "mensagem": "Erro interno: A chave GROQ_API_KEY não foi encontrada nas variáveis da Vercel."
        }
    
    prompt = f"""
    Você é um especialista em análise macroeconômica para o mercado financeiro brasileiro.
    Analise o seguinte cenário enviado pelo usuário e traga uma recomendação estratégica clara, humanizada e direta de quais setores ou investimentos na B3 podem se beneficiar ou exigir cautela.
    
    Cenário: {texto_recebido}
    
    Traga uma resposta direta, sem introduções longas, ideal para leitura em um chat de suporte.
    """
    
    # Conversando diretamente com a API da Groq via HTTP puro
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=8)
        
        if response.status_code == 200:
            dados_resposta = response.json()
            analise_real = dados_resposta["choices"][0]["message"]["content"]
        else:
            analise_real = f"Desculpe, a Groq retornou um erro código {response.status_code}: {response.text}"
            
    except Exception as e:
        analise_real = f"Desculpe, tive um problema ao conectar com o motor de análise. Erro: {str(e)}"

    return {
        "status": "sucesso",
        "mensagem": analise_real
    }