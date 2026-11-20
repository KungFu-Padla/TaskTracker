@echo off
rem ============================================
rem   TaskTracker - Installer (Lab 8)
rem ============================================
setlocal

echo ============================================
echo   Installing TaskTracker
echo ============================================
echo.

rem [1/5] Check Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found in PATH.
    echo Install Python from python.org and add it to PATH.
    pause
    exit /b 1
)
echo [1/5] Python found.
python --version
echo.

rem [2/5] Set install directory
set "INSTALL_DIR=%USERPROFILE%\TaskTracker"
echo [2/5] Install directory: %INSTALL_DIR%
echo.

rem [3/5] Copy project files
echo [3/5] Copying project files...
xcopy /E /I /Y "%~dp0..\*" "%INSTALL_DIR%" >nul
if %errorlevel% neq 0 (
    echo [ERROR] Failed to copy files.
    pause
    exit /b 1
)
echo       Files copied to %INSTALL_DIR%
echo.

rem [4/5] Install dependencies
echo [4/5] Installing dependencies (flask, pytest)...
pip install -r "%INSTALL_DIR%\requirements.txt"
if %errorlevel% neq 0 (
    echo [WARNING] Some dependencies failed to install. Check pip.
) else (
    echo       Dependencies installed.
)
echo.

rem [5/5] Create desktop shortcut
echo [5/5] Creating desktop shortcut...
set "SHORTCUT=%USERPROFILE%\Desktop\TaskTracker.bat"

echo @echo off > "%SHORTCUT%"
echo rem TaskTracker launcher >> "%SHORTCUT%"
echo cd /d "%INSTALL_DIR%" >> "%SHORTCUT%"
echo echo TaskTracker is starting... >> "%SHORTCUT%"
echo python app.py >> "%SHORTCUT%"
echo pause >> "%SHORTCUT%"

echo       Shortcut created: %SHORTCUT%
echo.

echo ============================================
echo   Installation completed successfully!
echo ============================================
echo.
echo To start the application:
echo   - Double-click TaskTracker.bat on your Desktop
echo   - Or run manually: python %INSTALL_DIR%\app.py
echo.
echo To run tests:
echo   cd /d "%INSTALL_DIR%"
echo   pytest
echo.
pause
exit /b 0