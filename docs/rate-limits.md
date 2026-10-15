# Rate limits

| Plan     | Requests per minute | Burst |
|----------|---------------------|-------|
| Sandbox  | 60                  | 10    |
| Standard | 600                 | 50    |
| Premium  | 3000                | 200   |

A request over the limit returns HTTP 429 with a `Retry-After` header in seconds.
Back off for that long before retrying.
