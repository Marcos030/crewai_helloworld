# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Módulo de configuração para gerenciar variáveis de ambiente
# Gerado por: Cursor AI
# Versão: Python 3.10+

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    """Classe de configuração para o projeto CrewAI"""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    print(f"🔑 OpenAI API Key carregada: {OPENAI_API_KEY[:8]}..." if OPENAI_API_KEY else "❌ OpenAI API Key não encontrada")
    OPENAI_MODEL_NAME = os.getenv('OPENAI_MODEL_NAME', 'gpt-4-turbo')
    
    # Serper API Configuration (para busca na web)
    SERPER_API_KEY = os.getenv('SERPER_API_KEY')
    print(f"🔍 Serper API Key carregada: {SERPER_API_KEY[:8]}..." if SERPER_API_KEY else "⚠️ Serper API Key não encontrada - busca na web limitada")
    
    # CrewAI Configuration
    CREWAI_VERBOSE = os.getenv('CREWAI_VERBOSE', 'True').lower() == 'true'
    CREWAI_DEBUG = os.getenv('CREWAI_DEBUG', 'False').lower() == 'true'
    
    # Application Configuration
    APP_ENV = os.getenv('APP_ENV', 'development')
    APP_DEBUG = os.getenv('APP_DEBUG', 'True').lower() == 'true'
    
    @classmethod
    def validate_config(cls):
        """Valida se as configurações obrigatórias estão definidas"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY não está definida no arquivo .env")
        
        return True
    
    @classmethod
    def validate_web_search_config(cls):
        """Valida se as configurações para busca na web estão definidas"""
        if not cls.SERPER_API_KEY:
            print("⚠️ SERPER_API_KEY não está definida - ferramentas de busca na web não funcionarão")
            return False
        return True
    
    @classmethod
    def get_config_summary(cls):
        """Retorna um resumo das configurações atuais"""
        return {
            'openai_model': cls.OPENAI_MODEL_NAME,
            'serper_api_configured': bool(cls.SERPER_API_KEY),
            'crewai_verbose': cls.CREWAI_VERBOSE,
            'crewai_debug': cls.CREWAI_DEBUG,
            'app_env': cls.APP_ENV,
            'app_debug': cls.APP_DEBUG
        }
# AI_GENERATED_CODE_END 