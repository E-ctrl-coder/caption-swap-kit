@echo off
echo Translating captions...
python translate_srt.py

echo.
echo Translation done. Opening translated.srt in Notepad for review...
start notepad.exe output\translated.srt

pause
echo Burning captions into video...
python burn_captions.py

pause
