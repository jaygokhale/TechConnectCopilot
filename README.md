# Tech Connect Copilot - Interactive Copilot agent project for Contoso, Inc. 

This project is a collaborative effort between Microsoft and Contoso, Inc. to create an interactive Copilot agent that can read data in a data table inside of an Azure Storage Account, and utilize it to help users self-serve their basic technical support needs.  The flow of this project is as follows:

1.  Ticket data to be exported from Contoso's ITSM on a regular basis into a data table within an Azure Storage Account.
2.  Azure AI Search will be used to index the data table, and it will utilize Azure OpenAI to generate embedding data, finally storing these vectors in a
    vector index.  It's search indexes will be made available to the Copilot agent by proxy of the Power Platform, and the azure AI Search connector contained therein.
3.  The copilot agent's flow is built and managed using Copilot studio, and published to the end users via Microsoft Teams. 

## Getting Started

The first step in this project is to deploy the infrastructure assets needed for the solution.  These steps can be found in the [Infrastructure](./00-infrastructure/README.md) instructions.

Next, you will need to create the index that the Copilot agent will use to answer questions.  This can be done using either a Python script or a Jupyter notebook.  The steps for both methods can be found in the [ai-search](./01-ai-search/README.md) instructions.

Third, you will need to import the solution file into Power Platform.  The steps for this can be found in the [Power Platform](./02-copilot/PowerPlatform.md) instructions.

Fourth, you will need to verify and configure the copilot agent in copilot studio.  The steps for this can be found in the [CopilotStudio](./02-copilot/CopilotStudio.md) instructions.

Fifth, you will need to publish the agent to Microsoft Teams.  The steps for this can be found in the [Publishing](./02-copilot/publish.md) instructions.

Finally, you will need to test the agent in Microsoft Teams.  The steps for this can be found in the [Testing](./02-copilot/testing.md) instructions.

## Reference

The material for this project is based on the following resources:

- [Copilot Studio - Overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)
- [Copilot Studio - Create a Copilot Agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot)
- [Copilot Studio - Publish a Copilot to Microsoft Teams](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)
- [Azure AI Search - Overview](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search)
- [Azure AI Search - Chat with your Data](https://learn.microsoft.com/en-us/azure/ai-services/openai/use-your-data-quickstart?context=%2Fazure%2Fsearch%2Fcontext%2Fcontext&tabs=keyless%2Ctypescript-keyless%2Cpython-new&pivots=ai-foundry-portal)


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
