# Power Platform Instructions

## Configure the Power Platform Environment

Go to [Power Platform Admin Center ](https://admin.powerplatform.microsoft.com/) and create a new environment.  You can choose whether or not to create an environment with or without a dataverse database.  

<img src="../assets/images/1.jpg" alt="Power Platform Admin Center" width="600" height="800">

<img src="../assets/images/2.jpg" alt="Create the new Environment" width="309" height="750">

Information on both options are below.  Be sure to select the correct environment for your licensing type.  The environment will take some time to Prepare.   Wait until the state says "ready" before continuing onward to step 2.

<img src="../assets/images/3.jpg" alt="Power Platform Env status" width="924" height="186">

- [Create an environment with a database](https://learn.microsoft.com/en-us/power-platform/admin/create-environment#create-an-environment-with-a-database)
- [Create an environment without a Database](https://learn.microsoft.com/en-us/power-platform/admin/create-environment#create-an-environment-with-a-database)

## Configure the Azure AI Search Connector

With the new environment prepared, it is time to create the required data connection to your Azure AI Search index.  go to the [Power Apps portal](https://make.powerapps.com/) and select the appropriate environment from the dropdown at the upper right corner of the browser window. 

<img src="../assets/images/4.jpg" alt="Power Platform Env selection" width="600" height="800">

Then, go to connectors and scroll down to Azure AI Search.  Click the Plus symbol to add this connector to your environment. 

<img src="../assets/images/5.jpg" alt="Power Platform Connector select" width="1134" height="523">

Configure this connector with the following values. Click save to continue.  You will know if the values and access are connect if the connector says that it is now connected.

<img src="../assets/images/6.jpg" alt="Power Platform Conn Variables" width="700" height="500">

- Azure AI Search endpoint (Available in the Azure portal or from the CLI)
- Azure AI Search API Key (Available in the Azure Portal)
- Display name (Enter the value you choose)
- Authentication Type (Access Key is all that is available at time of writing)

After saving, you will see the connector in the list of connectors.  If it says "connected" then you are ready to move on to the next step.  If no, go back and verify that you have entered the right values for the variables in the previous step. 

<img src="../assets/images/7.jpg" alt="Power Platform conn status" width="924" height="186">

You have now successfully configured the Azure AI Search connector for use in your Power Platform environment.  Please move on to the next step of [Creating the agent in Copilot Studio](./CopilotStudio.md)