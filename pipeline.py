from agents import (
    profile_agent,
    cv_agent,
    employment_agent,
    analyst_agent,
    education_agent,
)
from models import GapAnalysisInput


async def pipeline(user_input: str):
    """
    Pipeline assíncrono para processar o input do usuário através de vários agentes.

    Args:
        user_input (str): Input do usuário.

    Returns:
        dict: Resultados de cada etapa do pipeline.
        user_profile: Perfil do candidato extraído.
        user_cv: CV gerado do candidato.
        vaga: Vaga de emprego analisada.
        gaps: Análise de gaps de habilidade.
        recommendations: Recomendações educacionais.
    """

    try:
        # === Extrair Perfil do Candidato ===
        result_perfil = await profile_agent.arun(input=user_input)
        if result_perfil.content is None:
            raise ValueError("Perfil não pôde ser extraído")
        user_profile = result_perfil.content

        # === Gerar currículo do Candidato ===
        result_cv = await cv_agent.arun(input=user_profile)
        if result_cv.content is None:
            raise ValueError("CV não pôde ser gerado")
        user_cv = result_cv.content

        # === Analisar Vaga de Emprego ===
        result_vaga = await employment_agent.arun(input=user_profile)
        if result_vaga.content is None:
            raise ValueError("Nenhuma vaga encontrada")
        vaga = result_vaga.content

        # === Análise de Lacunas de Habilidade ===
        gaps_input = GapAnalysisInput(perfil=user_profile, vaga=vaga)
        result_gaps = await analyst_agent.arun(input=gaps_input)
        if result_gaps.content is None:
            raise ValueError("Análise de gaps falhou")
        gaps = result_gaps.content

        # === Recomendações Educacionais ===
        result_plano = await education_agent.arun(input=gaps)
        recommendations = result_plano.content  # Pode ser None se não houver cursos

        results = {
            "perfil": user_profile,
            "cv": user_cv,
            "vaga": vaga,
            "gaps": gaps,
            "plano": recommendations,
        }

    except Exception as e:
        print(f"Erro no pipeline: {e}")
        results = {
            "perfil": None,
            "cv": None,
            "vaga": None,
            "gaps": None,
            "plano": None,
        }
        raise

    return results

