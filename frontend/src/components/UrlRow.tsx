import { useState } from 'react';
import type { ShortUrl } from '../types/url';

interface Props {
  url: ShortUrl;
  onDelete: (shortCode: string) => Promise<void>;
}

export default function UrlRow({ url, onDelete }: Props) {
  const [isDeleting, setIsDeleting] = useState(false);

  const handleDelete = async () => {
    setIsDeleting(true);
    try {
      await onDelete(url.short_code);
    } finally {
      setIsDeleting(false);
    }
  };

  return (
    <tr className="border-t border-gray-100 hover:bg-gray-50">
      <td className="px-4 py-3 text-sm text-gray-600 max-w-xs truncate">
        <a
          href={url.original_url}
          target="_blank"
          rel="noopener noreferrer"
          className="hover:text-indigo-600 underline"
          title={url.original_url}
        >
          {url.original_url}
        </a>
      </td>
      <td className="px-4 py-3 text-sm font-mono">
        <a
          href={url.short_url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-indigo-600 hover:underline"
        >
          {url.short_url}
        </a>
      </td>
      <td className="px-4 py-3 text-sm text-gray-500 font-mono">{url.short_code}</td>
      <td className="px-4 py-3 text-right">
        <button
          onClick={handleDelete}
          disabled={isDeleting}
          className="px-3 py-1 text-xs bg-red-500 text-white rounded hover:bg-red-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        >
          {isDeleting ? 'Deleting…' : 'Delete'}
        </button>
      </td>
    </tr>
  );
}
