from os.path import exists
import webbrowser as wb

class OpenWebsitesWithFile :
    def __init__(self, path : str = "", filename : str = "", website_dict : dict = {}, function_website_link_dict : dict = {}) :
        self.path = path
        self.filename = filename
        self.website_dict = website_dict
        self.function_website_link_dict = function_website_link_dict

    # ACCESSEURS
    def get_path(self):
        return(self.path)

    def get_filename(self):
        return(self.filename)

    def get_website_dict(self):
        return(self.website_dict)

    def get_function_website_link_dict(self):
        return(self.function_website_link_dict)

    # MUTATEURS
    def set_path(self, new_path):
        self.path = new_path

    def set_filename(self, new_filename):
        self.filename = new_filename

    def set_website_dict(self, new_website_dict):
        self.website_dict = new_website_dict

    def set_function_website_link_dict(self, new_function_website_dict):
        self.function_website_link_dict = new_function_website_dict
    

def check_file_exists(path: str, filename: str) -> bool:
    """
    Check if a file with its local path exists

    Args:
        path (str): local path
        filename (str): name of the file

    Returns:
        bool: True if file exists, False otherwise
    """
    if path == "" or filename == "":
        return False
    return exists(f"{path}/{filename}")

# Display url using the default browser
# url = 'https://www.codebreakthrough.com/python-bootcamp/'
# wb.open(url)

### Open a website in a new window with the firefox browser 
# wb.get('firefox').open_new(url)

### Open a website in a new page with the firefox browser 
# wb.get('firefox').open_new_tab(url)

if __name__ == "__main__":
    PATH = "/home/jacky/projects/OpenWebsitesInterest/"
    ERROR_PATH = ""
    ERROR_PATH2 = "/home/jacky/projects/"
    FILENAME = "list_websites.txt"
    ERROR_FILENAME = ""
    ERROR_FILENAME2 = "notexistfile.txt"
    good_variables = OpenWebsitesWithFile(PATH, FILENAME)
    err_variables = OpenWebsitesWithFile(PATH, ERROR_FILENAME)
    err2_variables = OpenWebsitesWithFile(PATH, ERROR_FILENAME2)
    err3_variables = OpenWebsitesWithFile(ERROR_PATH, FILENAME)
    err4_variables = OpenWebsitesWithFile(ERROR_PATH2, FILENAME)
    err5_variables = OpenWebsitesWithFile(ERROR_PATH, ERROR_FILENAME)
    err6_variables = OpenWebsitesWithFile(ERROR_PATH, ERROR_FILENAME2)
    err7_variables = OpenWebsitesWithFile(ERROR_PATH2, ERROR_FILENAME)
    err8_variables = OpenWebsitesWithFile(ERROR_PATH2, ERROR_FILENAME2)
    print(check_file_exists(good_variables.get_path(), good_variables.get_filename()))
    print(check_file_exists(err_variables.get_path(), err_variables.get_filename()))