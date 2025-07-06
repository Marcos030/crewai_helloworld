# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Agente Editor para o projeto CrewAI (Exemplo)
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Agent
from src.utils.config import Config

class EditorAgent:
    """Agente especializado em edição e revisão de conteúdo"""
    
    @staticmethod
    def create():
        """Cria e retorna uma instância do agente editor"""
        return Agent(
            role='Editor',
            goal='Revisar e melhorar o conteúdo escrito',
            backstory="""Você é um editor experiente que melhora a qualidade do conteúdo escrito. 
            Você tem uma habilidade natural para identificar e corrigir erros gramaticais e de estilo.""",
            verbose=Config.CREWAI_VERBOSE,
            allow_delegation=False
        )
# AI_GENERATED_CODE_END 