from os.path import exists
import webbrowser as wb

class OpenWebsitesWithFile :
    def __init__(self, path : str = "", filename : str = "", website_dict : dict = {}, function_website_link_dict : dict = {}):
        self.path = path
        self.filename = filename
        self.website_dict = website_dict
        self.function_website_link_dict = function_website_link_dict

    def check_file_exists(self, path: str, filename: str) -> bool:
        """
        Check if a file with its local path exists

        Args:
            path (str): local path
            filename (str): name of the file

        Returns:
            bool: True if file exists, False otherwise
        """
        return exists(f"{path}/{filename}")

# Display url using the default browser
# url = 'https://www.codebreakthrough.com/python-bootcamp/'
# wb.open(url)

### Open a website in a new window with the firefox browser 
# wb.get('firefox').open_new(url)

### Open a website in a new page with the firefox browser 
# wb.get('firefox').open_new_tab(url)