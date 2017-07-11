# AzureRoleAssign
Tool to produce az-cli v2 commands to add groups with specific roles to many resource groups using json as response

https://wiki.clusterlab.com.br/index.php/AZURE

You can generate the group list and the role list with the following commands:
az ad group list > group.json
az ad sp list > keys.json
az role definition list| jq '.[]|{"properties"}'| jq '.[]|{"roleName"}' > roles.json
