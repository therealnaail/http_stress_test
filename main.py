import requests
import time

# Defines target URL and number of requests
target_url = input("Enter the target URL: ")
num_requests = int(input("Enter the number of requests to send: "))

# Define the headers to send with the requests
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
print("""
*******************************************************
WARNING! \n
This program is designed to be used for ethical \n
pentesting purposes only. The developer of this \n
program does not condone or support any malicious or \n
illegal activities that may be performed using \n
this program. The use of this stress test without \n
explicit permission from the targeted system's owner \n
is strictly prohibited and may be illegal. \n 

It is the responsibility of the user to ensure that \n
their use of this program complies with all applicable \n
laws and regulations. The developer of this program \n
is not responsible for any misuse or damage caused \n
by the use of this program. 
*******************************************************
""")

# Sends requests and times the execution
start_time = time.time()
for i in range(num_requests):
    response = requests.get(target_url, headers=headers)
    print("Request #%d: %d" % (i+1, response.status_code))
end_time = time.time()

# Calculates and prints total time and requests per second
total_time = end_time - start_time
requests_per_second = num_requests / total_time
print("Sent %d requests in %f seconds (%f requests per second)" % (num_requests, total_time, requests_per_second))