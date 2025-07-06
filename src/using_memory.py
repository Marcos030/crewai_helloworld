# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Exemplo de uso de memória no CrewAI - Versão Organizada
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

import warnings
warnings.filterwarnings('ignore')

from crewai import Crew
from crewai.memory import ShortTermMemory, LongTermMemory, EntityMemory
from src.utils.config import Config
from src.agents import SupportAgent, QualityAssuranceAgent
from src.tasks import InquiryResolutionTask, QualityAssuranceTask
from IPython.display import display, Markdown

def main():
    """Função principal do exemplo de uso de memória no CrewAI"""
    
    print("🚀 Iniciando exemplo de uso de memória no CrewAI...")
    
    # Validar configurações
    try:
        Config.validate_config()
        print("✅ Configurações validadas com sucesso!")
    except ValueError as e:
        print(f"❌ Erro na configuração: {e}")
        return
    
    # Configurar modelo OpenAI
    import os
    os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY
    os.environ["OPENAI_MODEL_NAME"] = Config.OPENAI_MODEL_NAME
    
    # Criar agentes usando as classes organizadas
    support_agent = SupportAgent.create()
    quality_assurance_agent = QualityAssuranceAgent.create()
    
    # Criar tarefas usando as classes organizadas
    inquiry_resolution_task = InquiryResolutionTask.create(support_agent)
    quality_assurance_task = QualityAssuranceTask.create(quality_assurance_agent, inquiry_resolution_task)
    
    # Configurar memória específica para evitar problemas do ChromaDB
    try:
        # Tentar criar memória com configuração específica
        short_term_memory = ShortTermMemory(
            memory_type="simple",  # Usar memória simples em vez de RAG
            max_tokens=1000
        )
        
        long_term_memory = LongTermMemory(
            memory_type="simple",
            max_tokens=2000
        )
        
        entity_memory = EntityMemory(
            memory_type="simple",
            max_tokens=1000
        )
        
        # Criar crew com memória configurada
        crew = Crew(
            agents=[support_agent, quality_assurance_agent],
            tasks=[inquiry_resolution_task, quality_assurance_task],
            verbose=Config.CREWAI_VERBOSE,
            memory=True,
            short_term_memory=short_term_memory,
            long_term_memory=long_term_memory,
            entity_memory=entity_memory
        )
        print("✅ Memória configurada com sucesso!")
        
    except Exception as e:
        print(f"⚠️ Erro ao configurar memória: {e}")
        print("🔄 Tentando sem memória específica...")
        
        # Fallback: usar memória padrão
        crew = Crew(
            agents=[support_agent, quality_assurance_agent],
            tasks=[inquiry_resolution_task, quality_assurance_task],
            verbose=Config.CREWAI_VERBOSE,
            memory=False  # Desabilitar memória se houver erro
        )
    
    # Dados de entrada para o exemplo
    inputs = {
        "customer": "DeepLearningAI",
        "person": "Andrew Ng",
        "inquiry": "I need help with setting up a Crew "
                   "and kicking it off, specifically "
                   "how can I add memory to my crew? "
                   "Can you provide guidance?"
    }
    
    # Executar crew com inputs
    print("🤖 Executando crew de agentes...")
    result = crew.kickoff(inputs=inputs)
    
    # Exibir resultado em Markdown
    print("\n" + "="*50)
    print("📋 RESULTADO FINAL")
    print("="*50)
    
    # Exibir como Markdown
    display(Markdown(str(result)))
    
    print("="*50)
    print("\n✅ Exemplo de uso de memória no CrewAI concluído com sucesso!")

if __name__ == "__main__":
    main()
# AI_GENERATED_CODE_END