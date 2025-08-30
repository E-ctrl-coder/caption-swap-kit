@echo off
setlocal

REM === Canonical English↔Arabic caption workflow ===
REM Input files must be placed in the "input" folder:
REM   - original.srt   (captions)
REM   - original.mp4   (video)
REM Output will be written to the "output" folder.

echo Translating captions (English ↔ Arabic)...
python translate_srt.py

echo.
echo Translation done. Opening translated.srt in Notepad for review...
start notepad.exe output\translated.srt

pause
echo Burning captions into video...
python burn_captions.py

pause
endlocal