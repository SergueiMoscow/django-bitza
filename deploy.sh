#!/bin/bash
cd /app
git pull origin main
#docker compose down
docker compose up -d --build