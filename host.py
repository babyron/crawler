import urllib.parse

def get_host(url):
	url_domain = urllib.parse.urlparse(url)
	domain = '{uri.scheme}://{uri.netloc}'.format(uri=url_domain)
	return domain


print(get_host("http://baidu.com/123/234"))