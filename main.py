import requests
from urllib.parse import urlparse

def get_http_headers(url):
    """
    Fetches and returns the HTTP headers of a given URL.
    
    Parameters:
        url (str): The URL to fetch headers from.
        
    Returns:
        dict: A dictionary of the HTTP headers.
    """
    try:
        response = requests.get(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers for {url}: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes given HTTP headers and extracts key information.
    
    Parameters:
        headers (dict): The HTTP headers to analyze.
        
    Returns:
        dict: A dictionary containing interesting header information.
    """
    analysis = {}
    analysis['Content-Type'] = headers.get('Content-Type', 'N/A')
    analysis['Server'] = headers.get('Server', 'N/A')
    analysis['Cache-Control'] = headers.get('Cache-Control', 'N/A')
    analysis['X-Content-Type-Options'] = headers.get('X-Content-Type-Options', 'N/A')
    return analysis

def main():
    """
    Main function to execute the OSINT tool.
    It takes user input for a URL, fetches headers, and analyzes them.
    """
    url = input("Enter a URL (starting with http:// or https://): ")
    
    # Validate URL format
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("Invalid URL. Please include 'http://' or 'https://'.")
        return
    
    headers = get_http_headers(url)
    if headers:
        print("\n=== HTTP Headers ===")
        for key, value in headers.items():
            print(f"{key}: {value}")
        
        print("\n=== Header Analysis ===")
        analysis = analyze_headers(headers)
        for key, value in analysis.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```