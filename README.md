# Azure Data Lake Gen2 Python Wrapper

This is a sandbox project for testing REST calls to Azure Data Lake Gen2 API.
REST API documentation is available at https://docs.microsoft.com/en-us/rest/api/storageservices/data-lake-storage-gen2

Current implementation serves only a exploratory test, and is not meant to be used in Production.

A better starting point for Production use is to evaluate the implementation of the Microsoft Azure Storage SDK for Python at https://github.com/Azure/azure-storage-python/tree/master/azure-storage-blob

## Authorization

This implementation only supports Shared Key authorization, based on a storage key. For more details on Shared Key 
authorization requirements, check https://docs.microsoft.com/en-us/rest/api/storageservices/authorize-with-shared-key.

Authentication with Azure Active Directory (AAD) is not implemented.
