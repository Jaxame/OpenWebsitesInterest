from os.path import exists
from arguments import construct_parameters
import pandas as pd
import webbrowser as wb

class OpenWebsitesWithFile :
    def __init__(self, path : str = "", filename : str = "", choice : str = "default") :
        self.path = path
        self.filename = filename
        self.choice = choice

    # ACCESSORS
    def get_path(self):
        return(self.path)

    def get_filename(self):
        return(self.filename)

    def get_choice(self):
        return(self.choice)

    # MUTATORS
    def set_path(self, new_path):
        self.path = new_path

    def set_filename(self, new_filename):
        self.filename = new_filename

    def set_choice(self, new_choice):
        self.choice = new_choice
        
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

def read_tsv_websites_file(path: str, filename : str) -> pd.DataFrame:
    """
    Return a DataFrame containing the information about the TSV website file

    Args:
        path (str): local path
        filename (str): name of the file

    Returns:
        pd.DataFrame: DataFrame of the file contents with 3 columns (Goal, Name and Url)
    """
    file = f"{path}/{filename}"
    return pd.read_csv(file, sep='\t', header = None, names=['Goal', 'Name', 'Url'])

# Display url using the default browser
# url = 'https://www.codebreakthrough.com/python-bootcamp/'
# wb.open(url)

### Open a website in a new window with the firefox browser 
# wb.get('firefox').open_new(url)

### Open a website in a new page with the firefox browser 
# wb.get('firefox').open_new_tab(url)

def main(path, filename, choice):
    tsv_file = OpenWebsitesWithFile(path, filename, choice)
    if check_file_exists(tsv_file.get_path(), tsv_file.get_filename()):
        df = read_tsv_websites_file(tsv_file.get_path(), tsv_file.get_filename())
    df_rows = df.loc[df["Goal"] == choice]
    df_right_urls = df_rows['Url']
    url_list = df_right_urls.tolist()
    for url in url_list:
        wb.open(url)

    


if __name__ == "__main__":
    args = construct_parameters()
    main(args.path, args.filename, args.choice)
    # TEST
    # PATH = "/home/jacky/projects/OpenWebsitesInterest/"
    # ERROR_PATH = ""
    # ERROR_PATH2 = "/home/jacky/projects/"
    # FILENAME = "list_websites.txt"
    # ERROR_FILENAME = ""
    # ERROR_FILENAME2 = "notexistfile.txt"
    # good_variables = OpenWebsitesWithFile(PATH, FILENAME)
    # err_variables = OpenWebsitesWithFile(PATH, ERROR_FILENAME)
    # err2_variables = OpenWebsitesWithFile(PATH, ERROR_FILENAME2)
    # err3_variables = OpenWebsitesWithFile(ERROR_PATH, FILENAME)
    # err4_variables = OpenWebsitesWithFile(ERROR_PATH2, FILENAME)
    # err5_variables = OpenWebsitesWithFile(ERROR_PATH, ERROR_FILENAME)
    # err6_variables = OpenWebsitesWithFile(ERROR_PATH, ERROR_FILENAME2)
    # err7_variables = OpenWebsitesWithFile(ERROR_PATH2, ERROR_FILENAME)
    # err8_variables = OpenWebsitesWithFile(ERROR_PATH2, ERROR_FILENAME2)
    # print(check_file_exists(good_variables.get_path(), good_variables.get_filename()))
    # print(check_file_exists(err_variables.get_path(), err_variables.get_filename()))
    
