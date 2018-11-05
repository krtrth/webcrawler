import requests
import bs4
import sys
import xlwt
from xlwt import Workbook




class GetData:

    def getPageUrl(self,soup):
        nextpage = soup.select('.pagination a')
        pageurl = nextpage[-1].get('href')
        print(pageurl)
        return pageurl

    # print(pageurlurl)


    # print(exp)

    # Workbook is created


    def makeExcel(self,title, exp, skill,k,sheet):


        # add_sheet is used to create sheet.

        n=k

        for x in title:
            sheet.write(n,0,x)
            n+=1

        n=k

        for x in exp:
            sheet.write(n,1,x)
            n+=1

        n=k

        for x in skill:
            sheet.write(n,2,x)
            n+=1

        return n

    def getSoup(self,pageurl):
        res = requests.get(pageurl)
    # sys.exit(res)

        soup = bs4.BeautifulSoup(res.text,'lxml')
        return soup

object = GetData()
pageurl = 'https://www.naukri.com/0-year-jobs'
wb = Workbook()
sheet = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)

sheet.write(0,0,'title')
sheet.write(0,1,'exp')
sheet.write(0,2,'skill')
# print(pageurl)
res=requests.get(pageurl)
soup = bs4.BeautifulSoup(res.text,'lxml')
k=1
for i in range(0,338):
    titlec = soup.select('.content li')
    expc = soup.select('.exp')
    skillc = soup.select('.skill')

    title = []
    exp = []
    skill = []


    for i in titlec:
        title.append(i.getText())

    for i in expc:
        exp.append(i.getText())

    for i in skillc:
        skill.append(i.getText())

    k = object.makeExcel(title,exp,skill,k,sheet)
    pageurl=object.getPageUrl(soup)
    res=requests.get(pageurl)
    soup = bs4.BeautifulSoup(res.text,'lxml')

wb.save('naukri.xls')
