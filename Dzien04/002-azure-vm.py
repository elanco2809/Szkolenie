# pip install azure - identity
# pip install azure-mgmt-compute

from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import VirtualMachine
import os

AZURE_SUBSCRIPTION_ID = ""


print(os.environ.get("AZURE_SUBSCRIPTION_ID"))

subscription_id = AZURE_SUBSCRIPTION_ID
credentials = ClientSecretCredential(
    client_id="9526ab1343db7",  # os.environ["AZURE_CLIENT_ID"],
    client_secret="F16AKdM4z5r",  # os.environ["AZURE_CLIENT_SECRET"],
    tenant_id="0ae705af731",  # os.environ["AZURE_TENANT_ID"],
)


compute_client : ComputeManagementClient = ComputeManagementClient(credentials, AZURE_SUBSCRIPTION_ID)

print("VM List")
for vm in compute_client.virtual_machines.list_all():
    print(vm.name, vm.id.split("/")[4])

compute_client.virtual_machines.\
    begin_create_or_update("test",
                           "linux-marian",
                            VirtualMachine(location="westeurope", tags={
                                "owner" : "MarianWitkowski"
                            })
                           ).wait()

print("Get info about VM")
details = compute_client.virtual_machines.get("TEST", "linux-marian")
print(details)

operation = compute_client.virtual_machines.begin_power_off("TEST","linux-marian")
operation.wait()
print("Po power-off")

operation = compute_client.virtual_machines.begin_start("TEST", "linux-marian")
operation.wait()
print("Po start")
