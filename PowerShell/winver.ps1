# Prompt the user for computer names
$computers = Read-Host -Prompt "Enter computer names or IPs (comma-separated)"

# Convert the comma-separated string to an array
$computers = $computers -split ','

foreach ($computer in $computers) {

    try {
        # Query the registry to get the Windows 10 build number
        $reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', $computer)
        $key = $reg.OpenSubKey("SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        $buildNumber = $key.GetValue("CurrentBuildNumber")
        $ubr = $key.GetValue("UBR")

        if ($buildNumber -and $ubr) {
            $fullVersion = "$buildNumber.$ubr"
            Write-Host "$computer : Windows Version $fullVersion"
        } else {
            Write-Host "Error: Failed to retrieve WinVer information on $computer."
        }
    } catch {
        if ($_.Exception.Message -like "*The network path was not found.*") {
            Write-Host "Error: $computer is unreachable."
        } else {
            Write-Host "Error: $_"
        }
    }
}
