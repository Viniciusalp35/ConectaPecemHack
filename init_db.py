import asyncio
from Knowledge_Courses_Jobs import courses_knowledge, jobs_knowledge


async def init_db_v2():
    print("🚀 [AGNO 2.0] Iniciando população do banco de dados...")

    # 1. Cursos
    print("\n📚 Processando Cursos (add_content)...")
    # Na v2.0, isso já dispara a vetorização!
    await courses_knowledge.add_content_async(
        name="Cursos Disponíveis", path="data/json_courses.json"
    )
    print("✅ Cursos adicionados e vetorizados!")

    # 2. Vagas
    print("\n📚 Processando Vagas (add_content)...")
    await jobs_knowledge.add_content_async(
        name="Vagas Disponíveis", path="data/job_offers.pdf"
    )
    print("✅ Vagas adicionadas e vetorizadas!")

    print("\n🏁 Banco de dados PRONTO. Pode rodar os testes.")


if __name__ == "__main__":
    asyncio.run(init_db_v2())
