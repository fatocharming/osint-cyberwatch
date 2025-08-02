import requests
from urllib.parse import urlparse

def get_http_headers(url):
    """
    Fetches and displays HTTP headers for a given URL.
    
    Args:
        url (str): The target URL to analyze.
        
    Returns:
        dict: HTTP headers retrieved from the response.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return None

def analyze_headers(headers):
    """
    Analyzes the HTTP headers and prints out important information.
    
    Args:
        headers (dict): The HTTP headers to analyze.
    """
    print("\n=== HTTP Headers Analysis ===")
    
    # Check for common security headers
    security_headers = ['X-Content-Type-Options', 'X-Frame-Options', 'Content-Security-Policy']
    for header in security_headers:
        if header in headers:
            print(f"{header}: {headers[header]}")
        else:
            print(f"{header}: NOT PRESENT")
    
    # Print server information
    server_info = headers.get('Server', 'No Server Header')
    print(f"Server: {server_info}")

def main():
    # Input URL from the user
    url = input("Enter a URL (e.g., http://example.com): ").strip()
    
    # Parse the URL to ensure it's valid
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        print("Invalid URL. Please include 'http://' or 'https://'.")
        return

    # Get and analyze HTTP headers
    headers = get_http_headers(url)
    if headers:
        analyze_headers(headers)

if __name__ == "__main__":
    main()
```