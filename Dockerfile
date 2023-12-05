# Use uma imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt /app/

# Instale as dependências do Django
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código-fonte para o diretório de trabalho
COPY . /app/

# Exponha a porta em que a aplicação estará rodando
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
