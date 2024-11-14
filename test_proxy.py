import requests
from decouple import UndefinedValueError
from decouple import config
# Initialize decouple to read from the .env file
# config = Config()  # No search_path argument needed

try:
    # Load proxy credentials from the .env file
    proxy_user = config('PROXY_USER')  # Will raise an error if not found
    proxy_pass = config('PROXY_PASSWORD')  # Will raise an error if not found
except UndefinedValueError as e:
    print(f"Error: Missing environment variable {e}")
    exit(1)

# Proxy settings
proxy_host = 'localhost'  # Replace with your proxy server's IP if remote
proxy_port = '1080'       # The port you exposed

# Test URL
test_url = 'http://ipinfo.io/ip'  # This will return the IP address

# Set up the proxy dictionary
proxies = {
    'http': f'socks5://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
    'https': f'socks5://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
}

try:
    # Make a request through the proxy
    response = requests.get(test_url, proxies=proxies, timeout=5)
    response.raise_for_status()  # Check if request was successful
    print("Proxy is working. Your IP via proxy is:", response.text.strip())
except requests.RequestException as e:
    print("Failed to connect to the proxy:", e)
