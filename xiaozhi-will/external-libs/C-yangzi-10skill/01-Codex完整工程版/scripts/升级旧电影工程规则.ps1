param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath
)

$ErrorActionPreference = "Stop"

$resolvedProjectPath = (Resolve-Path -LiteralPath $ProjectPath).Path
$projectControlPath = Join-Path $resolvedProjectPath "00_project"
$templatePath = Join-Path $PSScriptRoot "..\project-template"
$templateRoutingPath = Join-Path $templatePath "00_project\routing.md"
$templateAgentsPath = Join-Path $templatePath "AGENTS.md"
$templateReferenceMemoryPath = Join-Path $templatePath "00_project\reference-memory.md"
$templateStatusPath = Join-Path $templatePath "00_project\project-status.md"

if (-not (Test-Path -LiteralPath $projectControlPath)) {
    throw "这不是电影项目文件夹，缺少：$projectControlPath"
}

foreach ($requiredFile in @($templateAgentsPath, $templateRoutingPath, $templateReferenceMemoryPath, $templateStatusPath)) {
    if (-not (Test-Path -LiteralPath $requiredFile)) {
        throw "安装包缺少规则模板：$requiredFile"
    }
}

$backupPath = Join-Path $projectControlPath ("rule-backup-" + (Get-Date -Format "yyyyMMdd-HHmmss"))
New-Item -ItemType Directory -Path $backupPath -Force | Out-Null

$projectAgentsPath = Join-Path $resolvedProjectPath "AGENTS.md"
$projectRoutingPath = Join-Path $projectControlPath "routing.md"
$projectReferenceMemoryPath = Join-Path $projectControlPath "reference-memory.md"
$projectStatusPath = Join-Path $projectControlPath "project-status.md"

foreach ($existingFile in @($projectAgentsPath, $projectRoutingPath, $projectStatusPath)) {
    if (Test-Path -LiteralPath $existingFile) {
        Copy-Item -LiteralPath $existingFile -Destination $backupPath -Force
    }
}

if (-not (Test-Path -LiteralPath $projectStatusPath)) {
    Copy-Item -LiteralPath $templateStatusPath -Destination $projectStatusPath
} else {
    $statusText = Get-Content -LiteralPath $projectStatusPath -Raw
    $v3StatusLines = @(
        "项目入口：待判断（A从零 / B完整剧本 / C部分资料 / D高手镜头优化）",
        "作者剧本锁定：不适用 / 未确认 / 已锁定",
        "生产资料状态：未检查 / 缺失待补 / 已就绪",
        "视频模型：未选择 / Seedance 2.0 / MiniMax H3 / 双版本",
        "镜头规划状态：未开始 / 待确认 / 已确认",
        "连续性模式：纯文字 / Lira资产 / 首尾帧"
    )
    $missingStatusLines = $v3StatusLines | Where-Object { $statusText -notmatch [regex]::Escape($_.Split('：')[0] + '：') }
    if ($missingStatusLines.Count -gt 0) {
        Add-Content -LiteralPath $projectStatusPath -Value ("`r`n## V3 生产状态`r`n" + ($missingStatusLines -join "`r`n")) -Encoding utf8
    }
}

$projectKeyframesPath = Join-Path $resolvedProjectPath "05_shots\keyframes"
New-Item -ItemType Directory -Path $projectKeyframesPath -Force | Out-Null

Copy-Item -LiteralPath $templateAgentsPath -Destination $projectAgentsPath -Force
Copy-Item -LiteralPath $templateRoutingPath -Destination $projectRoutingPath -Force
$referenceMemoryResult = "已保留现有 00_project\reference-memory.md"
if (-not (Test-Path -LiteralPath $projectReferenceMemoryPath)) {
    Copy-Item -LiteralPath $templateReferenceMemoryPath -Destination $projectReferenceMemoryPath
    $referenceMemoryResult = "已新增空白 00_project\reference-memory.md"
}

$logPath = Join-Path $projectControlPath "rule-upgrade-log.md"
@"
# 规则升级记录

升级时间：$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
升级内容：V3 项目入口、作者剧本接管、镜头规划、双模型提示词、连续性编译与跨阶段参考记忆机制
已备份：$backupPath
参考记忆：$referenceMemoryResult
未修改：故事、角色、剧本、资产、表演、镜头、提示词和历史版本
"@ | Set-Content -LiteralPath $logPath -Encoding utf8

Write-Output "旧电影工程规则升级完成：$resolvedProjectPath"
Write-Output "规则备份位置：$backupPath"
Write-Output "已更新：AGENTS.md、00_project\routing.md、V3 项目状态字段、05_shots\keyframes"
Write-Output $referenceMemoryResult
Write-Output "未修改：所有创作成果与项目历史"
