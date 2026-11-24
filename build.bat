@echo off
echo [*] Compiling Hybrid Anomaly Engine with g++...
g++ -std=c++14 -O2 -I include src/lexer.cpp src/dfa.cpp src/moore.cpp src/turing_machine.cpp src/engine.cpp src/main.cpp -o anomaly_engine.exe
if %ERRORLEVEL% EQU 0 (
    echo [✓] Build Succeeded: anomaly_engine.exe
) else (
    echo [-] Build Failed!
)
