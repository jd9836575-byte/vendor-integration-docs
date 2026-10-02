# Webhooks

Example Freight Co. sends a webhook when a shipment changes state.

Events: `shipment.created`, `shipment.in_transit`, `shipment.delivered`, `shipment.exception`.

Each request carries an `X-EFC-Signature` header. Verify it with HMAC-SHA256 over the raw body
using your webhook secret, and reject any request whose signature does not match.

Respond with HTTP 200 within 5 seconds. Failed deliveries are retried 5 times over 24 hours.
