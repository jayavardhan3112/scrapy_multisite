# Multisite-Python-Crawler

Usage : scrapy crawl mySpider -a url=#enter_complete_url -a domain=#enter_allowed_domains_seperated_by_&

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install scrapy
pip install scrapyd
```
Download Curl from the website given below
```bash
https://curl.haxx.se/download.html
```

## Usage
An almost generic web crawler built using Scrapy and Python 3.7 to recursively crawl entire websites.

Developing a single generic crawler is difficult as different websites require different XPath expressions to retreive content.

This multisite crawler gets the paragraph tag text and outputs a JSON file of the following format

```python
{
	"pages" : [
			{
				"page" : "...."
				"content" : "...."
			},
			{
				"page" : "..."
				"content" : "..."
			}
		.
		.
		.
	]
}
```
## Finally
If required, it can be modified to read text from other tags by including explicit xpath statements too.

After installing scrapy using 'pip install scrapy' copy the entire repository onto any suitable location and use as per the usage.


## Scrapyd
To launch scrapy deamon instance. Then we have a seerver listening on 
http://localhost:6800/
```python
scrapyd
```

To deploy our project locally
```python
pip install git+https://github.com/scrapy/scrapyd-client.git
```

To Deploy : Go to your spider directory
```python
scrapyd-deploy default
```
before this go to scrapy.cfg change [deploy] -> [deploy:default].

Add URL : http://localhost:6800/.

Add project : your_project_name

Output : 

```.env
Packing version 1590398186
Deploying to project "scraper" in http://localhost:6800/addversion.json
Server response (200):
{"node_name": "Jais-MBP-2", "status": "ok", 
"project": "scraper", "version": "1590398186", "spiders": 1}
```
To launch the spider : 
```python
curl http://localhost:6800/schedule.json -d 
project=project_name -d spider=spider_name

```

Example :

### To Add a task
```.env
curl http://localhost:6800/schedule.json -d project=scraper -d 
spider=mySpider -d url=https://browneyedbibliophile.wordpress.com/ -d 
domain=browneyedbibliophile.wordpress.com
```
Output : 
```.env
{"node_name": "node_name", "status": "ok", "jobid": "aklsdhfjlasdfasdfsadfasd"}
```

### To Cancel a task
```.env
curl http://localhost:6800/cancel.json -d project=scraper -d job=2695cb169e6911eab70338f9d371ef52
```
Output : 
```.env
{"node_name": "node_name", "status": "ok", "prevstate": null}
```


### To List tasks
```.env
curl http://localhost:6800/listprojects.json
```
Output : 
```.env
{"node_name": "node_name", "status": "ok", "projects": ["scraper", "MovieScrap", "default"]}
```


### To List Versions
```.env
curl http://localhost:6800/listversions.json?project=scraper
```
Output : 
```.env
{"node_name": "node_name", "status": "ok", "versions": ["1590468982"]}
```


### To List Spiders
```.env
curl http://localhost:6800/listspiders.json?project=scraper
```
Output : 
```.env
{"node_name": "node_name", "status": "ok", "spiders": ["mySpider"]}
```


### To List Jobs
```.env
curl http://localhost:6800/listjobs.json?project=scraper
```
Output : 
```.env
{"node_name": "Jais-MBP-2", "status": "ok", "pending": [], "running": [], "finished": [{"id": "41660f429f0d11eab19538f9d371ef52", "spider": "mySpider", "start_time": "2020-05-26 10:26:27.999800", "end_time": "2020-05-26 10:26:32.869970"}, {"id": "6f963f689f0d11eab19538f9d371ef52", "spider": "mySpider", "start_time": "2020-05-26 10:27:48.000979", "end_time": "2020-05-26 10:27:54.865389"}]}
```



### To Delete Version
```.env
curl http://localhost:6800/delversion.json -d project=myproject -d version=r99
```
Output : 
```.env
{"status": "ok"}
```


### To Delete Project
```.env
curl curl http://localhost:6800/delproject.json -d project=myproject
```
Output : 
```.env
{"status": "ok"}
```
