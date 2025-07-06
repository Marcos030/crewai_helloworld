# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Tarefa de Revisão de Qualidade para o projeto CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Task

class QualityReviewTask:
    """Tarefa para revisar e validar a qualidade das respostas de suporte"""
    
    @staticmethod
    def create(agent, inquiry, support_response):
        """Cria e retorna uma tarefa de revisão de qualidade"""
        
        return Task(
            description=(
                f"Reveja a resposta de suporte fornecida para garantir que atenda aos mais altos padrões de qualidade:\n\n"
                f"CONSULTA ORIGINAL DO CLIENTE: {inquiry}\n\n"
                f"RESPOSTA DE SUPORTE FORNECIDA:\n{support_response}\n\n"
                f"Como especialista em garantia de qualidade, sua tarefa é:\n"
                f"1. Verificar se a resposta aborda completamente a consulta do cliente\n"
                f"2. Avaliar se a resposta é precisa e factualmente correta\n"
                f"3. Confirmar se o tom é profissional e amigável\n"
                f"4. Verificar se a resposta é clara e fácil de entender\n"
                f"5. Identificar qualquer informação faltante ou imprecisa\n"
                f"6. Sugerir melhorias se necessário\n"
                f"7. Aprovar a resposta se ela atender aos padrões de qualidade"
            ),
            agent=agent,
            expected_output=(
                "Uma avaliação completa da qualidade da resposta que inclui:\n"
                "- Confirmação de que todos os aspectos da consulta foram abordados\n"
                "- Verificação da precisão e completude das informações\n"
                "- Avaliação do tom e estilo da comunicação\n"
                "- Identificação de qualquer problema ou melhoria necessária\n"
                "- Aprovação final ou recomendações específicas para melhorias\n"
                "- Versão final da resposta aprovada para envio ao cliente"
            )
        )
# AI_GENERATED_CODE_END 