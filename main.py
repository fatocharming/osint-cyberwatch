import requests
from urllib.parse import urlparse

def fetch_http_headers(url):
    """
    Fetch the HTTP headers from the specified URL.
    
    Args:
    url (str): The URL to fetch headers from.
    
    Returns:
    dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.get(url)
        headers = response.headers
        return headers
    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """
    Analyze the HTTP headers to extract useful information.
    
    Args:
    headers (dict): The HTTP headers to analyze.
    
    Returns:
    str: A summary of important headers.
    """
    if not headers:
        return "No headers to analyze."
    
    summary = []
    important_headers = ['Server', 'Content-Type', 'X-Powered-By', 'Strict-Transport-Security']
    
    for header in important_headers:
        if header in headers:
            summary.append(f"{header}: {headers[header]}")
    
    return "\n".join(summary)

def main():
    """
    Main function to run the OSINT script.
    """
    # Example URL
    url = input("Enter a URL to analyze (e.g., http://example.com): ")
    
    # Parse the URL to ensure it's valid
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        print("Invalid URL. Please include http:// or https://")
        return
    
    print(f"\nFetching HTTP headers for: {url}")
    headers = fetch_http_headers(url)

    print("\nAnalyzing headers...")
    analysis = analyze_headers(headers)
    
    print("\n--- Header Analysis ---")
    print(analysis)

if __name__ == "__main__":
    main()
```