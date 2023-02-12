FROM python:3.11.0-slim-bullseye

# configura variaveis de ambiente
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# configura diretorio de trabalho
WORKDIR /api_dbic

# Instalação de dependencias

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
