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

echo "➡️ GET /sales/"
curl -s -X GET $BASE_URL/sales/ \
  -H "Authorization: Bearer $TOKEN" | jq

echo "➡️ POST /sales/"
curl -s -X POST $BASE_URL/sales/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_id": 3,
    "customer_id": 2,
    "deposit_paid": 3000,
    "installment_amount": 2000
  }' | jq

echo "➡️ GET /sales/1"
curl -s -X GET $BASE_URL/sales/1 \
  -H "Authorization: Bearer $TOKEN" | jq

echo "✅ SALES TEST COMPLETED"
