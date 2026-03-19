import { useState, useEffect, useCallback } from 'react';
import type { ShortUrl } from './types/url';
import { fetchUrls, shortenUrl, deleteUrl } from './api/urls';
import ShortenForm from './components/ShortenForm';
import ResultBanner from './components/ResultBanner';
import UrlTable from './components/UrlTable';

function App() {
  const [urls, setUrls] = useState<ShortUrl[]>([]);
  const [lastCreated, setLastCreated] = useState<ShortUrl | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const loadUrls = useCallback(async () => {
    try {
      const data = await fetchUrls();
      setUrls(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load URLs');
    }
  }, []);

  useEffect(() => {
    loadUrls();
  }, [loadUrls]);

  const handleShorten = async (url: string) => {
    setIsLoading(true);
    setError(null);
    try {
      const created = await shortenUrl(url);
      setLastCreated(created);
      await loadUrls();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to shorten URL');
    } finally {
      setIsLoading(false);
    }
  };

  const handleDelete = async (shortCode: string) => {
    setError(null);
    try {
      await deleteUrl(shortCode);
      if (lastCreated?.short_code === shortCode) {
        setLastCreated(null);
      }
      await loadUrls();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete URL');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-indigo-600 text-white py-6 px-4 shadow">
        <div className="max-w-5xl mx-auto">
          <h1 className="text-2xl font-bold">URL Shortener</h1>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 py-8 space-y-6">
        <div className="bg-white rounded-xl shadow-sm p-6 space-y-4">
          <h2 className="text-lg font-semibold text-gray-700">Shorten a URL</h2>
          <ShortenForm onShorten={handleShorten} isLoading={isLoading} />
          {error && (
            <p className="text-sm text-red-600 bg-red-50 border border-red-200 rounded px-3 py-2">
              {error}
            </p>
          )}
          {lastCreated && <ResultBanner url={lastCreated} />}
        </div>

        <div className="bg-white rounded-xl shadow-sm p-6">
          <h2 className="text-lg font-semibold text-gray-700 mb-4">All Shortened URLs</h2>
          <UrlTable urls={urls} onDelete={handleDelete} />
        </div>
      </main>
    </div>
  );
}

export default App;
