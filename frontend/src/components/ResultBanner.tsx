import { useState } from 'react';
import type { ShortUrl } from '../types/url';

interface Props {
  url: ShortUrl;
}

export default function ResultBanner({ url }: Props) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(url.short_url);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="flex items-center justify-between px-4 py-3 bg-green-50 border border-green-200 rounded-lg">
      <div className="text-sm text-green-800">
        <span className="font-medium">Shortened: </span>
        <a
          href={url.short_url}
          target="_blank"
          rel="noopener noreferrer"
          className="underline hover:text-green-600"
        >
          {url.short_url}
        </a>
      </div>
      <button
        onClick={handleCopy}
        className="ml-4 px-3 py-1 text-xs bg-green-600 text-white rounded hover:bg-green-700 transition-colors"
      >
        {copied ? 'Copied!' : 'Copy'}
      </button>
    </div>
  );
}
