from dataclasses import dataclass


@dataclass
class DataClassDisasterDeclaration:
    femaDeclarationString: str
    disasterNumber: int
    state: str
    declarationType: str
    declarationDate: str  # FEMA api lists as date type. Ex) "declarationDate":"1965-09-10T04:00:00.000Z"
    fyDeclared: int
    incidentType: str
    declarationTitle: str
    ihProgramDeclared: bool
    iaProgramDeclared: bool
    paProgramDeclared: bool
    hmProgramDeclared: bool
    incidentBeginDate: str  # FEMA api lists as date type. Ex) "incidentBeginDate":"1966-03-22T05:00:00.000Z"
    incidentEndDate: str  # FEMA api lists as date type. Ex) "incidentEndDate":"1965-09-10T04:00:00.000Z"
    disasterCloseoutDate: str  # FEMA api lists as date type. Ex) "disasterCloseOutDate":"1967-08-24T04:00:00.000Z"
    fipsStateCode: str
    fipsCountyCode: str
    placeCode: str
    designatedArea: str
    declarationRequestNumber: str
    lastRefresh: str  # FEMA api lists as date type. Ex) "lastRefresh":"2019-07-26T18:49:32.438Z"
    hash: str
    id: str
