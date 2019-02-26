from .requester import requester
import uuid
import requests

class path(requester):
    """
    Operations on Filesystem, such as list, create, delete, get properties and set properties.
    """
    
    def __init__(self, api_version, account_name, dns_suffix, key):
        super().__init__(api_version, account_name, dns_suffix, key)
    
    def list(self, file_system, recursive=True):
        verb = "GET"
        requestId = str(uuid.uuid1())
        url = "http://{account_name}.{dns_suffix}/{file_system}?recursive={recursive}&resource=filesystem" \
              .format(
                  account_name=self.account_name,
                  dns_suffix=self.dns_suffix,
                  file_system=file_system,
                  recursive=recursive)
        CanonicalizedResource = "/{account_name}/{file_system}\nrecursive:{recursive}\nresource:filesystem" \
            .format(file_system=file_system, account_name=self.account_name,recursive=recursive)
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

    def create_file(self, file_system, path, file_contents, size):
        """
        Creates a file
        """

        verb = "PUT"
        requestId = str(uuid.uuid1())
    
        url = "https://{account_name}.{dns_suffix}/{file_system}/{path}?resource=file" \
                .format(
                    account_name=self.account_name,
                    dns_suffix=self.dns_suffix,
                    file_system=file_system,
                    path=path)
        CanonicalizedResource = "/{account_name}/{file_system}/{path}\nresource:file" \
            .format(file_system=file_system,path=path, account_name=self.account_name)

        headers = self.common_headers(requestId)
        StringToSign = self.auth_template().format(
            verb=verb,
            ContentEncoding="",
            ContentLanguage="",
            ContentLength="",#str(size),
            ContentMD5="",
            ContentType="",#application/octet-stream",
            Date="",
            IfModifiedSince="",
            IfMatch="",
            IfNoneMatch="",
            IfUnmodifiedSince="",
            Range="",
            CanonicalizedHeaders=self.canonicalized_headers(headers),
            CanonicalizedResource=CanonicalizedResource)
        
        #print("String to sign:")
        #print(StringToSign)
        headers['Authorization'] = self.authorization_header(StringToSign)        
        #headers['Content-Length'] = str(size)
        #headers['Content-Type'] = "application/octet-stream"

        return requests.request(verb, url, headers=headers, data=file_contents)