import os
from scratchcloud import CloudClient, CloudChange
import time
import socket
from getpass import getpass

username = 'EloiStree'
project_id = '1058006745'
password = 'Password123'

udp_ipv4= "127.0.0.1"
udp_port= 12345

print("Write your password")
password = getpass("Enter your password: ")
# # Create password.txt file if not existing
# if not os.path.exists('scratchcloud_password.txt'):
#   with open('scratchcloud_password.txt', 'w') as file:
#     file.write(password)

# # Read password from password.txt
# with open('scratchcloud_password.txt', 'r') as file:
#   password = file.read().strip()

password = password.strip()  # Remove leading/trailing whitespaces
username = username.strip()  # Remove leading/trailing whitespaces
  # Display path of the password file
  
print(f"Password file path: {os.path.abspath('scratchcloud_password.txt')}")
print(f"Password: {password[:1]}*****")
print(f"Username: {username}")

client = CloudClient(username, project_id)

@client.event
async def on_connect():
    print('Connected!')

@client.event
async def on_disconnect():
    print('Disconnected!')

@client.event
async def on_message(cloud: CloudChange):
    print(f"{cloud.name} was set to {cloud.value}!")
    @client.event
    async def on_message(cloud: CloudChange):
      print(f"{cloud.name} was set to {cloud.value}!")
      udp_message = f"{cloud.name}={cloud.value}"
      udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      udp_socket.sendto(udp_message.encode(), (udp_ipv4, udp_port))
      udp_socket.close()


while True:
  try:
      client.run(password)
  except Exception as e:
      print('Failed to connect to Scratch Cloud. Please check your credentials and try again.')
      print(f'Error: {e}')
  time.sleep(5)  # Delay between reconnection attempts
