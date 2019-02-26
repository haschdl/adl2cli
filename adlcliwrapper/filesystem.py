import hmac
import hashlib
import base64
import uuid
import datetime
import requests
from .requester import requester


#Required headers on all requests:
# x-ms-client-request-id UUID
# x-ms-date 
# Authorization, in the format Authorization="[SharedKey|SharedKeyLite] <account_name>:<Signature>"  
#  where SharedKey or SharedKeyLite is the name of the authorization scheme, account_name is the name 
#  of the account requesting the resource, and Signature is a Hash-based Message Authentication Code 
# (HMAC) constructed from the request and computed by using the SHA256 algorithm, and then encoded 
# by using Base64 encoding.

class filesystem(requester):
    """
    Operations on Filesystem, such as list, create, delete, get properties and set properties.
    """
    
    def __init__(self, api_version, account_name, dns_suffix, key):
        super().__init__(api_version, account_name, dns_suffix, key)
    

    
    def create(self, fileSystemName):
        """
        Create a filesystem rooted at the specified location. If the filesystem already exists, 
        the operation fails. 

        :param fileSystemName: The filesystem identifier. The value must start and end with a letter or 
                                        number and must contain only letters, numbers, and the dash (-) character. 
                                        Consecutive dashes are not permitted. All letters must be lowercase. 
                                        The value must have between 3 and 63 characters.
        
        """
        verb = "PUT"
        requestId = str(uuid.uuid1())
    
        url = "https://{account_name}.{dns_suffix}/{fileSystem}?resource=filesystem" \
                .format(account_name=self.account_name, dns_suffix=self.dns_suffix, fileSystem=fileSystemName)
        CanonicalizedResource = "/{account}/{fileSystem}\nresource:filesystem".format(fileSystem=fileSystemName,account=self.account_name)

        headers = self.common_headers(requestId)
        StringToSign = self.auth_template().format(verb=verb,ContentEncoding="",ContentLanguage="",ContentLength="",
                            ContentMD5="",ContentType="",Date="",IfModifiedSince="",IfMatch="",
                            IfNoneMatch="",IfUnmodifiedSince="",Range="",
                            CanonicalizedHeaders=self.canonicalized_headers(headers),
                            CanonicalizedResource=CanonicalizedResource)
        
        headers['Authorization'] = self.authorization_header(StringToSign)        
        return requests.request(verb, url, headers=headers)
        
    def delete(self, fileSystemName):
        """
        Marks the filesystem for deletion. When a filesystem is deleted, a filesystem with the same 
        identifier cannot be created for at least 30 seconds. While the filesystem is being deleted, 
        attempts to create a filesystem with the same identifier will fail with status code 409 
        (Conflict), with the service returning additional error information indicating that the 
        filesystem is being deleted. All other operations, including operations on any files or 
        directories within the filesystem, will fail with status code 404 (Not Found) while the 
        filesystem is being deleted.

        Calls https://docs.microsoft.com/en-us/rest/api/storageservices/datalakestoragegen2/filesystem/delete
        """
        verb = "DELETE"
        requestId = str(uuid.uuid1())
    
        url = "https://{account_name}.{dns_suffix}/{fileSystem}?resource=filesystem" \
                .format(account_name=self.account_name, dns_suffix=self.dns_suffix, fileSystem=fileSystemName)
        CanonicalizedResource = "/{account}/{fileSystem}\nresource:filesystem".format(fileSystem=fileSystemName, account=self.account_name)

        headers = self.common_headers(requestId)
        StringToSign = self.auth_template().format(
            verb=verb, ContentEncoding="",
            ContentLanguage="",
            ContentLength="",
            ContentMD5="",
            ContentType="",
            Date="",
            IfModifiedSince="",
            IfMatch="",
            IfNoneMatch="",
            IfUnmodifiedSince="",
            Range="",
            CanonicalizedHeaders=self.canonicalized_headers(headers),
            CanonicalizedResource=CanonicalizedResource)
        
        headers['Authorization'] = self.authorization_header(StringToSign)        
        return requests.request(verb, url, headers=headers)    


    def list(self):
        """
        List filesystems and their properties in given account. 
        The response will include up to 5000 items. No filtering
        option is available.
        """

        verb = "GET"
        
        # For Gen2, list File system use resource=account
        url = "https://{account_name}.{dns_suffix}/?resource=account".format(account_name=self.account_name, dns_suffix=self.dns_suffix)
        CanonicalizedResource = "/{account}/\nresource:account".format(account=self.account_name)
        
        #For blob storage, list containers operation is:
        #  url = "https://{account_name}.{dns_suffix}/?comp=list".format(account_name=self.account_name, dns_suffix=self.dns_suffix)
        #  CanonicalizedResource = "/{account}/\comp:list".format(account=self.account_name)
        
        requestId = str(uuid.uuid1())

        #lower-case, Sort the headers lexicographically by header name, in ascending order
        headers = self.common_headers(requestId)
        
    
        StringToSign = self.auth_template().format(verb=verb,ContentEncoding="",ContentLanguage="",ContentLength="",
                            ContentMD5="",ContentType="",Date="",IfModifiedSince="",IfMatch="",
                            IfNoneMatch="",IfUnmodifiedSince="",Range="",CanonicalizedHeaders=self.canonicalized_headers(headers),
                            CanonicalizedResource=CanonicalizedResource)
        
        headers['Authorization'] = self.authorization_header(StringToSign)        
        return requests.request(verb, url, headers=headers)
