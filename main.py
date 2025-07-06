# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Exemplo básico de uso do CrewAI com estrutura organizada
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

import os
from dotenv import load_dotenv
from crewai import Crew
from src.agents.support_agent import SupportAgent
from src.agents.quality_assurance_agent import QualityAssuranceAgent
from src.tasks.support_task import SupportTask
from src.tasks.quality_review_task import QualityReviewTask

# Carregar variáveis de ambiente
load_dotenv()

def main():
    """Função principal do exemplo básico"""
    
    print("🚀 Iniciando exemplo básico do CrewAI...")
    
    # Criar agentes
    support_agent = SupportAgent.create()
    quality_agent = QualityAssuranceAgent.create()
    
    # Definir consulta do cliente
    customer_inquiry = "Como posso implementar autenticação JWT em uma API REST?"
    
    print(f"📝 Consulta do cliente: {customer_inquiry}")
    
    # Criar tarefas
    support_task = SupportTask.create(support_agent, customer_inquiry)
    quality_task = QualityReviewTask.create(quality_agent, customer_inquiry, "{support_response}")
    
    # Criar crew
    crew = Crew(
        agents=[support_agent, quality_agent],
        tasks=[support_task, quality_task],
        verbose=True
    )
    
    print("⚡ Executando crew...")
    
    # Executar crew
    result = crew.kickoff()
    
    print("\n" + "="*50)
    print("📋 RESULTADO FINAL:")
    print("="*50)
    print(result)
    print("="*50)

if __name__ == "__main__":
    main()
# AI_GENERATED_CODE_END 