import requests
from bs4 import BeautifulSoup

# URL fornecida (modifique para o link de sua preferencia)
url = "https://lnxrobs.github.io/select_script.html/"

# Fazer o download do HTML da página
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    html = response.text
else:
    print(f"Erro ao acessar a página: {response.status_code}")
    exit()

# Parse o HTML com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar o elemento <select> com o id "Agencia"
select_element = soup.find('select', {'id': 'Agencia'})

# Verificar se o select foi encontrado
if select_element:
    # Encontrar todas as opções dentro do select
    options = select_element.find_all('option')
    
    # Criar uma lista com os valores e textos das opções
    agencias = []
    for option in options:
        value = option.get('value')
        text = option.get_text()
        agencias.append({'value': value, 'text': text})
    
    # Exibir as opções encontradas
    for agencia in agencias:
        print(f"ID: {agencia['value']} - Nome: {agencia['text']}")
else:
    print("Elemento select com id 'Agencia' não encontrado.")
