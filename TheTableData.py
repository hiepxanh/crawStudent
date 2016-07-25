from bs4 import BeautifulSoup

class TheTableData:
    def __init__(self,htmlSource):
        self.htmlSource = htmlSource
    def tolist(self):
        soup=BeautifulSoup(self.htmlSource,"html.parser")
        table = soup.find("div",{"class":"table"})
        #print(table.prettify())
        rows = table.find_all("div",{"class":"row"})

        array = []
        for row in rows:
            cells = row.find_all("div",{"class":"cell"})
            for cell in cells:
                cell = cell.get_text().strip()
                #print(cell)
                array.append(cell)

        list = [array[i:i+15] for i in range (0,len(array),15)]
        list.pop(0)
        return list
