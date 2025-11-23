from markdown_pdf import MarkdownPdf, Section
from agno.tools import tool


@tool()
def save_cv_to_pdf(markdown_text: str, filename: str = "curriculo.pdf"):
    """
    Salva o texto do currículo em um arquivo PDF local.

    Args:
        markdown_text (str): O conteúdo completo do CV em formato Markdown.
        filename (str): O nome do arquivo a ser salvo (padrão: curriculo.pdf).

    Returns:
        str: Mensagem de confirmação com o caminho do arquivo.
    """
    try:
        pdf = MarkdownPdf()
        pdf.add_section(Section(markdown_text, toc=False))
        pdf.save(filename)
        return f"Sucesso: Arquivo salvo como '{filename}'."
    except Exception as e:
        return f"Erro ao salvar PDF: {str(e)}"
