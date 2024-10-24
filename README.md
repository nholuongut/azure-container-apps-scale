# Azure Container Apps scale configuration examples

![](https://i.imgur.com/waxVImv.png)
### [View all Roadmaps](https://github.com/nholuongut/all-roadmaps) &nbsp;&middot;&nbsp; [Best Practices](https://github.com/nholuongut/all-roadmaps/blob/main/public/best-practices/) &nbsp;&middot;&nbsp; [Questions](https://www.linkedin.com/in/nholuong/)
<br/>


## Pre-requisites

For all examples in this repository, you'll need to have a pre-existing Azure Container Apps environment and container registry. Create them using the Azure CLI.

The instructions are written for Bash. If you're using a different shell, you may need to adjust the commands.

1. Install the Azure CLI. You can find instructions [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).

    If you already have the Azure CLI installed, make sure you have the latest version by running:

    ```bash
    az upgrade
    ```

1. Install the Azure Container Apps extension by running the following command:

    ```bash
    az extension add --name containerapps --upgrade
    ```

    This command will also update the extension if you already have it installed.

1. Set some variables to use throughout the examples:

    ```bash
    export RESOURCE_GROUP_NAME=container-apps-scale
    export LOCATION=northeurope
    export ENVIRONMENT_NAME=container-apps-scale-env
    export ACR_NAME=containerappsscale$RANDOM
    ```

    The `ACR_NAME` variable is used to create a unique name for the container registry. If you want to use a specific name, replace the value of the variable with a name that is not already used by a container registry in Azure.

1. Create a resource group:

    ```bash
    az group create --name $RESOURCE_GROUP_NAME --location $LOCATION
    ```

1. Create an Azure Container Apps environment:

    ```bash
    az containerapp env create --name $ENVIRONMENT_NAME --resource-group $RESOURCE_GROUP_NAME \
        --location $LOCATION
    ```

1. Create a container registry:

    ```bash
    az acr create --name $ACR_NAME --resource-group $RESOURCE_GROUP_NAME \
        --location $LOCATION --sku Standard --admin-enabled true
    ```

You can now use the examples in this repository to learn how to configure scaling for your Azure Container Apps environment.

## Examples

- [Azure Service Bus job](azure-servicebus/job-python/README.md)

# 🚀 I'm are always open to your feedback.  Please contact as bellow information:
### [Contact ]
* [Name: nho Luong]
* [Skype](luongutnho_skype)
* [Github](https://github.com/nholuongut/)
* [Linkedin](https://www.linkedin.com/in/nholuong/)
* [Email Address](luongutnho@hotmail.com)

![](https://i.imgur.com/waxVImv.png)
![](Donate.png)
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/nholuong)

# License
* Nho Luong (c). All Rights Reserved.🌟