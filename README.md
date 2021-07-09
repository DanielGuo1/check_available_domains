<!-- PROJECT LOGO -->
[![Python](https://img.shields.io/badge/Language-Python-blue.svg?style=flat-square&logo=Python&logoColor=white)](https://www.python.org/) 
[![Domainr](https://img.shields.io/badge/API-Domainr-yellowgreen.svg?style=flat-square&logo=Domainr&logoColor=white)](https://domainr.com/docs/api) 
[![Coinmarketcap](https://img.shields.io/badge/API-Coinmarketcap-green.svg?style=flat-square&logo=Coinmarketcap&logoColor=white)](https://coinmarketcap.com/api/) 


<h1 align="center">Automatically check for available domains</h1>
<p align="center">
  <a href="![image](https://github.com/DanielGuo1/check_available_domains/blob/main/image.jpeg)">
    <img src="https://github.com/DanielGuo1/check_available_domains/blob/main/image.jpeg" alt="Logo" width="520" height="320">
  </a>
  <p align="center">
    Find domains available for purchase within seconds
  </p>
</p>


## About The Project
Automate your domain-availability-check process. Instead of typing every possible combination of words into a domain search check, use this script to automatically check multiple keywords/possible domains within seconds.

I provided some data (inside the data folder) if you want to check diffrent domains without scraping it.

## How does it work?
1. First you need a dataset. I used as an example [crytocurrencies](https://coinmarketcap.com/api/). I got the top most popular coins from coinmarketcap.
2. With that data, I wanted to check if any of these coins didn't registered a domain or if there is a similiar domain available (e.g. ethereum.com).
3. To check whether a domain is available, I used [Domainr](https://domainr.com/docs/api).
4. Last step is to evaluate the results (inside of Jupyter Notebook).

## Getting Started

You need to download python in order to run the script [Download Python here](https://www.python.org/downloads/).

### Prerequisites
Install all necessary packages:
   ```sh
   pip3 install -r requirements.txt
   ```
1. Get a free API Key at [https://domainr.com/docs/api](https://domainr.com/docs/api)
2. Clone the repo
   ```sh
   git clone https://github.com/DanielGuo1/check_available_domains.git
   ```
### Setup
1. Enter your API credentials in `check_avail_crypto_domains.py`
   ```python
    headers = {
        'x-rapidapi-key': "YOUR_API_KEY",
        'x-rapidapi-host': "domainr.p.rapidapi.com"
    }
   ```
2. If you want to scrape the crypto data, create an API Key at [crytocurrencies](https://coinmarketcap.com/api/).
3. Set the path to your file:
  ```python
    f = open("../data/YOUR_TXT_FILE.TXT", "r")
   ```
   
4. Run `check_avail_crypto_domains.py`
   ```python
   python3 check_avail_crypto_domains.py
   ```
5. Finally analyse the data. I used a simple Jupyter Notebook `analysis_avail_domains.ipynb`
