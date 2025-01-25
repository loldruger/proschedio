from typing import Optional, List, Literal


class CreateDatabaseData:
    def __init__(self, database_engine: Literal["mysql", "pg", "valkey", "kafka"], database_engine_version: str, region: str, plan: str, label: str):
        """
        Data structure used for creating a Vultr Managed Database.

        Args:
            database_engine (Literal["mysql", "pg", "valkey", "kafka"]): The database engine type for the Managed Database.
            database_engine_version (str): The version of the chosen database engine type for the Managed Database.
            region (str): The [Region id](#operation/list-regions) where the Managed Database is located.
            plan (str): The [Plan id](#operation/list-database-plans) to use when deploying this Managed Database.
            label (str): A user-supplied label for this Managed Database.
        """
        self._database_engine: Literal["mysql", "pg", "valkey", "kafka"] = database_engine
        self._database_engine_version: str = database_engine_version
        self._region: str = region
        self._plan: str = plan
        self._label: str = label
        self._tag: Optional[str] = None
        self._vpc_id: Optional[str] = None
        self._maintenance_dow: Optional[Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]] = None
        self._maintenance_time: Optional[str] = None
        self._trusted_ips: Optional[List[str]] = None
        self._mysql_sql_modes: Optional[List[str]] = None
        self._mysql_require_primary_key: Optional[bool] = None
        self._mysql_slow_query_log: Optional[bool] = None
        self._mysql_long_query_time: Optional[int] = None
        self._eviction_policy: Optional[str] = None
        
    def tag(self, tag: str) -> "CreateDatabaseData":
        """
        Set the user-supplied tag for this Managed Database.

        Args:
            tag (str): The user-supplied tag.

        Returns:
            CreateDatabaseData: The current object with the tag set.
        """
        self._tag = tag
        return self
    
    def vpc_id(self, vpc_id: str) -> "CreateDatabaseData":
        """
        Set the [VPC id](#operation/list-vpcs) to use when deploying this Managed Database.

        Args:
            vpc_id (str): The VPC ID.

        Returns:
            CreateDatabaseData: The current object with the VPC ID set.
        """
        self._vpc_id = vpc_id
        return self

    def maintenance_dow(self, maintenance_dow: Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]) -> "CreateDatabaseData":
        """
        Set the day of week for routine maintenance updates.

        Args:
            maintenance_dow (Literal["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]): The day of the week.

        Returns:
            CreateDatabaseData: The current object with the maintenance day of week set.
        """
        self._maintenance_dow = maintenance_dow
        return self

    def maintenance_time(self, maintenance_time: str) -> "CreateDatabaseData":
        """
        Set the preferred time (UTC) for routine maintenance updates in 24-hour HH:00 format.

        Args:
            maintenance_time (str): The preferred time in HH:00 format.

        Returns:
            CreateDatabaseData: The current object with the maintenance time set.
        """
        self._maintenance_time = maintenance_time
        return self
    
    def trusted_ips(self, trusted_ips: List[str]) -> "CreateDatabaseData":
        """
        Set a list of IP addresses allowed to access the Managed Database in CIDR notation.

        Args:
            trusted_ips (List[str]): The list of trusted IP addresses.

        Returns:
            CreateDatabaseData: The current object with the trusted IPs set.
        """
        self._trusted_ips = trusted_ips
        return self
    
    def mysql_sql_modes(self, mysql_sql_modes: List[str]) -> "CreateDatabaseData":
        """
        Set a list of SQL modes to enable (MySQL engine types only).

        Args:
            mysql_sql_modes (List[str]): The list of SQL modes.

        Returns:
            CreateDatabaseData: The current object with the MySQL SQL modes set.
        """
        self._mysql_sql_modes = mysql_sql_modes
        return self

    def mysql_require_primary_key(self, mysql_require_primary_key: bool) -> "CreateDatabaseData":
        """
        Set whether to require a primary key for all tables (MySQL engine types only).

        Args:
            mysql_require_primary_key (bool): Whether to require a primary key.

        Returns:
            CreateDatabaseData: The current object with the MySQL require primary key setting set.
        """
        self._mysql_require_primary_key = mysql_require_primary_key
        return self

    def mysql_slow_query_log(self, mysql_slow_query_log: bool) -> "CreateDatabaseData":
        """
        Set whether to enable slow query logging (MySQL engine types only).

        Args:
            mysql_slow_query_log (bool): Whether to enable slow query logging.

        Returns:
            CreateDatabaseData: The current object with the MySQL slow query logging setting set.
        """
        self._mysql_slow_query_log = mysql_slow_query_log
        return self

    def mysql_long_query_time(self, mysql_long_query_time: int) -> "CreateDatabaseData":
        """
        Set the number of seconds to denote a slow query (MySQL engine types only).

        Args:
            mysql_long_query_time (int): The number of seconds.

        Returns:
            CreateDatabaseData: The current object with the MySQL long query time set.
        """
        self._mysql_long_query_time = mysql_long_query_time
        return self
    
    def eviction_policy(self, eviction_policy: str) -> "CreateDatabaseData":
        """
        Set the data eviction policy (Valkey engine types only).

        Args:
            eviction_policy (str): The eviction policy.

        Returns:
            CreateDatabaseData: The current object with the eviction policy set.
        """
        self._eviction_policy = eviction_policy
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "database_engine": self._database_engine,
            "database_engine_version": self._database_engine_version,
            "region": self._region,
            "plan": self._plan,
            "label": self._label,
            "tag": self._tag,
            "vpc_id": self._vpc_id,
            "maintenance_dow": self._maintenance_dow,
            "maintenance_time": self._maintenance_time,
            "trusted_ips": self._trusted_ips,
            "mysql_sql_modes": self._mysql_sql_modes,
            "mysql_require_primary_key": self._mysql_require_primary_key,
            "mysql_slow_query_log": self._mysql_slow_query_log,
            "mysql_long_query_time": self._mysql_long_query_time,
            "eviction_policy": self._eviction_policy,
        }
        return {k: v for k, v in data.items() if v is not None}

