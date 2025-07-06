# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/06/2024
# Descrição: Script para configuração da Serper API
# Gerado por: Cursor AI
# Versão: Python 3.10+

import os
import webbrowser
from pathlib import Path

def setup_serper_api():
    """Script para configurar a Serper API Key"""
    
    print("🔍 CONFIGURAÇÃO DA SERPER API")
    print("=" * 50)
    
    # Verificar se o arquivo .env existe
    env_file = Path('.env')
    
    if not env_file.exists():
        print("📝 Criando arquivo .env...")
        create_env_file()
    else:
        print("✅ Arquivo .env encontrado")
    
    # Verificar se a Serper API Key já está configurada
    from dotenv import load_dotenv
    load_dotenv()
    
    current_key = os.getenv('SERPER_API_KEY')
    
    if current_key and current_key != 'your-serper-api-key-here':
        print(f"🔑 Serper API Key já configurada: {current_key[:8]}...")
        response = input("Deseja atualizar a chave? (s/n): ").lower()
        if response != 's':
            print("✅ Configuração mantida")
            return
    
    print("\n📋 PASSO A PASSO PARA CONFIGURAR A SERPER API:")
    print("1. Acesse https://serper.dev/")
    print("2. Crie uma conta gratuita")
    print("3. Obtenha sua API Key")
    print("4. Cole a chave abaixo")
    
    # Abrir o navegador
    open_browser = input("\nDeseja abrir o site da Serper no navegador? (s/n): ").lower()
    if open_browser == 's':
        webbrowser.open('https://serper.dev/')
    
    # Solicitar a API Key
    print("\n" + "=" * 50)
    api_key = input("Cole sua Serper API Key aqui: ").strip()
    
    if not api_key:
        print("❌ Nenhuma chave fornecida")
        return
    
    # Atualizar o arquivo .env
    update_env_file(api_key)
    
    print("✅ Serper API Key configurada com sucesso!")
    print("🔄 Reinicie o aplicativo para aplicar as mudanças")

def create_env_file():
    """Cria o arquivo .env baseado no exemplo"""
    try:
        with open('env.example', 'r', encoding='utf-8') as example_file:
            content = example_file.read()
        
        with open('.env', 'w', encoding='utf-8') as env_file:
            env_file.write(content)
        
        print("✅ Arquivo .env criado com sucesso!")
    except FileNotFoundError:
        print("❌ Arquivo env.example não encontrado")
        # Criar um arquivo .env básico
        basic_env_content = """# OpenAI API Key (obrigatório)
OPENAI_API_KEY=sk-proj-your-openai-api-key-here

# OpenAI Model Name
OPENAI_MODEL_NAME=gpt-4o-mini

# Serper API Key (para busca na web)
SERPER_API_KEY=your-serper-api-key-here

# Configurações do CrewAI
CREWAI_VERBOSE=True
CREWAI_DEBUG=False

# Configurações da aplicação
APP_ENV=development
APP_DEBUG=True
"""
        with open('.env', 'w', encoding='utf-8') as env_file:
            env_file.write(basic_env_content)
        print("✅ Arquivo .env básico criado")

def update_env_file(api_key):
    """Atualiza o arquivo .env com a nova API Key"""
    try:
        # Ler o arquivo atual
        with open('.env', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Atualizar ou adicionar a SERPER_API_KEY
        updated = False
        for i, line in enumerate(lines):
            if line.startswith('SERPER_API_KEY='):
                lines[i] = f'SERPER_API_KEY={api_key}\n'
                updated = True
                break
        
        if not updated:
            lines.append(f'SERPER_API_KEY={api_key}\n')
        
        # Escrever de volta
        with open('.env', 'w', encoding='utf-8') as file:
            file.writelines(lines)
        
        print("✅ Arquivo .env atualizado")
    except Exception as e:
        print(f"❌ Erro ao atualizar arquivo .env: {e}")

def test_serper_api():
    """Testa se a Serper API está funcionando"""
    print("\n🧪 TESTANDO A SERPER API...")
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv('SERPER_API_KEY')
        if not api_key or api_key == 'your-serper-api-key-here':
            print("❌ Serper API Key não configurada")
            return False
        
        # Teste simples com a ferramenta
        from crewai_tools import SerperDevTool
        
        search_tool = SerperDevTool()
        result = search_tool.run("teste simples")
        
        print("✅ Serper API funcionando corretamente!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar Serper API: {e}")
        return False

if __name__ == "__main__":
    print("🚀 CONFIGURADOR DA SERPER API")
    print("=" * 50)
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Configurar Serper API Key")
        print("2. Testar configuração atual")
        print("3. Sair")
        
        choice = input("\nOpção: ").strip()
        
        if choice == '1':
            setup_serper_api()
        elif choice == '2':
            test_serper_api()
        elif choice == '3':
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida")
# AI_GENERATED_CODE_END 