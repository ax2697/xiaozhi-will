param(
    [string]$Root,
    [string]$Config,
    [string]$Database,
    [switch]$IncludeIsolated,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

$scriptPath = Join-Path $PSScriptRoot '..\skills\film-knowledge-bridge\scripts\update_knowledge_index.ps1'
$arguments = @{}
if (-not [string]::IsNullOrWhiteSpace($Root)) { $arguments.Root = $Root }
if (-not [string]::IsNullOrWhiteSpace($Config)) { $arguments.Config = $Config }
if (-not [string]::IsNullOrWhiteSpace($Database)) { $arguments.Database = $Database }
if ($IncludeIsolated) { $arguments.IncludeIsolated = $true }
if ($DryRun) { $arguments.DryRun = $true }
& $scriptPath @arguments
exit $LASTEXITCODE