class UpdateDatabaseData:
    def __init__(self):
        """
        Data structure used for updating a Vultr Managed Database.
        """
        self._region: Optional[str] = None
        self._plan: Optional[str] = None
        self._label: Optional[str] = None
        self._tag: Optional[str] = None
        self._vpc_id: Optional[str] = None
        self._maintenance_dow: Optional[str] = None
        self._maintenance_time: Optional[str] = None
        self._cluster_time_zone: Optional[str] = None
        self._trusted_ips: Optional[List[str]] = None
        self._mysql_sql_modes: Optional[List[str]] = None
        self._mysql_require_primary_key: Optional[bool] = None
        self._mysql_slow_query_log: Optional[bool] = None
        self._mysql_long_query_time: Optional[int] = None
        self._eviction_policy: Optional[str] = None

    def region(self, region: str) -> "UpdateDatabaseData":
        """
        Set the [Region id](#operation/list-regions) where the Managed Database is located.

        Args:
            region (str): The Region ID.

        Returns:
            UpdateDatabaseData: The current object with the region set.
        """
        self._region = region
        return self

    def plan(self, plan: str) -> "UpdateDatabaseData":
        """
        Set the [Plan id](#operation/list-database-plans) for this Managed Database.

        Args:
            plan (str): The Plan ID.

        Returns:
            UpdateDatabaseData: The current object with the plan set.
        """
        self._plan = plan
        return self

    def label(self, label: str) -> "UpdateDatabaseData":
        """
        Set a user-supplied label for this Managed Database.

        Args:
            label (str): The user-supplied label.

        Returns:
            UpdateDatabaseData: The current object with the label set.
        """
        self._label = label
        return self

    def tag(self, tag: str) -> "UpdateDatabaseData":
        """
        Set the user-supplied tag for this Managed Database.

        Args:
            tag (str): The user-supplied tag.

        Returns:
            UpdateDatabaseData: The current object with the tag set.
        """
        self._tag = tag
        return self

    def vpc_id(self, vpc_id: str) -> "UpdateDatabaseData":
        """
        Set the [VPC id](#operation/list-vpcs) for this Managed Database.

        Args:
            vpc_id (str): The VPC ID.

        Returns:
            UpdateDatabaseData: The current object with the VPC ID set.
        """
        self._vpc_id = vpc_id
        return self

    def maintenance_dow(self, maintenance_dow: str) -> "UpdateDatabaseData":
        """
        Set the day of week for routine maintenance updates.

        Args:
            maintenance_dow (str): The day of the week.

        Returns:
            UpdateDatabaseData: The current object with the maintenance day of week set.
        """
        self._maintenance_dow = maintenance_dow
        return self

    def maintenance_time(self, maintenance_time: str) -> "UpdateDatabaseData":
        """
        Set the preferred time (UTC) for routine maintenance updates.

        Args:
            maintenance_time (str): The preferred time in HH:00 format.

        Returns:
            UpdateDatabaseData: The current object with the maintenance time set.
        """
        self._maintenance_time = maintenance_time
        return self

    def cluster_time_zone(self, cluster_time_zone: str) -> "UpdateDatabaseData":
        """
        Set the configured time zone in TZ database format.

        Args:
            cluster_time_zone (str): The time zone.

        Returns:
            UpdateDatabaseData: The current object with the cluster time zone set.
        """
        self._cluster_time_zone = cluster_time_zone
        return self

    def trusted_ips(self, trusted_ips: List[str]) -> "UpdateDatabaseData":
        """
        Set a list of IP addresses allowed to access the Managed Database.

        Args:
            trusted_ips (List[str]): The list of trusted IP addresses.

        Returns:
            UpdateDatabaseData: The current object with the trusted IPs set.
        """
        self._trusted_ips = trusted_ips
        return self

    def mysql_sql_modes(self, mysql_sql_modes: List[str]) -> "UpdateDatabaseData":
        """
        Set a list of SQL modes to enable (MySQL engine types only).

        Args:
            mysql_sql_modes (List[str]): The list of SQL modes.

        Returns:
            UpdateDatabaseData: The current object with the MySQL SQL modes set.
        """
        self._mysql_sql_modes = mysql_sql_modes
        return self

    def mysql_require_primary_key(self, mysql_require_primary_key: bool) -> "UpdateDatabaseData":
        """
        Set whether to require a primary key for all tables (MySQL engine types only).

        Args:
            mysql_require_primary_key (bool): Whether to require a primary key.

        Returns:
            UpdateDatabaseData: The current object with the MySQL require primary key setting set.
        """
        self._mysql_require_primary_key = mysql_require_primary_key
        return self

    def mysql_slow_query_log(self, mysql_slow_query_log: bool) -> "UpdateDatabaseData":
        """
        Set whether to enable slow query logging (MySQL engine types only).

        Args:
            mysql_slow_query_log (bool): Whether to enable slow query logging.

        Returns:
            UpdateDatabaseData: The current object with the MySQL slow query logging setting set.
        """
        self._mysql_slow_query_log = mysql_slow_query_log
        return self

    def mysql_long_query_time(self, mysql_long_query_time: int) -> "UpdateDatabaseData":
        """
        Set the number of seconds to denote a slow query (MySQL engine types only).

        Args:
            mysql_long_query_time (int): The number of seconds.

        Returns:
            UpdateDatabaseData: The current object with the MySQL long query time set.
        """
        self._mysql_long_query_time = mysql_long_query_time
        return self

    def eviction_policy(self, eviction_policy: str) -> "UpdateDatabaseData":
        """
        Set the data eviction policy (Valkey engine types only).

        Args:
            eviction_policy (str): The eviction policy.

        Returns:
            UpdateDatabaseData: The current object with the eviction policy set.
        """
        self._eviction_policy = eviction_policy
        return self
    
    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "region": self._region,
            "plan": self._plan,
            "label": self._label,
            "tag": self._tag,
            "vpc_id": self._vpc_id,
            "maintenance_dow": self._maintenance_dow,
            "maintenance_time": self._maintenance_time,
            "cluster_time_zone": self._cluster_time_zone,
            "trusted_ips": self._trusted_ips,
            "mysql_sql_modes": self._mysql_sql_modes,
            "mysql_require_primary_key": self._mysql_require_primary_key,
            "mysql_slow_query_log": self._mysql_slow_query_log,
            "mysql_long_query_time": self._mysql_long_query_time,
            "eviction_policy": self._eviction_policy,
        }
        return {k: v for k, v in data.items() if v is not None}

