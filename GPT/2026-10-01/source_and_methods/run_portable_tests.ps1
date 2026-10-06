# Runs the six portable methodology tests and the archived-input validation.
# No Parquet reader is required. Run from any directory on this host.
$ErrorActionPreference = 'Stop'
$sourceMethodsDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$bundledPython = 'C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
if (-not (Test-Path -LiteralPath $bundledPython)) {
    throw "Bundled Python unavailable: $bundledPython"
}
$previousPythonPath = $env:PYTHONPATH
try {
    Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
    & $bundledPython (Join-Path $sourceMethodsDir 'test_methodology_v2.py')
    if ($LASTEXITCODE -ne 0) { throw "methodology tests failed: $LASTEXITCODE" }
    & $bundledPython (Join-Path $sourceMethodsDir 'validate_methodology_v2.py')
    if ($LASTEXITCODE -ne 0) { throw "methodology validation failed: $LASTEXITCODE" }
} finally {
    if ($null -eq $previousPythonPath) {
        Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
    } else {
        $env:PYTHONPATH = $previousPythonPath
    }
}
