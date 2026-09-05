#!/usr/bin/env bash
# run_demo.sh - One-Click Bootstrapper for Proactive Commute Shield Enterprise
set -e

cd "$(dirname "$0")"
echo "========================================================"
echo " Booting Proactive Commute Shield Enterprise"
echo "========================================================"
python3 -m pip install streamlit requests --quiet
python3 -m streamlit run app.py --server.port 8501 --server.headless false
