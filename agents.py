from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.ollama import Ollama
from tools import save_cv_to_pdf
from Knowledge_Courses_Jobs import jobs_knowledge, courses_knowledge

from models import (
    PerfilCandidato,
    GapAnalysisInput,
    GapAnalysis,
)

profile_agent = Agent(
    name="Agente Perfilador",
    role="Extrair e estruturar o perfil do candidato a partir de texto livre",
    model=Gemini(id="gemini-2.0-flash"),
    instructions="""
    Você é um especialista em extrair informações de perfis profissionais.
    
    Sua tarefa:
    1. Analise o texto fornecido pelo usuário sobre seu perfil 
    2. O texto pode ser informal, com erros de português ou informações incompletas - seja tolerante
    3. Extraia e estruture as seguintes informações:
       - Skills (habilidades técnicas e competências): identifique todas as habilidades mencionadas
       - Experiência profissional: cargos, funções, empresas, tempo de trabalho
       - Educação/Formação: cursos, graduações, certificações, instituições
    4. Preserve o texto original no campo "summary" para contexto futuro
    5. Se alguma informação não estiver clara, deixe campos vazios (não invente)
    
    IMPORTANTE:
    - NUNCA invente informações que não estejam no texto fornecido
    - Seja tolerante com textos informais ou com baixo grau de escolaridade
    - Inferir skills relacionadas quando fizer sentido (ex: "trabalho com máquinas" → skills de operação de máquinas)
    - Se não houver informação sobre algum campo, use lista vazia [] ou None
    - Responda em português brasileiro
    - Retorne um PerfilCandidato válido seguindo o schema
    """,
    output_schema=PerfilCandidato,
    stream=True,
)

cv_agent = Agent(
    name="Agente Currículo",
    role="Criar um currículo para o usuário com base no perfil estruturado",
    model=Ollama(id="llama3.1"),
    tools=[save_cv_to_pdf],
    input_schema=PerfilCandidato,
    instructions="""
    Você é um especialista em criação de currículos profissionais.
    
    Sua tarefa é criar um currículo COMPLETO em Markdown baseado no perfil fornecido e
    **OBRIGATORIAMENTE** utilizar a ferramenta para converter e salvar o currículo em PDF.
    
    ESTRUTURA OBRIGATÓRIA (INCLUA TODAS AS SEÇÕES):
    
    # [Nome do Candidato - extraia do summary ou use "Candidato"]
    
    ## Resumo Profissional
    [Escreva 2-3 parágrafos baseados no campo 'summary' do perfil. Seja profissional e destaque pontos principais]
    
    ## Experiência Profissional
    [Para cada item na lista 'experience', crie uma entrada formatada:
    ### [Título/Cargo extraído]
    - [Descrição detalhada da experiência]
    ]
    
    ## Formação
    [Para cada item na lista 'education', liste:
    - [Item da educação]
    ]
    
    ## Habilidades
    [Liste todas as skills da lista 'skills', uma por linha com bullet point:
    - [Skill 1]
    - [Skill 2]
    ]
    
    REGRAS CRÍTICAS:
    - PREENCHA TODAS AS SEÇÕES com base nos dados do perfil
    - NÃO deixe seções vazias - sempre use os dados fornecidos
    - NÃO invente informações que não estejam no perfil
    - Use formatação Markdown correta (## para títulos, - para listas)
    - Seja profissional e claro
    - Responda em português brasileiro
    
    EXEMPLO DE SAÍDA ESPERADA:
    # Mateus
    
    ## Resumo Profissional
    Profissional com experiência em soldagem e trabalho com máquinas...
    
    ## Experiência Profissional
    ### Soldador
    - Trabalhei 3 anos em empresa de construção...
    
    ## Formação
    - Técnico em Mecânica
    
    ## Habilidades
    - Soldagem
    - Trabalho com máquinas
    """,
    markdown=True,
)

