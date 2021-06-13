
from bs4 import BeautifulSoup as bs
import requests

# target URL
def get_urls_list():
    urls=[]
    urls.append("https://fknol.com/stock/list/wilshire-5000.php")
    return urls

def get_html(url):
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    return soup
    
def get_cells(soup):
    cell_dict ={}
    table = soup.find("table")
    rows_list = []
    rows = table.find_all("tr")
    for row in rows:
        rows_list.append(row)
    rows_list = rows_list[2:]

    cell_list =[]
    for row in rows_list:
        cell = row.find_all("td")
        cell_list.append(cell)


# get elements 2,6 for the spreadsheet
    cell = str(cell_list[0][1]).strip("<td>").strip("</td>").strip("<b>").strip("</b>")
    cell = cell.split("(")[1]
    cell = cell.split(")")[0]
    cell_dict["TIKR": cell]
    cell = str(cell_list[0][5]).strip("<td></$")
    cell = float(cell)
    cell_dict["Price": cell]
    return cell_dict

def main():

# build list of urls

    urls = get_urls_list()

# get tables one at a time and strip the data required

    master_list =[]
    for url in urls:
        soup = get_html(url)
    
    master_list.append(get_cells(soup))

    print(master_list)

if __name__ == '__main__':
    main()
    
