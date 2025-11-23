from pydantic import BaseModel, Field
from typing import List, Optional


class PerfilCandidato(BaseModel):
    """Representa o perfil do candidato extraído do currículo."""

    skills: List[str] = Field(default_factory=list, description="Skills do candidato")
    experience: List[str] = Field(
        default_factory=list, description="Experiência do candidato"
    )
    education: List[str] = Field(
        default_factory=list, description="Educação do candidato"
    )
    summary: Optional[str] = Field(None, description="Texto original ou resumo")


class VagaEmprego(BaseModel):
    """Representa a vaga de emprego analisada."""

    title: str = Field(default="", description="Título da vaga de emprego")
    description: str = Field(default="", description="Descrição da vaga de emprego")
    requirements: List[str] = Field(
        default_factory=list, description="Requisitos da vaga de emprego"
    )


class SkillGap(BaseModel):
    """Representa uma habilidade faltante identificada na análise."""

    skill_name: str = Field(default="", description="Nome da habilidade faltante")
    importance: str = Field(
        default="", description="Importância (obrigatória, desejável)"
    )


class GapAnalysisInput(BaseModel):
    """Input combinado para o Agente Analista: Perfil + Vaga."""

    perfil: PerfilCandidato = Field(..., description="Perfil do candidato")
    vaga: VagaEmprego = Field(..., description="Vaga de emprego a ser analisada")


class GapAnalysis(BaseModel):
    """Representa o gap de habilidades identificado entre o perfil do candidato e a vaga de emprego."""

    job_title: str = Field(default="", description="Título da vaga de emprego")
    missing_skills: List[SkillGap] = Field(
        default_factory=list, description="Habilidades faltantes"
    )


class Curso(BaseModel):
    """Representa um curso encontrado para suprir um gap."""

    title: str = Field(default="", description="Título do curso")
    provider: Optional[str] = Field(None, description="Plataforma ou instituição")
    url: Optional[str] = Field(None, description="URL do curso")
    description: Optional[str] = Field(None, description="Descrição do curso")
    duration: Optional[str] = Field(None, description="Duração estimada")
    skill_covered: List[str] = Field(
        default_factory=list, description="Habilidades que este curso cobre"
    )


class PlanoEstudos(BaseModel):
    """Representa um plano de estudos sugerido para o candidato."""

    skill_gaps: List[SkillGap] = Field(
        default_factory=list, description="Gaps que foram buscados"
    )
    cursos: List[Curso] = Field(
        default_factory=list, description="Lista de cursos sugeridos"
    )
    quantidade: int = Field(0, description="Quantidade de cursos sugeridos")
    ordem: List[str] = Field(
        default_factory=list, description="Ordem dos cursos sugeridos"
    )


class CurriculumVitae(BaseModel):
    """CV do candidato em formato Markdown, pronto para conversão em PDF."""

    cv_markdown: str = Field(
        ..., description="Currículo completo formatado em Markdown (.md)"
    )

class CourseList():
    courses: list[Curso]
