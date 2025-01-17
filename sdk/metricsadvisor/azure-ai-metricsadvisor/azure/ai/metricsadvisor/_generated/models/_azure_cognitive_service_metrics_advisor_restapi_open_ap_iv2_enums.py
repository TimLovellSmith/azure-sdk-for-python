# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AnomalyAlertingConfigurationLogicType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """cross metrics operator
    
    should be specified when setting up multiple metric alerting configurations
    """

    AND_ENUM = "AND"
    OR_ENUM = "OR"
    XOR = "XOR"

class AnomalyDetectionConfigurationLogicType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """condition operator
    
    should be specified when combining multiple detection conditions
    """

    AND_ENUM = "AND"
    OR_ENUM = "OR"

class AnomalyDetectorDirection(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """detection direction
    """

    BOTH = "Both"
    DOWN = "Down"
    UP = "Up"

class AnomalyScope(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Anomaly scope
    """

    ALL = "All"
    DIMENSION = "Dimension"
    TOP_N = "TopN"

class AnomalyStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """anomaly status
    
    only return for alerting anomaly result
    """

    ACTIVE = "Active"
    RESOLVED = "Resolved"

class AnomalyValue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AUTO_DETECT = "AutoDetect"
    ANOMALY = "Anomaly"
    NOT_ANOMALY = "NotAnomaly"

class AuthenticationTypeEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """authentication type for corresponding data source
    """

    BASIC = "Basic"
    MANAGED_IDENTITY = "ManagedIdentity"
    AZURE_SQL_CONNECTION_STRING = "AzureSQLConnectionString"
    DATA_LAKE_GEN2_SHARED_KEY = "DataLakeGen2SharedKey"
    SERVICE_PRINCIPAL = "ServicePrincipal"
    SERVICE_PRINCIPAL_IN_KV = "ServicePrincipalInKV"

class ChangePointValue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AUTO_DETECT = "AutoDetect"
    CHANGE_POINT = "ChangePoint"
    NOT_CHANGE_POINT = "NotChangePoint"

class DataSourceCredentialType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of data source credential
    """

    AZURE_SQL_CONNECTION_STRING = "AzureSQLConnectionString"
    DATA_LAKE_GEN2_SHARED_KEY = "DataLakeGen2SharedKey"
    SERVICE_PRINCIPAL = "ServicePrincipal"
    SERVICE_PRINCIPAL_IN_KV = "ServicePrincipalInKV"

class DataSourceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of data source credential
    """

    AZURE_APPLICATION_INSIGHTS = "AzureApplicationInsights"
    AZURE_BLOB = "AzureBlob"
    AZURE_COSMOS_DB = "AzureCosmosDB"
    AZURE_DATA_EXPLORER = "AzureDataExplorer"
    AZURE_DATA_LAKE_STORAGE_GEN2 = "AzureDataLakeStorageGen2"
    AZURE_EVENT_HUBS = "AzureEventHubs"
    AZURE_TABLE = "AzureTable"
    ELASTICSEARCH = "Elasticsearch"
    HTTP_REQUEST = "HttpRequest"
    INFLUX_DB = "InfluxDB"
    MONGO_DB = "MongoDB"
    MY_SQL = "MySql"
    POSTGRE_SQL = "PostgreSql"
    SQL_SERVER = "SqlServer"

class Direction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """value filter direction
    """

    BOTH = "Both"
    DOWN = "Down"
    UP = "Up"

class EntityStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """data feed status
    """

    ACTIVE = "Active"
    PAUSED = "Paused"

class FeedbackQueryTimeMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """time mode to filter feedback
    """

    METRIC_TIMESTAMP = "MetricTimestamp"
    FEEDBACK_CREATED_TIME = "FeedbackCreatedTime"

class FeedbackType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """feedback type
    """

    ANOMALY = "Anomaly"
    CHANGE_POINT = "ChangePoint"
    PERIOD = "Period"
    COMMENT = "Comment"

class FillMissingPointType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """the type of fill missing point for anomaly detection
    """

    SMART_FILLING = "SmartFilling"
    PREVIOUS_VALUE = "PreviousValue"
    CUSTOM_VALUE = "CustomValue"
    NO_FILLING = "NoFilling"

class Granularity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """granularity of the time series
    """

    YEARLY = "Yearly"
    MONTHLY = "Monthly"
    WEEKLY = "Weekly"
    DAILY = "Daily"
    HOURLY = "Hourly"
    MINUTELY = "Minutely"
    SECONDLY = "Secondly"
    CUSTOM = "Custom"

class HookType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """hook type
    """

    WEBHOOK = "Webhook"
    EMAIL = "Email"

class IncidentStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """incident status
    
    only return for alerting incident result
    """

    ACTIVE = "Active"
    RESOLVED = "Resolved"

class IngestionStatusType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """latest ingestion task status for this data slice.
    """

    NOT_STARTED = "NotStarted"
    SCHEDULED = "Scheduled"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    NO_DATA = "NoData"
    ERROR = "Error"
    PAUSED = "Paused"

class NeedRollupEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """mark if the data feed need rollup
    """

    NO_ROLLUP = "NoRollup"
    NEED_ROLLUP = "NeedRollup"
    ALREADY_ROLLUP = "AlreadyRollup"

class PeriodType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """the type of setting period
    """

    AUTO_DETECT = "AutoDetect"
    ASSIGN_VALUE = "AssignValue"

class RollUpMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """roll up method
    """

    NONE = "None"
    SUM = "Sum"
    MAX = "Max"
    MIN = "Min"
    AVG = "Avg"
    COUNT = "Count"

class Severity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """min alert severity
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class SnoozeScope(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """snooze scope
    """

    METRIC = "Metric"
    SERIES = "Series"

class TimeMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """time mode
    """

    ANOMALY_TIME = "AnomalyTime"
    CREATED_TIME = "CreatedTime"
    MODIFIED_TIME = "ModifiedTime"

class ValueType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """data used to implement value filter
    """

    VALUE = "Value"
    MEAN = "Mean"

class ViewMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """data feed access mode, default is Private
    """

    PRIVATE = "Private"
    PUBLIC = "Public"
