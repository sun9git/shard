import requests
from lxml import html
from AbstractModule import AbstractModule

class LinkedinModule(AbstractModule):
	def try_login(self, uname, password):
		headers = { 'user-agent': AbstractModule().user_agent() }
		resp = requests.get("https://www.linkedin.com", headers= headers)

		tree = html.fromstring(resp.content)
		payload = tree.forms[0].fields
		payload = { k : v for k, v in payload.iteritems() }
		payload['session_key'] = uname
		payload['session_password'] = password
		loginResp = requests.post("https://www.linkedin.com/uas/login-submit", data= payload, headers= headers, cookies=resp.cookies, allow_redirects=False)

		if loginResp.status_code == 302:
			return True
		else:
			return False

linkedin = LinkedinModule()