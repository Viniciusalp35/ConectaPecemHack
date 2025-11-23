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
            response = time.arun(user_input, session_id=session_id, stream=True)
            last_result = None
            async for chunk in response:
                last_result = chunk
            return last_result

        except Exception as e:
            print("\nErro:", str(e))


if __name__ == "__main__":
    asyncio.run(main())
