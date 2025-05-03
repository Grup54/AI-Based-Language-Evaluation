@echo off

REM Sanal ortam kontrolü ve oluşturma
if not exist "venv\" (
    python -m venv venv
    echo Sanal ortam oluşturuldu.
)

REM Sanal ortamı etkinleştirme
call venv\Scripts\activate.bat
echo Sanal ortam seçildi.

echo Bağımlılıklar kuruluyor.
pip install -r requirements.txt

uvicorn main:app --reload --port 8000