import argparse

###################################

## Argparse & help message setup ##

###################################


def help_msg():
    """
    Customized help message in case of user failing to input a valid command.
    Returns:
        [help]: [description]
    """
    return '''
        To use this script, please respect the following format:
        open_website.py -p /path/of/the/file/ -f file.txt -c job
        
        [-p (required): Path to the tsv file (with 3 columns).]
        [-f (required): Name of the tsv file.]
        [-c (required): Choice of the Goal.]
    '''

def construct_parameters():
    parser = argparse.ArgumentParser(
        add_help=False,
        usage=help_msg(),
        description="Open websites wanted with a tsv file.")
    parser.add_argument("-p",
                        "--path",
                        metavar='',
                        help="Absolute path to the file",
                        dest='path',
                        type=str,
                        required=True)
    parser.add_argument("-f",
                        "--filename",
                        metavar='',
                        help="tsv file containing 3 columns",
                        dest='filename',
                        type=str,
                        required=True)
    parser.add_argument("-c",
                        "--choice",
                        metavar='',
                        help="Choice between value in the first column of your file",
                        dest='choice',
                        type=str,
                        required=True)

    args = parser.parse_args()
    return args