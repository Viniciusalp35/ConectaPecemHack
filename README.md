# ConectaPecemHack - Sistema de Empregabilidade do Porto do Pecém

Sistema multi-agente desenvolvido para o Hackathon do Porto do Pecém que recebe o perfil de um candidato, encontra vagas reais, identifica gaps, busca cursos e gera um CV otimizado.

## 🏗️ Arquitetura

O sistema utiliza um pipeline sequencial com 5 agentes especializados:

1. **Perfilador (Extractor)**: Extrai e estrutura o perfil do candidato a partir de texto livre
2. **Recrutador (RAG)**: Busca vagas reais nos editais do Porto do Pecém usando Knowledge Base
3. **Analista de Carreira**: Compara perfil vs. vaga e identifica gaps (Gap Analysis)
4. **Education Scout**: Busca cursos online para suprir os gaps identificados
5. **Escritor de CV**: Gera CV otimizado e plano de ação com cursos sugeridos

## 🛠️ Stack Tecnológica

- **Linguagem**: Python
- **Framework de Agentes**: Agno (antigo Phidata)
- **LLM**: OpenAI (GPT-4o)
- **Validação de Dados**: Pydantic
- **Web Scraping**: crawl4ai (a ser integrado)
- **VectorDB**: LanceDB (a ser integrado)

## 📦 Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure a variável de ambiente:
```bash
export OPENAI_API_KEY=your_api_key_here
```

Ou crie um arquivo `.env`:
```
OPENAI_API_KEY=your_api_key_here
```

## 🚀 Uso

Execute o arquivo principal:

```bash
python main.py
```

O sistema irá:
1. Processar o input do usuário (perfil do candidato)
2. Buscar vagas adequadas
3. Identificar gaps
4. Buscar cursos
5. Gerar CV otimizado e plano de ação

Os resultados serão salvos em `results.json`.

## 📁 Estrutura do Projeto

```
.
├── main.py              # Arquivo principal com orquestrador do pipeline
├── team.py              # Definição da classe Team e dos 5 agentes
├── models.py            # Modelos Pydantic para validação de dados
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## 🔧 Próximos Passos (Integrações)

- [ ] Integração com crawl4ai para busca de cursos (responsável: companheiros)
- [ ] Integração com LanceDB para Knowledge Base de vagas (responsável: companheiros)
- [ ] Adicionar Knowledge Base ao Agente Recrutador
- [ ] Adicionar tool crawl4ai ao Agente Education Scout

## 📝 Notas

- O sistema foi projetado para ser resiliente a falhas (especialmente na busca de cursos)
- Todos os dados entre agentes são validados via Pydantic
- O pipeline é sequencial para garantir estabilidade na demo