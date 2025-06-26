#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/6/26 17:23
# @Author  : Soin
# @File    : knowledge.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import html


class Knowledge:
    def __init__(self):
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
            # 'cookie': 'mtwebsession=101b7f3d4a51dda7aa1c88c4f2e99553; dekisession="Nzk5YjljMzEtMzMxMS00YzZhLWIzZjAtYjhmYjM4NjVjOGRifDIwMjUtMDYtMjZUMDk6MDI6Mjk="; _gid=GA1.2.1935168416.1750928555; _gd_visitor=ceea10b0-af91-4deb-84b9-12e01fb4c9ba; _gd_session=e645c8f6-df1b-45a5-86b5-69557be37ace; _ga=GA1.3.1876404062.1750928555; _gid=GA1.3.1935168416.1750928555; faro#lang=en; ASP.NET_SessionId=iu5ow4hlgokf1s3yctraanr2; __RequestVerificationToken=gUpSiNKhm25f8Zz3t6U58YuNhsXj_XJJ7YXwCDKvSEwBOzKzbRzHjBjovm2qqDdB55wluKLiUV83lFlKw9aN8InKzXIN6EAPscgtIopqnXA1; sxa_site=FARO; _gcl_au=1.1.1551898896.1750928585; _fbp=fb.1.1750928585858.558919541306919386; SC_ANALYTICS_GLOBAL_COOKIE=65ec6f90657646ae881366505e043c42|True; OptanonAlertBoxClosed=2025-06-26T09:07:57.333Z; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+26+2025+17%3A09%3A49+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=278ae6c8-4cb6-4257-aac3-35a2d5f18720&interactionCount=3&isAnonUser=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=%3B&AwaitingReconsent=false; _ga_34CW8W74KP=GS2.1.s1750928585$o1$g1$t1750929159$j60$l0$h0; _ga_JRFV3K3B8D=GS2.2.s1750928558$o1$g1$t1750929183$j60$l0$h0; _ga=GA1.1.1876404062.1750928555; _ga_DDKBMQBGK1=GS2.1.s1750928579$o1$g1$t1750929313$j50$l0$h1617356358; _ga_B3MEFHRN3F=GS2.1.s1750928557$o1$g1$t1750929313$j58$l0$h0; _ga_HHXN0SL94J=GS2.1.s1750928557$o1$g1$t1750929313$j58$l0$h0',
        }

    def decode_html_entities(self, text):
        """
        将 HTML 字符实体（如 &#20013;）转换为对应的 Unicode 字符。
        支持十进制和十六进制实体。
        """
        return html.unescape(text)

    def process_table(self, table: BeautifulSoup):
        date = table.find('td', {"data-th": '日期'})
        print(date.text)

    def page_get(self, url):
        response = requests.get(
            url=url,
            headers=self.headers,
        )
        # response.encoding = 'utf-8'
        # print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all('table', class_="mt-responsive-table")
        for table in tables:
            self.process_table(table)


if __name__ == '__main__':
    Knowledge().page_get(
        'https://zh-knowledge.faro.com/Hardware/FaroArm_and_ScanArm/FaroArm_and_ScanArm/User_Manuals_for_the_FaroArm-_ScanArm_and_Gage',
    )
