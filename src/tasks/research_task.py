# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Tarefa de Pesquisa para o projeto CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Task

class ResearchTask:
    """Tarefa de pesquisa e coleta de informações"""
    
    @staticmethod
    def create(researcher_agent):
        """Cria e retorna uma instância da tarefa de pesquisa"""
        return Task(
            description="""Pesquise sobre o tópico '{topic}' fornecendo informações 
            detalhadas, fatos relevantes e dados atualizados. Foque em aspectos 
            práticos, aplicações e benefícios deste tópico.""",
            agent=researcher_agent,
            expected_output="Relatório detalhado com fatos e dados sobre {topic}"
        )
# AI_GENERATED_CODE_END 