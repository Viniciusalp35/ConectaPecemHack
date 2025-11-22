import { MapPin, Clock, TrendingUp, AlertCircle } from 'lucide-react';

const jobs = [
  {
    title: 'Eletricista Júnior',
    company: 'Porto do Pecém - Empresa A',
    location: 'São Gonçalo do Amarante, CE',
    type: 'Tempo Integral',
    matchScore: 80,
    matchingSkills: ['Fiação Elétrica', 'Instalação Residencial', 'Trabalho em Equipe'],
    missingSkills: ['Certificação NR-10'],
    hasGap: true,
  },
  {
    title: 'Auxiliar de Manutenção',
    company: 'Indústria Pecém',
    location: 'São Gonçalo do Amarante, CE',
    type: 'Tempo Integral',
    matchScore: 65,
    matchingSkills: ['Manutenção Preventiva', 'Uso de Ferramentas'],
    missingSkills: ['Certificação NR-12', 'Curso Técnico em Mecânica'],
    hasGap: true,
  },
  {
    title: 'Assistente de Eletrotécnica',
    company: 'Terminal Portuário',
    location: 'São Gonçalo do Amarante, CE',
    type: 'Tempo Integral',
    matchScore: 45,
    matchingSkills: ['Diagnóstico de Problemas', 'Atenção aos Detalhes'],
    missingSkills: ['Curso Técnico em Eletrotécnica', 'NR-10', 'Experiência Industrial'],
    hasGap: true,
  },
];

export function OpportunityMatch() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Header */}
      <header className="bg-[#00979D] text-white px-6 py-8 shadow-lg">
        <h1 className="text-center mb-2">Oportunidades para Você</h1>
        <p className="text-center text-teal-100">Vagas compatíveis com seu perfil</p>
      </header>

      {/* Content */}
      <div className="px-4 py-6 space-y-5">
        {jobs.map((job, index) => (
          <div key={index} className="bg-white rounded-2xl shadow-lg border-2 border-gray-100 overflow-hidden">
            {/* Job Header */}
            <div className="p-5 border-b-2 border-gray-100">
              <h3 className="text-[#00979D] mb-2">{job.title}</h3>
              <p className="text-gray-600 mb-3">{job.company}</p>
              
              <div className="flex flex-col gap-2 text-sm text-gray-600">
                <div className="flex items-center gap-2">
                  <MapPin className="w-4 h-4" />
                  <span>{job.location}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Clock className="w-4 h-4" />
                  <span>{job.type}</span>
                </div>
              </div>
            </div>

            {/* Match Score */}
            <div className="bg-[#EBB641] p-5 border-b-2 border-yellow-600">
              <div className="flex items-center justify-between mb-3">
                <div className="flex items-center gap-2">
                  <TrendingUp className="w-5 h-5 text-gray-800" />
                  <span className="text-gray-800">Compatibilidade</span>
                </div>
                <span className="text-2xl text-gray-800">{job.matchScore}%</span>
              </div>
              
              <div className="w-full bg-yellow-600 rounded-full h-3">
                <div
                  className="bg-white rounded-full h-3 transition-all"
                  style={{ width: `${job.matchScore}%` }}
                ></div>
              </div>
            </div>

            {/* Matching Skills */}
            <div className="p-5 border-b-2 border-gray-100">
              <p className="text-xs text-[#00979D] mb-3">✓ SUAS COMPETÊNCIAS QUE COMBINAM</p>
              <div className="flex flex-wrap gap-2">
                {job.matchingSkills.map((skill, skillIndex) => (
                  <span
                    key={skillIndex}
                    className="bg-teal-50 text-[#00979D] px-4 py-2 rounded-full text-sm border-2 border-teal-200"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>

            {/* Skill Gap */}
            {job.hasGap && (
              <div className="bg-orange-50 p-5 border-b-2 border-orange-200">
                <div className="flex items-center gap-2 mb-3">
                  <AlertCircle className="w-5 h-5 text-orange-600" />
                  <p className="text-xs text-orange-700">QUALIFICAÇÕES NECESSÁRIAS</p>
                </div>
                <div className="flex flex-wrap gap-2">
                  {job.missingSkills.map((skill, skillIndex) => (
                    <span
                      key={skillIndex}
                      className="bg-white text-orange-700 px-4 py-2 rounded-full text-sm border-2 border-orange-300"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Action Button */}
            <div className="p-5">
              {job.hasGap ? (
                <button className="w-full bg-[#EBB641] text-gray-800 py-5 rounded-xl hover:bg-[#d9a531] transition-all shadow-md">
                  Qualificar Agora
                </button>
              ) : (
                <button className="w-full bg-[#00979D] text-white py-5 rounded-xl hover:bg-[#008389] transition-all shadow-md">
                  Candidatar-se
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}