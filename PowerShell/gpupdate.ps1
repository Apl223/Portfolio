# Prompt the user for computer names
$computers = Read-Host -Prompt "Enter the target workstation name or IPs (comma-separated)"

# Convert the comma-separated string to an array
$computers = $computers -split ','

# Path to PsExec executable
$psexecCommand = "psexec.exe"

foreach ($computer in $computers) {
    # Execute gpupdate /force remotely

    $process = & $psexecCommand "\\$computer" gpupdate /force
    
    if ($process -match "completed successfully") {
        Write-Host "gpupdate completed successfully on $computer. Restarting computer..."

        # Restart the computer
        & $psexecCommand "\\$computer" shutdown /r /t 0

        Write-Host "$computer is restarting..."
        
    } else {
        Write-Host "Error: gpupdate failed on $computer with output: $process"
    }
}