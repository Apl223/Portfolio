# Prompt the user for computer names
$computers = Read-Host -Prompt "Enter the target workstation name or IPs (comma-separated)"

# Convert the comma-separated string to an array
$computers = $computers -split ','

# Path to PsExec executable
$psexecCommand = "psexec.exe"

foreach ($computer in $computers) {
    echo ""
    # Execute actions remotely using PsExec and wmic
    Write-Host "Triggering Hardware Inventory Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000021}"' | Out-Null
    echo ""
    Write-Host "Triggering Application Deployment Evaluation Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000113}"' | Out-Null
    echo ""
    Write-Host "Triggering Discovery Data Collection Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000026}"' | Out-Null
    echo ""
    Write-Host "Triggering File Collection Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000003}"' | Out-Null
    echo ""
    Write-Host "Triggering IDMIF Collection Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000019}"' | Out-Null
    echo ""
    Write-Host "Triggering Machine Policy Retrieval Evaluation Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000020}"' | Out-Null
    echo ""
    Write-Host "Triggering Software Inventory Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000001}"' | Out-Null
    echo ""
    Write-Host "Triggering Software Metering Usage Report Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000016}"' | Out-Null
    echo ""
    Write-Host "Triggering Software Updates Deployment Evaluation Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000108}"' | Out-Null
    echo ""
    Write-Host "Triggering Software Updates Scan Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000113}"' | Out-Null
    echo ""
    Write-Host "Triggering User Policy Retrieval Evaluation Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000022}"' | Out-Null
    echo ""
    Write-Host "Triggering Windows Installer Source List Update Cycle on $computer..."
    & $psexecCommand "\\$computer" wmic /namespace:\\root\ccm path sms_client CALL TriggerSchedule '"{00000000-0000-0000-0000-000000000028}"' | Out-Null
    echo ""
    Write-Host "Actions in Configuration Manager completed on $computer."
}