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

def select_choice(df : pd.DataFrame, choice : str) -> pd.DataFrame :
    """
    Return only rows that matches the given choice in the DataFrame

    Args:
        df (pd.DataFrame): DataFrame containing all values in the tsv file
        choice (str): str name in the first column of the DataFrame

    Returns:
        pd.DataFrame: DataFrame containing only values with name choice 
    """
    return df.loc[df["Goal"] == choice]

def dataframe_to_list(df : pd.DataFrame) -> list:
    """
    Return a list of all urls wanted

    Args:
        df (pd.DataFrame): DataFrame containing only values with name choice

    Returns:
        list: list of all urls wanted
    """
    df_right_urls = df['Url']
    return df_right_urls.tolist()

def open_urls_websites(urls_list : list):
    """
    Open websites thanks to the urls list

    Args:
        urls_list (list): list of urls wanted
    """
    for url in urls_list:
        wb.open(url)

# Display url using the default browser
# url = 'https://www.codebreakthrough.com/python-bootcamp/'
# wb.open(url)

### Open a website in a new window with the firefox browser 
# wb.get('firefox').open_new(url)

### Open a website in a new page with the firefox browser 
# wb.get('firefox').open_new_tab(url)

def main(path, filename, choice):
    op_web = OpenWebsitesWithFile(path, filename, choice)
    if check_file_exists(op_web.get_path(), op_web.get_filename()):
        df = read_tsv_websites_file(op_web.get_path(), op_web.get_filename())
    df_rows = select_choice(df, op_web.get_choice())
    urls_choice_list = dataframe_to_list(df_rows)
    open_urls_websites(urls_choice_list)

if __name__ == "__main__":
    args = construct_parameters()
    main(args.path, args.filename, args.choice)
    
