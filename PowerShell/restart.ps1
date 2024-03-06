# Prompt the user for computer names
$computers = Read-Host -Prompt "Enter the target workstation name or IPs (comma-separated)"

# Convert the comma-separated string to an array
$computers = $computers -split ','

# Path to PsExec executable
$psexecCommand = "psexec.exe"

foreach ($computer in $computers) {
    
    # Restart the computer
    Write-Host "$computer is restarting..."
    & $psexecCommand "\\$computer" shutdown /r /t 0
        
}