import { useState } from 'react';
import { LifeInterview } from './components/LifeInterview';
import { TranslationDashboard } from './components/TranslationDashboard';
import { OpportunityMatch } from './components/OpportunityMatch';
import { StudyRoadmap } from './components/StudyRoadmap';
import { Mic, User, Briefcase, Map } from 'lucide-react';

type Screen = 'interview' | 'profile' | 'jobs' | 'roadmap';

export default function App() {
  const [activeScreen, setActiveScreen] = useState<Screen>('interview');

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col max-w-md mx-auto">
      {/* Main Content Area */}
      <div className="flex-1 overflow-y-auto pb-20">
        {activeScreen === 'interview' && <LifeInterview />}
        {activeScreen === 'profile' && <TranslationDashboard />}
        {activeScreen === 'jobs' && <OpportunityMatch />}
        {activeScreen === 'roadmap' && <StudyRoadmap />}
      </div>

      {/* Bottom Navigation */}
      <nav className="fixed bottom-0 left-0 right-0 max-w-md mx-auto bg-white border-t-2 border-gray-200 px-2 py-3 shadow-lg">
        <div className="flex justify-around items-center">
          <button
            onClick={() => setActiveScreen('interview')}
            className={`flex flex-col items-center gap-1 px-4 py-2 rounded-lg transition-colors ${
              activeScreen === 'interview'
                ? 'bg-teal-50 text-teal-700'
                : 'text-gray-600 hover:bg-gray-50'
            }`}
          >
            <Mic className="w-6 h-6" />
            <span className="text-xs">Entrevista</span>
          </button>

          <button
            onClick={() => setActiveScreen('profile')}
            className={`flex flex-col items-center gap-1 px-4 py-2 rounded-lg transition-colors ${
              activeScreen === 'profile'
                ? 'bg-teal-50 text-teal-700'
                : 'text-gray-600 hover:bg-gray-50'
            }`}
          >
            <User className="w-6 h-6" />
            <span className="text-xs">Perfil</span>
          </button>

          <button
            onClick={() => setActiveScreen('jobs')}
            className={`flex flex-col items-center gap-1 px-4 py-2 rounded-lg transition-colors ${
              activeScreen === 'jobs'
                ? 'bg-teal-50 text-teal-700'
                : 'text-gray-600 hover:bg-gray-50'
            }`}
          >
            <Briefcase className="w-6 h-6" />
            <span className="text-xs">Vagas</span>
          </button>

          <button
            onClick={() => setActiveScreen('roadmap')}
            className={`flex flex-col items-center gap-1 px-4 py-2 rounded-lg transition-colors ${
              activeScreen === 'roadmap'
                ? 'bg-teal-50 text-teal-700'
                : 'text-gray-600 hover:bg-gray-50'
            }`}
          >
            <Map className="w-6 h-6" />
            <span className="text-xs">Plano</span>
          </button>
        </div>
      </nav>
    </div>
  );
}