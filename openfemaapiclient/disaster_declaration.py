from dataclasses import dataclass


@dataclass
class DataClassDisasterDeclaration:
    id: str  # mapping uses id: femaOriginId
    incidentType: str
    declarationType: str  # uses varchar(2) on pg
    declarationTitle: str
    state: str
    designatedArea: str
    disasterNumber: int
    hash: str
    fyDeclared: int
    fipsStateCode: str  # uses varchar(2) on pg
    fipsCountyCode: str  # uses varchar(3) on pg
    paProgramDeclared: bool
    ihProgramDeclared: bool
    iaProgramDeclared: bool
    hmProgramDeclared: bool
    lastRefresh: str  # mapping uses lastRefresh: lastUpdatedDate
    incidentBeginDate: str
    incidentEndDate: str
    declarationDate: str
    disasterCloseoutDate: str
    femaDeclarationString: str
    placeCode: str
