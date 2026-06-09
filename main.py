import os
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from mangum import Mangum

# Tenta carregar o arquivo .env apenas se ele existir localmente (Codespaces)
if os.path.exists("./.env"):
    load_dotenv(dotenv_path="./.env")

app = FastAPI()

# Pega a chave direto do ambiente do servidor (Vercel ou Codespaces)
api_key = os.environ.get("GROQ_API_KEY")

# Inicializa o cliente padrão da Groq sem forçar o httpx antigo
client = Groq(api_key=api_key)

handler = Mangum(app)

class CenarioInput(BaseModel):
    cenario: str

@app.post("/analisar")
def analisar_cenario(dados: CenarioInput):
    texto_recebido = dados.cenario
    
    # Validação de segurança: se a chave sumir por algum motivo, avisa no erro
    if not os.environ.get("GROQ_API_KEY"):
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