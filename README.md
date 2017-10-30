# find_political_donors
A Python package to return statistical data on political donors, given input data from the FEC:
http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml

## Prerequisites
* Python3
* pip3
* virtualenv

## External Modules
* py
* pytest
* sortedcontainers

## Installation Instructions
1. Clone this repository
2. cd into the top level of the directory with this repository
3. Create a new virtualenv for python3:
```
virtualenv -k python3 venv
```
4. Activate the virtualenv:
```
source venv/bin/activate
```
5. Install the external module requirements:
```
pip3 install -r requirements.txt
```
## Usage
find_political_donors expects three arguments. A shell script has been provided in the top level to run find_political_donors with default filenames. To use, type:
```
./run.sh
```

The contents of run.sh are as follows:
```
python -m src ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt
```

The first argument is the input file, the second is the output file for data sorted by recipient and zip code, and the third is the output file for data sorted by recipient and date. These can be changed as desired.

## Input
The input file is expected to be a pipe-delimited file following the data dictionary convention listed here:
http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml

## Output
medianvals_by_zip.txt contains a pipe-delimited file with the following fields:
* recipient of the contribution
* 5-digit zip code of the contributor (or the first five characters of the ZIP_CODE field from the input file)
* running median of contributions received by recipient from the contributor's zip code, rounded to the nearest dollar
* total number of transactions received by recipient from the contributor's zip code
* total amount of contributions received by recipient from the contributor's zip code

medianvals_by_date.txt contains a pipe-delimited file with the following fields:
* recipient of the contribution
* date of the contribution
* median of contributions received by recipient on that date, rounded to the nearest dollar
* total number of transactions received by recipient on that date
* total amount of contributions received by recipient on that date

## Tests
In addition to the test within the insight_testsuite, multiple unit tests have been provided to test each individual method in all modules. These unit tests are available within the pytest_testsuite directory. To run them, within the top_level directory, run:
```
pytest pytest_testsuite/*
```

## Expected Runtime
This code has been tested on all contributions provided for 2017, a text file of roughly ~800 MB. The code takes around 1 minute to complete.