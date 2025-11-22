import { ArrowRight, CheckCircle, Zap } from 'lucide-react';
import { useState } from 'react';

const translations = [
  {
    informal: 'Ajudei meu tio com instalação elétrica em casas',
    formal: 'Conhecimento Básico em Eletricidade Residencial',
    skills: ['Fiação Elétrica', 'Instalação Residencial', 'Trabalho em Equipe'],
  },
  {
    informal: 'Consertei alguns aparelhos eletrônicos',
    formal: 'Manutenção e Reparo de Equipamentos Eletrônicos',
    skills: ['Diagnóstico de Problemas', 'Reparo Manual', 'Atenção aos Detalhes'],
  },
  {
    informal: 'Ajudei na manutenção de máquinas',
    formal: 'Experiência em Manutenção Mecânica',
    skills: ['Manutenção Preventiva', 'Uso de Ferramentas', 'Resolução de Problemas'],
  },
];

export function TranslationDashboard() {
  const [showPDFModal, setShowPDFModal] = useState(false);

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Header */}
      <header className="bg-[#00979D] text-white px-6 py-8 shadow-lg">
        <h1 className="text-center mb-2">Seu Perfil Profissional</h1>
        <p className="text-center text-teal-100">IA traduziu sua experiência</p>
      </header>

      {/* Content */}
      <div className="px-4 py-6 space-y-4">
        {/* Stats */}
        <div className="bg-[#EBB641] text-gray-800 rounded-2xl p-6 shadow-lg">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-2">
              <Zap className="w-6 h-6" />
              <span>Competências Identificadas</span>
            </div>
            <span className="text-3xl">9</span>
          </div>
          <div className="w-full bg-yellow-600 rounded-full h-3">
            <div className="bg-white rounded-full h-3 w-3/4"></div>
          </div>
          <p className="mt-2 text-sm text-gray-700">75% do perfil completo</p>
        </div>

        {/* Translation Cards */}
        {translations.map((item, index) => (
          <div key={index} className="bg-white rounded-2xl shadow-lg border-2 border-gray-100 overflow-hidden">
            {/* Informal Input */}
            <div className="bg-gray-50 p-5 border-b-2 border-gray-200">
              <p className="text-xs text-gray-500 mb-2">SUA EXPERIÊNCIA</p>
              <p className="text-gray-800">{item.informal}</p>
            </div>

            {/* Arrow Indicator */}
            <div className="flex justify-center -my-4 relative z-10">
              <div className="bg-[#00979D] text-white rounded-full p-3 shadow-lg">
                <ArrowRight className="w-5 h-5 rotate-90" />
              </div>
            </div>

            {/* Formal Translation */}
            <div className="bg-teal-50 p-5 border-t-2 border-[#EBB641]">
              <div className="flex items-center gap-2 mb-3">
                <CheckCircle className="w-5 h-5 text-[#00979D]" />
                <p className="text-xs text-[#00979D]">COMPETÊNCIA PROFISSIONAL</p>
              </div>
              <p className="text-gray-800 mb-4">{item.formal}</p>

              {/* Skill Badges */}
              <div className="flex flex-wrap gap-2">
                {item.skills.map((skill, skillIndex) => (
                  <span
                    key={skillIndex}
                    className="bg-[#EBB641] text-gray-800 px-4 py-2 rounded-full text-sm border-2 border-yellow-600"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          </div>
        ))}

        {/* Add More Button */}
        <button className="w-full bg-white text-[#00979D] border-2 border-[#00979D] py-5 rounded-xl hover:bg-teal-50 transition-colors">
          + Adicionar Mais Experiências
        </button>

        {/* Export Resume Button */}
        <button 
          onClick={() => setShowPDFModal(true)}
          className="w-full bg-[#EBB641] text-gray-800 py-5 rounded-xl hover:bg-[#d9a531] transition-colors shadow-lg"
        >
          📄 Gerar Currículo Profissional
        </button>
      </div>

      {/* PDF Preview Modal */}
      {showPDFModal && <PDFPreviewModal onClose={() => setShowPDFModal(false)} />}
    </div>
  );
}