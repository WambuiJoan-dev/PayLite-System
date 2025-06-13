#!/bin/bash

BASE_URL="http://localhost:5000"
ADMIN_USERNAME="Martin"
ADMIN_PASSWORD="Martin@1"

TOKEN=$(curl -s -X POST $BASE_URL/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "'$ADMIN_USERNAME'", "password": "'$ADMIN_PASSWORD'"}' | jq -r .access_token)

if [ "$TOKEN" == "null" ] || [ -z "$TOKEN" ]; then
  echo "❌ Login failed. Cannot continue tests."
  exit 1
fi

echo "✅ Login OK. Token acquired."

echo "➡️ GET /payments/"
curl -s -X GET $BASE_URL/payments/ \
  -H "Authorization: Bearer $TOKEN" | jq

echo "➡️ POST /payments/"
curl -s -X POST $BASE_URL/payments/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "amount_paid": 3000,
    "sale_id": 4
  }' | jq

echo "➡️ GET /payments/1"
curl -s -X GET $BASE_URL/payments/1 \
  -H "Authorization: Bearer $TOKEN" | jq

echo "✅ PAYMENTS TEST COMPLETED"
