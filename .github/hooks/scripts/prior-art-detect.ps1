# prior-art-detect.ps1
# UserPromptSubmit hook — Windows version
# Install: copy to ~\.copilot\hooks\scripts\prior-art-detect.ps1

$input_data = [Console]::In.ReadToEnd()

try {
    $data = $input_data | ConvertFrom-Json
    $prompt = $data.prompt
} catch {
    exit 0
}

$pattern = '/kiro-spec|spec-design|spec-requirement|spec-tasks|design\.md|requirements\.md|tasks\.md|architecture|implement'

if ($prompt -match $pattern) {
    $output = @{
        hookSpecificOutput = @{
            hookEventName = "UserPromptSubmit"
            additionalContext = "💡 Prior art check recommended: this looks like a design or implementation decision. Before building, consider running: @prior-art full <your topic>  (checks concept names, OSS options, platform-native features, failure modes)"
        }
    }
    $output | ConvertTo-Json -Compress
}
