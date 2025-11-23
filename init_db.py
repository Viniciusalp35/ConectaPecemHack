import asyncio
from Knowledge_Courses_Jobs import courses_knowledge, jobs_knowledge


async def init_db():
    print("Iniciando população do banco de dados...")

    # 1. Cursos
    print("\nProcessando Cursos (add_content)...")
    # Na v2.0, isso já dispara a vetorização!
    await courses_knowledge.add_content_async(
        name="Cursos Disponíveis", path="data/json_courses.json"
    )
    print("Cursos adicionados e vetorizados")

    # 2. Vagas
    print("\nProcessando Vagas (add_content)...")
    await jobs_knowledge.add_content_async(
        name="Vagas Disponíveis", path="data/job_offers.pdf"
    )
    print("Vagas adicionadas e vetorizadas!")

    print("\nBanco de dados pronto.")


if __name__ == "__main__":
    asyncio.run(init_db())
