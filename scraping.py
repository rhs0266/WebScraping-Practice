import codecs
import requests 
from bs4 import BeautifulSoup 
import os


def trade_spider(max_pages): 
	page = 1
	file = codecs.open("result.html", 'w', 'utf-8')
	file.write("<table style=\"text-align:center;\">\n")
	while page <= max_pages: 
		url = 'http://koitp.org/results/?page=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, 'lxml')
		for tr in soup.find_all('tr'):
			flag = 0
			tds = tr.find_all('td')
			if (len(tds) < 2):
				continue
			if (tds[1].get_text().find('_r4') == -1):
				continue
			user = tds[1].get_text()
			score_info = tds[5].get_text()
			score = score_info.split(' ')[0]
			# id = tds[2].get_text().strip()
			id = tds[2].a.get('title')
			detail = 'http://koitp.org' + tds[7].a.get('href')
			
			file.write("<tr>\n")
			file.write("<td>" + user + "</td>\n")
			file.write("<th>" + score + "</th>\n")
			file.write("<td>" + id + "</td>\n")
			file.write("<td> <a href = \"" + detail + "\">" + "Detail" + "</a> </td>\n")
			file.write("</tr>\n")
		page += 1
	file.write("</table>")
#0 <td>265546</td>, 
#1 <td>sophie10_r4</td>, 
#2 <td><a data-placement="bottom" data-toggle="tooltip" href="/problem/REPRESENTATIVE/read/" title="\uad6c\uac04\uc758 \ub300\ud45c\uac12">REPRESENTATIVE</a>\n</td>, 
#3 <td>Java</td>, 
#4 <td>\uc644\ub8cc</td>, 
#5 <td>100 / 100</td>, 
#6 <td><a class="datetime-tooltip" data-placement="bottom" data-toggle="tooltip" title="2017\ub144 05\uc6d4 27\uc77c 20\uc2dc 55\ubd84 31\ucd08">57\ubd84 \uc804</a>\n</td>, 
#7 <td><a class="btn btn-xs btn-primary" href="/results/265546/">\uc790\uc138\ud788</a></td>



trade_spider(10)
os.startfile('result.html')