param(
    [string]$CodexHome = $env:CODEX_HOME
)

$ErrorActionPreference = "Stop"
$expectedSkills = @(
    "ai-film-router",
    "film-synopsis",
    "film-characters",
    "film-worldbuilding",
    "film-treatment",
    "film-screenplay",
    "film-lira-assets",
    "film-acting",
    "film-cinedance",
    "film-knowledge-bridge"
)

if ([string]::IsNullOrWhiteSpace($CodexHome)) {
    $CodexHome = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".codex"
}

$sourceRoot = Join-Path $PSScriptRoot "..\skills"
$targetRoot = Join-Path $CodexHome "skills"

foreach ($skillName in $expectedSkills) {
    $skillFile = Join-Path $sourceRoot "$skillName\SKILL.md"
    if (-not (Test-Path -LiteralPath $skillFile)) {
        throw "安装包不完整，缺少：$skillFile"
    }
}

New-Item -ItemType Directory -Path $targetRoot -Force | Out-Null

$existingKnowledgeConfig = @(
    (Join-Path $targetRoot "film-knowledge-bridge\references\knowledge-base.json"),
    (Join-Path $targetRoot "film-knowledge-bridge\knowledge-base.json")
) | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
$preservedKnowledgeConfig = $null
if ($existingKnowledgeConfig) {
    $preservedKnowledgeConfig = [System.IO.File]::ReadAllBytes($existingKnowledgeConfig)
}

$conflicts = @($expectedSkills | Where-Object {
    Test-Path -LiteralPath (Join-Path $targetRoot $_)
})

$backupRoot = $null
if ($conflicts.Count -gt 0) {
    $backupRoot = Join-Path $CodexHome ("skills-backup-" + (Get-Date -Format "yyyyMMdd-HHmmss-fff"))
    New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null

    foreach ($skillName in $conflicts) {
        Move-Item -LiteralPath (Join-Path $targetRoot $skillName) -Destination $backupRoot
    }
}

foreach ($skillName in $expectedSkills) {
    Copy-Item -LiteralPath (Join-Path $sourceRoot $skillName) -Destination $targetRoot -Recurse
}

$knowledgeConfigResult = "无旧配置，首次调用知识库时选择一次文件夹"
if ($null -ne $preservedKnowledgeConfig) {
    $knowledgeConfigTarget = Join-Path $targetRoot "film-knowledge-bridge\references\knowledge-base.json"
    New-Item -ItemType Directory -Path (Split-Path -Parent $knowledgeConfigTarget) -Force | Out-Null
    [System.IO.File]::WriteAllBytes($knowledgeConfigTarget, $preservedKnowledgeConfig)
    $knowledgeConfigResult = "已保留原知识库路径：$knowledgeConfigTarget"
}

$missing = @($expectedSkills | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $targetRoot "$($_)\SKILL.md"))
})

if ($missing.Count -gt 0) {
    throw "安装校验失败，缺少：$($missing -join '、')"
}

Write-Output "安装完成：10 个 Skill（原 9 个电影 Skill + 本地知识库外挂）"
Write-Output "安装位置：$targetRoot"
if ($backupRoot) {
    Write-Output "旧版本备份：$backupRoot"
} else {
    Write-Output "旧版本备份：无（未发现同名 Skill）"
}
Write-Output "知识库配置：$knowledgeConfigResult"
