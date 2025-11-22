import { useState, useRef } from 'react';
import { Mic, Send, Volume2, Square, Loader2 } from 'lucide-react';

interface Message {
  type: 'ai' | 'user';
  text: string;
}

export function LifeInterview() {
  const [isListening, setIsListening] = useState(false); // Gravando áudio?
  const [isProcessing, setIsProcessing] = useState(false); // Enviando/Transcrevendo?
  const [inputText, setInputText] = useState('');
  const [messages, setMessages] = useState<Message[]>([
    {
      type: 'ai',
      text: 'Olá! Eu sou a assistente da Conecta Pecém. Conte-me sobre as suas experiências de trabalho, tarefas diárias ou trabalhos informais. Pode falar ou digitar!',
    },
  ]);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);

  // --- FUNÇÃO: Iniciar Gravação ---
  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      
      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data);
        }
      };

      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        const formData = new FormData();
        formData.append('file', audioBlob, 'gravacao.webm');

        setIsProcessing(true);

        try {
          console.log("📤 A enviar áudio para o backend...");

          // --- ATENÇÃO: URL do Backend Python ---
          const response = await fetch('http://localhost:8000/api/transcribe', {
            method: 'POST',
            body: formData,
          });

          if (!response.ok) {
            throw new Error(`Erro no servidor: ${response.status}`);
          }

          const data = await response.json();
          console.log("Transcrição recebida:", data.text);
          
          setInputText((prev) => {
            return prev ? `${prev} ${data.text}` : data.text;
          });

        } catch (error) {
          console.error("Erro na integração:", error);
          setMessages(prev => [
            ...prev, 
            { type: 'ai', text: "Tive um problema técnico ao processar o seu áudio. Por favor, verifique se o backend está a correr." }
          ]);
        } finally {
          setIsProcessing(false);
          stream.getTracks().forEach(track => track.stop());
        }
      };

      mediaRecorder.start();
      setIsListening(true);

    } catch (err) {
      console.error("Erro ao aceder ao microfone:", err);
      alert("Não foi possível aceder ao microfone. Verifique as permissões do seu navegador.");
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && isListening) {
      mediaRecorderRef.current.stop();
      setIsListening(false);
    }
  };

  const handleVoiceInput = () => {
    if (isListening) {
      stopRecording();
    } else {
      startRecording();
    }
  };

  const handleSend = () => {
    if (inputText.trim()) {
      setMessages(prev => [...prev, { type: 'user', text: inputText }]);
      setInputText('');

      // Simulação da resposta da IA
      setTimeout(() => {
        setMessages(prev => [
          ...prev,
          {
            type: 'ai',
            text: 'Excelente! Identifiquei experiências valiosas em eletricidade e manutenção. Vou traduzir isto para competências profissionais. Quer adicionar mais alguma experiência?',
          },
        ]);
      }, 1000);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white flex flex-col">
      {/* Header */}
      <header className="bg-[#00979D] text-white px-6 py-8 shadow-lg">
        <h1 className="text-center mb-2">Conecta Pecém</h1>
        <p className="text-center text-teal-100">A sua história vale muito</p>
      </header>

      {/* Área de Chat */}
      <div className="flex-1 px-4 py-6 space-y-4 overflow-y-auto">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[80%] rounded-2xl px-5 py-4 shadow-md ${
                message.type === 'user'
                  ? 'bg-[#00979D] text-white'
                  : 'bg-white text-gray-800 border-2 border-gray-100'
              }`}
            >
              {message.type === 'ai' && (
                <div className="flex items-center gap-2 mb-2">
                  <Volume2 className="w-4 h-4 text-[#00979D]" />
                  <span className="text-[#00979D]">Assistente IA</span>
                </div>
              )}
              <p>{message.text}</p>
            </div>
          </div>
        ))}

        {isListening && (
          <div className="flex justify-center">
            <div className="bg-red-50 text-red-800 rounded-2xl px-5 py-4 shadow-md border-2 border-red-200 flex items-center gap-3">
              <div className="flex gap-1 h-4 items-center">
                <div className="w-1 h-4 bg-red-500 rounded-full animate-pulse"></div>
                <div className="w-1 h-6 bg-red-500 rounded-full animate-pulse delay-75"></div>
                <div className="w-1 h-4 bg-red-500 rounded-full animate-pulse delay-150"></div>
              </div>
              <span className="font-medium">A gravar áudio...</span>
            </div>
          </div>
        )}
      </div>

      {/* Área de Input */}
      <div className="bg-white border-t-2 border-gray-200 px-4 py-5 shadow-lg">
        <div className="mb-4">
          <label className="block text-gray-700 mb-3 text-sm font-medium">
            Conte sobre as suas tarefas e trabalhos:
          </label>
          <div className="flex gap-2">
            <input
              type="text"
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSend()}
              placeholder="Digite aqui ou use o microfone..."
              disabled={isListening || isProcessing}
              className="flex-1 px-4 py-4 border-2 border-gray-300 rounded-xl focus:outline-none focus:border-[#00979D] disabled:bg-gray-100 disabled:text-gray-400 transition-colors"
            />
            <button
              onClick={handleSend}
              disabled={!inputText.trim() || isListening || isProcessing}
              className="bg-[#00979D] text-white px-5 rounded-xl hover:bg-[#008389] transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <Send className="w-5 h-5" />
            </button>
          </div>
        </div>

        <button
          onClick={handleVoiceInput}
          disabled={isProcessing}
          className={`w-full py-5 rounded-xl flex items-center justify-center gap-3 transition-all shadow-lg ${
            isListening
              ? 'bg-red-500 text-white hover:bg-red-600'
              : isProcessing
                ? 'bg-gray-200 text-gray-500 cursor-not-allowed'
                : 'bg-[#EBB641] text-gray-800 hover:bg-[#d9a531]'
          }`}
        >
          {isListening ? (
            <>
              <Square className="w-6 h-6 fill-current" />
              <span className="text-lg font-bold">Parar Gravação</span>
            </>
          ) : isProcessing ? (
            <>
              <Loader2 className="w-6 h-6 animate-spin" />
              <span className="text-lg">A processar áudio...</span>
            </>
          ) : (
            <>
              <Mic className="w-7 h-7" />
              <span className="text-lg font-medium">Falar com Microfone</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
}