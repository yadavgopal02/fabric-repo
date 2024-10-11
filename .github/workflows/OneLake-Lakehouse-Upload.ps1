#Powershell script to upload files to OneLake

#Install the following module if you haven't got in installed
#Install-Module Az.Storage -Repository PSGallery -Force

###############################################################################################################################################################################
#Fill in the paramters
$tenantId = '55ea6196-70b9-4411-92f5-04a54791f120'                                                #Get from the Azure Portal
$workspaceGUID = '0fde94f2-391e-42c0-bc8c-f29f17cac5f6'                                           #Get from Power BI URL
$lakehouseGUID = '958077ec-bae1-4bda-b9a2-2116158d5879'                                           #Get from Power BI URL

$localFolderPath = ''                                         #Local file path always end with /
$localFiles = @('Samplecsvdata.csv')                                           #Remove all files for entire folder - @(). #Otherwise list files out - @('File1.csv', 'File2.txt', 'File3.pdf')
$uploadFolderPath = '/Files/test/'                                 #Leave '/Files/' for root folder, always end with /

###############################################################################################################################################################################

Connect-AzAccount -TenantId $tenantId | out-null
#az login --username "gopal.yadav@stratacent.com" --password 'F2afgchgrf@Strata'
Install-Module -Name Az.Storage -Repository PSGallery -Force -Scope CurrentUser
Import-Module Az.Storage
Get-Command -Module Az.Storage
$ctx = New-AzStorageContext -StorageAccountName 'onelake' -UseConnectedAccount -endpoint 'fabric.microsoft.com' 
#Context is needed to upload to Onelake and not Data Lake

$Count = $localFiles.Count
if ($Count -eq 0)                       #If there were no files provided, upload entire folder
{
   $Files = Get-ChildItem -Path $localFolderPath
    foreach ($f in $Files) 
    {
          $uploadPath = $lakehouseGUID + $uploadFolderPath + $f
          $localPath = $localFolderPath + $f
          New-AzDataLakeGen2Item -Context $ctx -FileSystem $workspaceGUID -Path $uploadPath -Source $localPath -Force | out-null
          $TextOutput = "Uploading " + $f
          Write-Output $TextOutput
    }    

}
else                                    #If there were files provided, upload those files
{   
    foreach ($f in $localFiles)
    {
            $uploadPath = $lakehouseGUID + $uploadFolderPath + $f
            $localPath = $localFolderPath + $f
            New-AzDataLakeGen2Item -Context $ctx -FileSystem $workspaceGUID -Path $uploadPath -Source $localPath -Force | out-null
            $TextOutput = "Uploading " + $f
            Write-Output $TextOutput
    }
}
