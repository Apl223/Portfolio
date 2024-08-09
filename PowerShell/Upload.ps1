$Workstation = Read-Host "Enter the target workstation name or IP"  # Prompting for workstation name
echo "Navigate and select the driver you want to upload."

# Opening File Explorer to select the file
Add-Type -AssemblyName System.Windows.Forms
$openFileDialog = New-Object System.Windows.Forms.OpenFileDialog
$openFileDialog.InitialDirectory = "\\server\SD_SW\Software\SMG_Share"
$openFileDialog.ShowDialog() | Out-Null
$DriverPath = $openFileDialog.FileName

# Prompting for destination path
$DestinationPath = Read-Host "Enter the destination path on the workstation: \\$Workstation\..."

# Constructing full paths
$DriverPath = "$DriverPath"
$DestinationPath = "\\$Workstation\$DestinationPath"

# Copying the file to the destination
echo "Uploading..."
Copy-Item -Path $DriverPath -Destination $DestinationPath -Recurse
echo "Finished"
