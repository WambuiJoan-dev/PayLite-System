#!/bin/bash

BASE_URL="http://localhost:5000"


ADMIN_USERNAME="Martin"
ADMIN_PASSWORD="Martin@1"

ADMIN_TOKEN=$(curl -s -X POST $BASE_URL/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "'$ADMIN_USERNAME'", "password": "'$ADMIN_PASSWORD'"}' | jq -r .access_token)

if [ "$ADMIN_TOKEN" == "null" ] || [ -z "$ADMIN_TOKEN" ]; then
  echo "❌ Admin login failed. Cannot continue tests."
  exit 1
fi

echo "✅ Admin Login OK."

echo "➡️ DELETE /customers/12 as Admin"
curl -s -X DELETE $BASE_URL/customers/12 \
  -H "Authorization: Bearer $ADMIN_TOKEN" | jq


USER_USERNAME="Jedidah"
USER_PASSWORD="Jeddy@1"

USER_TOKEN=$(curl -s -X POST $BASE_URL/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "'$USER_USERNAME'", "password": "'$USER_PASSWORD'"}' | jq -r .access_token)

if [ "$USER_TOKEN" == "null" ] || [ -z "$USER_TOKEN" ]; then
  echo "❌ User login failed. Skipping user role test."
else
  echo "✅ User Login OK."

  echo "➡️ DELETE /customers/12 as Non-Admin"
  curl -s -X DELETE $BASE_URL/customers/12 \
    -H "Authorization: Bearer $USER_TOKEN" | jq
fi

echo "✅ ROLES TEST COMPLETED"
