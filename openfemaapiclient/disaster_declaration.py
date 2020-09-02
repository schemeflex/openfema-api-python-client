from dataclasses import dataclass
from datetime import datetime


def declaration_mapper(records):
    declaration_datetime_fields = {"declarationDate", "incidentBeginDate", "incidentEndDate", "disasterCloseoutDate", "lastRefresh"}
    results = []
    for record in records:
        mapped_result = {k: __to_datetime(v) if k in declaration_datetime_fields else v for k, v in record.items()}
        results.append(DisasterDeclaration(**mapped_result))
    return results


def __to_datetime(value):
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ") if value else None


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
