# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AggregationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Aggregation type."""

    AVERAGE = "Average"
    """Average value."""
    COUNT = "Count"
    """Total count."""
    NONE = "None"
    """Aggregation will be average in this case."""
    TOTAL = "Total"
    """Total sum."""
    PERCENTILE75 = "Percentile75"
    """75th percentile."""
    PERCENTILE90 = "Percentile90"
    """90th percentile."""
    PERCENTILE95 = "Percentile95"
    """95th percentile."""
    PERCENTILE96 = "Percentile96"
    """96th percentile."""
    PERCENTILE97 = "Percentile97"
    """97th percentile."""
    PERCENTILE98 = "Percentile98"
    """98th percentile."""
    PERCENTILE99 = "Percentile99"
    """99th percentile."""
    PERCENTILE999 = "Percentile999"
    """99.9th percentile."""
    PERCENTILE9999 = "Percentile9999"
    """99.99th percentile."""


class CertificateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Types of certificates supported."""

    AKV_CERT_URI = "AKV_CERT_URI"
    """If the certificate is stored in an Azure Key Vault."""


class FileStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """File status."""

    NOT_VALIDATED = "NOT_VALIDATED"
    """File is not validated."""
    VALIDATION_SUCCESS = "VALIDATION_SUCCESS"
    """File is validated."""
    VALIDATION_FAILURE = "VALIDATION_FAILURE"
    """File validation is failed."""
    VALIDATION_INITIATED = "VALIDATION_INITIATED"
    """File validation is in progress."""
    VALIDATION_NOT_REQUIRED = "VALIDATION_NOT_REQUIRED"
    """Validation is not required."""


class FileType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Types of file supported."""

    JMX_FILE = "JMX_FILE"
    """If the file is a JMX script."""
    USER_PROPERTIES = "USER_PROPERTIES"
    """If the file is a user properties file."""
    ADDITIONAL_ARTIFACTS = "ADDITIONAL_ARTIFACTS"
    """If the file is not among any of the other supported file types."""
    ZIPPED_ARTIFACTS = "ZIPPED_ARTIFACTS"
    """If the file is a compressed archive containing a collection of various artifacts or resources."""
    URL_TEST_CONFIG = "URL_TEST_CONFIG"
    """If the file is a JSON config file to define the requests for a URL test."""
    TEST_SCRIPT = "TEST_SCRIPT"
    """If the file is a test script."""


class MetricUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Metric unit."""

    NOT_SPECIFIED = "NotSpecified"
    """No unit specified."""
    PERCENT = "Percent"
    """Percentage."""
    COUNT = "Count"
    """Value count."""
    SECONDS = "Seconds"
    """Seconds."""
    MILLISECONDS = "Milliseconds"
    """Milliseconds"""
    BYTES = "Bytes"
    """Bytes"""
    BYTES_PER_SECOND = "BytesPerSecond"
    """Bytes per second"""
    COUNT_PER_SECOND = "CountPerSecond"
    """Count per second"""


class PFAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Action to take on failure of pass/fail criteria."""

    CONTINUE_ENUM = "continue"
    """Test will continue to run even if pass fail metric criteria metric gets failed."""
    STOP = "stop"
    """Test run will stop if pass fail criteria metric is not passed."""


