# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Exemplo avançado do CrewAI com memória e ferramentas externas
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

import os
from dotenv import load_dotenv
from crewai import Crew
from src.agents.support_agent import SupportAgent
from src.agents.quality_assurance_agent import QualityAssuranceAgent
from src.tasks.inquiry_resolution_task import InquiryResolutionTask
from src.tasks.quality_review_task import QualityReviewTask

# Carregar variáveis de ambiente
load_dotenv()

def main():
    """Função principal do exemplo com memória e ferramentas"""
    
    print("🚀 Iniciando exemplo avançado do CrewAI com memória e ferramentas...")
    
    # Criar agentes
    support_agent = SupportAgent.create()
    quality_agent = QualityAssuranceAgent.create()
    
    # Definir consulta do cliente
    customer_inquiry = "Como posso implementar autenticação JWT em uma API REST usando Python e Flask?"
    
    print(f"📝 Consulta do cliente: {customer_inquiry}")
    
    # Criar tarefas
    support_task = InquiryResolutionTask.create(support_agent, customer_inquiry)
    quality_task = QualityReviewTask.create(quality_agent, customer_inquiry, "{support_response}")
    
    # Criar crew com memória (desabilitada temporariamente devido a problemas de compatibilidade)
    crew = Crew(
        agents=[support_agent, quality_agent],
        tasks=[support_task, quality_task],
        verbose=True,
        # memory=True,  # Desabilitado devido a problemas com ChromaDB
        # memory_config={
        #     "type": "chroma",
        #     "chroma_db_impl": "duckdb+parquet",
        #     "persist_directory": "./memory"
        # }
    )
    
    print("⚡ Executando crew com ferramentas externas...")
    
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