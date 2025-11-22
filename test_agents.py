import asyncio
import sys
from typing import Optional

from agents import (
    profile_agent,
    employment_agent,
    analyst_agent,
    education_agent,
    cv_agent,
)

from models import (
    GapAnalysisInput,
    PerfilCandidato,
    VagaEmprego,
    GapAnalysis,
    PlanoEstudos,
    CurriculumVitae,
)


async def run_agent(agent, input_data, stream: bool = False):
    """
    Helper para executar agente com ou sem stream.
    Retorna o resultado final.
    """
    if stream:
        # Se tem stream, iterar e pegar o último chunk
        last_result = None
        async for chunk in agent.arun(input_data, stream=True):
            last_result = chunk
        return last_result
    else:
        # Sem stream, retorna direto
        return await agent.arun(input_data, stream=False)


async def test_profile_agent() -> Optional[PerfilCandidato]:
    """Testa o Agente Perfilador."""
    print("=" * 60)
    print("TESTE: Agente Perfilador")
    print("=" * 60)

    user_input = """
    Olá, me chamo Mateus e tenho experiência com solda.
    Trabalhei 3 anos em uma empresa de construção.
    Fiz curso técnico em mecânica.
    """

    print(f"\n📝 Input: {user_input.strip()}\n")
    print("🔄 Processando...\n")

    try:
        # profile_agent tem stream=True, então precisa iterar
        result = await run_agent(profile_agent, user_input, stream=True)
        if result and result.content:
            perfil = result.content
            print("✅ Perfil extraído com sucesso!")
            print(f"\nSkills: {perfil.skills}")
            print(f"Experiência: {perfil.experience}")
            print(f"Educação: {perfil.education}")
            print(f"Summary: {perfil.summary}")
            return perfil
        else:
            print("❌ Agente retornou None")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback

        traceback.print_exc()
        return None


async def test_employment_agent(
    perfil: Optional[PerfilCandidato],
) -> Optional[VagaEmprego]:
    """Testa o Agente Recrutador."""
    print("\n" + "=" * 60)
    print("TESTE: Agente Recrutador")
    print("=" * 60)

    if perfil is None:
        print("⚠️  Pulando teste - perfil não disponível")
        return None

    print(f"\n📝 Input (Perfil): {perfil.model_dump()}\n")
    print("🔄 Processando...\n")

    try:
        result = await run_agent(employment_agent, perfil, stream=False)
        if result and result.content:
            vaga = result.content
            print("✅ Vaga encontrada!")
            print(f"\nTítulo: {vaga.title}")
            print(f"Descrição: {vaga.description}")
            print(f"Requisitos: {vaga.requirements}")
            return vaga
        else:
            print("❌ Agente retornou None")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback

        traceback.print_exc()
        return None


async def test_analyst_agent(
    perfil: Optional[PerfilCandidato], vaga: Optional[VagaEmprego]
) -> Optional[GapAnalysis]:
    """Testa o Agente Analista."""
    print("\n" + "=" * 60)
    print("TESTE: Agente Analista de Carreira")
    print("=" * 60)

    if perfil is None or vaga is None:
        print("⚠️  Pulando teste - perfil ou vaga não disponíveis")
        return None

    gaps_input = GapAnalysisInput(perfil=perfil, vaga=vaga)
    print("\n📝 Input (Perfil + Vaga):\n")
    print(f"Perfil skills: {perfil.skills}")
    print(f"Vaga requisitos: {vaga.requirements}\n")
    print("🔄 Processando...\n")

    try:
        result = await run_agent(analyst_agent, gaps_input, stream=False)
        if result and result.content:
            gaps = result.content
            print("✅ Análise de gaps concluída!")
            print(f"\nVaga analisada: {gaps.job_title}")
            print(f"Skills faltantes: {len(gaps.missing_skills)}")
            for gap in gaps.missing_skills:
                print(f"  - {gap.skill_name} ({gap.importance})")
            return gaps
        else:
            print("❌ Agente retornou None")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback

        traceback.print_exc()
        return None


