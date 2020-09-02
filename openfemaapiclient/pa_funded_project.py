from dataclasses import dataclass
from datetime import datetime


def funded_project_mapper(records):
    funded_project_datetime_fields = {"lastRefresh", "declarationDate", "obligatedDate"}
    results = []
    for record in records:
        mapped_result = {k: __to_datetime(v) if k in funded_project_datetime_fields else v for k, v in record.items()}
        results.append(PAFundedProject(**mapped_result))
    return results


def __to_datetime(value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ") if value else None


@dataclass(frozen=True)
class PAFundedProject:
    disasterNumber: int
    pwNumber: int
    applicationTitle: str
    applicantId: str
    county: str
    countyCode: int
    stateNumberCode: int
    state: str
    projectAmount: float
    stateCode: str
    totalObligated: float
    federalShareObligated: float
    damageCategory: str
    dcc: str
    lastRefresh: datetime
    id: str
    hash: str
    projectSize: str
    damageCategoryCode: str
    declarationDate: datetime
    incidentType: str
    obligatedDate: datetime
