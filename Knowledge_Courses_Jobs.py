import asyncio
from agno.agent import Agent
from agno.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.embedder.google import GeminiEmbedder 

courses_vector_db = LanceDb(
        table_name="available_courses",
        uri="/tmp/lancedb",
        search_type=SearchType.hybrid,
        embedder=GeminiEmbedder()
        )

jobs_vector_db = LanceDb(
        table_name="job_offers",
        uri="/tmp/lancedb",
        search_type=SearchType.hybrid,
        embedder=GeminiEmbedder()
        )

courses_knowledge = Knowledge(
        vector_db=courses_vector_db,
        )

jobs_knowledge = Knowledge(
        vector_db=jobs_vector_db
        )

courses_knowledge.add_content_async(
    name="Cursos Disponíveis",
    path="data/json_courses.json" 
)

jobs_knowledge.add_content_async(
    name="Vagas Disponíveis",
    path="data/job_offers.pdf" 
)
