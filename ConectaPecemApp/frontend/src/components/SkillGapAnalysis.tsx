import { CheckCircle, AlertCircle, ArrowLeft, BookOpen, Clock, TrendingUp } from 'lucide-react';

interface SkillGapAnalysisProps {
  onBack: () => void;
  onEnrollCourse: () => void;
}

export function SkillGapAnalysis({ onBack, onEnrollCourse }: SkillGapAnalysisProps) {
  const matchPercentage = 80;
  const circumference = 2 * Math.PI * 70;
  const strokeDashoffset = circumference - (matchPercentage / 100) * circumference;

  const matchedSkills = [
    'Instalação Residencial',
    'Fiação Elétrica Básica',
    'Trabalho em Equipe',
    'Uso de Ferramentas Manuais',
    'Diagnóstico de Problemas',
    'Manutenção Preventiva',
  ];

  const missingSkills = [
    {
      name: 'Certificação NR-10',
      description: 'Segurança em Instalações Elétricas',
      priority: 'high',
    },
    {
      name: 'Experiência Industrial',
      description: 'Prática em ambiente industrial',
      priority: 'medium',
    },
  ];

  const recommendedCourse = {
    title: 'Curso NR-10 - Segurança em Instalações Elétricas',
    provider: 'SENAI Ceará',
    duration: '40 horas',
    startDate: 'Próxima turma: 15 Jan 2025',
    location: 'Presencial - Maracanaú, CE',
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Header */}
      <header className="bg-[#00979D] text-white px-6 py-8 shadow-lg">
        <button
          onClick={onBack}
          className="flex items-center gap-2 mb-4 hover:bg-teal-700 px-3 py-2 rounded-lg transition-colors -ml-3"
        >
          <ArrowLeft className="w-5 h-5" />
          <span>Voltar</span>
        </button>
        <h1 className="text-center mb-2">Análise de Compatibilidade</h1>
        <p className="text-center text-lg text-white">
          <span className="inline-block bg-teal-700 px-4 py-2 rounded-lg">
            Eletricista Júnior
          </span>
        </p>
      </header>

      {/* Content */}
      <div className="px-4 py-6 space-y-6">
        {/* Match Meter - Hero Section */}
        <div className="bg-white rounded-2xl shadow-lg p-8 border-2 border-gray-100">
          <div className="flex flex-col items-center">
            {/* Circular Progress */}
            <div className="relative w-48 h-48 mb-4">
              <svg className="w-48 h-48 transform -rotate-90">
                {/* Background Circle */}
                <circle
                  cx="96"
                  cy="96"
                  r="70"
                  stroke="#e5e7eb"
                  strokeWidth="12"
                  fill="none"
                />
                {/* Progress Circle */}
                <circle
                  cx="96"
                  cy="96"
                  r="70"
                  stroke="#00979D"
                  strokeWidth="12"
                  fill="none"
                  strokeDasharray={circumference}
                  strokeDashoffset={strokeDashoffset}
                  strokeLinecap="round"
                  className="transition-all duration-1000"
                />
              </svg>
              {/* Center Text */}
              <div className="absolute inset-0 flex flex-col items-center justify-center">
                <div className="text-5xl text-[#00979D]" style={{ fontWeight: 700 }}>
                  {matchPercentage}%
                </div>
                <div className="text-sm text-gray-600 mt-1">Compatível</div>
              </div>
            </div>

            {/* Encouraging Message */}
            <div className="text-center">
              <h2 className="text-xl text-[#00979D] mb-2" style={{ fontWeight: 600 }}>
                Você tem {matchPercentage}% do perfil!
              </h2>
              <p className="text-gray-600">
                Você está quase lá. Com apenas 1 qualificação, você estará pronto para esta vaga!
              </p>
            </div>
          </div>
        </div>

        {/* Comparison List */}
        <div className="space-y-4">
          {/* What You Have - Matched Skills */}
          <div className="bg-white rounded-2xl shadow-lg border-2 border-[#00979D] overflow-hidden">
            <div className="bg-[#00979D] text-white px-6 py-4">
              <div className="flex items-center gap-3">
                <TrendingUp className="w-6 h-6" />
                <h3 className="text-lg" style={{ fontWeight: 600 }}>
                  ✓ O que você já tem
                </h3>
              </div>
            </div>
            <div className="p-6">
              <div className="space-y-3">
                {matchedSkills.map((skill, index) => (
                  <div
                    key={index}
                    className="flex items-start gap-3 bg-teal-50 p-4 rounded-xl border border-teal-200"
                  >
                    <CheckCircle className="w-6 h-6 text-[#00979D] flex-shrink-0 mt-0.5" />
                    <span className="text-gray-800">{skill}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* What's Missing - Skill Gaps */}
          <div className="bg-white rounded-2xl shadow-lg border-2 border-[#EBB641] overflow-hidden">
            <div className="bg-[#EBB641] text-gray-800 px-6 py-4">
              <div className="flex items-center gap-3">
                <AlertCircle className="w-6 h-6" />
                <h3 className="text-lg" style={{ fontWeight: 600 }}>
                  ! O que falta
                </h3>
              </div>
            </div>
            <div className="p-6">
              <div className="space-y-3">
                {missingSkills.map((skill, index) => (
                  <div
                    key={index}
                    className="bg-yellow-50 p-5 rounded-xl border-2 border-yellow-300"
                  >
                    <div className="flex items-start gap-3">
                      <AlertCircle className="w-6 h-6 text-[#EBB641] flex-shrink-0 mt-0.5" />
                      <div className="flex-1">
                        <h4 className="text-gray-800 mb-1" style={{ fontWeight: 600 }}>
                          {skill.name}
                        </h4>
                        <p className="text-sm text-gray-600">{skill.description}</p>
                        {skill.priority === 'high' && (
                          <span className="inline-block mt-2 bg-orange-500 text-white px-3 py-1 rounded-full text-xs">
                            Prioridade Alta
                          </span>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Actionable Roadmap */}
        <div className="bg-gradient-to-br from-teal-50 to-yellow-50 rounded-2xl shadow-lg border-2 border-[#00979D] overflow-hidden">
          <div className="bg-[#00979D] text-white px-6 py-4">
            <h3 className="text-lg text-center" style={{ fontWeight: 600 }}>
              💡 Como resolver isso?
            </h3>
          </div>
          
          <div className="p-6">
            <div className="bg-white rounded-xl p-5 shadow-md border-2 border-yellow-300 mb-5">
              <div className="flex items-start gap-3 mb-4">
                <BookOpen className="w-6 h-6 text-[#EBB641] flex-shrink-0" />
                <div className="flex-1">
                  <h4 className="text-gray-800 mb-2" style={{ fontWeight: 600 }}>
                    {recommendedCourse.title}
                  </h4>
                  <div className="space-y-2 text-sm text-gray-700">
                    <div className="flex items-center gap-2">
                      <span className="text-[#00979D]">📍</span>
                      <span>{recommendedCourse.provider}</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <Clock className="w-4 h-4 text-[#00979D]" />
                      <span>{recommendedCourse.duration}</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-[#00979D]">📅</span>
                      <span>{recommendedCourse.startDate}</span>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-[#00979D]">📍</span>
                      <span>{recommendedCourse.location}</span>
                    </div>
                  </div>
                </div>
              </div>

              {/* Impact Statement */}
              <div className="bg-teal-50 rounded-lg p-4 border border-teal-200 mb-4">
                <p className="text-sm text-gray-800 text-center">
                  <span className="text-[#00979D]" style={{ fontWeight: 600 }}>
                    ⚡ Ao completar este curso:
                  </span>
                  <br />
                  Sua compatibilidade aumentará para <span style={{ fontWeight: 700 }}>95%</span> e você 
                  estará qualificado para se candidatar!
                </p>
              </div>

              {/* CTA Button */}
              <button
                onClick={onEnrollCourse}
                className="w-full bg-[#EBB641] text-gray-800 py-5 rounded-xl hover:bg-[#d9a531] transition-all shadow-lg text-lg"
                style={{ fontWeight: 600 }}
              >
                Inscrever no Curso
              </button>
            </div>

            {/* Alternative Action */}
            <button className="w-full bg-white text-[#00979D] border-2 border-[#00979D] py-4 rounded-xl hover:bg-teal-50 transition-colors">
              Ver Plano de Estudos Completo
            </button>
          </div>
        </div>

        {/* Encouragement Footer */}
        <div className="bg-white rounded-2xl p-6 text-center border-2 border-gray-100">
          <p className="text-gray-700 mb-2">
            🎯 <span style={{ fontWeight: 600 }}>Você está no caminho certo!</span>
          </p>
          <p className="text-sm text-gray-600">
            Muitos profissionais começaram exatamente onde você está. 
            Com dedicação, você alcançará seus objetivos!
          </p>
        </div>
      </div>
    </div>
  );
}
