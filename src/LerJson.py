import json
class LerJson:
    def __init__(self,config,tipo):
        self.conffile = config
        self.tipo=tipo
        self.dados = json.loads(open(self.conffile).read())
    def getAzCommands(self):
        for k1, v1 in self.dados.items():
            if self.tipo == "grupo":
                for k2 in self.dados[k1]["GroupID"]:
                    for k3 in self.dados[k1]["Roles"]:
                        print("az role assignment create  --assignee " + k2['objectId'] + " --role " + k3 + " --resource-group " + self.dados[k1]["ResourceGroup"])
            if self.tipo == "key":
                for k2 in self.dados[k1]["App-Keys"]:
                    for k3 in self.dados[k1]["Roles"]:
                        print("az role assignment create  --assignee " + k2['appId'] + " --role " + k3 + " --resource-group " + self.dados[k1]["ResourceGroup"])