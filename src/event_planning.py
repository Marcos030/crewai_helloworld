# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Sistema de Planejamento de Eventos com CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

# =============================================================================
# IMPORTS E CONFIGURAÇÕES
# =============================================================================

import warnings
warnings.filterwarnings('ignore')

import os
import json
from pprint import pprint
from pydantic import BaseModel
from IPython.display import Markdown

from crewai import Agent, Crew, Task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from src.utils.config import Config

# =============================================================================
# CONFIGURAÇÃO DE CHAVES DE API
# =============================================================================

def setup_api_keys():
    """Configura as chaves de API necessárias"""
    try:
        # Configurar OpenAI
        os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY
        os.environ["OPENAI_MODEL_NAME"] = Config.OPENAI_MODEL_NAME
        
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

# =============================================================================
# MODELOS DE DADOS
# =============================================================================

class VenueDetails(BaseModel):
    """Modelo Pydantic para detalhes do local do evento"""
    name: str
    address: str
    capacity: int
    booking_status: str

# =============================================================================
# FERRAMENTAS
# =============================================================================

def initialize_tools():
    """Inicializa as ferramentas necessárias para os agentes"""
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    return search_tool, scrape_tool

# =============================================================================
# DEFINIÇÃO DOS AGENTES
# =============================================================================

def create_venue_coordinator(search_tool, scrape_tool):
    """Cria o agente coordenador de local"""
    return Agent(
        role="Coordenador de Local",
        goal="Identificar e reservar um local apropriado baseado nos requisitos do evento",
        tools=[search_tool, scrape_tool],
        verbose=True,
        backstory=(
            "Com um aguçado senso de espaço e compreensão da logística de eventos, "
            "você se destaca em encontrar e garantir o local perfeito que se adequa "
            "ao tema, tamanho e restrições orçamentárias do evento."
        )
    )

def create_logistics_manager(search_tool, scrape_tool):
    """Cria o agente gerente de logística"""
    return Agent(
        role='Gerente de Logística',
        goal="Gerenciar toda a logística do evento incluindo catering e equipamentos",
        tools=[search_tool, scrape_tool],
        verbose=True,
        backstory=(
            "Organizado e orientado a detalhes, você garante que todos os aspectos "
            "logísticos do evento, desde o catering até a configuração de equipamentos, "
            "sejam executados perfeitamente para criar uma experiência sem problemas."
        )
    )

def create_marketing_agent(search_tool, scrape_tool):
    """Cria o agente de marketing e comunicação"""
    return Agent(
        role="Agente de Marketing e Comunicação",
        goal="Promover efetivamente o evento e comunicar-se com os participantes",
        tools=[search_tool, scrape_tool],
        verbose=True,
        backstory=(
            "Criativo e comunicativo, você elabora mensagens convincentes e "
            "engaja com potenciais participantes para maximizar a exposição "
            "e participação no evento."
        )
    )

# =============================================================================
# DEFINIÇÃO DAS TAREFAS
# =============================================================================

def create_venue_task(venue_coordinator):
    """Cria a tarefa de busca de local"""
    return Task(
        description="Encontre um local em {event_city} que atenda aos critérios para {event_topic}.",
        expected_output="Todos os detalhes de um local específico escolhido para acomodar o evento.",
        human_input=True,
        output_json=VenueDetails,
        output_file="venue_details.json",
        agent=venue_coordinator
    )

def create_logistics_task(logistics_manager):
    """Cria a tarefa de logística"""
    return Task(
        description="Coordene o catering e equipamentos para um evento com {expected_participants} "
                   "participantes em {tentative_date}.",
        expected_output="Confirmação de todos os arranjos logísticos incluindo catering e configuração de equipamentos.",
        human_input=True,
        async_execution=True,
        agent=logistics_manager
    )

