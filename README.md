# 🐾 API Pet

Este projeto consiste em uma API desenvolvida em Flask para gerenciamento de informações relacionadas a pets. Ela permite cadastrar, atualizar, remover e visualizar informações sobre os pets, sendo ideal para sistemas de adoção, clínicas veterinárias ou qualquer aplicação que precise gerenciar dados de animais. 

## 🚀 Tecnologias Utilizadas

- 🐍 Python
- 🌐 Flask
- 🔄 Flask-CORS
- 🗄️ SQLAlchemy
- ✅ Pytest (para testes automatizados)
- 🧹 Pylint (para linting e boas práticas)

## 📦 Configuração do Ambiente

### ✅ Pré-requisitos
Certifique-se de ter o **Python** instalado na sua máquina. 

### 📥 Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/API-pet.git
   cd API-pet
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## ▶️ Como Executar

Execute o seguinte comando para iniciar a API:
```sh
python run.py
```
A API estará disponível em `http://127.0.0.1:5000/`.

## 🛠️ Estrutura do Projeto

| Pasta/Arquivo     | Descrição |
|-------------------|-----------|
| 📜 `run.py`       | Ponto de entrada da aplicação. |
| 📜 `requirements.txt` | Lista de dependências do projeto. |
| 🗄️ `storage.db`   | Banco de dados local (SQLite). |
| 📜 `.gitignore`   | Arquivos e pastas ignorados no repositório. |
| 📂 `tests/`       | Testes automatizados. |
| 📂 `models/`      | Modelos do banco de dados (ORM com SQLAlchemy). |
| 📂 `routes/`      | Definição das rotas e endpoints da API. |
| 📂 `services/`    | Lógica de negócios e manipulação de dados. |
| 📂 `schemas/`     | Validações e serialização de dados com Pydantic. |
| 📂 `config/`      | Configurações gerais do projeto. |
| 📂 `utils/`       | Funções auxiliares reutilizáveis. |

## 🧪 Testes
Para rodar os testes automatizados, utilize:
```sh
pytest
```
---


