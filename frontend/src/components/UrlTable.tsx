import type { ShortUrl } from '../types/url';
import UrlRow from './UrlRow';

interface Props {
  urls: ShortUrl[];
  onDelete: (shortCode: string) => Promise<void>;
}

export default function UrlTable({ urls, onDelete }: Props) {
  if (urls.length === 0) {
    return (
      <p className="text-center text-gray-400 py-8">No shortened URLs yet.</p>
    );
  }

  return (
    <div className="overflow-x-auto rounded-lg border border-gray-200">
      <table className="w-full bg-white">
        <thead className="bg-gray-50 text-left">
          <tr>
            <th className="px-4 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wide">Original URL</th>
            <th className="px-4 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wide">Short URL</th>
            <th className="px-4 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wide">Code</th>
            <th className="px-4 py-3"></th>
          </tr>
        </thead>
        <tbody>
          {urls.map((url) => (
            <UrlRow key={url.id} url={url} onDelete={onDelete} />
          ))}
        </tbody>
      </table>
    </div>
  );
}
