from datetime import datetime, timedelta
from openfemaapiclient.disaster_declaration import DisasterDeclaration, declaration_mapper

import logging
import requests

log = logging.getLogger('openfema-api-client')


def __create_payload(page_number=0,
                     is_preflight=False,
                     last_updated_start=None,
                     last_updated_end=None,
                     items_per_page=1000):
    minimum_date = last_updated_start if last_updated_start is not None \
        else datetime.now().replace(microsecond=0, second=0, minute=0, hour=0) - timedelta(days=1)
    maximum_date = last_updated_end if last_updated_end is not None \
        else datetime.now().replace(microsecond=0, second=0, minute=0, hour=0) + timedelta(days=2)
    payload = {
        '$filter': f'lastRefresh ge \'{minimum_date}\' and lastRefresh le \'{maximum_date}\'',
        '$inlinecount': 'allpages'
    }

    if page_number > 0:
        payload['$skip'] = page_number * items_per_page

    if is_preflight:
        payload['$limit'] = 0

    return payload


def __fetch_page(url, page_number, data_field_name, last_updated_start=None, last_updated_end=None,
                 response_mapper=None):
    page_payload = __create_payload(page_number=page_number, last_updated_start=last_updated_start,
                                    last_updated_end=last_updated_end)
    page_response = requests.get(url, page_payload)
    data = page_response.json().get(data_field_name, [])
    mapped_response = response_mapper(data) if response_mapper is not None else data
    return mapped_response


def fetch_from_api(url, last_updated_start, last_updated_end=None, items_per_page=1000, response_mapper=None):
    metadata = __fetch_metadata(url, last_updated_start, last_updated_end)
    total_count = metadata.get('count', 0)
    data_field_name = metadata.get('entityname')
    if total_count == 0:
        log.debug("No records found")
        return []

    if data_field_name is None:
        log.error(f"Invalid metadata response from FEMA. No 'entityname' found: [Metadata ${metadata}]")
        return []

    total_pages = total_count // items_per_page + 1
    log.debug(f"Total pages to fetch: {total_pages}")

    return [record
            for curr_page in range(total_pages)
            for record in __fetch_page(url, curr_page, data_field_name, last_updated_start,
                                       last_updated_end=last_updated_end,
                                       response_mapper=response_mapper)]


def fetch_from_api_generator(url, last_updated_start, last_updated_end=None, items_per_page=1000, response_mapper=None):
    metadata = __fetch_metadata(url, last_updated_start, last_updated_end)
    total_count = metadata.get('count', 0)
    data_field_name = metadata.get('entityname')
    if total_count == 0:
        log.debug("No records found")
        return None

    if data_field_name is None:
        log.error(f"Invalid metadata response from FEMA. No 'entityname' found: [Metadata ${metadata}]")
        return None

    total_pages = total_count // items_per_page + 1
    log.debug(f"Total pages to fetch: {total_pages}")

    def generator():
        for curr_page in range(total_pages):
            yield __fetch_page(url, curr_page, data_field_name, last_updated_start,
                               last_updated_end=last_updated_end,
                               response_mapper=response_mapper)

    return {
        'total_count': total_count,
        'total_pages': total_pages,
        'generator': generator
    }


def __fetch_metadata(url, last_updated_start=None, last_updated_end=None):
    preflight_payload = __create_payload(is_preflight=True, last_updated_start=last_updated_start,
                                         last_updated_end=last_updated_end)
    preflight_response = requests.get(url, preflight_payload)

    return preflight_response.json().get('metadata')


def fetch_disaster_declarations():
    return fetch_from_api("https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries", datetime.now() - timedelta(days=1), response_mapper=declaration_mapper)


def fetch_pa_applicants():
    return fetch_from_api("https://www.fema.gov/api/open/v1/PublicAssistanceApplicants", datetime.now() - timedelta(days=1), response_mapper=applicant_mapper)


def fetch_pa_funded_projects():
    return fetch_from_api("https://www.fema.gov/api/open/v1/PublicAssistanceFundedProjectsDetails", datetime.now() - timedelta(days=1), response_mapper=funded_project_mapper)