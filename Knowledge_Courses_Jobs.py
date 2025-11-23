from agno.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector
from agno.knowledge.embedder.ollama import OllamaEmbedder
from agno.db.postgres import PostgresDb

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

embedder = OllamaEmbedder(id="openhermes")

course_content_db = PostgresDb(db_url=db_url, knowledge_table="course_contents")

jobs_content_db = PostgresDb(db_url=db_url, knowledge_table="jobs_contents")

courses_vector_db = PgVector(
    table_name="available_courses",
    db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    embedder=embedder,
)

jobs_vector_db = PgVector(
    table_name="job_offers",
    db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    embedder=embedder,
)

courses_knowledge = Knowledge(
    vector_db=courses_vector_db,
)

jobs_knowledge = Knowledge(vector_db=jobs_vector_db)
