import pytest
import logging

from vultr.apis.database import *

logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_list_database_plans(api_key):
    """
    Test list_database_plans function with different parameter combinations.
    """
    try:
        # Test case 1: List all database plans
        result = await list_database_plans()
        if result.get("status") != 200:
            raise Exception(f"list_database_plans (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_database_plans - no params) - Response Data:\n%s", result)

        # Test case 2: List database plans with engine filter
        result = await list_database_plans(engine="mysql")
        if result.get("status") != 200:
            raise Exception(f"list_database_plans(engine='mysql') failed: {result}")
        logger.info("\nTest Case 2 (list_database_plans - engine filter) - Response Data:\n%s", result)

        # Test case 3: List database plans with nodes filter
        result = await list_database_plans(nodes=1)
        if result.get("status") != 200:
            raise Exception(f"list_database_plans(nodes=1) failed: {result}")
        logger.info("\nTest Case 3 (list_database_plans - nodes filter) - Response Data:\n%s", result)

        # Test case 4: List database plans with region filter
        result = await list_database_plans(region="ewr")
        if result.get("status") != 200:
            raise Exception(f"list_database_plans(region='ewr') failed: {result}")
        logger.info("\nTest Case 4 (list_database_plans - region filter) - Response Data:\n%s", result)

        # Test case 5: List database plans with all filters
        result = await list_database_plans(engine="mysql", nodes=1, region="ewr")
        if result.get("status") != 200:
            raise Exception(f"list_database_plans(engine='mysql', nodes=1, region='ewr') failed: {result}")
        logger.info("\nTest Case 5 (list_database_plans - all filters) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_databases(api_key):
    """
    Test list_databases function with different parameter combinations.
    """
    try:
        # Test case 1: List all databases
        result = await list_databases()
        if result.get("status") != 200:
            raise Exception(f"list_databases (no params) failed: {result}")
        logger.info("\nTest Case 1 (list_databases - no params) - Response Data:\n%s", result)

        # Test case 2: List databases with label filter
        result = await list_databases(label="your_database_label") # Replace 'your_database_label' with a real label
        if result.get("status") != 200:
            raise Exception(f"list_databases(label=...) failed: {result}")
        logger.info("\nTest Case 2 (list_databases - label filter) - Response Data:\n%s", result)

        # Test case 3: List databases with tag filter
        result = await list_databases(tag="your_database_tag") # Replace 'your_database_tag' with a real tag
        if result.get("status") != 200:
            raise Exception(f"list_databases(tag=...) failed: {result}")
        logger.info("\nTest Case 3 (list_databases - tag filter) - Response Data:\n%s", result)

        # Test case 4: List databases with region filter
        result = await list_databases(region="ewr")
        if result.get("status") != 200:
            raise Exception(f"list_databases(region='ewr') failed: {result}")
        logger.info("\nTest Case 4 (list_databases - region filter) - Response Data:\n%s", result)

        # Test case 5: List databases with all filters
        # Replace 'your_database_label' and 'your_database_tag' with real values
        # result = await list_databases(label="your_database_label", tag="your_database_tag", region="ewr")
        # if result.get("status") != 200:
        #     raise Exception(f"list_databases(label=..., tag=..., region='ewr') failed: {result}")
        # logger.info("\nTest Case 5 (list_databases - all filters) - Response Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_database(api_key):
    """
    Test create_database function.
    """
    try:
        # Test case: Create a database (replace with your desired parameters)
        create_data = database.CreateDatabaseData(database_engine="mysql", database_engine_version="8", region="ewr", plan="vultr-dbaas-startup-8-1-50-mysql", label="test-database")
        result = await create_database(data=create_data)

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_database(api_key):
    """
    Test get_database function.
    """
    try:
        # Test case: Get database information (replace 'your_database_id' with a real database ID)
        result = await get_database(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_database(api_key):
    """
    Test update_database function.
    """
    try:
        # Test case: Update database information (replace 'your_database_id' with a real database ID)
        update_data = database.UpdateDatabaseData().label("updated-database-label")
        result = await update_database(database_id="your_database_id", data=update_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_database(api_key):
#     """
#     Test delete_database function.
#     """
#     try:
#         # Test case: Delete database (replace 'your_database_id' with a real database ID)
#         result = await delete_database(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_database_usage(api_key):
    """
    Test get_database_usage function.
    """
    try:
        # Test case: Get database usage (replace 'your_database_id' with a real database ID)
        result = await get_database_usage(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_database_users(api_key):
    """
    Test list_database_users function.
    """
    try:
        # Test case: List database users (replace 'your_database_id' with a real database ID)
        result = await list_database_users(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_database_user(api_key):
    """
    Test create_database_user function.
    """
    try:
        # Test case: Create a database user (replace 'your_database_id' with a real database ID)
        create_data = database.CreateDatabaseUserData(username="testuser")
        result = await create_database_user(database_id="your_database_id", data=create_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_database_user(api_key):
    """
    Test get_database_user function.
    """
    try:
        # Test case: Get database user information (replace with your desired parameters)
        result = await get_database_user(database_id="your_database_id", username="your_username") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_database_user(api_key):
    """
    Test update_database_user function.
    """
    try:
        # Test case: Update database user information (replace with your desired parameters)
        update_data = database.UpdateDatabaseUserData(password="newpassword")
        result = await update_database_user(database_id="your_database_id", username="your_username", data=update_data) # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_database_user(api_key):
#     """
#     Test delete_database_user function.
#     """
#     try:
#         # Test case: Delete database user (replace with your desired parameters)
#         result = await delete_database_user(database_id="your_database_id", username="your_username") # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_database_user_access_control(api_key):
    """
    Test update_database_user_access_control function.
    """
    try:
        # Test case: Update database user access control (replace with your desired parameters)
        update_data = database.UpdateDatabaseUserAccessControlData()
        update_data.permission = "read" # Example permission
        result = await update_database_user_access_control(database_id="your_database_id", username="your_username", data=update_data) # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_logical_databases(api_key):
    """
    Test list_logical_databases function.
    """
    try:
        # Test case: List logical databases (replace 'your_database_id' with a real database ID)
        result = await list_logical_databases(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_logical_database(api_key):
    """
    Test create_logical_database function.
    """
    try:
        # Test case: Create a logical database (replace with your desired parameters)
        create_data = database.CreateDatabaseLogicalDatabaseData(name="testdb")
        result = await create_logical_database(database_id="your_database_id", data=create_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_logical_database(api_key):
    """
    Test get_logical_database function.
    """
    try:
        # Test case: Get logical database information (replace with your desired parameters)
        result = await get_logical_database(database_id="your_database_id", db_name="your_db_name") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_logical_database(api_key):
#     """
#     Test delete_logical_database function.
#     """
#     try:
#         # Test case: Delete logical database (replace with your desired parameters)
#         result = await delete_logical_database(database_id="your_database_id", db_name="your_db_name") # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_topics(api_key):
    """
    Test list_topics function.
    """
    try:
# Test case: List topics (replace 'your_database_id' with a real database ID)
        result = await list_topics(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_topic(api_key):
    """
    Test create_topic function.
    """
    try:
        # Test case: Create a topic (replace with your desired parameters)
        create_data = database.CreateDatabaseTopicData(name="test-topic", partitions=1, replication=1, retention_hours=168, retention_bytes=1073741824)
        result = await create_topic(database_id="your_database_id", data=create_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_topic(api_key):
    """
    Test get_topic function.
    """
    try:
        # Test case: Get topic information (replace with your desired parameters)
        result = await get_topic(database_id="your_database_id", topic_name="your_topic_name") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_topic(api_key):
    """
    Test update_topic function.
    """
    try:
        # Test case: Update topic information (replace with your desired parameters)
        update_data = database.UpdateDatabaseTopicData(partitions=2, replication=1, retention_hours=336, retention_bytes=2147483648)
        result = await update_topic(database_id="your_database_id", topic_name="your_topic_name", data=update_data) # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_topic(api_key):
#     """
#     Test delete_topic function.
#     """
#     try:
#         # Test case: Delete topic (replace with your desired parameters)
#         result = await delete_topic(database_id="your_database_id", topic_name="your_topic_name") # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_quotas(api_key):
    """
    Test list_quotas function.
    """
    try:
        # Test case: List quotas (replace 'your_database_id' with a real database ID)
        result = await list_quotas(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_quota(api_key):
    """
    Test create_quota function.
    """
    try:
        # Test case: Create a quota (replace with your desired parameters)
        create_data = database.CreateDatabaseQuotaData(client_id=123, consumer_byte_rate=1048576, producer_byte_rate=1048576, request_percentage=50, user="testuser")
        result = await create_quota(database_id="your_database_id", data=create_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_maintenance_updates(api_key):
    """
    Test list_maintenance_updates function.
    """
    try:
        # Test case: List maintenance updates (replace 'your_database_id' with a real database ID)
        result = await list_maintenance_updates(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_start_maintenance_update(api_key):
    """
    Test start_maintenance_update function.
    """
    try:
        # Test case: Start maintenance update (replace 'your_database_id' with a real database ID)
        result = await start_maintenance_update(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_migration_status(api_key):
    """
    Test get_migration_status function.
    """
    try:
        # Test case: Get migration status (replace 'your_database_id' with a real database ID)
        result = await get_migration_status(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_start_migration(api_key):
    """
    Test start_migration function.
    """
    try:
        # Test case: Start migration (replace with your desired parameters)
        migration_data = database.StartDatabaseMigrationData(host="source_host", port=3306, username="source_user", password="source_password", ssl=True)
        result = await start_migration(database_id="your_database_id", data=migration_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_detach_migration(api_key):
#     """
#     Test detach_migration function.
#     """
#     try:
#         # Test case: Detach migration (replace 'your_database_id' with a real database ID)
#         result = await detach_migration(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_read_replica(api_key):
    """
    Test create_read_replica function.
    """
    try:
        # Test case: Create read replica (replace with your desired parameters)
        replica_data = database.CreateDatabaseReadReplicaData(region="ewr", label="test-replica")
        result = await create_read_replica(database_id="your_database_id", data=replica_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_promote_read_replica(api_key):
    """
    Test promote_read_replica function.
    """
    try:
        # Test case: Promote read replica (replace 'your_database_id' with a real database ID)
        result = await promote_read_replica(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_backup_information(api_key):
    """
    Test get_backup_information function.
    """
    try:
        # Test case: Get backup information (replace 'your_database_id' with a real database ID)
        result = await get_backup_information(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_restore_from_backup(api_key):
    """
    Test restore_from_backup function.
    """
    try:
        # Test case: Restore from backup (replace with your desired parameters)
        restore_data = database.RestoreDatabaseFromBackupData(label="restored-database", type="latest", date="2023-10-26", time="14:30:00")
        result = await restore_from_backup(database_id="your_database_id", data=restore_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_fork_from_backup(api_key):
    """
    Test fork_from_backup function.
    """
    try:
        # Test case: Fork from backup (replace with your desired parameters)
        fork_data = database.ForkDatabaseFromBackupData(label="forked-database", region="ewr", plan="vultr-dbaas-startup-8-1-50-mysql", vpc_id="your_vpc_id", type="latest", date="2023-10-26", time="14:30:00") # Replace 'your_vpc_id' with a real VPC ID
        result = await fork_from_backup(database_id="your_database_id", data=fork_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 202:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_connection_pools(api_key):
    """
    Test list_connection_pools function.
    """
    try:
        # Test case: List connection pools (replace 'your_database_id' with a real database ID)
        result = await list_connection_pools(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_create_connection_pool(api_key):
    """
    Test create_connection_pool function.
    """
    try:
        # Test case: Create a connection pool (replace with your desired parameters)
        pool_data = database.CreateDatabaseConnectionPoolData(name="test-pool", database="defaultdb", username="your_username", mode="session", size=5) # Replace 'your_username' with a real username
        result = await create_connection_pool(database_id="your_database_id", data=pool_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 201:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_get_connection_pool(api_key):
    """
    Test get_connection_pool function.
    """
    try:
        # Test case: Get connection pool information (replace with your desired parameters)
        result = await get_connection_pool(database_id="your_database_id", pool_name="your_pool_name") # Replace with your desired parameters

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_connection_pool(api_key):
    """
    Test update_connection_pool function.
    """
    try:
        # Test case: Update connection pool information (replace with your desired parameters)
        pool_data = database.UpdateDatabaseConnectionPoolData(database="defaultdb", username="your_username", mode="transaction", size=10) # Replace 'your_username' with a real username
        result = await update_connection_pool(database_id="your_database_id", pool_name="your_pool_name", data=pool_data) # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

# @pytest.mark.asyncio
# async def test_delete_connection_pool(api_key):
#     """
#     Test delete_connection_pool function.
#     """
#     try:
#         # Test case: Delete connection pool (replace with your desired parameters)
#         result = await delete_connection_pool(database_id="your_database_id", pool_name="your_pool_name") # Replace with your desired parameters

#         if result.get("status") != 204:
#             raise Exception(result)

#         logger.info("\nResponse Data:\n%s", result)

#     except Exception as e:
#         logger.error("Error: %s", e)
#         pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_advanced_options(api_key):
    """
    Test list_advanced_options function.
    """
    try:
        # Test case: List advanced options (replace 'your_database_id' with a real database ID)
        result = await list_advanced_options(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_update_advanced_option(api_key):
    """
    Test update_advanced_option function.
    """
    try:
        # Test case: Update advanced option (replace with your desired parameters)
        result = await update_advanced_option(database_id="your_database_id", option_name="max_connections", value="100") # Replace with your desired parameters

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_list_version_upgrades(api_key):
    """
    Test list_version_upgrades function.
    """
    try:
        # Test case: List version upgrades (replace 'your_database_id' with a real database ID)
        result = await list_version_upgrades(database_id="your_database_id") # Replace 'your_database_id' with a real database ID

        if result.get("status") != 200:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")

@pytest.mark.asyncio
async def test_start_version_upgrade(api_key):
    """
    Test start_version_upgrade function.
    """
    try:
        # Test case: Start version upgrade (replace with your desired parameters)
        upgrade_data = database.StartDatabaseMaintenanceData(version="16")
        result = await start_version_upgrade(database_id="your_database_id", data=upgrade_data) # Replace 'your_database_id' with a real database ID

        if result.get("status") != 204:
            raise Exception(result)

        logger.info("\nResponse Data:\n%s", result)

    except Exception as e:
        logger.error("Error: %s", e)
        pytest.fail(f"Test failed with error: {e}")