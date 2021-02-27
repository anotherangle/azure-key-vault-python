from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


KVUri = "your_key_Vault_uri"
secretName = "your_secret_name"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
retrieved_secret = client.get_secret(secretName)

print(f"The value of secret '{secretName}' is: '{retrieved_secret.value}'")
