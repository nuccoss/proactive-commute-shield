@echo off
REM run_demo.bat
REM One-Click Bootstrapper for Shibuya 9/5 Arsenal
echo ========================================================
echo  Booting Proactive Mobility Concierge (Shibuya 9/5)
echo ========================================================
cd /d "%~dp0"
python -m pip install streamlit requests --quiet
python -m streamlit run app.py --server.port 8501 --server.headless false
pause
