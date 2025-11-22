import { Check, Circle, Clock, MapPin, Calendar, ExternalLink } from 'lucide-react';

const roadmapSteps = [
  {
    title: 'Curso NR-10 - Segurança em Instalações Elétricas',
    provider: 'SENAI Ceará',
    duration: '40 horas',
    location: 'Presencial - Maracanaú, CE',
    startDate: 'Próxima turma: 15 Jan 2025',
    status: 'todo',
    priority: 'high',
    description: 'Certificação obrigatória para trabalhar com eletricidade',
  },
  {
    title: 'Curso Técnico em Eletrotécnica',
    provider: 'SENAI Ceará',
    duration: '1200 horas (18 meses)',
    location: 'Semipresencial',
    startDate: 'Início: Fev 2025',
    status: 'todo',
    priority: 'high',
    description: 'Formação técnica completa em sistemas elétricos industriais',
  },
  {
    title: 'NR-12 - Segurança em Máquinas',
    provider: 'SESI Ceará',
    duration: '16 horas',
    location: 'Online',
    startDate: 'Disponível agora',
    status: 'todo',
    priority: 'medium',
    description: 'Certificação para trabalhar com manutenção de máquinas',
  },
  {
    title: 'Programa de Preparação para Indústria',
    provider: 'Instituto Pecém',
    duration: '3 meses',
    location: 'Presencial - São Gonçalo do Amarante',
    startDate: 'Jan 2025',
    status: 'todo',
    priority: 'medium',
    description: 'Prepara jovens para entrada no mercado industrial',
  },
];

export function StudyRoadmap() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Header */}
      <header className="bg-[#00979D] text-white px-6 py-8 shadow-lg">
        <h1 className="text-center mb-2">Seu Plano de Qualificação</h1>
        <p className="text-center text-teal-100">Caminho para suas oportunidades</p>
      </header>

      {/* Progress Summary */}
      <div className="px-4 py-6">
        <div className="bg-[#00979D] text-white rounded-2xl p-6 shadow-lg mb-6">
          <div className="flex items-center justify-between mb-4">
            <span>Progresso do Plano</span>
            <span className="text-2xl">0/4</span>
          </div>
          <div className="w-full bg-teal-600 rounded-full h-3">
            <div className="bg-white rounded-full h-3 w-0"></div>
          </div>
          <p className="mt-3 text-sm text-teal-100">Comece sua jornada de qualificação!</p>
        </div>

        {/* Roadmap Timeline */}
        <div className="relative">
          {/* Timeline Line */}
          <div className="absolute left-6 top-0 bottom-0 w-1 bg-[#00979D]"></div>

          {/* Roadmap Steps */}
          <div className="space-y-6">
            {roadmapSteps.map((step, index) => (
              <div key={index} className="relative pl-16">
                {/* Status Icon */}
                <div className="absolute left-0 top-2">
                  {step.status === 'completed' ? (
                    <div className="w-12 h-12 bg-green-500 rounded-full flex items-center justify-center shadow-lg">
                      <Check className="w-6 h-6 text-white" />
                    </div>
                  ) : step.status === 'inProgress' ? (
                    <div className="w-12 h-12 bg-[#EBB641] rounded-full flex items-center justify-center shadow-lg animate-pulse">
                      <Clock className="w-6 h-6 text-gray-800" />
                    </div>
                  ) : (
                    <div className="w-12 h-12 bg-gray-300 rounded-full flex items-center justify-center shadow-lg">
                      <Circle className="w-6 h-6 text-white" />
                    </div>
                  )}
                </div>

                {/* Step Card */}
                <div className={`bg-white rounded-2xl shadow-lg border-2 overflow-hidden ${
                  step.priority === 'high' ? 'border-[#EBB641]' : 'border-gray-100'
                }`}>
                  {/* Priority Badge */}
                  {step.priority === 'high' && (
                    <div className="bg-[#EBB641] text-gray-800 px-5 py-2 text-sm">
                      🎯 Alta Prioridade - Requerido para Eletricista Júnior
                    </div>
                  )}

                  <div className="p-5">
                    <h3 className="text-[#00979D] mb-2">{step.title}</h3>
                    <p className="text-gray-600 mb-4">{step.description}</p>

                    {/* Details */}
                    <div className="space-y-2 text-sm text-gray-700 mb-4">
                      <div className="flex items-start gap-2">
                        <ExternalLink className="w-4 h-4 mt-0.5 flex-shrink-0" />
                        <span>{step.provider}</span>
                      </div>
                      <div className="flex items-start gap-2">
                        <Clock className="w-4 h-4 mt-0.5 flex-shrink-0" />
                        <span>{step.duration}</span>
                      </div>
                      <div className="flex items-start gap-2">
                        <MapPin className="w-4 h-4 mt-0.5 flex-shrink-0" />
                        <span>{step.location}</span>
                      </div>
                      <div className="flex items-start gap-2">
                        <Calendar className="w-4 h-4 mt-0.5 flex-shrink-0" />
                        <span>{step.startDate}</span>
                      </div>
                    </div>

                    {/* Action Buttons */}
                    <div className="flex gap-2">
                      <button className="flex-1 bg-[#00979D] text-white py-4 rounded-xl hover:bg-[#008389] transition-all shadow-md">
                        Ver Detalhes
                      </button>
                      <button className="flex-1 bg-white text-[#00979D] border-2 border-[#00979D] py-4 rounded-xl hover:bg-teal-50 transition-colors">
                        Inscrever-se
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Help Card */}
        <div className="mt-8 bg-yellow-50 rounded-2xl p-6 border-2 border-[#EBB641]">
          <h3 className="text-gray-800 mb-2">Precisa de Ajuda?</h3>
          <p className="text-gray-700 mb-4">
            Nossa equipe pode auxiliar com inscrições, financiamento e transporte para os cursos.
          </p>
          <button className="w-full bg-[#EBB641] text-gray-800 py-4 rounded-xl hover:bg-[#d9a531] transition-all shadow-md">
            Falar com Orientador
          </button>
        </div>
      </div>
    </div>
  );
}