class CreateDatabaseUserData:
    def __init__(self, username: str):
        """
        Data structure used for creating a database user within a Vultr Managed Database.

        Args:
            username (str): The username of the database user.
        """
        self._username: str = username
        self._password: Optional[str] = None
        self._encryption: Optional[Literal["caching_sha2_password", "mysql_native_password"]] = None
        self._permission: Optional[Literal["admin", "read", "write", "readwrite"]] = None

    def password(self, password: str) -> "CreateDatabaseUserData":
        """
        Set the password for the database user (omit to auto-generate).

        Args:
            password (str): The password for the database user.

        Returns:
            CreateDatabaseUserData: The current object with the password set.
        """
        self._password = password
        return self

    def encryption(self, encryption: Literal["caching_sha2_password", "mysql_native_password"]) -> "CreateDatabaseUserData":
        """
        Set the password encryption type (MySQL engine types only).

        Args:
            encryption (Literal["caching_sha2_password", "mysql_native_password"]): The encryption type.

        Returns:
            CreateDatabaseUserData: The current object with the encryption type set.
        """
        self._encryption = encryption
        return self

    def permission(self, permission: Literal["admin", "read", "write", "readwrite"]) -> "CreateDatabaseUserData":
        """
        Set the permission level (Kafka engine types only).

        Args:
            permission (Literal["admin", "read", "write", "readwrite"]): The permission level.

        Returns:
            CreateDatabaseUserData: The current object with the permission level set.
        """
        self._permission = permission
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "username": self._username,
            "password": self._password,
            "encryption": self._encryption,
            "permission": self._permission,
        }
        return {k: v for k, v in data.items() if v is not None}

