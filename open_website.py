from os.path import isfile
import webbrowser as wb

def check_file_exists(path: str) -> bool:
    if isfile(path):
        print("The file exists")
        return True
    else:
        return False

# Display url using the default browser
url = 'https://www.codebreakthrough.com/python-bootcamp/'
wb.open(url)

### Open a website in a new window with the firefox browser 
# wb.get('firefox').open_new(url)

### Open a website in a new page with the firefox browser 
# wb.get('firefox').open_new_tab(url)