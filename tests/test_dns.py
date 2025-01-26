import pytest
import logging

from vultr.apis.dns import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_domains(api_key):
    """
    Test list_domains function with different parameter combinations.
    """
    try:
        # Test case 1: List all domains
        result = await list_domains()
        if result.get("status") != 200:
            raise Exception(f"list_domains (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_domains - no params) - Response Data:\n%s", result)

        # Test case 2: List domains with per_page
        result = await list_domains(per_page=50)
        if result.get("status") != 200:
            raise Exception(f"list_domains(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_domains - per_page) - Response Data:\n%s", result)

        # Test case 3: List domains with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_cursor_here' with a real cursor from a previous response
        # result = await list_domains(cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_domains(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_domains - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_domain(api_key):
    """
    Test create_domain function.
    """
    try:
        # Test case: Create a domain (replace with your desired parameters)
        create_data = dns.CreateDomainData(domain="example-domain.com").ip("192.168.1.1").dns_sec("disabled")
        result = await create_domain(data=create_data)

        # 400 : Domain already exists
        if result.get("status") != 201 and result.get("status") != 400:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_domain(api_key):
    """
    Test get_domain function.
    """
    try:
        # Test case: Get domain information (replace 'your_domain' with a real domain)
        result = await get_domain(dns_domain="your_domain")  # Replace 'your_domain' with a real domain

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_domain(api_key):
    """
    Test update_domain function.
    """
    try:
        # Test case: Update domain information (replace 'your_domain' with a real domain)
        update_data = dns.UpdateDomainData(dns_sec="enabled")
        result = await update_domain(dns_domain="your_domain", data=update_data)  # Replace 'your_domain' with a real domain

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_domain(api_key):
#     """
#     Test delete_domain function.
#     """
#     try:
#         # Test case: Delete domain (replace 'your_domain' with a real domain)
#         result = await delete_domain(dns_domain="your_domain")  # Replace 'your_domain' with a real domain

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_domain_soa(api_key):
    """
    Test get_domain_soa function.
    """
    try:
        # Test case: Get domain SOA information (replace 'your_domain' with a real domain)
        result = await get_domain_soa(dns_domain="your_domain")  # Replace 'your_domain' with a real domain

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_domain_soa(api_key):
    """
    Test update_domain_soa function.
    """
    try:
        # Test case: Update domain SOA information (replace 'your_domain' with a real domain)
        update_data = dns.UpdateDomainSOAData().email("updated@example.com")
        result = await update_domain_soa(dns_domain="your_domain", data=update_data)  # Replace 'your_domain' with a real domain

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_domain_dnssec(api_key):
    """
    Test get_domain_dnssec function.
    """
    try:
        # Test case: Get domain DNSSEC information (replace 'your_domain' with a real domain)
        result = await get_domain_dnssec(dns_domain="your_domain")  # Replace 'your_domain' with a real domain

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_domain_records(api_key):
    """
    Test list_domain_records function with different parameter combinations.
    """
    try:
        # Test case 1: List all domain records (replace 'your_domain' with a real domain)
        result = await list_domain_records(dns_domain="your_domain") # Replace 'your_domain' with a real domain
        if result.get("status") != 200:
            raise Exception(f"list_domain_records (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_domain_records - no params) - Response Data:\n%s", result)

        # Test case 2: List domain records with per_page
        result = await list_domain_records(dns_domain="your_domain", per_page=50) # Replace 'your_domain' with a real domain
        if result.get("status") != 200:
            raise Exception(f"list_domain_records(per_page=50) failed: {result}")
        logger.info("\nTest Case 2 (list_domain_records - per_page) - Response Data:\n%s", result)

        # Test case 3: List domain records with cursor (assuming a cursor is available from previous responses)
        # Replace 'your_domain' and 'your_cursor_here' with real values
        # result = await list_domain_records(dns_domain="your_domain", cursor="your_cursor_here")
        # if result.get("status") != 200:
        #     raise Exception(f"list_domain_records(cursor=...) failed: {result}")
        # logger.info("\nTest Case 3 (list_domain_records - cursor) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_domain_record(api_key):
    """
    Test create_domain_record function.
    """
    try:
        # Test case: Create a domain record (replace with your desired parameters)
        create_data = dns.CreateDomainRecordData(name="testrecord", type="A", data="192.168.1.1", ttl=300)
        result = await create_domain_record(dns_domain="your_domain", data=create_data) # Replace 'your_domain' with a real domain

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_domain_record(api_key):
    """
    Test get_domain_record function.
    """
    try:
        # Test case: Get domain record information (replace with your desired parameters)
        result = await get_domain_record(dns_domain="your_domain", record_id="your_record_id") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_domain_record(api_key):
    """
    Test update_domain_record function.
    """
    try:
        # Test case: Update domain record information (replace with your desired parameters)
        update_data = dns.UpdateDomainRecordData().name("updated-record").data("192.168.1.2")
        result = await update_domain_record(dns_domain="your_domain", record_id="your_record_id", data=update_data) # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_domain_record(api_key):
#     """
#     Test delete_domain_record function.
#     """
#     try:
#         # Test case: Delete domain record (replace with your desired parameters)
#         result = await delete_domain_record(dns_domain="your_domain", record_id="your_record_id") # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")