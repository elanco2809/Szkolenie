# pip install azure-storage-blob

from azure.storage.blob import ContainerClient, BlobServiceClient, BlobClient, StandardBlobTier, PremiumPageBlobTier

cs = ""

block_service_client : BlobServiceClient = BlobServiceClient.from_connection_string(cs)
account_info = block_service_client.get_account_information()
print(account_info)

CONTAINER_NAME = "kontener1"
BLOB_NAME = "auto.jpg"

try:
    container_client : ContainerClient = ContainerClient.from_connection_string(cs, CONTAINER_NAME)
    container_client.create_container()
    container_client.set_container_metadata( {"departament":"IT"} )
    print(container_client.get_container_properties().metadata)
except Exception as exc:
    print(exc)

blob_client: BlobClient = BlobClient.from_connection_string(conn_str=cs,
                                                            container_name=CONTAINER_NAME,
                                                            blob_name=BLOB_NAME)
# zapisz
with open("../Dzien02/images/WY3371X.jpg","rb") as fd:
    blob_client.upload_blob(fd, overwrite=True)
    #blob_client.set_standard_blob_tier(StandardBlobTier.Cool)
    #blob_client.set_premium_page_blob_tier(PremiumPageBlobTier.)

# odczyt
with open("auto.jpg","wb") as fd:
    fd.write( blob_client.download_blob().readall() )

# listowanie blobów
for blob in container_client.list_blobs():
    print(blob.name)

# usuwanie blobow
blob_client.delete_blob()

# listowanie kontenerów
all_containers = block_service_client.list_containers(include_metadata=True)
for container in all_containers:
    print(f"{container['name']}, {container['metadata']}")

block_service_client.delete_container(CONTAINER_NAME)


