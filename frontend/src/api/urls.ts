import type { ShortUrl, UrlListResponse } from '../types/url';

async function handleResponse<T>(res: Response): Promise<T> {
  if (!res.ok) {
    let message = `HTTP ${res.status}`;
    try {
      const body = await res.json();
      if (body.detail) message = body.detail;
    } catch {
      // ignore parse errors
    }
    throw new Error(message);
  }
  return res.json();
}

export async function fetchUrls(): Promise<ShortUrl[]> {
  const res = await fetch('/api/v1/urls/');
  const data = await handleResponse<UrlListResponse>(res);
  return data.urls;
}

export async function shortenUrl(originalUrl: string): Promise<ShortUrl> {
  const res = await fetch('/api/v1/urls/shorten', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ original_url: originalUrl }),
  });
  return handleResponse<ShortUrl>(res);
}

export async function deleteUrl(shortCode: string): Promise<void> {
  const res = await fetch(`/api/v1/urls/${shortCode}`, { method: 'DELETE' });
  if (!res.ok) {
    let message = `HTTP ${res.status}`;
    try {
      const body = await res.json();
      if (body.detail) message = body.detail;
    } catch {
      // ignore parse errors
    }
    throw new Error(message);
  }
}
