param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectTitle,
    [string]$ProjectRoot
)

$templatePath = Join-Path $PSScriptRoot "..\project-template"

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
    $documents = [Environment]::GetFolderPath("MyDocuments")
    $workflowRoot = Join-Path $documents "AI STUDIO洋子AI电影工作流"
    $ProjectRoot = Join-Path $workflowRoot "电影项目"
}

New-Item -ItemType Directory -Path $ProjectRoot -Force | Out-Null
$ProjectPath = Join-Path $ProjectRoot $ProjectTitle

if (Test-Path -LiteralPath $ProjectPath) {
    throw "项目目录已存在：$ProjectPath。请使用一个新名称，避免覆盖已有项目。"
}

Copy-Item -LiteralPath $templatePath -Destination $ProjectPath -Recurse

$statusPath = Join-Path $ProjectPath "00_project\project-status.md"
$briefPath = Join-Path $ProjectPath "00_project\brief.md"

(Get-Content -LiteralPath $statusPath -Raw).Replace("项目名称：", "项目名称：$ProjectTitle") |
    Set-Content -LiteralPath $statusPath -Encoding utf8
(Get-Content -LiteralPath $briefPath -Raw).Replace("项目名称：", "项目名称：$ProjectTitle") |
    Set-Content -LiteralPath $briefPath -Encoding utf8

Write-Host "项目已创建：$ProjectPath"
Write-Host "请用 Codex 打开这个项目文件夹，然后直接输入：启动项目：我要做一部……"
