from team import time
from rich.console import Console

console = Console()


def main():
    # 1. Cria o time
    console.print(
        "\n[bold blue]🚀 SISTEMA DE EMPREGABILIDADE (MODE: TEAM ORCHESTRATION)[/bold blue]"
    )
    console.print("O Time de Agentes está pronto. Digite sua história para começar.\n")

    while True:
        try:
            # 2. Input do usuário
            user_input = console.input("[bold green]Você:[/bold green] ").strip()

            if user_input.lower() in ["sair", "exit", "quit"]:
                console.print("[bold blue]👋 Até logo![/bold blue]")
                break

            if not user_input:
                continue

            console.print(
                "\n[bold yellow]🤖 O Time está trabalhando...[/bold yellow]\n"
            )

            # 3. Execução do Time
            # O método .print_response() gerencia o stream e mostra a saída dos membros
            time.print_response(user_input, stream=True, markdown=True)

            console.print("\n" + "-" * 50 + "\n")

        except KeyboardInterrupt:
            console.print("\n[bold red]🛑 Execução interrompida.[/bold red]")
            break
        except Exception as e:
            console.print(f"\n[bold red]❌ Erro no Time:[/bold red] {e}")
            # Opcional: mostrar traceback se necessário
            # import traceback; traceback.print_exc()


if __name__ == "__main__":
    main()
