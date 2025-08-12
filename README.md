# LinkedIn-Selenium-Automation
Este projeto usa Python, Selenium e Poetry para acessar automaticamente seu perfil do LinkedIn

## Tecnologias usadas

- Python 3.x
- [Poetry](https://python-poetry.org/)
- Selenium 3+
- webdriver-manager
- python-dotenv

---

## Como usar

### 1. Clone ou baixe este repositório

```bash
git clone https://github.com/gabrielmango/LinkedIn-Selenium-Automation.git
cd LinkedIn-Selenium-Automation
````

### 2. Configure o ambiente com Poetry

```bash
poetry install
```

### 3. Crie um arquivo `.env` no diretório raiz com o conteúdo:

```
LINKEDIN_USER=seu_email_ou_usuario
LINKEDIN_PASS=sua_senha
LINKEDIN_PROFILE=https://www.linkedin.com/in/seu-perfil/
```

> **Importante:** Nunca compartilhe seu `.env` publicamente.

### 4. Execute o script

```bash
poetry run python main.py
```

---

## Como funciona

* O script abre o navegador Chrome usando Selenium.
* Faz login no LinkedIn usando as credenciais do `.env`.
* Acessa o perfil do usuário especificado no `.env`.
* Fecha o navegador automaticamente.

---

## Avisos

* O LinkedIn pode bloquear sua conta temporariamente se detectar automação.
* Use este script apenas para fins pessoais e respeitando os termos de uso do LinkedIn.
* Para evitar problemas, não execute o script repetidamente em curtos períodos.

---

## Personalização

* Para usar outro navegador, ajuste o driver no `main.py`.
* Para adicionar funcionalidades, basta editar o script.

---

## Suporte

Se tiver dúvidas, pode abrir uma issue ou me chamar!

---

## Licença

MIT License
