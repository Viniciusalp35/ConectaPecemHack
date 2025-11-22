from agno.agent import Agent
from agno.models.ollama import Ollama
from models import (
    CurriculumVitae,
    PerfilCandidato,
    VagaEmprego,
    GapAnalysisInput,
    GapAnalysis,
    PlanoEstudos,
)

profile_agent = Agent(
    name="Agente Perfilador",
    role="Extrair e estruturar o perfil do candidato a partir de texto livre",
    model=Ollama(id="llama3.1"),
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
    input_schema=PerfilCandidato,
    instructions="""
    Você é um especialista em criação de currículos profissionais.
    
    Sua tarefa:
    1. Receba o perfil estruturado do candidato (skills, experiência, educação)
    2. Crie um currículo profissional bem formatado e claro em markdown na seguinte estrutura:

       ## Resumo Profissional
       [2-3 linhas baseadas no summary]
       
       ## Experiência Profissional
       ### [Cargo] | [Período]
       - [Descrição]
       
       ## Formação
       - [Educação]

       ## Skills
       - [Skills]

    3. Inclua seções para Informações Pessoais, Educação, Experiência e Skills
    4. Use bullet points para listar skills e experiências

    IMPORTANTE:
    - NÃO INVENTE informações - use APENAS o que está no perfil
    - Se alguma seção estiver vazia (ex: sem educação), omita essa seção
    - Responda em português brasileiro
    """,
    output_schema=CurriculumVitae,
)

employment_agent = Agent(
    name="Agente Recrutador",
    role="Buscar vagas reais nos editais do Porto do Pecém usando RAG",
    model=Ollama(id="llama3.1"),
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
       - "Retorne a MELHOR vaga encontrada (a mais adequada ao perfil).
         Se encontrar múltiplas, escolha a que tem maior compatibilidade."
    4. NUNCA invente ou crie vagas - use APENAS vagas encontradas na Knowledge Base
    5. Se não encontrar vagas adequadas, retorne uma VagaEmprego vazia (title="", description="", requirements=[])
    
    IMPORTANTE:
    - Você NÃO precisa calcular gaps precisos - apenas encontrar vagas relacionadas
    - Trabalhe apenas com vagas existentes no banco de dados
    - Responda em português brasileiro
    - Seja preciso e não alucine informações
    """,
    output_schema=VagaEmprego,
)

analyst_agent = Agent(
    name="Agente Analista de Carreira",
    role="Identificar os Skill Gaps entre o perfil do candidato e a vaga",
    model=Ollama(id="llama3.1"),
    input_schema=GapAnalysisInput,
    instructions="""
    Você é um analista de carreira especializado em análise de habilidades faltantes.
    
    Sua tarefa:
    1. Compare o perfil do candidato com os requisitos da vaga 
    2. Identifique quais habilidades o candidato NÃO possui mas a vaga exige
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
)

education_agent = Agent(
    name="Agente Educacional",
    role="Sugerir cursos para suprir os gaps de habilidades identificados",
    model=Ollama(id="llama3.1"),
    input_schema=GapAnalysis,
    # tool = crawl4ai(),
    instructions="""
    Você é um especialista em educação e desenvolvimento profissional.

    Sua tarefa:
    1. Analise a lista de habilidades faltantes (Skill Gaps) fornecida
    2. Se a lista for vazia, retorne um PlanoEstudos vazio (sem cursos)
    3. Para cada habilidade faltante, USE A TOOL "crawl4ai" para buscar cursos reais na internet
    4. A tool retornará resultados de busca - extraia informações relevantes
    5. Para cada curso encontrado, estruture seguindo o modelo "Curso"

    IMPORTANTE:
    - SEMPRE use a tool para buscar cursos - não invente cursos
    - Se a tool falhar para uma skill, continue com as outras (seja resiliente)
    - Limite buscas para não travar (máximo 3-5 skills por vez)
    - Responda em português brasileiro
    """,
    output_schema=PlanoEstudos,
)