def create_marketing_task(marketing_agent):
    """Cria a tarefa de marketing"""
    return Task(
        description="Promova o {event_topic} visando engajar pelo menos {expected_participants} "
                   "participantes potenciais.",
        expected_output="Relatório sobre atividades de marketing e engajamento de participantes formatado como markdown.",
        # async_execution=True,  # Removido - apenas uma tarefa assíncrona permitida
        output_file="marketing_report.md",
        agent=marketing_agent
    )

# =============================================================================
# CONFIGURAÇÃO DO EVENTO
# =============================================================================

def get_event_details():
    """Retorna os detalhes do evento a ser planejado"""
    return {
        'event_topic': "Conferência de Inovação Tecnológica",
        'event_description': "Um encontro de inovadores tecnológicos e líderes da indústria "
                            "para explorar tecnologias futuras.",
        'event_city': "São Paulo",
        'tentative_date': "2025-09-15",
        'expected_participants': 500,
        'budget': 20000,
        'venue_type': "Sala de Conferência"
    }

# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================

def main():
    """Função principal do sistema de planejamento de eventos"""
    
    print("🚀 Iniciando sistema de planejamento de eventos...")
    
    # Configurar chaves de API
    if not setup_api_keys():
        print("❌ Não foi possível configurar as chaves de API. Encerrando...")
        return
    
    # Inicializar ferramentas
    search_tool, scrape_tool = initialize_tools()
    
    # Criar agentes
    venue_coordinator = create_venue_coordinator(search_tool, scrape_tool)
    logistics_manager = create_logistics_manager(search_tool, scrape_tool)
    marketing_agent = create_marketing_agent(search_tool, scrape_tool)
    
    # Criar tarefas
    venue_task = create_venue_task(venue_coordinator)
    logistics_task = create_logistics_task(logistics_manager)
    marketing_task = create_marketing_task(marketing_agent)
    
    # Obter detalhes do evento
    event_details = get_event_details()
    
    print(f"📅 Planejando evento: {event_details['event_topic']}")
    print(f"📍 Local: {event_details['event_city']}")
    print(f"👥 Participantes esperados: {event_details['expected_participants']}")
    
    # Criar crew
    # Reorganizar tarefas: tarefa assíncrona deve ser a última
    event_management_crew = Crew(
        agents=[venue_coordinator, logistics_manager, marketing_agent],
        tasks=[venue_task, marketing_task, logistics_task],  # logistics_task (assíncrona) por último
        verbose=True
    )
    
    print("⚡ Executando crew de planejamento de eventos...")
    
    # Executar crew
    result = event_management_crew.kickoff(inputs=event_details)
    
    print("\n" + "="*50)
    print("📋 RESULTADO DO PLANEJAMENTO:")
    print("="*50)
    print(result)
    print("="*50)
    
    # Exibir resultados dos arquivos gerados
    display_results()

def display_results():
    """Exibe os resultados dos arquivos gerados"""
    print("\n📁 ARQUIVOS GERADOS:")
    print("-" * 30)
    
    # Exibir detalhes do local
    try:
        with open('venue_details.json', 'r', encoding='utf-8') as f:
            venue_data = json.load(f)
        print("🏢 DETALHES DO LOCAL:")
        pprint(venue_data)
    except FileNotFoundError:
        print("❌ Arquivo venue_details.json não encontrado")
    except Exception as e:
        print(f"❌ Erro ao ler venue_details.json: {e}")
    
    # Exibir relatório de marketing
    try:
        print("\n📊 RELATÓRIO DE MARKETING:")
        with open('marketing_report.md', 'r', encoding='utf-8') as f:
            marketing_content = f.read()
        print(marketing_content)
    except FileNotFoundError:
        print("❌ Arquivo marketing_report.md não encontrado")
    except Exception as e:
        print(f"❌ Erro ao ler marketing_report.md: {e}")

# =============================================================================
# EXECUÇÃO
# =============================================================================

if __name__ == "__main__":
    main()
# AI_GENERATED_CODE_END