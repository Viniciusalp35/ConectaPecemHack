from team import time
import asyncio


async def main():
    session_id = "demo_session"
    print("🚢 Ajudante de Empregabilidade - Porto do Pecém e Complexo")
    print("Digite 'sair' ou 'exit' para encerrar\n")

    while True:
        user_input = input("Input: ")
        if user_input.lower() == "sair" or user_input.lower() == "exit":
            break
        if not user_input:
            continue

        try:
            response = await time.arun(user_input, session_id=session_id)
            print(response.content)

        except Exception as e:
            print("\nErro:", str(e))


if __name__ == "__main__":
    asyncio.run(main())
