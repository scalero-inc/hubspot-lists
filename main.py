#%%
import datetime
import os
from os import environ

import requests
import pandas as pd

import logging

# Replace 'your_api_key' with your actual HubSpot API key
API_KEY = environ.get('API_KEY', '')
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}
ILS_LIST_IDS = environ.get('ILS_LIST_IDS', '').split(',')
MEMBERSHIP_URL = 'https://api.hubapi.com/crm/v3/lists/{listId}/memberships'


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    logger.info('Starting script...')
    list_results = []
    for list_id in ILS_LIST_IDS:
        next_url = MEMBERSHIP_URL.format(listId=list_id)
        i = 0
        logger.info(f'Processing list {list_id}...')
        while next_url:
            response = requests.get(next_url, headers=HEADERS)
            if response.status_code == 200:
                results = response.json()['results']
                results = [{**item, 'contact_list_id': list_id} for item in results]
                list_results += results
                i += 1
                next_url = response.json()['paging']['next']['link'] if 'next' in response.json()['paging'] else None
            else:
                logger.error(f'Failed to retrieve data for list {list_id}: {response.status_code}, {response}')
                next_url = None

    results_df = pd.DataFrame(list_results)
    results_df.rename(columns={'recordId': 'contact_id', 'membershipTimestamp': 'added_at'}, inplace=True)

    try:
        os.makedirs('files')
        logger.info('Directory created')
    except FileExistsError:
        pass
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    results_df.to_csv(f"files/results_{now}.csv", index=False)
    logger.info('Script completed successfully')
