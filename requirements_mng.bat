@echo off
setlocal enabledelayedexpansion

set "LIBRARIES=mercury ee geemap datetime colorama gcloud earthengine-api notebook"
set "SUCCESS="
set "FAIL="

for %%L in (%LIBRARIES%) do (
    echo Installing %%L...
    python -m pip install %%L
    if !errorlevel! equ 0 (
        set "SUCCESS=!SUCCESS! %%L"
    ) else (
        set "FAIL=!FAIL! %%L"
    )
)

if not "!SUCCESS!" == "" (
    echo LIBRARIES INSTALLED SUCCESSFULLY:!SUCCESS!
)

if not "!FAIL!" == "" (
    echo LIBRARIES FAILED TO INSTALL:!FAIL!
)

pause
