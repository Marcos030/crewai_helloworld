# =============================
# 1. Imports e controle de warnings
# =============================
import warnings
warnings.filterwarnings('ignore')

import os
from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool, ScrapeWebsiteTool, MDXSearchTool, SerperDevTool
from IPython.display import Markdown, display
from src.utils.config import Config

# =============================
# 2. Configuração de ambiente e chaves de API
# =============================
def setup_api_keys():
    """Configura as chaves de API necessárias"""
    try:
        # Configurar OpenAI
        os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY or ''
        os.environ["OPENAI_MODEL_NAME"] = Config.OPENAI_MODEL_NAME or 'gpt-4-turbo'
        # Configurar Serper API para busca na web
        if Config.SERPER_API_KEY:
            os.environ["SERPER_API_KEY"] = Config.SERPER_API_KEY
            print("🔍 Serper API Key configurada para busca na web!")
        else:
            print("⚠️ Serper API Key não configurada - ferramentas de busca na web podem falhar")
        print("🔑 Chaves de API configuradas com sucesso!")
        return True
    except ImportError:
        print("⚠️ Módulo utils não encontrado. Verifique se o arquivo utils.py existe.")
        return False
    except Exception as e:
        print(f"❌ Erro ao configurar chaves de API: {e}")
        return False

setup_api_keys()

# =============================
# 3. Definição das ferramentas (tools)
# =============================
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_resume = FileReadTool(file_path='src/files/fake_resume.md')
semantic_search_resume = MDXSearchTool(mdx='src/files/fake_resume.md')

# =============================
# 4. Definição dos agentes
# =============================
pesquisador = Agent(
    role="Pesquisador de Vagas de Tecnologia",
    goal="Realizar análises detalhadas de vagas de emprego para ajudar candidatos a se destacarem.",
    tools=[scrape_tool, search_tool],
    verbose=True,
    backstory=(
        "Como Pesquisador de Vagas, sua habilidade em navegar e extrair informações críticas de anúncios de emprego é incomparável. "
        "Suas competências ajudam a identificar as qualificações e habilidades necessárias buscadas pelos empregadores, formando a base para personalização eficaz de candidaturas."
    )
)

perfilador = Agent(
    role="Perfilador Pessoal para Engenheiros",
    goal="Realizar pesquisas aprofundadas sobre candidatos para ajudá-los a se destacar no mercado de trabalho.",
    tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
    verbose=True,
    backstory=(
        "Com habilidades analíticas, você sintetiza informações de diversas fontes para criar perfis pessoais e profissionais completos, servindo de base para aprimoramento personalizado de currículos."
    )
)

estrategista_curriculo = Agent(
    role="Estrategista de Currículos para Engenheiros",
    goal="Encontrar as melhores formas de fazer um currículo se destacar no mercado de trabalho.",
    tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
    verbose=True,
    backstory=(
        "Com visão estratégica e atenção aos detalhes, você refina currículos para destacar as habilidades e experiências mais relevantes, garantindo que estejam alinhados com os requisitos da vaga."
    )
)

preparador_entrevista = Agent(
    role="Preparador de Entrevistas para Engenharia",
    goal="Criar perguntas e pontos de discussão para entrevistas com base no currículo e nos requisitos da vaga.",
    tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
    verbose=True,
    backstory=(
        "Seu papel é fundamental para antecipar a dinâmica das entrevistas. Com sua habilidade de formular perguntas-chave e pontos de discussão, você prepara candidatos para o sucesso, garantindo que possam abordar com confiança todos os aspectos da vaga desejada."
    )
)

# =============================
# 5. Definição das tasks
# =============================
tarefa_pesquisa = Task(
    description=(
        "Analise a URL da vaga fornecida ({job_posting_url}) para extrair as principais habilidades, experiências e qualificações exigidas. Utilize as ferramentas para coletar conteúdo, identificar e categorizar os requisitos. Responda sempre em português do Brasil."
    ),
    expected_output=(
        "Uma lista estruturada dos requisitos da vaga, incluindo habilidades, qualificações e experiências necessárias."
    ),
    agent=pesquisador,
    async_execution=True
)

tarefa_perfil = Task(
    description=(
        "Compile um perfil pessoal e profissional detalhado utilizando as URLs do GitHub ({github_url}) e o texto pessoal ({personal_writeup}). Utilize ferramentas para extrair e sintetizar informações dessas fontes. Responda sempre em português do Brasil."
    ),
    expected_output=(
        "Um documento de perfil abrangente que inclua habilidades, experiências em projetos, contribuições, interesses e estilo de comunicação."
    ),
    agent=perfilador,
    async_execution=True
)

tarefa_estrategia_curriculo = Task(
    description=(
        "Utilizando o perfil e os requisitos da vaga obtidos nas tarefas anteriores, personalize o currículo para destacar as áreas mais relevantes. Utilize ferramentas para ajustar e aprimorar o conteúdo do currículo. Não invente informações. Atualize todas as seções, incluindo resumo inicial, experiência profissional, habilidades e educação, para refletir melhor as competências do candidato e como elas se alinham à vaga. Responda sempre em português do Brasil."
    ),
    expected_output=(
        "Um currículo atualizado que destaque de forma eficaz as qualificações e experiências do candidato relevantes para a vaga."
    ),
    output_file="files/tailored_resume.md",
    context=[tarefa_pesquisa, tarefa_perfil],
    agent=estrategista_curriculo
)

tarefa_preparacao_entrevista = Task(
    description=(
        "Crie um conjunto de possíveis perguntas de entrevista e pontos de discussão com base no currículo personalizado e nos requisitos da vaga. Utilize ferramentas para gerar perguntas e tópicos relevantes. Use essas perguntas e pontos para ajudar o candidato a destacar os principais pontos do currículo e como ele se encaixa na vaga. Responda sempre em português do Brasil."
    ),
    expected_output=(
        "Um documento contendo perguntas-chave e pontos de discussão que o candidato deve preparar para a entrevista inicial."
    ),
    output_file="files/interview_materials.md",
    context=[tarefa_pesquisa, tarefa_perfil, tarefa_estrategia_curriculo],
    agent=preparador_entrevista
)

# =============================
# 6. Definição da crew
# =============================
job_application_crew = Crew(
    agents=[pesquisador, perfilador, estrategista_curriculo, preparador_entrevista],
    tasks=[tarefa_pesquisa, tarefa_perfil, tarefa_estrategia_curriculo, tarefa_preparacao_entrevista],
    verbose=True
)

# =============================
# 7. Execução do processo e exibição do resultado
# =============================
job_application_inputs = {
    'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
    'github_url': 'https://github.com/joaomdmoura',
    'personal_writeup': """Noah é um Líder de Engenharia de Software com 18 anos de experiência, especializado em gestão de equipes remotas e presenciais, e especialista em múltiplas linguagens e frameworks. Possui MBA e forte atuação em IA e ciência de dados. Noah liderou grandes iniciativas tecnológicas e startups, comprovando sua capacidade de impulsionar inovação e crescimento no setor de tecnologia. Ideal para cargos de liderança que exigem visão estratégica e inovadora."""
}

# Esta execução pode demorar
result = job_application_crew.kickoff(inputs=job_application_inputs)

display(Markdown("files/tailored_resume.md"))
display(Markdown("files/interview_materials.md"))