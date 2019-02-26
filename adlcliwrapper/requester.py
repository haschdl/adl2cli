import hmac
import datetime
import hashlib
import base64


class requester():
    """
    Base class for all operations
    """

    def __init__(self, api_version, account_name, dns_suffix, shared_key):
        self.account_name = account_name
        self.dns_suffix = dns_suffix
        self.shared_key = shared_key
        self.api_version = api_version

    def auth_template(self):
        return (
            "{verb}\n"
            "{ContentEncoding}\n"
            "{ContentLanguage}\n"
            "{ContentLength}\n"
            "{ContentMD5}\n"
            "{ContentType}\n"
            "{Date}\n"
            "{IfModifiedSince}\n"
            "{IfMatch}\n"
            "{IfNoneMatch}\n"
            "{IfUnmodifiedSince}\n"
            "{Range}\n"
            "{CanonicalizedHeaders}\n"
            "{CanonicalizedResource}"
            )

    def common_headers(self, request_id):
        return {
            "x-ms-client-request-id": request_id,
            "x-ms-date": datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'),
            "x-ms-version": self.api_version
                }

    def authorization_header(self, message_to_sign):
        dig = hmac.new(
            base64.b64decode(self.shared_key),
            msg=message_to_sign.encode('utf-8'),
            digestmod=hashlib.sha256).digest()
        encoded_signature = base64.b64encode(dig).decode()
        return "SharedKey {accountName}:{signature}".format(
            accountName=self.account_name,
            signature=encoded_signature)

    def canonicalized_headers(self, headers):
        return '\n'.join("{!s}:{!s}".format(key, val) for (key, val) in headers.items())
