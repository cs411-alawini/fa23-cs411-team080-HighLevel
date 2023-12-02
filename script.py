# import requests

# def search_repositories_with_dependency_and_version(library, version, token):
#     """
#     Search GitHub repositories for a specific library and version in pom.xml files.
#     """
#     query = f"{library}+{version}+in:file+language:xml+filename:pom"
#     url = f"https://api.github.com/search/code?q={query}"
#     headers = {'Authorization': f'token {token}'}

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         items = response.json().get('items', [])
#         repo_urls = [item['repository']['html_url'] for item in items]
#         return repo_urls
#     except requests.HTTPError as http_err:
#         return f"HTTP error occurred: {http_err}"
#     except Exception as err:
#         return f"An error occurred: {err}"

# def save_results_to_file(results, filename):
#     """
#     Save the search results to a file.
#     """
#     with open(filename, 'w') as file:
#         for url in results:
#             file.write(url + '\n')

# # Personal Access Token - Replace with your actual token
# token = "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"

# # File to save results
# output_file = "repository_urls.txt"

# # Searching for repositories with both "commons-cli" and "1.5.0" in their pom.xml files
# repositories = search_repositories_with_dependency_and_version("commons-cli", "1.5.0", token)

# # Save results to file
# save_results_to_file(repositories, output_file)
import requests
import json

def search_github_for_dependency(library, version, token):
    """
    Search GitHub repositories for a specific library dependency using authentication.
    """
    query = f"{library}+filename:pom.xml+{version}"
    url = f"https://api.github.com/search/code?q={query}"
    headers = {'Authorization': f'token {token}'}
    repo_urls = []

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        items = response.json().get('items', [])
        for item in items:
            repo_url = item['repository']['html_url']  # Extract the repository URL
            repo_urls.append(repo_url)
        return repo_urls
    else:
        return f"Error: {response.status_code}"

def save_results_to_file(results, filename):
    """
    Save the search results to a file.
    """
    with open(filename, 'w') as file:
        for url in results:
            file.write(url + '\n')

# Personal Access Token (Replace with your token)
your_token = "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"

# File to save results
output_file = "search_results.txt"

# Searching for repositories that depend on commons-cli 1.5.0
results = search_github_for_dependency("commons-cli", "1.5.0", your_token)

# Save results to file
save_results_to_file(results, output_file)
