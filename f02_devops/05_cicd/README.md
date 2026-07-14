# CI/CD e GitHub Actions

Nesta fase do treinamento foram estudados os fundamentos de **Integração Contínua (CI)** e **Entrega Contínua (CD)**, aprendendo a automatizar testes, validações, builds e deploys utilizando **GitHub Actions**.

---

### Conteúdos Abordados

#### Fundamentos de CI/CD
* Conceitos de Integração Contínua (CI) e Entrega Contínua (CD).
* Pipeline de desenvolvimento.
* Build, testes e deploy automatizados.
* Boas práticas de automação.

#### GitHub Actions
* Estrutura de um workflow em YAML.
* Gatilhos (`push` e `pull_request`).
* Jobs e Steps.
* Runners.
* Actions reutilizáveis.
* Dependência entre jobs (`needs`).

#### Qualidade de Código
* Execução automática de testes.
* Linting com Ruff.
* Matrix de versões do Python.
* Debug de pipelines.

#### Containers e Publicação
* Build automático de imagens Docker.
* Publicação no GitHub Container Registry (GHCR).
* Versionamento utilizando SHA dos commits.

#### Deploy Automatizado
* Publicação utilizando GitHub Pages.
* Configuração de permissões.
* Fluxo completo da esteira de CI/CD.

---

### Comandos Praticados

`git push` • `git pull` • `pytest` • `ruff check` • `docker build` • `docker push` • `docker login` • `ghcr.io` • `GITHUB_TOKEN` • `github.sha` • `workflow.yml`

---

#### Habilidades Desenvolvidas

Ao final desta fase, fui capaz de:
* Compreender o funcionamento de pipelines de CI/CD.
* Criar workflows utilizando GitHub Actions.
* Automatizar testes e validações de qualidade.
* Executar builds automáticos de aplicações.
* Publicar imagens Docker no GitHub Container Registry.
* Configurar deploy automatizado com GitHub Pages.
* Diagnosticar e corrigir falhas em pipelines.
* Aplicar boas práticas de automação no ciclo de desenvolvimento.

