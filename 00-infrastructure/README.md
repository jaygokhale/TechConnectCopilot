# Azure Assets deployment

## Steps to deploy to azure

1.  Install az cli using the distribution of your choice from the link below. Here are instructions on how to install the azure CLI. https://learn.microsoft.com/en-us/cli/azure/install-azure-cli . If the Azure Cli is already installed you can check with az --version. 
2.  After install, do az login.  Select your tenant / subscription. 
3.  run the following command to create a resource group.  Replace the values in <> with your own values.
    az group create --name <your-resource-group-name> --location <your-location>
4.  Open the parameters.json file and replace the values in <> with your own values.
5.  run the following command to deploy the resources.  Replace the values in <> with your own values.
    az deployment group create --resource-group <your-resource-group-name> --template-file main.bicep --parameters parameters.json
