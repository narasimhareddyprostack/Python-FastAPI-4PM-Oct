import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout, JSONDecodeError

def get_request(url, headers=None, params=None, timeout=10):
    try:
        response = requests.get(
            url,
            headers=headers or {},
            params=params,
            timeout=timeout
        )
        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Try to parse JSON
        try:
            return response.json()
        except JSONDecodeError:
            print("Response is not valid JSON. Returning raw text.")
            return response.text

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Status code: {response.status_code}")
    except ConnectionError:
        print("Error: Could not connect to the server. Check your internet or the URL.")
    except Timeout:
        print(f"Request timed out after {timeout} seconds.")
    except RequestException as err:
        print(f"An unexpected error occurred: {err}")
    except Exception as e:
        print(f"Unknown error: {e}")

    return None


#invoke restapi and print data
url='https://jsonplaceholder.typicode.com/gt'
data=get_request(url)
print(data)