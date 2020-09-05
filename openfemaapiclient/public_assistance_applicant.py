from dataclasses import dataclass
from datetime import datetime
from .dateutils import try_extract_date

DATETIME_FIELDS = {"lastRefresh"}


def applicant_mapper(records):
    results = []
    for record in records:
        mapped_result = {k: try_extract_date(v) if k in DATETIME_FIELDS else v for k, v in record.items()}
        results.append(PublicAssistanceApplicant(**mapped_result))
    return results


@dataclass(frozen=True)
class PublicAssistanceApplicant:
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
