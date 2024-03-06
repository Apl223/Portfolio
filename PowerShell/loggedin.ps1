# Prompt the user for computer names
$computers = Read-Host -Prompt "Enter the target workstation name or IPs (comma-separated)"

# Convert the comma-separated string to an array
$computers = $computers -split ','

foreach ($computer in $computers) {
    
    # Query
    query user /server:$computer

    Write-Host "Querying to see if anyone is logged onto $computer..."
        
}