# Prompt the user for computer names
# This script doesn't work well when querying multiple computers, results will overlap and readability will be worse.
$computer = Read-Host -Prompt "Enter the target workstation name or IP (comma-separated)"

Write-Host "Querying to see if anyone is logged onto $computer..."
# Query
query user /server:$computer