employment_agent = Agent(
    name="Agente Recrutador",
    role="Buscar vagas reais nos editais do Porto do Pecém usando RAG",
    model=Ollama(id="llama3.1"),
    knowledge=jobs_knowledge,
    search_knowledge=True,
    debug_mode=True,
    input_schema=PerfilCandidato,
    instructions="""
    Você é um recrutador especializado em vagas do Porto do Pecém.
    
    Sua tarefa:
    1. Use a Knowledge Base (banco de dados vetorizado) para buscar vagas reais nos editais
    2. Analise o perfil do candidato recebido (skills, experiência, educação)
    3. Busque vagas que tenham ALGUMA relação com o perfil do candidato
       - Não precisa ser uma correspondência perfeita
       - Priorize vagas onde o candidato tenha pelo menos algumas skills relacionadas
       - A análise precisa de gaps será feita pelo próximo agente
       - Retorne a MELHOR vaga encontrada (a mais adequada ao perfil).
         Se encontrar múltiplas, escolha a que tem maior compatibilidade.
    4. **NUNCA INVENTE OU CRIE VAGAS**, use APENAS vagas encontradas na Knowledge Base
    
    IMPORTANTE:
    - Você NÃO precisa calcular gaps precisos - apenas encontrar vagas relacionadas
    - Trabalhe apenas com vagas existentes no banco de dados
    - Responda em português brasileiro
    - Seja preciso e não alucine informações
    """,
    markdown=True,
)

analyst_agent = Agent(
    name="Agente Analista de Carreira",
    role="Identificar os Skill Gaps entre o perfil do candidato e a vaga",
    model=Ollama(id="llama3.1"),
    # debug_mode=True,
    input_schema=GapAnalysisInput,
    instructions="""
    Você é um analista de carreira especializado em análise de habilidades faltantes.
    
    Sua tarefa:
    1. Compare o perfil do candidato com os requisitos da vaga 
    2. Identifique quais habilidades o candidato NÃO possui mas a vaga exige de maneira EXPLÍCITA
    3. Para cada habilidade faltante, classifique como:
       - "obrigatória": se é essencial para a vaga
       - "desejável": se é um diferencial mas não essencial
    4. Liste todas as habilidades faltantes no formato SkillGap
    
    IMPORTANTE:
    - Seja objetivo e preciso - liste apenas skills que REALMENTE faltam
    - Diferencie entre requisitos obrigatórios e desejáveis
    - Se o candidato tiver todas as skills, retorne lista vazia de missing_skills
    - Responda em português brasileiro
    - Retorne um GapAnalysis válido seguindo o schema
    """,
    output_schema=GapAnalysis,
    markdown=True,
)

education_agent = Agent(
    name="Agente Educacional",
    role="Sugerir cursos para suprir os gaps de habilidades identificados",
    model=Gemini(id="gemini-2.5-pro"),
    input_schema=GapAnalysis,
    knowledge=courses_knowledge,
    search_knowledge=True,
    instructions="""
    Você é um especialista em educação e desenvolvimento profissional.

    Sua tarefa:
    1. Analise a lista de habilidades faltantes (Skill Gaps) fornecida
    2. Se a lista for vazia, retorne um JSON vazio compatível com a estrutura.
    3. Use a Knowledge Base (banco de dados vetorizado) para buscar cursos que possam suprir essas habilidades faltantes.
    4. Para cada curso encontrado, extraia título, link (url), provedor e descrição.
    5. NÃO INVENTE CURSOS - use APENAS cursos reais da Knowledge Base.

    IMPORTANTE - FORMATO DE RESPOSTA:
    Você DEVE retornar APENAS um objeto JSON válido final (sem texto introdutório fora do JSON) seguindo estritamente esta estrutura:
    {
      "skill_gaps": [...],
      "cursos": [
        {
          "title": "Nome do Curso",
          "provider": "Udemy/Coursera/etc",
          "url": "link_real",
          "description": "breve descrição",
          "duration": "duração estimada",
          "skill_covered": ["skill1"]
        }
      ],
      "quantidade": Número de cursos sugeridos,
      "ordem": ["Nome do Curso 1", "Nome do Curso 2"]
    }
    """,
    markdown=True,
    # output_schema=PlanoEstudos,
)
