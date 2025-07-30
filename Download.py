import gdown
import os

# Pasta de destino
os.makedirs("nllb-200-distilled-600M", exist_ok=True)

# Lista de arquivos com IDs e nomes desejados
files = [
    {
        "id": "1XXWHjrQO3KKLaDwrl3PWB125tDGLIx12",
        "output": "nllb-200-distilled-600M/config.json"
    },
    {
        "id": "1DJaU7qHDjPsWjk4uzQ8o_iGf0f_GQvL1",
        "output": "nllb-200-distilled-600M/model.bin"
    },
    {
        "id": "15qVODozlECPx0TFkHbJpPs16IN7qmqsG",
        "output": "nllb-200-distilled-600M/shared_vocabulary.json"
    }
]

# Baixar cada arquivo
for file in files:
    url = f"https://drive.google.com/uc?id={file['id']}"
    print(f"⬇️ Baixando {file['output']} ...")
    gdown.download(url, file['output'], quiet=False)

print("✅ Download concluído.")
