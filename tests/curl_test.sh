#!/bin/bash

BASE_URL="http://localhost:5000"
ADMIN_USERNAME="Martin"
ADMIN_PASSWORD="Wambua"

TOKEN=$(curl -s -X POST $BASE_URL/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "'$ADMIN_USERNAME'", "password": "'$ADMIN_PASSWORD'"}' | jq -r .access_token)

if [ "$TOKEN" == "null" ] || [ -z "$TOKEN" ]; then
  echo "❌ Login failed. Cannot continue tests."
  exit 1
fi

echo "✅ Login OK. Token acquired."

curl -s -X GET $BASE_URL/customers/ \
  -H "Authorization: Bearer $TOKEN" | jq

curl -s -X POST $BASE_URL/phones/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "brand": "Techno",
    "model": "Camon 18",
    "price": 18000,
    "stock_quantity": 35
  }' | jq

curl -s -X POST $BASE_URL/sales/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_id": 3,
    "customer_id": 2,
    "deposit_paid": 3000,
    "installment_amount": 2000
  }' | jq

curl -s -X POST $BASE_URL/payments/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "amount_paid": 3000,
    "sale_id": 4
  }' | jq

curl -s -X DELETE $BASE_URL/customers/12 \
  -H "Authorization: Bearer $TOKEN" | jq

echo "✅ CURL TEST COMPLETED"