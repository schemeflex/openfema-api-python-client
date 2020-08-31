from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DataClassDisasterDeclaration:
    femaDeclarationString: str
    disasterNumber: int
    state: str
    declarationType: str
    declarationDate: datetime  # Ex) "declarationDate":"1965-09-10T04:00:00.000Z"
    fyDeclared: int
    incidentType: str
    declarationTitle: str
    ihProgramDeclared: bool
    iaProgramDeclared: bool
    paProgramDeclared: bool
    hmProgramDeclared: bool
    incidentBeginDate: datetime
    incidentEndDate: datetime
    disasterCloseoutDate: datetime
    fipsStateCode: str
    fipsCountyCode: str
    placeCode: str
    designatedArea: str
    declarationRequestNumber: str
    lastRefresh: datetime
    hash: str
    id: str
