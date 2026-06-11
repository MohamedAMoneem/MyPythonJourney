@echo off

:loop

cd /d "C:\Users\rayra\OneDrive\Desktop\learning python"

git add --all

git commit -m "auto push"

git push origin main

echo Complete. Relaunching...

timeout /t 300 /nobreak >nul

goto loop