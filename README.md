# LinkedIn Selenium Automation

Automação com Selenium para acessar o LinkedIn, realizar login e coletar links das conexões, com simulação de comportamento humano para evitar bloqueios.

---

## Funcionalidades

- Login no LinkedIn usando credenciais armazenadas em `.env`
- Simulação de digitação humana letra a letra com delays aleatórios
- Movimentação do mouse até os campos antes da digitação
- Scrolls lentos e graduais para simular leitura natural da página
- Acesso à lista de conexões e coleta dos links dos perfis
- Armazenamento dos links das conexões em arquivo `conexoes_links.txt`
- Uso do `webdriver_manager` para baixar o ChromeDriver automaticamente compatível com a versão do navegador

---

## Pré-requisitos

- Python 3.11 ou superior
- [Poetry](https://python-poetry.org/) (opcional, recomendado para gerenciamento de dependências)
- Google Chrome instalado

---

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/gabrielmango/LinkedIn-Selenium-Automation.git
cd LinkedIn-Selenium-Automation
````

2. Instale as dependências com Poetry:

```bash
poetry install
```

Ou usando pip diretamente:

```bash
pip install -r requirements.txt
```

3. Configure seu arquivo `.env` na raiz do projeto com as credenciais e perfil LinkedIn:

```env
LINKEDIN_USER=seu_email_ou_usuario
LINKEDIN_PASS=sua_senha
LINKEDIN_PROFILE=https://www.linkedin.com/in/seu-perfil/
```

---

## Uso

Execute o script principal:

```bash
poetry run python main.py
```

Ou, se não usar Poetry:

```bash
python main.py
```

O script vai:

* Fazer login no LinkedIn
* Acessar a página de conexões
* Rolar a página para carregar todas as conexões
* Extrair os links dos perfis das conexões
* Salvar esses links no arquivo `conexoes_links.txt`

---

## Estrutura do projeto

```
.
├── main.py              # Script principal com automação humanizada
├── .env                 # Arquivo com variáveis de ambiente (não versionar)
├── conexoes_links.txt   # Arquivo gerado com links das conexões
├── README.md            # Este arquivo
├── pyproject.toml       # Configuração Poetry (se usado)
└── requirements.txt     # Dependências (se não usar Poetry)
```

---

## Observações

* Os seletores e XPaths podem precisar ser ajustados caso o LinkedIn atualize o layout.
* Evite rodar o script em alta frequência para não ser bloqueado.
* Sempre respeite os termos de uso do LinkedIn.

---

## Commit recomendados

Use mensagens claras para cada nova funcionalidade, por exemplo:

```
Feature: Add collection of connection links and save them to a txt file.
Feature: Humanize interactions with slow typing and natural scrolling.
Fix: Fix errors when locating dynamic elements.
```

---

## Contribuição

Contribuições são bem-vindas! Abra issues e pull requests para melhorias.

---

## Licença

Este projeto é licenciado sob a MIT License.

---


Qualquer dúvida ou ajuda, só chamar!

