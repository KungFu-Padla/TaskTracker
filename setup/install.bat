@echo off
rem TaskTracker — установочный скрипт (ЛР 8, Setup Creator)
echo ============================================
echo   Установка TaskTracker
echo ============================================
echo.

rem Проверка наличия Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo ОШИБКА: Python не найден в PATH. Установите Python с python.org
    pause
    exit /b 1
)

echo [1/4] Копирование файлов приложения...
xcopy /E /I /Y "..\*" "%USERPROFILE%\TaskTracker\" >nul

echo [2/4] Установка зависимостей...
pip install -r "%USERPROFILE%\TaskTracker\requirements.txt"

echo [3/4] Создание ярлыка на рабочем столе...
echo ^<^& echo @echo off ^> "%USERPROFILE%\Desktop\TaskTracker.bat"
echo cd /d "%USERPROFILE%\TaskTracker" ^>> "%USERPROFILE%\Desktop\TaskTracker.bat"
echo python app.py ^>> "%USERPROFILE%\Desktop\TaskTracker.bat"

echo [4/4] Завершение...
echo.
echo Установка завершена. Ярлык: %USERPROFILE%\Desktop\TaskTracker.bat
pause
