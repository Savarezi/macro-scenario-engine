import os  # <-- Adicionado para o Python entender o os.getenv
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv(dotenv_path="./.env")

# Inicializa a nossa API
app = FastAPI()

# Configura o cliente do Groq buscando a chave de forma escondida do arquivo .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # <-- Corrigido e fechado direitinho!

# Criamos o modelo de dados que o Typebot vai enviar
class CenarioInput(BaseModel):
    cenario: str

# Criamos a nossa "porta" de entrada (endpoint)
@app.post("/analisar")
def analisar_cenario(dados: CenarioInput):
    texto_recebido = dados.cenario
    
    # Criamos o prompt para a Inteligência Artificial do Groq ler o cenário econômico
    prompt = f"""
    Você é um especialista em análise macroeconômica para o mercado financeiro brasileiro.
    Analise o seguinte cenário enviado pelo usuário e traga uma recomendação estratégica clara, humanizada e direta de quais setores ou investimentos na B3 podem se beneficiar ou exigir cautela.
    
    Cenário: {texto_recebido}
    
    Traga uma resposta direta, sem introduções longas, ideal para leitura em um chat de suporte.
    """
    
    try:
        # Chamamos o modelo Llama 3.3 estável e atualizado do Groq
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Nome oficial e ativo do modelo no Groq
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        # Pegamos o texto gerado pela IA
        analise_real = completion.choices[0].message.content
        
    except Exception as e:
        # Caso dê algum erro com a chave ou conexão, ele avisa sem travar a API
        analise_real = f"Desculpe, tive um problema ao conectar com o motor de análise. Erro: {str(e)}"

    # Devolvemos a análise real gerada pelo Groq para o Typebot receber
    return {
        "status": "sucesso",
        "mensagem": analise_real
    }