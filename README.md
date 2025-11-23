# 🚀 [Conecta Pecém] - Sistema Multiagentes de Carreira

## 📝 Sobre o Projeto

ConectaPecém é uma plataforma pensada para auxiliar as pessoas a ingressarem no mercado de trabalho do porto do Pecém. Com uma simples descrição de si mesmo com suas
experiências e habilidades a plataforma é capaz de gerar um currículo, dizer qual vaga o usuário melhor se encaixa e gerar um plano de estudos para o usuário melhor 
preencher aquela vaga.
---

## 🤖 Arquitetura dos Agentes

Este projeto utiliza uma arquitetura multiagentes onde cada "bot" possui uma responsabilidade única na pipeline de processamento:

1.  **Agente Perfilador:** Recebe a entrada bruta do usuário e estrutura um perfil de habilidades (Hard/Soft Skills) e experiências.
2.  **Agente Curriculo (CV):** Gera um currículo otimizado com base no perfil estruturado.
3.  **Agente Recrutador:** Analisa o perfil e busca/seleciona a vaga de emprego que melhor se adapta ao candidato.
4.  **Agente Analista de Carreira:** Compara o perfil do usuário com os requisitos da vaga selecionada e identifica o que falta (lacunas técnicas ou de experiência).
5.  **Agente Educacional:** Com base nos gaps identificados, recomenda cursos, livros e roteiros de estudo para suprir as necessidades.

---

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

* [Python 3.12+](https://www.python.org/)
* [Git](https://git-scm.com/)
* Chave de API (Google Gemini) configurada.
* Ollama (https://ollama.com/download) instalado.
* PostgreSQL (https://www.postgresql.org/) instalado.
* Docker (https://docs.docker.com/desktop/setup/install/mac-install/) instalado.


---

## 💻 Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

### 1. Clone o repositório
```bash
git clone [https://github.com/seu-usuario/seu-projeto.git](https://github.com/seu-usuario/seu-projeto.git)
cd seu-projeto

2. Crie o ambiente virtual
python -m venv venv
.\venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

4. Configure o database
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agnohq/pgvector:16

5. Incie o database
python init_db.py

6. Para inicar os agentes
python test_agents.py
```
