from dataclasses import dataclass
from datetime import datetime


def applicant_mapper(records):
    applicant_datetime_fields = {"lastRefresh"}
    results = []
    for record in records:
        mapped_result = {k: __to_datetime(v) if k in applicant_datetime_fields else v for k, v in record.items()}
        results.append(PAApplicant(**mapped_result))
    return results


def __to_datetime(value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ") if value else None


@dataclass(frozen=True)
class PAApplicant:
    state: str
    applicantName: str
    disasterNumber: int
    addressLine1: str
    zipCode: str
    addressLine2: str
    hash: str
    city: str
    lastRefresh: datetime
    id: str
    applicantId: str