class UpdateDatabaseUserData:
    def __init__(self, password: Optional[str] = None):
        """
        Data structure used for updating a database user within a Vultr Managed Database.

        Args:
            password (Optional[str]): The password for the database user (can be empty to auto-generate).
        """
        self._password: Optional[str] = password
    
    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "password": self._password
        }
        return {k: v for k, v in data.items() if v is not None}

class UpdateDatabaseUserAccessControlData:
    def __init__(self):
        """
        Data structure used for configuring access control settings for a Managed Database user (Valkey and Kafka engine types only).
        """
        self._acl_categories: Optional[List[str]] = None
        self._acl_channels: Optional[List[str]] = None
        self._acl_commands: Optional[List[str]] = None
        self._acl_keys: Optional[List[str]] = None
        self._permission: Optional[Literal["admin", "read", "write", "readwrite"]] = None

    def acl_categories(self, acl_categories: List[str]) -> "UpdateDatabaseUserAccessControlData":
        """
        Set the ACL categories array (Valkey).

        Args:
            acl_categories (List[str]): The ACL categories.

        Returns:
            UpdateDatabaseUserAccessControlData: The current object with the ACL categories set.
        """
        self._acl_categories = acl_categories
        return self

    def acl_channels(self, acl_channels: List[str]) -> "UpdateDatabaseUserAccessControlData":
        """
        Set the ACL channels array (Valkey).

        Args:
            acl_channels (List[str]): The ACL channels.

        Returns:
            UpdateDatabaseUserAccessControlData: The current object with the ACL channels set.
        """
        self._acl_channels = acl_channels
        return self

    def acl_commands(self, acl_commands: List[str]) -> "UpdateDatabaseUserAccessControlData":
        """
        Set the ACL commands array (Valkey).

        Args:
            acl_commands (List[str]): The ACL commands.

        Returns:
            UpdateDatabaseUserAccessControlData: The current object with the ACL commands set.
        """
        self._acl_commands = acl_commands
        return self
    
    def acl_keys(self, acl_keys: List[str]) -> "UpdateDatabaseUserAccessControlData":
        """
        Set the ACL keys array (Valkey).

        Args:
            acl_keys (List[str]): The ACL keys.

        Returns:
            UpdateDatabaseUserAccessControlData: The current object with the ACL keys set.
        """
        self._acl_keys = acl_keys
        return self
    
    def permission(self, permission: Literal["admin", "read", "write", "readwrite"]) -> "UpdateDatabaseUserAccessControlData":
        """
        Set the Kafka permissions.

        Args:
            permission (Literal["admin", "read", "write", "readwrite"]): The permission level.

        Returns:
            UpdateDatabaseUserAccessControlData: The current object with the permission level set.
        """
        self._permission = permission
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "acl_categories": self._acl_categories,
            "acl_channels": self._acl_channels,
            "acl_commands": self._acl_commands,
            "acl_keys": self._acl_keys,
            "permission": self._permission
        }
        return {k: v for k, v in data.items() if v is not None}

class CreateDatabaseLogicalDatabaseData:
    def __init__(self, name: str):
        """
        Data structure used for creating a new logical database within a Vultr Managed Database (MySQL and PostgreSQL only).

        Args:
            name (str): The name of the logical database.
        """
        self._name: str = name

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "name": self._name
        }

