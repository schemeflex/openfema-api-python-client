# openfema-api-client-python
Note: **This is a bare-bones initial release, expect breaking changes until release 1.0.0 **

The goal of this library is to wrap the OpenFEMA API specification and provide
an easy-to-use interface for fetching data from the OpenFEMA APIs.

## Requirements
 - Python 3.7+ (for dataclasses usage)

### Currently Supported Data Sets
 - [Disaster Declarations (v2)](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2)
 - [Public Assistance Applicants (v1)](https://www.fema.gov/openfema-data-page/public-assistance-applicants)
 - [Public Assistance Funded Projects Details (v1)](https://www.fema.gov/openfema-data-page/public-assistance-funded-projects-details)

## Example Usage
#### Fetch all documents from a date range
```
from datetime import datetime
from openfemaapiclient import fetch_pa_applicants, PublicAssistanceApplicant


yesterday =  datetime.now().replace(microsecond=0, second=0, minute=0, hour=0) - timedelta(days=1)
applicants: PublicAssistanceApplicant = fetch_pa_applicants(yesterday)

for applicant in applicants:
    print(applicant)
```

#### Fetch pages via generator for a date range
```
from datetime import datetime
from openfemaapiclient import create_pa_applicants_generator, PublicAssistanceApplicant


yesterday =  datetime.now().replace(microsecond=0, second=0, minute=0, hour=0) - timedelta(days=1)
applicant_wrapper = create_pa_applicants_generator(yesterday)

total_count = applicant_wrapper.get('total_count')
total_pages = applicant_wrapper.get('total_pages')
page_generator = applicant_wrapper.get('generator')

if page_generator is None:
    return

for applicant_page in page_generator:
    for applicant in applicant_page:
        print(applicant)
```