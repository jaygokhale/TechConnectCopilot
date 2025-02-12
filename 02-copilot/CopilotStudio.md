# Copilot Studio Instructions

## Configure the Agent and Knowledge Sources in Copilot Studio
 Go to [Copilot Studio Preview Center](https://copilotstudio.preview.microsoft.com) and select the appropriate environment from the dropdown at the upper right corner of the browser window as you did previously with the Power Platform steps.  
 
 ### NOTE: as of time of writing, the features used in this exercise are in preview.  Thus, it is important to use the preview version of Copilot Studio.

 From here, you can start to build your agent. The first step is to create a new agent.  Click the "Create Agent" button to get started.  Otherwise, you can attempt to "speak your agent into existence using prompt engineering.  The prompt that this exercise used to create this agent is below.

``` I want to create an agent that can act as a level 1 help desk support agent.  The agent will be published to Microsoft Teams, and when I user clicks on the agent and starts a new session by saying technical support, the conversation should begin.  The agent should ask the user their name, and it should be stored as a global variable called "user_name".   Then, the agent should ask the user which city they are in, and their city should be stored as a global variable called "city".  Next, the agent should ask the user if this is a new issue, or an existing issue.  This choice should be in the form of a multiple choice question with buttons, and when the user selects the value, it should be stored in a global variable called "issue_type" which can accept one or two values, new issue or existing issue.  

If the value is new issue, the next step is to ask the user what their problem seems to be, and this will be stored as a new variable called "problem_statement". This value is passed onto generative AI for understanding and reasoning.  Generative AI will query the azure search index knowledge source for any relevant previous cases. The agent will respond to the user with a brief restatement of the problem, and then present the previous cases to the user for their review.  It will then ask them if any of the presented cases match their problem, and if they are able to help the user to solve their issue.  The user will then be presented with another multiple choice question with two possible answers, yes and no.  If the user answers yes, then proceed to the conversation closeout step mentioned below.  

If the value for the "issue_type" variable is "existing issue", then ask the user if they have a previous case number.  They can either enter an 8 digit case number, or say "I don't have one".  If they enter the 8 digit case number, query the azure search index for the case number and present it to the user with a brief description of the status of the case.  If they don't, then proceed onto the "connect to a live agent" step mentioned below.

For the live agent step, simply display a message stating that "this function is under construction.  Please check back later."  Proceed to the conversation closeout step below.
```

The prompt above creates a conversational agent in Copilot Studio.  But, this is just the start.  There is still much to do before this agent can be published and used successfully by users.  The next step is to add in the knowledge source that the agent will use to query for information.  Click on the "Knowledge Sources" tab and then click the "Add Knowledge Source" button.  Select the Azure AI Search connector that you created in the previous step, and then select the index that you want to use.  In this case, it is the index shown below.  Click save to continue.  Then, if connected properly, you will see the status of the connector as "connected" as shown below.

With the knowledge source configured, you can now start to build out the conversation.  Click on the "Topics" tab and review the topics created by generative AI during agent creation.  Review each ot these topics to get an idea of how accurately the agent was created.  You can edit the topics to add or remove steps, and you can also add in new topics as needed.  The topics that were created by generative AI are shown below.

You can now proceed to the next step of [Configuring the Conversation](./Conversation.md)