class CreateDatabaseTopicData:
    def __init__(self, name: str, partitions: int, replication: int, retention_hours: int, retention_bytes: int):
        """
        Data structure used for creating a new topic within a Vultr Managed Database (Kafka engine types only).

        Args:
            name (str): The name for the database topic.
            partitions (int): The number of partitions.
            replication (int): The replication factor.
            retention_hours (int): The retention hours.
            retention_bytes (int): The retention bytes.
        """
        self._name: str = name
        self._partitions: int = partitions
        self._replication: int = replication
        self._retention_hours: int = retention_hours
        self._retention_bytes: int = retention_bytes

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "name": self._name,
            "partitions": self._partitions,
            "replication": self._replication,
            "retention_hours": self._retention_hours,
            "retention_bytes": self._retention_bytes,
        }

class UpdateDatabaseTopicData:
    def __init__(self, partitions: int, replication: int, retention_hours: int, retention_bytes: int):
        """
        Data structure used for updating a topic within a Vultr Managed Database (Kafka engine types only).

        Args:
            partitions (int): The number of partitions for the database topic.
            replication (int): The replication factor for the database topic.
            retention_hours (int): The retention hours for the database topic.
            retention_bytes (int): The retention bytes for the database topic.
        """
        self._partitions: int = partitions
        self._replication: int = replication
        self._retention_hours: int = retention_hours
        self._retention_bytes: int = retention_bytes

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "partitions": self._partitions,
            "replication": self._replication,
            "retention_hours": self._retention_hours,
            "retention_bytes": self._retention_bytes,
        }

class CreateDatabaseQuotaData:
    def __init__(self, client_id: int, consumer_byte_rate: int, producer_byte_rate: int, request_percentage: int, user: str):
        """
        Data structure used for creating a new quota within a Vultr Managed Database (Kafka engine types only).

        Args:
            client_id (int): The client ID for the database quota. Note: Creating a new quota with the same client ID and user will overwrite the previous record.
            consumer_byte_rate (int): The consumer byte rate for the database quota.
            producer_byte_rate (int): The producer byte rate for the database quota.
            request_percentage (int): The CPU request percentage for the database quota.
            user (str): The [user](#operation/list-database-users) for the database quota.
        """
        self._client_id: int = client_id
        self._consumer_byte_rate: int = consumer_byte_rate
        self._producer_byte_rate: int = producer_byte_rate
        self._request_percentage: int = request_percentage
        self._user: str = user

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "client_id": self._client_id,
            "consumer_byte_rate": self._consumer_byte_rate,
            "producer_byte_rate": self._producer_byte_rate,
            "request_percentage": self._request_percentage,
            "user": self._user,
        }

class StartDatabaseMaintenanceData:
    def __init__(self, version: str):
        """
        Data structure used for starting a version upgrade for a Vultr Managed Database (PostgreSQL engine types only).

        Args:
            version (str): The version number to upgrade the Managed Database to.
        """
        self._version: str = version
    
    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "version": self._version
        }

class StartDatabaseMigrationData:
    def __init__(self, host: str, port: int, username: str, password: str, ssl: bool):
        """
        Data structure used for starting a migration to a Vultr Managed Database.

        Args:
            host (str): The host name of the source server.
            port (int): The connection port of the source server.
            username (str): The username of the source server. Uses `default` for Valkey if left empty or unset.
            password (str): The password of the source server.
            ssl (bool): The true/false value for whether SSL is needed to connect to the source server.
        """
        self._host: str = host
        self._port: int = port
        self._username: str = username
        self._password: str = password
        self._database: Optional[str] = None
        self._ignored_databases: Optional[str] = None
        self._ssl: bool = ssl

    def database(self, database: str) -> "StartDatabaseMigrationData":
        """
        Set the database of the source server. Required for MySQL/PostgreSQL engine types, but excluded for Valkey.

        Args:
            database (str): The database of the source server.

        Returns:
            StartDatabaseMigrationData: The current object with the database set.
        """
        self._database = database
        return self

    def ignored_databases(self, ignored_databases: str) -> "StartDatabaseMigrationData":
        """
        Set a comma-separated list of ignored databases on the source server. Excluded for Valkey engine types.

        Args:
            ignored_databases (str): Comma-separated list of ignored databases.

        Returns:
            StartDatabaseMigrationData: The current object with the ignored databases set.
        """
        self._ignored_databases = ignored_databases
        return self

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        data = {
            "host": self._host,
            "port": self._port,
            "username": self._username,
            "password": self._password,
            "database": self._database,
            "ignored_databases": self._ignored_databases,
            "ssl": self._ssl,
        }
        return {k: v for k, v in data.items() if v is not None}

