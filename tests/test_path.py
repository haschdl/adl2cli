import os
from adlcliwrapper.path import path

account_name = os.getenv("AZ_ADL_ACCOUNT")
dns_suffix = os.getenv("AZ_DNS_SUFFIX")
key = os.getenv("AZ_SHARED_KEY")
apiVersion = os.getenv("AZ_API_VERSION")




def test_path_const():
    """Tests ADL Gen2 path list operation"""

    cli = path(apiVersion, account_name, dns_suffix, key)
    assert isinstance(cli, path)

def test_path_list():
    """Tests ADL Gen2 path list operation"""

    cli = path(apiVersion, account_name, dns_suffix, key)
    resp = cli.list("fs01")
    print(resp.json())
    assert resp.json()['paths']
    
def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))



def test_path_create_file():
    """Tests ADL Gen2 path ist operation"""

    cli = path(apiVersion, account_name, dns_suffix, key)
    local_path = 'C:/Sandbox/adlcli/tests/data/file01.png'
    size = os.path.getsize(local_path)
    with open(local_path, 'rb') as fh:
        #file_contents = fh.read()
        resp = cli.create_file("fs01", "file1.png", fh, size)

        pretty_print_POST(resp.request)
    print(resp.content)
    assert False