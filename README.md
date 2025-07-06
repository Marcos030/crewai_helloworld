# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Documentação do projeto CrewAI Hello World
# Gerado por: Cursor AI

# CrewAI Hello World

Este é um projeto de exemplo utilizando CrewAI para demonstrar a criação de agentes de IA colaborativos.

## Estrutura do Projeto

```
helloworld/
├── src/
│   ├── agents/
│   │   └── __init__.py
│   ├── tasks/
│   │   └── __init__.py
│   ├── utils/
│   │   └── __init__.py
│   └── main.py
├── config/
│   └── settings.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Marcos030/crewai_helloworld.git
cd crewai_helloworld
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas chaves de API
```

## Uso

Execute o projeto principal:
```bash
python src/main.py
```

## Configuração

Certifique-se de configurar as seguintes variáveis de ambiente no arquivo `.env`:

- `OPENAI_API_KEY`: Sua chave de API da OpenAI
- `OPENAI_MODEL_NAME`: Modelo a ser utilizado (padrão: gpt-3.5-turbo)

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT.
# AI_GENERATED_CODE_END 