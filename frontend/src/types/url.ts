export interface ShortUrl {
  id: number;
  original_url: string;
  short_code: string;
  short_url: string;
}

export interface UrlListResponse {
  urls: ShortUrl[];
}
