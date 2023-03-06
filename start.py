import os
import subprocess
import urllib.request
import json

# Update package list and install required packages
subprocess.run(['apt', 'update', '-y'])
subprocess.run(['apt', 'install','xz-utils', '-y'])

# Create directory for Trilium data and download database file
os.makedirs('{HOME}/trilium-data', exist_ok=True)
urllib.request.urlretrieve('https://lmao.vtz.workers.dev/0:/document.db', '{HOME}/trilium-data/document.db')
print('Database file downloaded.')

# Download and extract Trilium binary
response = urllib.request.urlopen('https://api.github.com/repos/zadam/trilium/releases/latest')
data = json.loads(response.read())
download_url = [a['browser_download_url'] for a in data['assets'] if a['name'].startswith('trilium-linux-x64-server-')][0]
filename = download_url.split('/')[-1]
urllib.request.urlretrieve(download_url, filename)
subprocess.run(['tar', '-Jxvf', filename, '--strip-components=1'])
os.remove(filename)
print('Trilium binary downloaded and extracted.')

# Run Trilium
subprocess.run(['./trilium.sh'])
