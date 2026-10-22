param(
    [Parameter(Mandatory = $true)]
    [string]$KnowledgeRoot
)

$ErrorActionPreference = "Stop"
$codexHome = if ([string]::IsNullOrWhiteSpace($env:CODEX_HOME)) {
    Join-Path ([Environment]::GetFolderPath("UserProfile")) ".codex"
} else {
    $env:CODEX_HOME
}

$installedScript = Join-Path $codexHome "skills\film-knowledge-bridge\scripts\configure_knowledge_base.ps1"
$packageScript = Join-Path $PSScriptRoot "..\skills\film-knowledge-bridge\scripts\configure_knowledge_base.ps1"
$scriptPath = if (Test-Path -LiteralPath $installedScript) { $installedScript } else { $packageScript }

if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "缺少知识库配置脚本：$scriptPath"
}

& $scriptPath -Root $KnowledgeRoot
exit $LASTEXITCODE
