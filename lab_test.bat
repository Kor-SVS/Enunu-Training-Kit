@echo off
title LAB TEST

setlocal
cd /D "%~dp0"
call venv\Scripts\activate.bat
set MECAB_KO_DIC_PATH=C:\mecab\mecab-ko-dic -r C:\mecab\mecabrc
"C:\Program Files\Git\bin\bash.exe" train\run.sh --stage 0 --stop_stage 0
endlocal

pause