# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Tarefa de Resolução de Consultas com ferramentas externas
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Task
from crewai_tools import ScrapeWebsiteTool

class InquiryResolutionTask:
    """Tarefa para resolver consultas de clientes usando ferramentas externas"""
    
    @staticmethod
    def create(agent, inquiry):
        """Cria e retorna uma tarefa de resolução de consultas"""
        
        return Task(
            description=(
                f"Analise a seguinte consulta do cliente e forneça uma resposta completa e útil:\n\n"
                f"CONSULTA DO CLIENTE: {inquiry}\n\n"
                f"Para fornecer a melhor resposta possível:\n"
                f"1. Use a ferramenta de busca na web para obter informações atualizadas sobre o tópico\n"
                f"2. Se a consulta for sobre um produto ou serviço específico, busque informações na documentação oficial\n"
                f"3. Forneça uma resposta detalhada que aborde todos os pontos da consulta\n"
                f"4. Mantenha um tom profissional e amigável\n"
                f"5. Inclua exemplos práticos quando apropriado\n"
                f"6. Se houver múltiplas opções ou soluções, explique as vantagens de cada uma"
            ),
            agent=agent,
            expected_output=(
                "Uma resposta completa e bem estruturada que:\n"
                "- Aborda todos os aspectos da consulta do cliente\n"
                "- Inclui informações relevantes e atualizadas\n"
                "- É clara, concisa e fácil de entender\n"
                "- Mantém um tom profissional e amigável\n"
                "- Fornece valor real ao cliente"
            ),
            tools=[ScrapeWebsiteTool()]
        )
# AI_GENERATED_CODE_END 