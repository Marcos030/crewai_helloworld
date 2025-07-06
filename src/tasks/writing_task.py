# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Tarefa de Escrita para o projeto CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Task

class WritingTask:
    """Tarefa de escrita e criação de conteúdo"""
    
    @staticmethod
    def create(writer_agent, research_task):
        """Cria e retorna uma instância da tarefa de escrita"""
        return Task(
            description="""Com base na pesquisa realizada sobre '{topic}', crie um 
            artigo informativo e envolvente. O artigo deve ser acessível ao público 
            geral e destacar os pontos mais importantes sobre este tópico.""",
            agent=writer_agent,
            expected_output="Artigo completo sobre {topic}",
            context=[research_task]
        )
# AI_GENERATED_CODE_END 