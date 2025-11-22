import { X, Download, Share2, FileText } from 'lucide-react';

interface PDFPreviewModalProps {
  onClose: () => void;
}

export function PDFPreviewModal({ onClose }: PDFPreviewModalProps) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
      {/* Modal Container */}
      <div className="bg-white rounded-3xl shadow-2xl max-w-lg w-full max-h-[90vh] flex flex-col overflow-hidden">
        {/* Modal Header */}
        <div className="bg-[#00979D] text-white px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <FileText className="w-6 h-6" />
            <div>
              <h2 className="text-lg">Pré-visualização do Currículo</h2>
              <p className="text-sm text-teal-100">Pronto para compartilhar</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-white hover:bg-teal-700 rounded-full p-2 transition-colors"
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        {/* PDF Document Preview */}
        <div className="flex-1 overflow-y-auto bg-gray-100 p-4">
          {/* The Actual Document - Professional Resume */}
          <div className="bg-white shadow-lg mx-auto" style={{ width: '210mm', maxWidth: '100%', aspectRatio: '210/297' }}>
            {/* Document Content */}
            <div className="p-8 text-black">
              {/* Document Header */}
              <div className="border-b-2 border-gray-300 pb-4 mb-6">
                <div className="flex items-start justify-between">
                  <div>
                    <h1 className="text-2xl mb-1" style={{ fontWeight: 700 }}>João Silva Santos</h1>
                    <p className="text-sm text-gray-600">São Gonçalo do Amarante, CE</p>
                    <p className="text-sm text-gray-600">+55 85 99999-9999 • joao.silva@email.com</p>
                  </div>
                  <div className="text-right">
                    <div className="text-xs text-[#00979D]" style={{ fontWeight: 600 }}>CONECTA PECÉM</div>
                    <div className="text-xs text-gray-500">Perfil Certificado</div>
                  </div>
                </div>
              </div>

              {/* Objective */}
              <div className="mb-6">
                <h2 className="text-lg mb-2 text-black border-b border-gray-300 pb-1" style={{ fontWeight: 700 }}>
                  OBJETIVO PROFISSIONAL
                </h2>
                <p className="text-sm text-gray-800">
                  Busco oportunidade na área industrial como Eletricista ou Auxiliar de Manutenção, 
                  aplicando minhas competências práticas e disposição para aprendizado contínuo.
                </p>
              </div>

              {/* Competências Técnicas */}
              <div className="mb-6">
                <h2 className="text-lg mb-3 text-black border-b border-gray-300 pb-1" style={{ fontWeight: 700 }}>
                  COMPETÊNCIAS TÉCNICAS
                </h2>
                <div className="space-y-3">
                  <div>
                    <h3 className="text-sm mb-1" style={{ fontWeight: 600 }}>Conhecimento Básico em Eletricidade Residencial</h3>
                    <ul className="text-sm text-gray-700 list-disc list-inside pl-2">
                      <li>Fiação Elétrica</li>
                      <li>Instalação Residencial</li>
                      <li>Trabalho em Equipe</li>
                    </ul>
                  </div>
                  <div>
                    <h3 className="text-sm mb-1" style={{ fontWeight: 600 }}>Manutenção e Reparo de Equipamentos Eletrônicos</h3>
                    <ul className="text-sm text-gray-700 list-disc list-inside pl-2">
                      <li>Diagnóstico de Problemas</li>
                      <li>Reparo Manual</li>
                      <li>Atenção aos Detalhes</li>
                    </ul>
                  </div>
                  <div>
                    <h3 className="text-sm mb-1" style={{ fontWeight: 600 }}>Experiência em Manutenção Mecânica</h3>
                    <ul className="text-sm text-gray-700 list-disc list-inside pl-2">
                      <li>Manutenção Preventiva</li>
                      <li>Uso de Ferramentas</li>
                      <li>Resolução de Problemas</li>
                    </ul>
                  </div>
                </div>
              </div>

              {/* Experiência Prática */}
              <div className="mb-6">
                <h2 className="text-lg mb-3 text-black border-b border-gray-300 pb-1" style={{ fontWeight: 700 }}>
                  EXPERIÊNCIA PRÁTICA
                </h2>
                <div className="space-y-3">
                  <div>
                    <h3 className="text-sm mb-1" style={{ fontWeight: 600 }}>Auxiliar em Instalações Elétricas</h3>
                    <p className="text-xs text-gray-600 mb-1">Trabalhos Informais • 2022 - 2024</p>
                    <p className="text-sm text-gray-700">
                      Auxiliei em instalações elétricas residenciais, desenvolvendo conhecimento 
                      prático em fiação, conexões e resolução de problemas elétricos básicos.
                    </p>
                  </div>
                  <div>
                    <h3 className="text-sm mb-1" style={{ fontWeight: 600 }}>Técnico em Reparos Eletrônicos</h3>
                    <p className="text-xs text-gray-600 mb-1">Autônomo • 2023 - Atual</p>
                    <p className="text-sm text-gray-700">
                      Realizei manutenção e conserto de aparelhos eletrônicos, desenvolvendo 
                      habilidades de diagnóstico e reparo manual.
                    </p>
                  </div>
                </div>
              </div>

              {/* Qualificações em Andamento */}
              <div className="mb-4">
                <h2 className="text-lg mb-2 text-black border-b border-gray-300 pb-1" style={{ fontWeight: 700 }}>
                  QUALIFICAÇÕES EM ANDAMENTO
                </h2>
                <ul className="text-sm text-gray-700 list-disc list-inside">
                  <li>NR-10 - Segurança em Instalações Elétricas (SENAI)</li>
                  <li>Curso Técnico em Eletrotécnica (Previsão 2025)</li>
                </ul>
              </div>

              {/* Footer */}
              <div className="mt-8 pt-4 border-t border-gray-200 text-center">
                <p className="text-xs text-gray-500">
                  Currículo gerado através da plataforma Conecta Pecém
                </p>
                <p className="text-xs text-gray-400">
                  www.conectapecem.com.br
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Action Bar - Fixed Footer */}
        <div className="bg-white border-t-2 border-gray-200 px-6 py-5">
          <div className="space-y-3">
            {/* Primary Actions */}
            <div className="grid grid-cols-2 gap-3">
              <button className="bg-[#EBB641] text-gray-800 py-4 px-4 rounded-xl hover:bg-[#d9a531] transition-all shadow-md flex items-center justify-center gap-2">
                <Download className="w-5 h-5" />
                <span>Baixar PDF</span>
              </button>
              <button className="bg-[#EBB641] text-gray-800 py-4 px-4 rounded-xl hover:bg-[#d9a531] transition-all shadow-md flex items-center justify-center gap-2">
                <Share2 className="w-5 h-5" />
                <span>WhatsApp</span>
              </button>
            </div>

            {/* Secondary Actions */}
            <div className="flex items-center justify-center gap-6 text-sm">
              <button className="text-[#00979D] hover:underline">
                Editar Informações
              </button>
              <button onClick={onClose} className="text-gray-600 hover:underline">
                Fechar
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
