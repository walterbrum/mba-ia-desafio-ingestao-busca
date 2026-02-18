# Desafio MBA Engenharia de Software com IA - Full Cycle

Projeto de ingestão e busca semântica de documentos PDF utilizando LangChain, PostgreSQL com pgVector.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.12+
- **Framework**: LangChain
- **Banco de Dados**: PostgreSQL + pgVector
- **Containerização**: Docker & Docker Compose
- **LLM**: OpenAI GPT-5-nano
- **Embeddings**: OpenAI text-embedding-3-small

## Pré-requisitos

- Python 3.12 ou superior
- Docker e Docker Compose
- Conta OpenAI com API Key

## Configuração do Ambiente

### 1. Clone o repositório e navegue até a pasta
```bash
git clone <seu-repositorio>
cd mba-ia-desafio-ingestao-busca
```

### 2. Crie e ative o ambiente virtual Python
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Copie o arquivo `.env.example` para `.env` e configure suas variáveis:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:
```env
OPENAI_API_KEY=sua_api_key_aqui
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/rag
PG_VECTOR_COLLECTION_NAME=gpt5_collection
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
PDF_PATH=./document.pdf
```

## Como testar o projeto

Execute os comandos:

### 1. Iniciar o banco de dados
```bash
docker compose up -d
```

### 2. Executar a ingestão do PDF
```bash
python3 src/ingest.py
```

### 3. Iniciar o chat interativo
```bash
python3 src/chat.py
```

Pronto! O projeto estará pronto para testes.