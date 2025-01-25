# Test Adweb

## Requisitos

- Python 3.x
- Node.js (com npm ou yarn)
- Django
- Vue.js + Vite
- SQlite

## Estrutura do Projeto

/backend # Contém o backend em Django 
/frontend # Contém o frontend em Vue.js com Vite


## Instruções de Execução

### Backend (Django)

1. **Instale as dependências do backend:**

   Se você ainda não tiver o `virtualenv`, instale-o com:

   ```bash
   pip install virtualenv
   ```

Em seguida, crie e ative um ambiente virtual:

```bash
virtualenv venv
source venv/bin/activate  # Para sistemas Unix
venv\Scripts\activate     # Para Windows
```
Agora instale as dependências do Django e outras necessárias:

```bash
pip install -r backend/requirements.txt
```

2. **Configuração do Banco de Dados:**

Realize as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```
Inicie o servidor Django:

```bash
python manage.py runserver
```

### Frontend (Vue)

1 **Instale as dependências do frontend:**
No diretório frontend, instale as dependências:

```bash
cd frontend
npm install  # ou yarn install, se você usar yarn
```

3 **Configure variáveis de ambiente:**
Copie as informações do arquivo .env.example para um arquivo chamado .env

```bash
cat .env.example > .env
```

Com as dependências instaladas, inicie o servidor de desenvolvimento do Vite:

```bash
npm run dev  # ou yarn dev
```

3 **Inicie o servidor de desenvolvimento:**

Com as dependências instaladas, inicie o servidor de desenvolvimento do Vite:

```bash
npm run dev  # ou yarn dev
```