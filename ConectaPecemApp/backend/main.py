import os
import shutil
import whisper # A biblioteca da OpenAI rodando localmente
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. Configuração de CORS (Fundamental para o React acessar o Python)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite todas as origens para facilitar o desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Carregamento do Modelo (Executa apenas uma vez na inicialização)
print("📥 Carregando modelo Whisper...")

model = whisper.load_model("small")
print("✅ Modelo carregado e pronto para ouvir!")

@app.post("/api/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Recebe áudio de qualquer dispositivo, salva temporariamente 
    e transcreve usando a IA local.
    """
    print(f"Recebendo áudio: {file.filename}")
    
    temp_filename = f"temp_{file.filename}"
    
    try:
        # Salva o arquivo no disco
        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Transcreve
        # O Whisper detecta automaticamente se é webm, mp4, wav, etc.
        result = model.transcribe(temp_filename, language="pt")
        text = result["text"].strip()
        
        print(f"Transcrição: {text}")
        return {"text": text}
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
        
    finally:
        # Limpeza
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

if __name__ == "__main__":
    import uvicorn
    print("Iniciando servidor na porta 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
