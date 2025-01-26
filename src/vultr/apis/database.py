from http import HTTPMethod
from typing import Optional, List, Literal

from proschedio import composer
from vultr import get_key
from vultr.apis import _const
from vultr.structs import database

async def list_database_plans(engine: Optional[Literal["mysql", "pg", "valkey", "kafka"]], nodes: Optional[int], region: Optional[str]):
    """
    List Managed Database Plans.

    Args:
        engine (Optional[Literal["mysql", "pg", "valkey", "kafka"]]): Filter by engine type.
        nodes (Optional[int]): Filter by number of nodes.
        region (Optional[str]): Filter by [Region id](#operation/list-regions).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_DATABASE_LIST_PLANS) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if engine is not None:
        request.add_param("engine", engine)
    if nodes is not None:
        request.add_param("nodes", nodes)
    if region is not None:
        request.add_param("region", region)

    return await request.request()

async def list_databases(label: Optional[str], tag: Optional[str], region: Optional[str]):
    """
    List all Managed Databases in your account.

    Args:
        label (Optional[str]): Filter by label.
        tag (Optional[str]): Filter by specific tag.
        region (Optional[str]): Filter by [Region id](#operation/list-regions).

    Returns:
        requests.Response: The response from the API.
    """
    request = composer.Request(_const.URL_DATABASE_LIST) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}")

    if label is not None:
        request.add_param("label", label)
    if tag is not None:
        request.add_param("tag", tag)
    if region is not None:
        request.add_param("region", region)

    return await request.request()

async def create_database(data: database.CreateDatabaseData):
    """
    Create a new Managed Database in a `region` with the desired `plan`. Supply optional attributes as desired.

    Args:
        data (CreateDatabaseData): The data to create the Managed Database.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_LIST) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_database(database_id: str):
    """
    Get information about a Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_ID.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_database(database_id: str, data: database.UpdateDatabaseData):
    """
    Update information for a Managed Database. All attributes are optional. If not set, the attributes will retain their original values.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (UpdateDatabaseData): The data to update the Managed Database.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_ID.assign("database-id", database_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_database(database_id: str):
    """
    Delete a Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_ID.assign("database-id", database_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_database_usage(database_id: str):
    """
    Get disk, memory, and vCPU usage information for a Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_USAGE.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_database_users(database_id: str):
    """
    List all database users within the Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_USERS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def create_database_user(database_id: str, data: database.CreateDatabaseUserData):
    """
    Create a new database user within the Managed Database. Supply optional attributes as desired.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (CreateDatabaseUserData): The data to create the database user.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_USERS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_database_user(database_id: str, username: str):
    """
    Get information about a Managed Database user.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        username (str): The [database user](#operation/list-database-users).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_USER.assign("database-id", database_id).assign("username", username)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_database_user(database_id: str, username: str, data: database.UpdateDatabaseUserData):
    """
    Update database user information within a Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        username (str): The [database user](#operation/list-database-users).
        data (UpdateDatabaseUserData): The data to update the database user.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_USER.assign("database-id", database_id).assign("username", username)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_database_user(database_id: str, username: str):
    """
    Delete a database user within a Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        username (str): The [database user](#operation/list-database-users).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_USER.assign("database-id", database_id).assign("username", username)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_database_user_access_control(database_id: str, username: str, data: database.UpdateDatabaseUserAccessControlData):
    """
    Configure access control settings for a Managed Database user (Valkey and Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        username (str): The [database user](#operation/list-database-users).
        data (UpdateDatabaseUserAccessControlData): The data to update the database user access control.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_USER_ACCESS_CONTROL.assign("database-id", database_id).assign("username", username)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def list_logical_databases(database_id: str):
    """
    List all logical databases within the Managed Database (MySQL and PostgreSQL only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_LOGICAL_DATABASES.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def create_logical_database(database_id: str, data: database.CreateDatabaseLogicalDatabaseData):
    """
    Create a new logical database within the Managed Database (MySQL and PostgreSQL only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (CreateDatabaseLogicalDatabaseData): The data to create the logical database.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_LOGICAL_DATABASES.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_logical_database(database_id: str, db_name: str):
    """
    Get information about a logical database within a Managed Database (MySQL and PostgreSQL only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        db_name (str): The [logical database name](#operation/list-database-dbs).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_LOGICAL_DATABASE.assign("database-id", database_id).assign("db-name", db_name)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def delete_logical_database(database_id: str, db_name: str):
    """
    Delete a logical database within a Managed Database (MySQL and PostgreSQL only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        db_name (str): The [logical database name](#operation/list-database-dbs).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_LOGICAL_DATABASE.assign("database-id", database_id).assign("db-name", db_name)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_topics(database_id: str):
    """
    List all topics within the Managed Database (Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_TOPICS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def create_topic(database_id: str, data: database.CreateDatabaseTopicData):
    """
    Create a new topic within the Managed Database (Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (CreateDatabaseTopicData): The data to create the topic.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_TOPICS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_topic(database_id: str, topic_name: str):
    """
    Get information about a Managed Database topic (Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        topic_name (str): The [database topic](#operation/list-database-topics).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_TOPIC.assign("database-id", database_id).assign("topic-name", topic_name)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_topic(database_id: str, topic_name: str, data: database.UpdateDatabaseTopicData):
    """
    Update topic information within a Managed Database (Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        topic_name (str): The [database topic](#operation/list-database-topics).
        data (UpdateDatabaseTopicData): The data to update the topic.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_TOPIC.assign("database-id", database_id).assign("topic-name", topic_name)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_topic(database_id: str, topic_name: str):
    """
    Delete a topic within a Managed Database (Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        topic_name (str): The [database topic](#operation/list-database-topics).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_TOPIC.assign("database-id", database_id).assign("topic-name", topic_name)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_quotas(database_id: str):
    """
    List all quotas within the Managed Database (Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_QUOTAS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def create_quota(database_id: str, data: database.CreateDatabaseQuotaData):
    """
    Create a new quota within the Managed Database (Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (CreateDatabaseQuotaData): The data to create the quota.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_QUOTAS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def list_maintenance_updates(database_id: str):
    """
    List all available version upgrades within the Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_MAINTENANCE.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def start_maintenance_update(database_id: str):
    """
    Start maintenance updates for the Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_MAINTENANCE.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_migration_status(database_id: str):
    """
    View the status of a migration attached to the Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_MIGRATION.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def start_migration(database_id: str, data: database.StartDatabaseMigrationData):
    """
    Start a migration to the Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (StartDatabaseMigrationData): The data to start the migration.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_MIGRATION.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def detach_migration(database_id: str):
    """
    Detach a migration from the Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_MIGRATION.assign("database-id", database_id)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def create_read_replica(database_id: str, data: database.CreateDatabaseReadReplicaData):
    """
    Create a read-only replica node for the Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (CreateDatabaseReadReplicaData): The data to create the read replica.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_READ_REPLICA.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def promote_read_replica(database_id: str):
    """
    Promote a read-only replica node to its own primary Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_PROMOTE_READ_REPLICA.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def get_backup_information(database_id: str):
    """
    Get backup information for the Managed Database.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_BACKUPS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def restore_from_backup(database_id: str, data: database.RestoreDatabaseFromBackupData):
    """
    Create a new Managed Database from a backup.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (RestoreDatabaseFromBackupData): The data to restore from backup.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_RESTORE.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def fork_from_backup(database_id: str, data: database.ForkDatabaseFromBackupData):
    """
    Fork a Managed Database to a new subscription from a backup.

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (ForkDatabaseFromBackupData): The data to fork from backup.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_FORK.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def list_connection_pools(database_id: str):
    """
    List all connection pools within the Managed Database (PostgreSQL engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_CONNECTION_POOLS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def create_connection_pool(database_id: str, data: database.CreateDatabaseConnectionPoolData):
    """
    Create a new connection pool within the Managed Database (PostgreSQL engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (CreateDatabaseConnectionPoolData): The data to create the connection pool.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_CONNECTION_POOLS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def get_connection_pool(database_id: str, pool_name: str):
    """
    Get information about a Managed Database connection pool (PostgreSQL engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        pool_name (str): The [connection pool name](#operation/list-connection-pools).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_CONNECTION_POOL.assign("database-id", database_id).assign("pool-name", pool_name)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_connection_pool(database_id: str, pool_name: str, data: database.UpdateDatabaseConnectionPoolData):
    """
    Update connection-pool information within a Managed Database (PostgreSQL engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        pool_name (str): The [connection pool name](#operation/list-connection-pools).
        data (UpdateDatabaseConnectionPoolData): The data to update the connection pool.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_CONNECTION_POOL.assign("database-id", database_id).assign("pool-name", pool_name)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()

async def delete_connection_pool(database_id: str, pool_name: str):
    """
    Delete a connection pool within a Managed Database (PostgreSQL engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        pool_name (str): The [connection pool name](#operation/list-connection-pools).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_CONNECTION_POOL.assign("database-id", database_id).assign("pool-name", pool_name)) \
        .set_method(HTTPMethod.DELETE) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def list_advanced_options(database_id: str):
    """
    List all configured and available advanced options for the Managed Database (MySQL, PostgreSQL, and Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_ADVANCED_OPTIONS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def update_advanced_option(database_id: str, option_name: str, value: str):
    """
    Updates an advanced configuration option for the Managed Database (MySQL, PostgreSQL, and Kafka engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        option_name (str): The name of the advanced option to update.
        value (str): The new value for the advanced option.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_ADVANCED_OPTIONS.assign("database-id", database_id)) \
        .set_method(HTTPMethod.PUT) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body({
            option_name: value
        }) \
        .request()

async def list_version_upgrades(database_id: str):
    """
    List all available version upgrades within the Managed Database (PostgreSQL engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_VERSION_UPGRADE.assign("database-id", database_id)) \
        .set_method(HTTPMethod.GET) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .request()

async def start_version_upgrade(database_id: str, data: database.StartDatabaseMaintenanceData):
    """
    Start a version upgrade for the Managed Database (PostgreSQL engine types only).

    Args:
        database_id (str): The [Managed Database ID](#operation/list-databases).
        data (StartDatabaseMaintenanceData): The data to start the version upgrade.

    Returns:
        requests.Response: The response from the API.
    """
    return await composer.Request(_const.URL_DATABASE_VERSION_UPGRADE.assign("database-id", database_id)) \
        .set_method(HTTPMethod.POST) \
        .add_header("Authorization", f"Bearer {get_key()}") \
        .add_header("Content-Type", "application/json") \
        .set_body(data.to_json()) \
        .request()