
# pip install azure-mgmt-resource
#  pip install msrestazure

from azure.mgmt.resource import ResourceManagementClient
from azure.identity import ClientSecretCredential

AZURE_SUBSCRIPTION_ID = ""


subscription_id = AZURE_SUBSCRIPTION_ID
credentials = ClientSecretCredential(
    client_id="",  # os.environ["AZURE_CLIENT_ID"],
    client_secret="",  # os.environ["AZURE_CLIENT_SECRET"],
    tenant_id="",  # os.environ["AZURE_TENANT_ID"],
)

def print_item(group):
    print("="*50)
    print("Name:", group.name)
    print("Id:", group.id)
    print("Location:", group.location)
    print("Tags:", group.tags)

client = ResourceManagementClient(credentials, subscription_id)
print("List Resource Groups")
for item in client.resource_groups.list():
    print_item(item)

GROUP_NAME = "marianwitkowskigroup"
GROUP_PROPS = { "location":"westus" }
print("Create res gorup")
client.resource_groups.create_or_update(GROUP_NAME, GROUP_PROPS )

#GROUP_PROPS["location"] = "westeurope"
#client.resource_groups.create_or_update(GROUP_NAME, GROUP_PROPS )

client.resource_groups.begin_delete(GROUP_NAME).wait()

print("OK")




