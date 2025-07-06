# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Arquivo principal do projeto CrewAI Hello World - Versão Organizada
# Gerado por: Cursor AI
# Versão: Python 3.10+, CrewAI 0.28.0+

import warnings
warnings.filterwarnings('ignore')

from crewai import Crew
from src.utils.config import Config
from src.agents import ResearcherAgent, WriterAgent
from src.tasks import ResearchTask, WritingTask
from IPython.display import display, Markdown

def main():
    """Função principal do projeto CrewAI Hello World"""
    
    print("🚀 Iniciando CrewAI Hello World...")
    
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
    researcher = ResearcherAgent.create()
    writer = WriterAgent.create()
    
    # Criar tarefas usando as classes organizadas
    research_task = ResearchTask.create(researcher)
    writing_task = WritingTask.create(writer, research_task)
    
    # Criar crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=Config.CREWAI_VERBOSE
    )
    
    # Executar crew com inputs
    print("🤖 Executando crew de agentes...")
    result = crew.kickoff(inputs={"topic": "Oportunidades de negócios no Brasil com IA"})
    
    # Exibir resultado em Markdown
    print("\n" + "="*50)
    print("📋 RESULTADO FINAL")
    print("="*50)
    
    # Exibir como Markdown
    display(Markdown(str(result)))
    
    print("="*50)
    print("\n✅ Projeto CrewAI Hello World concluído com sucesso!")

if __name__ == "__main__":
    main()
# AI_GENERATED_CODE_END 