class PFAgFunc(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Aggregation functions for pass/fail criteria."""

    COUNT = "count"
    """Criteria applies for count value."""
    PERCENTAGE = "percentage"
    """Criteria applies for given percentage value."""
    AVG = "avg"
    """Criteria applies for avg value."""
    P50 = "p50"
    """Criteria applies for 50th percentile value."""
    P75 = "p75"
    """Criteria applies for 75th percentile value."""
    P90 = "p90"
    """Criteria applies for 90th percentile value."""
    P95 = "p95"
    """Criteria applies for 95th percentile value."""
    P96 = "p96"
    """Criteria applies for 96th percentile value."""
    P97 = "p97"
    """Criteria applies for 97th percentile value."""
    P98 = "p98"
    """Criteria applies for 98th percentile value."""
    P99 = "p99"
    """Criteria applies for 99th percentile value."""
    P99_9 = "p99.9"
    """Criteria applies for 99.9th percentile value."""
    P99_99 = "p99.99"
    """Criteria applies for 99.99th percentile value."""
    MIN = "min"
    """Criteria applies for minimum value."""
    MAX = "max"
    """Criteria applies for maximum value."""


class PFMetrics(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Metrics for pass/fail criteria."""

    RESPONSE_TIME_MS = "response_time_ms"
    """Pass fail criteria for response time metric in milliseconds."""
    LATENCY = "latency"
    """Pass fail criteria for latency metric in milliseconds."""
    ERROR = "error"
    """Pass fail criteria for error metric."""
    REQUESTS = "requests"
    """Pass fail criteria for total requests."""
    REQUESTS_PER_SEC = "requests_per_sec"
    """Pass fail criteria for request per second."""


class PFResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Pass/fail criteria result."""

    PASSED = "passed"
    """Given pass fail criteria metric has passed."""
    UNDETERMINED = "undetermined"
    """Given pass fail criteria metric couldn't determine."""
    FAILED = "failed"
    """Given pass fail criteria metric has failed."""


class PFTestResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Test result based on pass/fail criteria."""

    PASSED = "PASSED"
    """Pass/fail criteria has passed."""
    NOT_APPLICABLE = "NOT_APPLICABLE"
    """Pass/fail criteria is not applicable."""
    FAILED = "FAILED"
    """Pass/fail criteria has failed."""


class RecommendationCategory(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Category of Recommendation."""

    THROUGHPUT_OPTIMIZED = "ThroughputOptimized"
    """The recommendation for this category optimizes the throughput/RPS (Requests per Second) of the
    app."""
    COST_OPTIMIZED = "CostOptimized"
    """The recommendation for this category optimizes the cost of the app."""


class RequestDataLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Request data collection level for test run."""

    NONE = "NONE"
    """No request data will be collected"""
    ERRORS = "ERRORS"
    """Request data will be collected in case of failed requests"""


class ResourceKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Kind of the resource on which test profile is created."""

    FUNCTIONS_FLEX_CONSUMPTION = "FunctionsFlexConsumption"
    """Resource is a Azure FunctionApp on Flex Consumption Plan."""


class SecretType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Types of secrets supported."""

    AKV_SECRET_URI = "AKV_SECRET_URI"
    """If the secret is stored in an Azure Key Vault."""
    SECRET_VALUE = "SECRET_VALUE"
    """If the secret value provided as plain text."""


class Status(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Test run status."""

    ACCEPTED = "ACCEPTED"
    """Test run request is accepted."""
    NOTSTARTED = "NOTSTARTED"
    """Test run is not yet started."""
    PROVISIONING = "PROVISIONING"
    """Test run is provisioning."""
    PROVISIONED = "PROVISIONED"
    """Test run is provisioned."""
    CONFIGURING = "CONFIGURING"
    """Test run is getting configured."""
    CONFIGURED = "CONFIGURED"
    """Test run configuration is done."""
    EXECUTING = "EXECUTING"
    """Test run has started executing."""
    EXECUTED = "EXECUTED"
    """Test run execution is completed."""
    DEPROVISIONING = "DEPROVISIONING"
    """Test run is getting deprovisioned."""
    DEPROVISIONED = "DEPROVISIONED"
    """Test run is deprovisioned."""
    DONE = "DONE"
    """Test run is completed."""
    CANCELLING = "CANCELLING"
    """Test run is being cancelled."""
    CANCELLED = "CANCELLED"
    """Test run request is cancelled."""
    FAILED = "FAILED"
    """Test run request is failed."""
    VALIDATION_SUCCESS = "VALIDATION_SUCCESS"
    """Test run JMX file is validated."""
    VALIDATION_FAILURE = "VALIDATION_FAILURE"
    """Test run JMX file validation is failed."""


class TestKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Test kind."""

    URL = "URL"
    """URL Test"""
    JMX = "JMX"
    """JMX Test"""
    LOCUST = "Locust"
    """Locust Test"""


class TestProfileRunStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Test profile run status."""

    ACCEPTED = "ACCEPTED"
    """Test profile run request is accepted."""
    NOTSTARTED = "NOTSTARTED"
    """Test profile run is not yet started."""
    EXECUTING = "EXECUTING"
    """Test profile run has started executing."""
    DONE = "DONE"
    """Test profile run has completed successfully."""
    CANCELLING = "CANCELLING"
    """Test profile run is being cancelled."""
    CANCELLED = "CANCELLED"
    """Test profile run is cancelled."""
    FAILED = "FAILED"
    """Test profile run has failed."""


class TimeGrain(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Time Grain."""

    PT5S = "PT5S"
    """5 seconds, available only if test run duration is less than 10 minutes."""
    PT10S = "PT10S"
    """10 seconds, available only if test run duration is less than 10 minutes."""
    PT1M = "PT1M"
    """1 minute"""
    PT5M = "PT5M"
    """5 minutes, available only if test run duration is greater than 1 minute."""
    PT1H = "PT1H"
    """1 hour, available only if test run duration is greater than 1 minute."""
