from googlesearch import search
import time
import random

# List of rotating proxies (replace with actual proxies)
proxies = ['proxy1.example.com', 'proxy2.example.com', 'proxy3.example.com']

def search_with_proxy(query, num_results=10, pause=2):
    for proxy in proxies:
        try:
            # Perform Google search using the current proxy
            search_results = search(query, tld="co.in", num=num_results, stop=num_results, pause=pause, proxy=proxy)
            for j in search_results:
                print(j)
            return  # Exit the loop if successful
        except Exception as e:
            print(f"Failed with proxy {proxy}: {e}")
            continue  # Try the next proxy

    print("All proxies failed. Please try again later.")

if __name__ == "__main__":
    query = "site:manilatimes.net global warming"
    search_with_proxy(query)
