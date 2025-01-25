from http import HTTPMethod
from typing import Optional, Literal

from proschedio import composer
from vultr import const, get_key
from vultr.structs import dns

async def list_domains(per_page: Optional[int], cursor: Optional[str]):
    """
    List all DNS Domains in your account.

    Args:
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_DOMAIN_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def create_domain(data: dns.CreateDomainData):
    """
    Create a DNS Domain for `domain`. If no `ip` address is supplied a domain with no records will be created.

    Args:
        data (CreateDomainData): The data to create the DNS Domain.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_domain(dns_domain: str):
    """
    Get information for the DNS Domain.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN.assign("dns-domain", dns_domain)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_domain(dns_domain: str, data: dns.UpdateDomainData):
    """
    Update the DNS Domain.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
        data (UpdateDomainData): The data to update the DNS Domain.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN.assign("dns-domain", dns_domain)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_domain(dns_domain: str):
    """
    Delete the DNS Domain.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN.assign("dns-domain", dns_domain)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_domain_soa(dns_domain: str):
    """
    Get SOA information for the DNS Domain.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN_SOA.assign("dns-domain", dns_domain)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_domain_soa(dns_domain: str, data: dns.UpdateDomainSOAData):
    """
    Update the SOA information for the DNS Domain. All attributes are optional. If not set, the attributes will retain their original values.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
        data (UpdateDomainSOAData): The data to update the SOA information.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN_SOA.assign("dns-domain", dns_domain)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_domain_dnssec(dns_domain: str):
    """
    Get the DNSSEC information for the DNS Domain.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN_DNSSEC.assign("dns-domain", dns_domain)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_domain_records(dns_domain: str, per_page: Optional[int], cursor: Optional[str]):
    """
    Get the DNS records for the Domain.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
        per_page (Optional[int]): Number of items requested per page. Default is 100 and Max is 500.
        cursor (Optional[str]): Cursor for paging. See [Meta and Pagination](#section/Introduction/Meta-and-Pagination).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(const.URL_DOMAIN_RECORDS.assign("dns-domain", dns_domain)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if per_page is not None:
        request.add_param("per_page", per_page)
    if cursor is not None:
        request.add_param("cursor", cursor)

    return await request.request()

async def create_domain_record(dns_domain: str, data: dns.CreateDomainRecordData):
    """
    Create a DNS record.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
        data (CreateDomainRecordData): The data to create the DNS record.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN_RECORDS.assign("dns-domain", dns_domain)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_domain_record(dns_domain: str, record_id: str):
    """
    Get information for a DNS Record.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
        record_id (str): The [DNS Record id](#operation/list-dns-domain-records).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN_RECORD.assign("dns-domain", dns_domain).assign("record-id", record_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_domain_record(dns_domain: str, record_id: str, data: dns.UpdateDomainRecordData):
    """
    Update the information for a DNS record. All attributes are optional. If not set, the attributes will retain their original values.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
        record_id (str): The [DNS Record id](#operation/list-dns-domain-records).
        data (UpdateDomainRecordData): The data to update the DNS record.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN_RECORD.assign("dns-domain", dns_domain).assign("record-id", record_id)) \
        .set_method(HTTPMethod.PATCH) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_domain_record(dns_domain: str, record_id: str):
    """
    Delete the DNS record.

    Args:
        dns_domain (str): The [DNS Domain](#operation/list-dns-domains).
        record_id (str): The [DNS Record id](#operation/list-dns-domain-records).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(const.URL_DOMAIN_RECORD.assign("dns-domain", dns_domain).assign("record-id", record_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()