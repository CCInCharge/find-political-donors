# find_political_donors
A Python package to return statistical data on political donors, given input data from the FEC:
http://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml

# How it works
For data that is to be grouped by zip code, the data was assumed to be sequentially streaming to the program. Output data was also required to be produced sequentially, and there could be no assumptions made about the sequence in which data was coming in (sorted, grouped, etc). Additionally, a running median (as well as sum and number of contributions) needed to be kept for the incoming data, grouped by recipient and zip code. The naive way to solve this problem is to have a container that stores contribution amounts (say, in a list) for each contribution grouped by recipient and zip code. Then, when a new data row is read in, the transaction amount can be stored in said list. In order to calculate the median, it would then be necessary to sort the list, resulting in O(m log m) run time for every time that a median must be calculated, assuming that m is the number of data points in an indiviudal list. Also, we need to know where in the list to insert the data, as the data is to be grouped by recipient and zip code - at worst, this may be O(n) runtime, assuming that n is the number of rows in the data.

For data that is to be grouped by date, the naive way to solve the problem is to read the entire text file, sort the data by recipient, sort the data by date, then calculate the median for each recipient/date grouping, as well as the sum and number of contributions. Sorting the data by recipient, then sorting the data by date results in two O(n log n) operations, not to mention the need to sort the data in each grouping to calculate the median (O(m log m)).

We notice that, for medianvals_by_zip.txt, we are constantly checking to see if data matches an already existing grouping of recipient and zip code. Additionally, we need an efficient way to calculate the running median. The solution uses a dict to store data, where the key is a string of recipient|zip code, and the value is a MedianHeap data structure (which I wrote). This makes the operation of checking whether or not the recipient and zip code is in our data very quick, an O(1) operation instead of O(n). The MedianHeap data structure is a structure of two heaps (one min-heap, one max-heap) that can be used to very quickly calculate a running median. For each recipient|zip code group, we maintain a max-heap of the lower half of the contribution amounts, and then a min-heap of the upper half of the contribution amounts. If a new value to be added is less than or equal to the root of the max-heap of the lower half, then we add it there. Otherwise, we add it to the min-heap of the upper half. We also rebalance the heaps as necessary to ensure that their sizes are within one at most. Then, the median is simply the average of the two heap roots if the sizes are equal, or the root of the heap with one extra element. We also maintain a running sum any time a new value is added to the MedianHeap. This makes adding elements to the MedianHeap O(log m) runtime, and calculating the median is O(1).

We do something very similar for medianvals_by_date.txt. We are constantly checking to see if data matches an already existing grouping of recipient and date in this case. Additionally, the final output must be sorted by recipient and date. It makes sense to simply keep the data structure in sorted order to prevent the two O(n log n) sort operations at the end. The functionality is very similar to the calculating for medianvals_by_zip.txt, but instead of maintaining a dict of MedianHeaps, we use a SortedDict of MedianHeaps instead. The SortedDict is very similar to a dict, but it maintains keys in sorted order. Then, if we pass data into this dict with keys of recipient|date (where date is in Year Month Day format), then we automatically have the data in sorted order - we then simply pop the values off in sorted order when outputting data to file. The SortedDict comes from a third-party module, but is benchmarked to have a runtime of roughly O(n^1/3) for adding values. Again, calculating the median of a group of data is O(1), due to the use of the MedianHeaps.

Through the use of these data structures, the code scales quite well for large inputs. It has been tested on the FEC data for 2017, which is about 800 MB and has about 2 million lines of code. It completes in about 1 minute on this data set.

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