import { useState } from 'react';

interface Props {
  onShorten: (url: string) => Promise<void>;
  isLoading: boolean;
}

export default function ShortenForm({ onShorten, isLoading }: Props) {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const trimmed = inputValue.trim();
    if (!trimmed) return;
    await onShorten(trimmed);
    setInputValue('');
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2">
      <input
        type="url"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="https://example.com/long-url"
        required
        className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
      />
      <button
        type="submit"
        disabled={isLoading}
        className="px-6 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
      >
        {isLoading ? 'Shortening…' : 'Shorten'}
      </button>
    </form>
  );
}
