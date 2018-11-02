#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import requests
with requests.Session() as s:
	url = "https://org.mephi.ru/auth/login?uname=kav052&password=1Dartvaders"
	r = s.get(url)
	print(r.content)