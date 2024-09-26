import requests


def download_file(url, file_name):
    
    '''
    download a file from the provided url and save it locally
    '''
    file_name = f"{file_name}.{url.split('.')[-1].lower()}"
    
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file'{file_name}'")
        print(f" Status code: {response.status_code}")
        
# to test and debug the code
if __name__ == "__main__":
    url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Fsearch%3Fq%3Dpython%2BLogo&psig=AOvVaw31DRA5PUO22oLfdSpi7Bbp&ust=1727234755566000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPjmgIDR2ogDFQAAAAAdAAAAABAE'
    download_file(url, 'python_logo')
	
        
