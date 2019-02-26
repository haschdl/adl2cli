from adlcliwrapper.filesystem import filesystem
import os
from json import dumps
import uuid
import pytest


account_name = os.getenv("AZ_ADL_ACCOUNT")
dns_suffix = os.getenv("AZ_DNS_SUFFIX")
key = os.getenv("AZ_SHARED_KEY")
apiVersion = os.getenv("AZ_API_VERSION")




def test_const():
    """Tests ADL Gen2 list operation"""

    cli = filesystem(apiVersion, account_name, dns_suffix, key)

    assert isinstance(cli, filesystem)


def test_list():
    """Tests ADL Gen2 FileSystem list operation
    """

    cli = filesystem(apiVersion, account_name, dns_suffix, key)
    resp = cli.list()
    fileSystems = resp.json()
    print(dumps(fileSystems,indent=4))
    assert fileSystems['filesystems']


def test_create():
    """Tests ADL Gen2 FileSystem create operation
    See more at https://docs.microsoft.com/en-us/rest/api/storageservices/datalakestoragegen2/filesystem/create"""

    cli = filesystem(apiVersion, account_name, dns_suffix, key)
    fileSystemName = "fs-" + str(uuid.uuid1())
    respCreate = cli.create(fileSystemName)
    assert respCreate.status_code == 201 #Created


def test_delete():
    """Tests ADL Gen2 FileSystem delete operation
    """
    cli = filesystem(apiVersion, account_name, dns_suffix, key)

    fileSystemName = "fs-" + str(uuid.uuid1())
    respCreate = cli.create(fileSystemName)
    assert respCreate.status_code == 201 #Created
    respDelete = cli.delete(fileSystemName)
    assert respDelete.status_code == 202 #Accepted
