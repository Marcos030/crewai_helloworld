# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Tarefa de Suporte Básico para o projeto CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Task

class SupportTask:
    """Tarefa básica de suporte ao cliente"""
    
    @staticmethod
    def create(agent, inquiry):
        """Cria e retorna uma tarefa de suporte básico"""
        
        return Task(
            description=(
                f"Analise a seguinte consulta do cliente e forneça uma resposta útil:\n\n"
                f"CONSULTA DO CLIENTE: {inquiry}\n\n"
                f"Como representante de suporte, sua responsabilidade é:\n"
                f"1. Entender completamente a consulta do cliente\n"
                f"2. Fornecer uma resposta clara e precisa\n"
                f"3. Manter um tom amigável e profissional\n"
                f"4. Garantir que a resposta seja completa e útil"
            ),
            agent=agent,
            expected_output=(
                "Uma resposta completa e bem estruturada que:\n"
                "- Aborda a consulta do cliente de forma clara\n"
                "- É precisa e factualmente correta\n"
                "- Mantém um tom profissional e amigável\n"
                "- Fornece valor real ao cliente"
            )
        )
# AI_GENERATED_CODE_END 