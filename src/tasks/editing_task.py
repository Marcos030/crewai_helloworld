# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Tarefa de Edição para o projeto CrewAI (Exemplo)
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Task

class EditingTask:
    """Tarefa de edição e revisão de conteúdo"""
    
    @staticmethod
    def create(editor_agent, writing_task):
        """Cria e retorna uma instância da tarefa de edição"""
        return Task(
            description="""Revise o artigo escrito e corrija erros gramaticais e de estilo. 
            O artigo deve ser acessível ao público geral.""",
            agent=editor_agent,
            expected_output="Artigo revisado e corrigido",
            context=[writing_task]
        )
# AI_GENERATED_CODE_END 