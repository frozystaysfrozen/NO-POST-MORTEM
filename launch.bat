@echo off
title WINDON'T KERNEL
mode con: cols=60 lines=30
powershell -NoProfile -Command "$hwnd = (Get-Process -Id $PID).MainWindowHandle; $style = [Win32.User32]::GetWindowLong($hwnd, -16); [Win32.User32]::SetWindowLong($hwnd, -16, $style -band (-1 -bxor 0x40000 -bxor 0x10000))"
cls

echo WINDON'T KERNEL
echo ================================
echo.
timeout /t 1 /nobreak >nul

echo Checking CPU................. UNKNOWN
echo Checking RAM................. UNKNOWN
echo Checking GPU................. UNKNOWN

timeout /t 1 /nobreak >nul

echo.
echo Checking firmware........... ERROR
timeout /t 1 /nobreak >nul

echo IDT........................ INVALID
timeout /t 1 /nobreak >nul

echo Exception dispatch......... FAILED
timeout /t 1 /nobreak >nul

echo.
echo 7@a%%dKHG^&*
echo xP9!z#2L@q^
echo M4^&v]Q@1*{x
echo %%K!7a$Dg#92
echo qW@3^fH^&*z!
echo.
timeout /t 1 /nobreak >nul

echo TRIPLE FAULT
timeout /t 1 /nobreak >nul

echo.
echo SYSTEM RESET
timeout /t 1 /nobreak >nul

echo ENTERING EMERGENCY SHELL...

timeout /t 1 /nobreak >nul

echo REBOOTING...

timeout /t 2 /nobreak >nul

cls

echo WINDON'T EMERGENCY SHELL
echo ======================================
echo.
echo WELCOME TO THE WINDON'T EMERGENCY SHELL.
echo.
echo SCANNING YOUR SYSTEM...

timeout /t 2 /nobreak >nul
echo.
echo THE SHELL HAS DETECTED THAT
echo SOMETHING IS WRONG WITH YOUR SYSTEM.

timeout /t 2 /nobreak >nul
echo.
echo.
echo.
echo STARTING (NO) POST-MORTEM...

timeout /t 3 /nobreak >nul

title EMERGENCY SHELL
python "(NO) POST-MORTEM.py"