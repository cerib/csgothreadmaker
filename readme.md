# Required Software:
1. Python3
  - On Windows I recommend installing it through chocolatey, check out https://chocolatey.org/install
  - After installing chocolatey, run this command on the terminal: choco install python3 --pre 
2. Install the following libraries: BeautifulSoup and urllib3
  - pip install beautifulsoup4
  - pip install urllib3

# How to use:

1. Find the HLTV match page link. For example, https://www.hltv.org/matches/2339092/faze-vs-nip-blast-premier-spring-series-2020
2. Navigate to the folder where you have hltv.py
3. Run the script like this: **`python ./hltv.py https://www.hltv.org/matches/2339092/faze-vs-nip-blast-premier-spring-series-2020`**
4. Copy and paste the console output
# Notes:

Early version, still very buggy. If the team name in the HLTV match page has spaces or special characters, the team icon will not be displayed correctly, and for now you'll have to find the correct name for it and replace it manually.
