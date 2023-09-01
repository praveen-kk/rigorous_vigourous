function Verify_b_LargerThan5 {
    param (
        [int]$b
    )

    if ($b -gt 5) {
        Write-Host "b=$b is larger than 5."
    } else {
        Write-Host "b=$b is not larger than 5."
    }
}

# Call the function with a command-line argument
$cliArgument = Read-Host "Enter the value of b "
Verify_b_LargerThan5 $cliArgument
