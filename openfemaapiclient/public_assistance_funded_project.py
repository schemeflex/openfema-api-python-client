from dataclasses import dataclass
from datetime import datetime
from .dateutils import try_extract_date

DATETIME_FIELDS = {"lastRefresh", "declarationDate", "obligatedDate"}


def funded_project_mapper(records):
    results = []
    for record in records:
        mapped_result = {k: try_extract_date(v) if k in DATETIME_FIELDS else v for k, v in record.items()}
        results.append(PAFundedProject(**mapped_result))
    return results


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
