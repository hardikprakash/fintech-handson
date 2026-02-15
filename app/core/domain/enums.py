from enum import Enum


class EntityType(Enum):
    COMPANY = "company"
    PARTNERSHIP = "partnership"
    SOLE_PROPRIETOR = "sole_proprietor"
    LLC = "llc"
    CORPORATION = "corporation"


class FilingType(Enum):
    INITIAL = "initial"
    ANNUAL = "annual"
    QUARTERLY = "quarterly"
    AMENDMENT = "amendment"



class IngestionTaskStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"


class AuditAction(Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    ARCHIVE = "archive"
    RESTORE = "restore"


class AuditEntityType(Enum):
    ENTITY = "entity"
    FILING = "filing"
    AMENDMENT = "amendment"
    INGESTION_EVENT = "ingestion_event"