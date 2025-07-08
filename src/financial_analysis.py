# =============================
# 1. Imports e controle de warnings
# =============================
import warnings
warnings.filterwarnings('ignore')

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from langchain_openai import ChatOpenAI
from IPython.display import Markdown
from src.utils.config import Config

# =============================
# 2. Configuração de ambiente e chaves de API
# =============================
def setup_api_keys():
    """Configura as chaves de API necessárias"""
    try:
        # Configurar OpenAI
        os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY or ''
        os.environ["OPENAI_MODEL_NAME"] = Config.OPENAI_MODEL_NAME or 'gpt-4-turbo'
        # Configurar Serper API para busca na web
        if Config.SERPER_API_KEY:
            os.environ["SERPER_API_KEY"] = Config.SERPER_API_KEY
            print("🔍 Serper API Key configurada para busca na web!")
        else:
            print("⚠️ Serper API Key não configurada - ferramentas de busca na web podem falhar")
        print("🔑 Chaves de API configuradas com sucesso!")
        return True
    except ImportError:
        print("⚠️ Módulo utils não encontrado. Verifique se o arquivo utils.py existe.")
        return False
    except Exception as e:
        print(f"❌ Erro ao configurar chaves de API: {e}")
        return False

setup_api_keys()

# =============================
# 3. Definição das ferramentas (tools)
# =============================
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# =============================
# 4. Definição dos agentes
# =============================
data_analyst_agent = Agent(
    role="Analista de Dados",
    goal="Monitorar e analisar dados de mercado em tempo real para identificar tendências e prever movimentos do mercado.",
    backstory="Especializado em mercados financeiros, este agente utiliza modelagem estatística e aprendizado de máquina para fornecer insights cruciais. Com habilidade para dados, o Analista de Dados é fundamental para informar decisões de negociação.",
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)

trading_strategy_agent = Agent(
    role="Desenvolvedor de Estratégias de Negociação",
    goal="Desenvolver e testar diversas estratégias de negociação com base nos insights do Analista de Dados.",
    backstory="Com profundo entendimento dos mercados financeiros e análise quantitativa, este agente cria e refina estratégias de negociação. Avalia o desempenho de diferentes abordagens para determinar as opções mais lucrativas e avessas ao risco.",
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)

execution_agent = Agent(
    role="Consultor de Execução de Ordens",
    goal="Sugerir estratégias ótimas de execução de ordens com base nas estratégias aprovadas.",
    backstory="Especialista em analisar o timing, preço e detalhes logísticos das operações. Avalia esses fatores para fornecer sugestões fundamentadas sobre quando e como executar ordens para maximizar a eficiência e aderência à estratégia.",
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)

risk_management_agent = Agent(
    role="Consultor de Riscos",
    goal="Avaliar e fornecer insights sobre os riscos associados às atividades de negociação propostas.",
    backstory="Com profundo conhecimento em modelos de avaliação de risco e dinâmica de mercado, este agente analisa os riscos das operações propostas. Oferece análise detalhada da exposição ao risco e sugere salvaguardas para garantir que as operações estejam alinhadas à tolerância ao risco da empresa.",
    verbose=True,
    allow_delegation=True,
    tools=[scrape_tool, search_tool]
)

# =============================
# 5. Definição das tasks
# =============================
data_analysis_task = Task(
    description=(
        "Monitorar e analisar continuamente os dados de mercado para a ação selecionada ({stock_selection}). Utilizar modelagem estatística e aprendizado de máquina para identificar tendências e prever movimentos do mercado. Responda sempre em português do Brasil."
    ),
    expected_output=(
        "Insights e alertas sobre oportunidades ou ameaças significativas de mercado para {stock_selection}."
    ),
    agent=data_analyst_agent,
)

strategy_development_task = Task(
    description=(
        "Desenvolver e refinar estratégias de negociação com base nos insights do Analista de Dados e na tolerância ao risco definida pelo usuário ({risk_tolerance}). Considerar as preferências de negociação ({trading_strategy_preference}). Responda sempre em português do Brasil."
    ),
    expected_output=(
        "Um conjunto de estratégias de negociação potenciais para {stock_selection} que estejam alinhadas à tolerância ao risco do usuário."
    ),
    agent=trading_strategy_agent,
)

execution_planning_task = Task(
    description=(
        "Analisar as estratégias de negociação aprovadas para determinar os melhores métodos de execução para {stock_selection}, considerando as condições atuais do mercado e precificação ótima. Responda sempre em português do Brasil."
    ),
    expected_output=(
        "Planos detalhados sugerindo como e quando executar ordens para {stock_selection}."
    ),
    agent=execution_agent,
)

risk_assessment_task = Task(
    description=(
        "Avaliar os riscos associados às estratégias de negociação e planos de execução propostos para {stock_selection}. Fornecer análise detalhada dos riscos potenciais e sugerir estratégias de mitigação. Responda sempre em português do Brasil."
    ),
    expected_output=(
        "Um relatório abrangente de análise de riscos detalhando riscos potenciais e recomendações de mitigação para {stock_selection}."
    ),
    agent=risk_management_agent,
)

# =============================
# 6. Definição da crew
# =============================
financial_trading_crew = Crew(
    agents=[
        data_analyst_agent,
        trading_strategy_agent,
        execution_agent,
        risk_management_agent
    ],
    tasks=[
        data_analysis_task,
        strategy_development_task,
        execution_planning_task,
        risk_assessment_task
    ],
    manager_llm=ChatOpenAI(model="gpt-4-turbo", temperature=0.7),
    process=Process.hierarchical,
    verbose=True
)

# =============================
# 7. Execução do processo e exibição do resultado
# =============================
financial_trading_inputs = {
    'stock_selection': 'BBAS3',
    'initial_capital': '100000',
    'risk_tolerance': 'Média',
    'trading_strategy_preference': 'Day Trade',
    'news_impact_consideration': True
}

def format_markdown_result(result):
    """Formata o resultado do crew como Markdown bonito."""
    import json
    if isinstance(result, dict):
        md = "# Resultado da Análise Financeira\n"
        for k, v in result.items():
            md += f"\n## {k}\n"
            if isinstance(v, (dict, list)):
                md += f'```json\n{json.dumps(v, indent=2, ensure_ascii=False)}\n```\n'
            else:
                md += f'{v}\n'
        return md
    elif isinstance(result, list):
        md = "# Resultado da Análise Financeira\n\n"
        for item in result:
            md += f'- {item}\n'
        return md
    else:
        return str(result)

# Esta execução pode demorar
result = financial_trading_crew.kickoff(inputs=financial_trading_inputs)

Markdown(format_markdown_result(result))