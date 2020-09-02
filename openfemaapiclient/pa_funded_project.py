from dataclasses import dataclass
from datetime import datetime

# Uses the pa funded projects details api endpoint.


@dataclass(frozen=True)
class DisasterDeclaration:
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
