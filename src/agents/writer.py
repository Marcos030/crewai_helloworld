# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Agente Escritor para o projeto CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Agent
from src.utils.config import Config

class WriterAgent:
    """Agente especializado em escrita e criação de conteúdo"""
    
    @staticmethod
    def create():
        """Cria e retorna uma instância do agente escritor"""
        return Agent(
            role='Escritor',
            goal='Criar conteúdo claro e envolvente baseado em pesquisas sobre o tópico "{topic}"',
            backstory="""Você é um escritor talentoso que transforma informações 
            complexas em conteúdo acessível e interessante. Você tem uma 
            habilidade natural para comunicar ideias de forma clara sobre 
            o tópico '{topic}'.""",
            verbose=Config.CREWAI_VERBOSE,
            allow_delegation=False
        )
# AI_GENERATED_CODE_END 