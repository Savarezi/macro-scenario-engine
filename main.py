import os
import httpx  # <-- 1. IMPORTANTE: Adicionamos o httpx
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from mangum import Mangum

# Carrega as variáveis do arquivo .env (localmente)
load_dotenv(dotenv_path="./.env")

app = FastAPI()

# <-- 2. CORREÇÃO CRÍTICA PARA A VERCEL: 
# Criamos um cliente HTTP que fecha a conexão após o uso, evitando o Connection Error
http_client = httpx.Client(transport=httpx.HTTPTransport(local_address="0.0.0.0"))
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    http_client=http_client  # Passamos o cliente customizado para a Groq
)

handler = Mangum(app)

class CenarioInput(BaseModel):
    cenario: str

@app.post("/analisar")
def analisar_cenario(dados: CenarioInput):
    texto_recebido = dados.cenario
    
    prompt = f"""
    Você é um especialista em análise macroeconômica para o mercado financeiro brasileiro.
    Analise o seguinte cenário enviado pelo usuário e traga uma recomendação estratégica clara, humanizada e direta de quais setores ou investimentos na B3 podem se beneficiar ou exigir cautela.
    
    Cenário: {texto_recebido}
    
    Traga uma resposta direta, sem introduções longas, ideal para leitura em um chat de suporte.
    """
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        analise_real = completion.choices[0].message.content
        
    except Exception as e:
        analise_real = f"Desculpe, tive um problema ao conectar com o motor de análise. Erro: {str(e)}"

    return {
        "status": "sucesso",
        "mensagem": analise_real
    }