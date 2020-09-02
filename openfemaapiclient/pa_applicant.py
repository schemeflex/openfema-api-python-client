from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class PAApplicant:
    state: str
    applicantName: str
    disasterNumber: int
    addressLine1: str
    declarationDate: datetime  # Ex) "declarationDate":"1965-09-10T04:00:00.000Z"
    fyDeclared: int
    incidentType: str
    zipCode: str
    addressLine2: str
    hash: str
    city: str
    lastRefresh: datetime
    id: str
    applicantId: str
