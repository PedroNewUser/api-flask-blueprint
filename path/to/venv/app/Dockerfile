# Usa a imagem base oficial do Python 3.8 com um ambiente mais enxuto
FROM python:3.8-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho no container
COPY requirements.txt requirements.txt

# Instala as dependências do Python especificadas no requirements.txt
# --no-cache-dir evita o armazenamento em cache dos pacotes para reduzir o tamanho da imagem
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório atual para o diretório de trabalho no container
COPY . /app

# Expõe a porta 5000 para permitir o acesso externo ao serviço Flask
EXPOSE 5000

# Define a variável de ambiente FLASK_RUN_HOST para que o Flask escute em todas as interfaces de rede
ENV FLASK_RUN_HOST=0.0.0.0

# Comando padrão para iniciar o aplicativo Flask
CMD ["flask", "run"]
