import requests
import subprocess
import sys, getopt
import numpy
import pandas as pd
from bs4 import BeautifulSoup



def scrap_data():
    """
    DOCSTRING: Scarps data from https://www.kernal.org/ and turns the kernal table on website into a dataframe and returns it
    returns: pandas.Dataframe()
    """
    URL = "https://www.kernel.org/"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="releases")

    rows = results.find_all("tr")

    data = []
    for row in rows:
        cols = row.find_all("td")
        once_completed = False
        for element in cols:

            a_tag = element.findChild("a")
            if a_tag:
                if (once_completed):
                    pass
                else:
                    data.append(a_tag.get("href"))
                once_completed = True

            else:
                data.append(element.text.strip())

    data = [ele for ele in data if ele]
    
    pd.options.display.max_colwidth = 200
    df = pd.DataFrame(
        columns=['Type', 'Name', 'Release Date', 'Downlod Link'])
    mover = 0
    for i in range(9):
        df.loc[i] = [data[i + mover]] + [data[i + mover + 1]] + \
            [data[i + mover + 2]] + [data[i + mover + 3]]
        mover += 3

    #item = df.loc['Download Link']
    #print(type(item))
    #print(item)
    return df

def main(argv):

    try:
        opts, args = getopt.getopt(argv,"hsid:",["help", "download", "download_latest"])

    except getopt.GetoptError:
        print("Press -h or --help for help")
        sys.exit(2)
    for opt, arg, in opts:

        if opt in ('-h', '--help'):
            print("Press -d and the number to download specfic kernal image")
            print(scrap_data())

            print('\n\n\n-i,    --download_latest_stable,        Downloads and installs latest stable kernal')
            print('-h,  --help,         Print this help menu')
            sys.exit()

        elif opt in ('-i', '--download_latest_stable'):
            temp_df = scrap_data()
            stable_row = temp_df.loc[1, :]
            print(stable_row)
            download_link = str(stable_row.iloc[3])
            subprocess.run(['wget', download_link])
if __name__ == "__main__":
    main(sys.argv[1:])