async def test_education_agent(gaps: Optional[GapAnalysis]) -> Optional[PlanoEstudos]:
    """Testa o Agente Educacional."""
    print("\n" + "=" * 60)
    print("TESTE: Agente Educacional")
    print("=" * 60)

    if gaps is None:
        print("⚠️  Pulando teste - gaps não disponíveis")
        return None

    print(f"\n📝 Input (Gaps): {len(gaps.missing_skills)} skills faltantes\n")
    print("🔄 Processando...\n")

    try:
        result = await run_agent(education_agent, gaps, stream=False)
        if result and result.content:
            plano = result.content
            print("✅ Plano de estudos gerado!")
            print(f"\nCursos encontrados: {plano.quantidade}")
            print(f"Ordem sugerida: {plano.ordem}")
            for curso in plano.cursos[:3]:  # Mostra primeiros 3
                print(f"\n  - {curso.title}")
                print(f"    Plataforma: {curso.provider}")
                print(f"    URL: {curso.url}")
            return plano
        else:
            print("❌ Agente retornou None")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback

        traceback.print_exc()
        return None


async def test_cv_agent(perfil: Optional[PerfilCandidato]) -> Optional[CurriculumVitae]:
    """Testa o Agente de CV."""
    print("\n" + "=" * 60)
    print("TESTE: Agente Currículo")
    print("=" * 60)

    if perfil is None:
        print("⚠️  Pulando teste - perfil não disponível")
        return None

    print(f"\n📝 Input (Perfil): {perfil.model_dump()}\n")
    print("🔄 Processando...\n")

    try:
        result = await run_agent(cv_agent, perfil, stream=True)
        if result and result.content:
            cv = result.content
            print("✅ CV gerado!")

            # Debug: verificar tipo e conteúdo
            print(f"\n📊 Tipo do CV: {type(cv)}")
            print(f"📊 Tem cv_markdown? {hasattr(cv, 'cv_markdown')}")

            if hasattr(cv, "cv_markdown"):
                cv_text = cv.cv_markdown
                print(f"📊 Tamanho do CV: {len(cv_text)} caracteres")
                print("\n📄 CV completo:\n")
                print("=" * 60)
                print(cv_text)
                print("=" * 60)
            else:
                print("\n📄 CV (objeto completo):\n")
                print(cv)
            return cv
        else:
            print("❌ Agente retornou None")
            if result:
                print(f"Debug - result type: {type(result)}")
                print(f"Debug - result.content: {result.content}")
            return None
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback

        traceback.print_exc()
        return None


async def test_all_agents():
    """Testa todos os agentes em sequência."""
    print("\n" + "INICIANDO TESTES DOS AGENTES" + "\n")

    # Perfilador
    perfil = await test_profile_agent()

    # Recrutador
    # vaga = await test_employment_agent(perfil)

    # Analista
    # gaps = await test_analyst_agent(perfil, vaga)

    # Educacional
    # plano = await test_education_agent(gaps)

    # CV
    cv = await test_cv_agent(perfil)

    # Resumo
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    print(f"✅ Perfilador: {'OK' if perfil else 'FALHOU'}")
    # print(f"✅ Recrutador: {'OK' if vaga else 'FALHOU'}")
    # print(f"✅ Analista: {'OK' if gaps else 'FALHOU'}")
    # print(f"✅ Educacional: {'OK' if plano else 'FALHOU'}")
    print(f"✅ CV: {'OK' if cv else 'FALHOU'}")
    print("=" * 60 + "\n")


async def test_single_agent(agent_name: str):
    """Testa um agente específico."""
    agent_name = agent_name.lower()

    if agent_name == "perfilador" or agent_name == "profile":
        await test_profile_agent()
    elif agent_name == "recrutador" or agent_name == "employment":
        # Precisa de perfil primeiro
        perfil = await test_profile_agent()
        await test_employment_agent(perfil)
    elif agent_name == "analista" or agent_name == "analyst":
        # Precisa de perfil e vaga
        perfil = await test_profile_agent()
        vaga = await test_employment_agent(perfil)
        await test_analyst_agent(perfil, vaga)
    elif agent_name == "educacional" or agent_name == "education":
        # Precisa de gaps
        perfil = await test_profile_agent()
        vaga = await test_employment_agent(perfil)
        gaps = await test_analyst_agent(perfil, vaga)
        await test_education_agent(gaps)
    elif agent_name == "cv" or agent_name == "curriculo":
        perfil = await test_profile_agent()
        cv = await test_cv_agent(perfil)
    else:
        print(f"❌ Agente '{agent_name}' não reconhecido")
        print("Agentes disponíveis: perfilador, recrutador, analista, educacional, cv")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        agent_name = sys.argv[1]
        asyncio.run(test_single_agent(agent_name))
    else:
        asyncio.run(test_all_agents())
