# Prompt the user for computer names
$computers = Read-Host -Prompt "Enter computer names or IPs (comma-separated)"
 
# Convert the comma-separated string to an array
$computers = $computers -split ','
 
# Path to PsExec executable
$psexecCommand = "psexec.exe"
 
foreach ($computer in $computers) {
	echo ""
	Write-Host "MAC for the NIC thats currently being used for internet access:"
	Get-WmiObject -Class Win32_NetworkAdapterConfiguration -ComputerName $computer | Where-Object { $_.IPEnabled -eq $true -and $_.DefaultIPGateway -ne $null } | Select-Object -ExpandProperty MACAddress
	echo ""
}