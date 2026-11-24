# PowerShell build script for Hybrid DFA-LLM Anomaly Engine
Write-Host "[*] Compiling C++ Hybrid Anomaly Engine..." -ForegroundColor Cyan

$includeDir = Join-Path $PSScriptRoot "include"
$srcFiles = @(
    (Join-Path $PSScriptRoot "src/lexer.cpp"),
    (Join-Path $PSScriptRoot "src/dfa.cpp"),
    (Join-Path $PSScriptRoot "src/moore.cpp"),
    (Join-Path $PSScriptRoot "src/turing_machine.cpp"),
    (Join-Path $PSScriptRoot "src/engine.cpp"),
    (Join-Path $PSScriptRoot "src/main.cpp")
)
$outputExe = Join-Path $PSScriptRoot "anomaly_engine.exe"

$compileCmd = "g++ -std=c++14 -O2 -I `"$includeDir`" " + ($srcFiles -join " ") + " -o `"$outputExe`""
Invoke-Expression $compileCmd

if ($LASTEXITCODE -eq 0) {
    Write-Host "[✓] Compilation successful: $outputExe" -ForegroundColor Green
} else {
    Write-Host "[-] Compilation failed with exit code $LASTEXITCODE" -ForegroundColor Red
}
