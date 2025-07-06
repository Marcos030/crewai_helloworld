# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Agente Pesquisador para o projeto CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Agent
from src.utils.config import Config

class ResearcherAgent:
    """Agente especializado em pesquisa e coleta de informações"""
    
    @staticmethod
    def create():
        """Cria e retorna uma instância do agente pesquisador"""
        return Agent(
            role='Pesquisador',
            goal='Realizar pesquisas detalhadas sobre o tópico específico "{topic}"',
            backstory="""Você é um pesquisador experiente com vasto conhecimento 
            em diversas áreas. Sua especialidade é coletar e analisar informações 
            de forma precisa e objetiva sobre o tópico '{topic}'.""",
            verbose=Config.CREWAI_VERBOSE,
            allow_delegation=False
        )
# AI_GENERATED_CODE_END 