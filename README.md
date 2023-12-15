This repo is part of the BIoinformatics and Data-Analysis POwer TOols collection: [BiDaUxPoTo](https://github.com/bidauxpoto)

# Installation
```
conda install -c molinerislab tabular_data_manipulation
```

# Tools 
This repo contains 3 tools

## fasta2tab
```
fasta2tab [-s|--single-line] <FASTA >TAB
	-s write each sequence on a single line
```
## fasta2tab
```
Usage: 
		tab2fasta.py <TAB >FASTA
		
		Transforms a tab-delimited file with two columns into a FASTA file;
		each row in the input is converted into a FASTA block.
	

Options:
  -h, --help            show this help message and exit
  -s, --already_sorted  assume input already sorted on firs column.
```

# tab2matrix
```
Usage: 
        tab2matrix.py [OPTIONS]
        
        .META: stdin
            1 id1
            2 id2
            3 val

        Builds a weighted incidence matrix out of a map file.
    

Options:
  -h, --help            show this help message and exit
  -c COLUMNS, --columns=COLUMNS
                        add columns to the matrix using as their labels those
                        specified in COLUMNS - a space separated list (in
                        single or double quotes). Values will be NA [default:
                        none]
  -w ROWS, --rows=ROWS  add rows to the matrix using as their labels those
                        specified in COLUMNS - a space separated list (in
                        single or double quotes). Values will be NA [default:
                        none]
  -C COLUMNS, --columns_from_file=COLUMNS
                        same as -c but takes the list from file [default:
                        none]
  -s, --sorted          assume the input block sorted on the first column
                        (memory efficient) [default: False]
  -S, --sorted_column_out
                        columns are reported in lexicographic order [default:
                        True]
  -k, --kill            kill columns not reported in -c or -C [default: False]
  -i, --assume_sorted   do not check for lexicographic sorting of first column
                        [default: False]
  -t, --transpose       transpose the output matrix [default: False]
  -e MISSING_VALUES, --missing_values=MISSING_VALUES
                        specify the string used in place of missing values
                        [default: NA]
  -r ROW_ID, --row_id=ROW_ID
                        the label used for the first column in the header
                        [default: >ROW_ID]
```
