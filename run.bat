@echo off
echo =========================================================
echo Executive Productivity Agent - Arjun Malhotra
echo Built for AIONOS Technical Evaluation (21-25 Sep 2026)
echo =========================================================
echo.

python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [WARNING] Streamlit installation failed or pip not found. Falling back to zero-dependency CLI mode...
    python cli.py
    pause
    exit /b
)

echo.
echo Launching Interactive Executive Web Dashboard...
python -m streamlit run app.py
pause
