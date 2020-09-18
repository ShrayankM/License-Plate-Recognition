import requests


def send(ph, message):
	url = "https://www.fast2sms.com/dev/bulk"

	querystring = {"authorization":"9BgwbfA1hinpuZNQRELIWJoMcVqS3PtlsXjCxvH6FKYkDyd0me7JavXkZshCSBMrqPdbjI48xtfiYe1n",
		        "sender_id":"FSTSMS",
		        "message":message,
		        "language":"english",
		        "route":"p",
		        "numbers":"8605511687"}

	headers = {
	    'cache-control': "no-cache"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	print(response.text)
