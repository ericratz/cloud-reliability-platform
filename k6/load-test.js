import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

const errorRate = new Rate('errors');

export const options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_failed:   ['rate<0.05'],   // fail if error rate >= 5%
    http_req_duration: ['p(95)<500'],   // fail if p95 latency >= 500ms
    errors:            ['rate<0.05'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'http://localhost:8000';

export default function () {
  const endpoints = ['/', '/health', '/slo'];
  const url = `${BASE_URL}${endpoints[Math.floor(Math.random() * endpoints.length)]}`;

  const res = http.get(url);

  const ok = check(res, { 'status 2xx': (r) => r.status >= 200 && r.status < 300 });
  errorRate.add(!ok);

  sleep(1);
}