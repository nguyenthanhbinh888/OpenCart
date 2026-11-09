@echo off
title OpenCart Server
echo Starting OpenCart server at http://localhost:8000 ...
cd /d "%~dp0upload"

where php >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    php -S localhost:8000
) else (
    "%LOCALAPPDATA%\Microsoft\WinGet\Packages\PHP.PHP.8.2_Microsoft.Winget.Source_8wekyb3d8bbwe\php.exe" -S localhost:8000
)
pause

