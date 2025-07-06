# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Documentação dos exemplos do projeto CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

# Exemplos do Projeto CrewAI

## 📄 `main.py` - Exemplo Básico
**Descrição:** Exemplo básico de uso do CrewAI com pesquisa e escrita

**Funcionalidades:**
- ✅ Agente Pesquisador
- ✅ Agente Escritor
- ✅ Tarefa de Pesquisa
- ✅ Tarefa de Escrita
- ❌ Sem memória
- ❌ Sem ferramentas externas

**Execução:**
```bash
python src/main.py
```

**Resultado:** Artigo sobre "Oportunidades de negócios no Brasil com IA"

---

## 📄 `using_memory.py` - Exemplo com Memória
**Descrição:** Exemplo avançado com memória e ferramentas de scraping

**Funcionalidades:**
- ✅ Agente de Suporte
- ✅ Agente de Qualidade
- ✅ Tarefa de Resolução de Consultas
- ✅ Tarefa de Revisão de Qualidade
- ✅ **Memória habilitada**
- ✅ **Ferramentas de scraping** (crewai_tools)

**Execução:**
```bash
python src/using_memory.py
```

**Resultado:** Resposta de suporte sobre como adicionar memória ao CrewAI

---

## 🔧 Diferenças Principais

| Característica | main.py | using_memory.py |
|----------------|---------|-----------------|
| **Memória** | ❌ | ✅ |
| **Ferramentas** | ❌ | ✅ (ScrapeWebsiteTool) |
| **Contexto** | Pesquisa/Escrita | Suporte ao Cliente |
| **Complexidade** | Básico | Avançado |
| **Agentes** | 2 | 2 |
| **Tarefas** | 2 | 2 |

## 🚀 Como Escolher

### Use `main.py` se:
- Está começando com CrewAI
- Quer um exemplo simples e direto
- Precisa de pesquisa e escrita básica
- Não precisa de memória ou ferramentas

### Use `using_memory.py` se:
- Quer ver memória em ação
- Precisa de ferramentas externas
- Quer um exemplo de suporte ao cliente
- Está familiarizado com CrewAI

## 📁 Estrutura Organizada

Ambos os exemplos seguem a estrutura organizada:

```
src/
├── agents/
│   ├── researcher.py
│   ├── writer.py
│   ├── support_agent.py
│   └── quality_assurance_agent.py
├── tasks/
│   ├── research_task.py
│   ├── writing_task.py
│   ├── inquiry_resolution_task.py
│   └── quality_assurance_task.py
├── utils/
│   └── config.py
├── main.py
└── using_memory.py
```

## 🔄 Próximos Passos

1. **Execute ambos os exemplos** para ver as diferenças
2. **Modifique os inputs** para testar diferentes cenários
3. **Adicione novos agentes** seguindo o padrão
4. **Experimente com memória** em outros contextos
# AI_GENERATED_CODE_END 