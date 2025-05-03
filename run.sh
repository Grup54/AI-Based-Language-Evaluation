#!/bin/bash

if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo -e "\033[1;36mSanal ortam oluşturuldu.\033[0m"
fi

source venv/bin/activate
echo -e "\033[1;36mSanal ortam seçildi.\033[0m"

echo -e "\033[1;36mBağımlılıklar kuruluyor.\033[0m"
pip install -r requirements.txt

uvicorn main:app --reload --port 8000