### Requirements  


#### Windows :


##### In admistrator Powershell : 
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
```
choco install ffmpeg
```

##### In cmd or Powershell : 
```
pip install --upgrade youtube-dl
```
```
pip install --upgrade ffmpeg
```
```
pip install --upgrade ffprobe
```
```
pip install --upgrade termcolor
```
```
pip install --upgrade colorama
```
