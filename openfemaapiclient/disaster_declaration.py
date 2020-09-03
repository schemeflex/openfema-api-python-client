from dataclasses import dataclass
from datetime import datetime

from .dateutils import try_extract_date

DATETIME_FIELDS = {"declarationDate", "incidentBeginDate", "incidentEndDate", "disasterCloseoutDate",
                   "lastRefresh"}


def declaration_mapper(records):
    results = []
    for record in records:
        mapped_result = {k: try_extract_date(v) if k in DATETIME_FIELDS else v for k, v in record.items()}
        results.append(DisasterDeclaration(**mapped_result))
    return results


@dataclass(frozen=True)
class DisasterDeclaration:
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
