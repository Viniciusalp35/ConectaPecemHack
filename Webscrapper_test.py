from agents import (scrapper_agent)
import asyncio
import json
from webscrapper_tool import Webscrapper as webt
from trinner import trinner

async def main():
    all_courses = []

    raw_data = await webt("https://www.senai-ce.org.br/cursos?cidade=44")
    crops = trinner(raw_data)
    for i in range(len(crops)):
        try:
            print(f"🔄 Carregando crop {i+1}")
            result = await scrapper_agent.arun(input=crops[i])

            if result.content and result.content.courses:
                course_find = result.content.courses
                for course in course_find:
                    if course.title != "null" and course not in all_courses and course.title != "" and course.url != "null":
                        all_courses.append(course.model_dump())
            else:
                print(f"Nada encontrado no Crop {i+1}")
                continue
        except Exception as e:
            print(f"Error na execução: {e}")

    json_estruturado = {"courses": all_courses}

    json_formatado = json.dumps(json_estruturado,indent=2,ensure_ascii=False)

    # json_formatado = result.content.model_dump_json(indent=2)

    # with open("Resultado_MD.txt","w",encoding='utf-8') as MD:
    #     MD.write(dados)
    print("Carregamento de Cursos finalizado ✅\nResultados podem ser encontrados no arquivo Resultado_LLM.json")

    with open("Resultados_LLM.json","w",encoding="utf-8") as teste:
        teste.write(str(json_formatado))


if __name__ == "__main__":
    asyncio.run(main())