class CreateDatabaseReadReplicaData:
    def __init__(self, region: str, label: str):
        """
        Data structure used for creating a read-only replica node for a Vultr Managed Database.

        Args:
            region (str): The [Region id](#operation/list-regions) where the Managed Database is located.
            label (str): A user-supplied label for this Managed Database.
        """
        self._region: str = region
        self._label: str = label

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "region": self._region,
            "label": self._label,
        }

class RestoreDatabaseFromBackupData:
    def __init__(self, label: str, type: str, date: str, time: str):
        """
        Data structure used for creating a new Vultr Managed Database from a backup.

        Args:
            label (str): A user-supplied label for this Managed Database.
            type (str): The type of backup restoration to use for this Managed Database.
            date (str): The [backup date](#operation/get-backup-information) to use when restoring the Managed Database in YYYY-MM-DD date format.
            time (str): The [backup time](#operation/get-backup-information) to use when restoring the Managed Database in HH-MM-SS time format (24-hour UTC).
        """
        self._label: str = label
        self._type: str = type
        self._date: str = date
        self._time: str = time

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "label": self._label,
            "type": self._type,
            "date": self._date,
            "time": self._time,
        }

class ForkDatabaseFromBackupData:
    def __init__(self, label: str, region: str, plan: str, vpc_id: str, type: str, date: str, time: str):
        """
        Data structure used for forking a Vultr Managed Database to a new subscription from a backup.

        Args:
            label (str): A user-supplied label for this Managed Database.
            region (str): The [Region id](#operation/list-regions) where the Managed Database is located.
            plan (str): The [Plan id](#operation/list-database-plans) to use when deploying this Managed Database.
            vpc_id (str): The [VPC id](#operation/list-vpcs) to use when deploying this Managed Database.
            type (str): The type of backup restoration to use for this Managed Database.
            date (str): The [backup date](#operation/get-backup-information) to use when restoring the Managed Database in YYYY-MM-DD date format.
            time (str): The [backup time](#operation/get-backup-information) to use when restoring the Managed Database in HH-MM-SS time format (24-hour UTC).
        """
        self._label: str = label
        self._region: str = region
        self._plan: str = plan
        self._vpc_id: str = vpc_id
        self._type: str = type
        self._date: str = date
        self._time: str = time

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "label": self._label,
            "region": self._region,
            "plan": self._plan,
            "vpc_id": self._vpc_id,
            "type": self._type,
            "date": self._date,
            "time": self._time,
        }

class CreateDatabaseConnectionPoolData:
    def __init__(self, name: str, database: str, username: str, mode: str, size: int):
        """
Data structure used for creating a new connection pool within a Vultr Managed Database (PostgreSQL engine types only).

        Args:
            name (str): The name of the connection pool.
            database (str): The logical database associated with the connection pool.
            username (str): The database user associated with the connection pool.
            mode (str): The mode for the connection pool.
            size (int): The size of the connection pool.
        """
        self._name: str = name
        self._database: str = database
        self._username: str = username
        self._mode: str = mode
        self._size: int = size

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "name": self._name,
            "database": self._database,
            "username": self._username,
            "mode": self._mode,
            "size": self._size,
        }

class UpdateDatabaseConnectionPoolData:
    def __init__(self, database: str, username: str, mode: str, size: int):
        """
        Data structure used for updating a connection pool within a Vultr Managed Database (PostgreSQL engine types only).

        Args:
            database (str): The logical database associated with the connection pool.
            username (str): The database user associated with the connection pool.
            mode (str): The mode for the connection pool.
            size (int): The size of the connection pool.
        """
        self._database: str = database
        self._username: str = username
        self._mode: str = mode
        self._size: int = size

    def to_json(self):
        """
        Convert the data structure to a JSON format that can be used for Vultr API requests.

        Returns:
            dict: The data in JSON format.
        """
        return {
            "database": self._database,
            "username": self._username,
            "mode": self._mode,
            "size": self._size,
        }