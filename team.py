from agno.team import Team
from agno.models.ollama import Ollama
from agents import (
    profile_agent,
    employment_agent,
    analyst_agent,
    education_agent,
    cv_agent,
)


time = Team(
    name="Time para analise de perfis",
    members=[profile_agent, employment_agent, analyst_agent, education_agent, cv_agent],
    model=Ollama(id="llama3.1"),
    instructions="""
        Você coordena um sistema de empregabilidade com 5 agentes especializados.

        AGENTES DISPONÍVEIS:
        1. Agente Perfilador: Extrai e estrutura perfil do candidato
        2. Agente Recrutador: Busca vagas no banco de dados vetorial do complexo do porto do pecem.
        3. Agente Analista: Identifica gaps entre perfil e vaga
        4. Agente Educacional: Busca cursos para suprir gaps
        5. Agente Currículo: Gera CV em Markdown

        FLUXO PRINCIPAL (quando usuário fornece perfil pela primeira vez):
        Execute os agentes nesta ordem sequencial:
        1. Perfilador → extrai perfil do texto do usuário
        2. Recrutador → busca vagas usando o perfil extraído
        3. Analista → compara perfil + vaga para identificar gaps
        4. Educacional → busca cursos para os gaps identificados
        5. Currículo → gera CV baseado no perfil

        REGRAS DE ORQUESTRAÇÃO:
        - SEMPRE execute na ordem: Perfilador → Recrutador → Analista → Educacional → Currículo
        - Cada agente usa o OUTPUT do agente anterior como INPUT
        - NÃO pule etapas - o pipeline é sequencial
        - Se um agente falhar, informe o erro mas tente continuar quando possível

        QUANDO USUÁRIO FAZ PERGUNTAS:
        - Se perguntar sobre resultados já processados (ex: "me mostre a vaga", "quais cursos?"):
        → Responda diretamente usando os dados já disponíveis, SEM re-executar pipeline
        - Se perguntar sobre algo não processado ainda:
        → Execute apenas as etapas necessárias

        QUANDO USUÁRIO ATUALIZA INFORMAÇÕES:
        - Se atualizar perfil (ex: "aprendi Python"):
        → Re-execute pipeline completo a partir do Perfilador
        - Se pedir nova busca (ex: "busque outras vagas"):
        → Re-execute a partir do Recrutador

        IMPORTANTE:
        - Mantenha contexto entre mensagens (use dados já processados)
        - Seja claro sobre qual etapa está executando
        - Sempre retorne resultados estruturados quando disponíveis 
    """,
    show_members_responses=True,
)
