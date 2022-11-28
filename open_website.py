from os.path import isfile
import webbrowser as wb

def check_file_exists(path: str) -> bool:
    """
    Check if file exists with a good path

    Args:
        path (str): Absolute path with name file to check

    Raises:
        FileExistsError: Error with the path or the name of the file

    Returns:
        bool: True if file exists, FileExistsError otherwise
    """
    if isfile(path):
        print("The file exists")
        return True
    else:
        raise FileExistsError("It's not a file, we can't open it")

# TESTING check_file_exists
print(check_file_exists("/home/jacky/projects/OpenWebsitesInterest/list_websites.txt"))
print(check_file_exists("/home/jacky/projects/OpenWebsitesInterest/list_websites.tx"))

# Display url using the default browser
# url = 'https://www.codebreakthrough.com/python-bootcamp/'
# wb.open(url)

### Open a website in a new window with the firefox browser 
# wb.get('firefox').open_new(url)

### Open a website in a new page with the firefox browser 
# wb.get('firefox').open_new_tab(url)