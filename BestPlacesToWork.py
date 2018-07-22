#Made by Arman Lokhandwala 07/2018
from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup
import time



def main():
    file = open('PlacesToApply.csv', 'w')
    header = ", Company, Rank last year, Years on list, HQ location, Employees, Job openings, Industry, Revenue, Year Founded, Type of organization, Number of work sites, Website, Number of Perks, Perks \n ,"
    file.write(header)
    company = "/best-companies/salesforce/"
    count = 0
    while count < 100:
        data_to_write, company = GetCompanyInfo("http://fortune.com/" + company)
        if company == "/best-companies/atlantic-health-sytstem/":
            company = "/best-companies/hyland/"
        print(count,company)
        for entry in data_to_write:
            if (',') in entry:
                # index = line_to_write.index(entry)
                # line_to_write.remove(entry)
                entry = entry.replace(',', '')
                # line_to_write.insert(index, entry)
            file.write(entry + ",")
            # file.write(str(line_to_write))
        count+=1

def GetCompanyInfo(url):

    page_to_read = urlopen(url)

    soup =  Soup(page_to_read, "html.parser")
    line_to_write = []

    line_to_write.append(soup.find('h1').text)

    info_to_parse = soup.findAll("p", {"class":"remove-bottom-margin"})
    website = soup.find("div", {"class":"columns small-9 medium-6 company-info-card-data"}).text

    size_of_info_table = len(info_to_parse)
    i = 0
    while i+1 < size_of_info_table:
        #((info_to_parse[i].text + ": " + info_to_parse[i+1].text))
        line_to_write.append(info_to_parse[i+1].text)
        i+=2
    line_to_write.append(website)


    perks = (soup.find("div", {"class":"list"}).find_all("div", {"class":"title"}))
    number_of_perks = len(perks)
    line_to_write.append(str(number_of_perks))
    perks_list = []
    for perk in perks:
        perks_list.append(perk.text)

    line_to_write.append(str(perks_list) + "\n")

    found_div = soup.find_all("div",{"class":"nav-button"})
    if len(found_div) > 1:
        found_div = found_div[1]
    else:
        found_div = found_div[0]
    next_page = found_div.find('a')['href']

    # for entry in line_to_write:
    #     if (',') in entry:
    #         # index = line_to_write.index(entry)
    #         # line_to_write.remove(entry)
    #         entry = entry.replace(',', '')
    #         # line_to_write.insert(index, entry)
    #     file.write(entry + ",")
    # #file.write(str(line_to_write))
    page_to_read.close()

    return line_to_write, next_page

start = time.time()
main()
print("Time taken: " + "{0:.2f}".format(time.time() - start) + " seconds")