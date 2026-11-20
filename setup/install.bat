@echo off
chcp 65001 >nul
rem ============================================
rem   TaskTracker - установочный скрипт (ЛР 8)
rem ============================================
setlocal

echo ============================================
echo   Установка TaskTracker
echo ============================================
echo.

rem [1/5] Проверка Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [ОШИБКА] Python не найден в PATH.
    echo Установите Python с python.org и добавьте в PATH.
    pause
    exit /b 1
)
echo [1/5] Python найден.
python --version
echo.

rem [2/5] Определение папки установки
set "INSTALL_DIR=%USERPROFILE%\TaskTracker"
echo [2/5] Папка установки: %INSTALL_DIR%
echo.

rem [3/5] Копирование файлов проекта
echo [3/5] Копирование файлов проекта...
xcopy /E /I /Y "%~dp0..\*" "%INSTALL_DIR%" >nul
if %errorlevel% neq 0 (
    echo [ОШИБКА] Не удалось скопировать файлы.
    pause
    exit /b 1
)
echo       Файлы скопированы в %INSTALL_DIR%
echo.

rem [4/5] Установка зависимостей
echo [4/5] Установка зависимостей (flask, pytest)...
pip install -r "%INSTALL_DIR%\requirements.txt"
if %errorlevel% neq 0 (
    echo [ПРЕДУПРЕЖДЕНИЕ] Не все зависимости установились. Проверьте pip.
) else (
    echo       Зависимости установлены.
)
echo.

rem [5/5] Создание ярлыка на рабочем столе
echo [5/5] Создание ярлыка на рабочем столе...
set "SHORTCUT=%USERPROFILE%\Desktop\TaskTracker.bat"

echo @echo off > "%SHORTCUT%"
echo rem TaskTracker - ярлык приложения >> "%SHORTCUT%"
echo cd /d "%INSTALL_DIR%" >> "%SHORTCUT%"
echo echo TaskTracker запускается... >> "%SHORTCUT%"
echo python app.py >> "%SHORTCUT%"
echo pause >> "%SHORTCUT%"

echo       Ярлык создан: %SHORTCUT%
echo.

echo ============================================
echo   Установка завершена успешно!
echo ============================================
echo.
echo Запуск приложения:
echo   - Дважды кликните по ярлыку TaskTracker на рабочем столе
echo   - Или запустите вручную: python %INSTALL_DIR%\app.py
echo.
echo Для запуска тестов:
echo   cd /d "%INSTALL_DIR%"
echo   pytest
echo.
pause
exit /b 0