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
        SequencesToSPSS.py -i reads.fasta -g genome.fasta [-t] x [-k] y
        
        [-i (required): Input the fasta file containing your reads.]
        [-g (required): Input the fasta file containing your reference genome.]
        [-t (optional [2]): Input x = the solidity threshold you want to use.]
        [-k (optional [31]): Input y = the k-mer size you want to use.]
        
    '''

def construct_parameters():
    parser = argparse.ArgumentParser(
        add_help=False,
        usage=help_msg(),
        description="Compressed representation and indexing\
            of a set of k-mers extracted from sequencing data.")
    parser.add_argument("-i",
                        "--reads",
                        metavar='',
                        help="fasta file containing a set of reads",
                        dest='reads',
                        type=str,
                        required=True)
    parser.add_argument("-g",
                        "--genome",
                        metavar='',
                        help="fasta file containing a reference genome",
                        dest='genome',
                        type=str,
                        required=True)
    parser.add_argument("-t",
                        "--solidity_threshold",
                        metavar='',
                        help="solidity threshold (kmers occurring less than t\
                            times are not extracted) (default=2)",
                        dest='solid_t',
                        type=int,
                        required=False,
                        default=2)
    parser.add_argument("-k",
                        "--kmer_size",
                        metavar='',
                        help="kmer size (default=31)",
                        dest='k_size',
                        type=int,
                        required=False,
                        default=31)

    args = parser.parse_args()
    return args