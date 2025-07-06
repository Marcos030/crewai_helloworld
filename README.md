# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: README do projeto CrewAI Hello World
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

# CrewAI Hello World

Este projeto demonstra o uso básico do CrewAI com exemplos práticos de agentes e tarefas organizados.

## 📋 Estrutura do Projeto

```
helloworld/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── support_agent.py
│   │   └── quality_assurance_agent.py
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── inquiry_resolution_task.py
│   │   └── quality_assurance_task.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── main.py
│   ├── using_memory.py
│   └── event_planning.py
├── .env
├── env.example
├── setup_serper.py
├── requirements.txt
└── README.md
```

## 🚀 Instalação

### 1. Configurar Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 2. Instalar Dependências

```bash
# Instalar dependências básicas
pip install -r requirements.txt

# Instalar crewai-tools (sem dependências problemáticas)
pip install crewai-tools --no-deps
```

### 3. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `env.example`:

```env
# OpenAI API Key (obrigatório)
OPENAI_API_KEY=sua_chave_api_aqui
OPENAI_MODEL_NAME=gpt-4o-mini

# Serper API Key (opcional - para busca na web)
SERPER_API_KEY=sua_serper_api_key_aqui

# Configurações do CrewAI
CREWAI_VERBOSE=True
CREWAI_DEBUG=False

# Configurações da aplicação
APP_ENV=development
APP_DEBUG=True
```

## 🔍 Configuração da Serper API (Busca na Web)

Para melhorar a funcionalidade de busca na web dos agentes, configure a Serper API:

### Opção 1: Script Automático

```bash
python setup_serper.py
```

O script irá:
- Abrir o site da Serper no navegador
- Guiar você através do processo de registro
- Configurar automaticamente o arquivo `.env`

### Opção 2: Configuração Manual

1. **Acesse**: https://serper.dev/
2. **Crie uma conta gratuita**
3. **Obtenha sua API Key**
4. **Adicione ao arquivo `.env`**:
   ```env
   SERPER_API_KEY=sua_chave_aqui
   ```

### Testar a Configuração

```bash
python setup_serper.py
# Escolha opção 2: "Testar configuração atual"
```

## 📖 Exemplos

### Exemplo Básico (`main.py`)

Demonstração simples de agentes e tarefas sem memória:

```bash
python src/main.py
```

### Exemplo com Memória (`using_memory.py`)

Demonstração avançada com memória habilitada:

```bash
python src/using_memory.py
```

### Exemplo de Planejamento de Eventos (`event_planning.py`)

Sistema completo de planejamento de eventos com múltiplos agentes:

```bash
python src/event_planning.py
```

## 🔧 Configuração

### Agentes

- **SupportAgent**: Agente de suporte ao cliente
- **QualityAssuranceAgent**: Agente de garantia de qualidade
- **VenueCoordinator**: Coordenador de local para eventos
- **LogisticsManager**: Gerente de logística para eventos
- **MarketingAgent**: Agente de marketing e comunicação

### Tarefas

- **InquiryResolutionTask**: Resolução de consultas de clientes
- **QualityAssuranceTask**: Revisão de qualidade das respostas
- **VenueTask**: Busca e seleção de locais para eventos
- **LogisticsTask**: Coordenação de logística de eventos
- **MarketingTask**: Estratégias de marketing para eventos

## 🧠 Funcionalidades de Memória

O exemplo `using_memory.py` demonstra:

- **Short Term Memory**: Memória de curto prazo para sessões
- **Long Term Memory**: Memória de longo prazo persistente
- **Entity Memory**: Memória de entidades e relacionamentos

## 🌐 Ferramentas Externas

### SerperDevTool
- **Função**: Busca na web
- **Configuração**: Requer SERPER_API_KEY
- **Uso**: Agentes podem buscar informações atualizadas

### ScrapeWebsiteTool
- **Função**: Extração de conteúdo de websites
- **Configuração**: Funciona com SerperDevTool
- **Uso**: Agentes podem ler conteúdo de páginas web

## ⚠️ Notas Importantes

### Problemas de Compilação

Se encontrar erros relacionados ao Microsoft Visual C++ Build Tools:

1. **Solução Recomendada**: Use `pip install crewai-tools --no-deps`
2. **Alternativa**: Instale o Microsoft Visual C++ Build Tools se necessário

### Dependências Opcionais

- `embedchain`: Requer Microsoft Visual C++ Build Tools
- Ferramentas externas: Podem requerer dependências adicionais

### Configuração de APIs

- **OpenAI API**: Obrigatória para funcionamento básico
- **Serper API**: Opcional, melhora busca na web
- **Sem Serper API**: Agentes funcionam com conhecimento interno

## 🎯 Uso

1. **Configure sua API Key** no arquivo `.env`
2. **Configure Serper API** (opcional) para busca na web
3. **Execute o exemplo básico**: `python src/main.py`
4. **Teste com memória**: `python src/using_memory.py`
5. **Teste planejamento de eventos**: `python src/event_planning.py`

## 📝 Logs de Código Gerado por IA

Este projeto segue as regras de logging de código gerado por IA:

```python
# AI_GENERATED_CODE_START
# [AI Generated] Data: DD/MM/YYYY
# Descrição: Descrição da alteração
# Gerado por: Cursor AI
# Versão: Versão das dependências
# ... código ...
# AI_GENERATED_CODE_END
```

## 🤝 Contribuição

1. Mantenha a estrutura organizada em pastas
2. Siga os padrões de logging de código gerado por IA
3. Teste os exemplos antes de fazer alterações

## 📄 Licença

Este projeto é de uso educacional e demonstrativo.
# AI_GENERATED_CODE_END 