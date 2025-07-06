# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Tarefa de Qualidade para o projeto CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

from crewai import Task

class QualityAssuranceTask:
    """Tarefa de revisão de qualidade"""
    
    @staticmethod
    def create(quality_assurance_agent, inquiry_resolution_task):
        """Cria e retorna uma instância da tarefa de qualidade"""
        return Task(
            description=(
                "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
                "Ensure that the answer is comprehensive, accurate, and adheres to the "
                "high-quality standards expected for customer support.\n"
                "Verify that all parts of the customer's inquiry "
                "have been addressed thoroughly, with a helpful and friendly tone.\n"
                "Check for references and sources used to find the information, "
                "ensuring the response is well-supported and "
                "leaves no questions unanswered."
            ),
            expected_output=(
                "A final, detailed, and informative response "
                "ready to be sent to the customer.\n"
                "This response should fully address the "
                "customer's inquiry, incorporating all "
                "relevant feedback and improvements.\n"
                "Don't be too formal, we are a chill and cool company "
                "but maintain a professional and friendly tone throughout."
            ),
            agent=quality_assurance_agent,
            context=[inquiry_resolution_task]
        )
# AI_GENERATED_CODE_END 