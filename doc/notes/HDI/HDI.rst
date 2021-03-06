*************************
HOPSTACK Data Interpreter
*************************

New Name System for HHDI and HDISS objects:
----------------------------------------

Example:

::

    "data-string`r-L1-P1-directory`100-111`"

    Data Reference          : "https://something.com/something.tar.gz`r-L1-P1-directory`100-111`"
    URL                     : https://something.com/something.tar.gz
    Parameter               : `r-L1-P1-directory`100-111`
    Parameter Declaration   : `r-L1-P1-directory`
    Parameter Type          : r
    Parameter Settings      : L1-P1
    Return File Type        : directory
    Parameter Type Settings : 100-111


Unix File type Support:
-----------------------

Unix file types:

1. Regular File
2. Directory
3. Symbolic Link
4. Named Pipe
5. Socket
6. Device File
7. Door

* Think about which (if not all) of the file type should be supported.
* How could socket files be of use?

Tunnel Interfaces:
------------------

Tunnel interfaces structures that define the any combination of the number, 
type, and order of files passed between LASOs

Example Scenario: station_1 is expecting to output one fasta file, and one
genbank file. Station_2 expects one fasta file and one genbank file. If 
station_2 gets something else, it will throw an error or warning

Raw Data Handeling:
-------------------

To ways of passing raw data:

1. Unix Pipes/redirects
    * How do you HDIRECTLY pipe the output of the previous station to the
      current station (without saving output into a file)?
2. string via command line
    * use a delimiter and a verified file path

**Tasks for both:**

* build a few default parsers for fasta, fastq, genbank, etc
* build an class to extend to create parsers easily


HOPSTACK Data Interpreter String Syntax (HDISS, HDISS):
========================================================

HDISS Data Strings:
------------------

1. URL with added schemes
2. RAW Data

HDISS Parameters:
----------------

Filter with a python Regex expressoin:

::

    "/datastring/path/thing`r`python-regex-expression`"

Filter by one or more extentions:

::

    "/datastring/path/thing`e`.fasta,.log,.etc`"

    "/datastring/path/thing`e`.fasta .log .etc`"

    "/datastring/path/thing`e`.fasta, .log, .etc`"

Filter by filename one or more substrings:

::

    "/datastring/path/thing`s`subtring, substring1`

Filter by range (looks for a complete numbers in file names):

::

    "/datasrting/path/thing`r`0-100`"

Filter by reference type and Level #: (cannot be used as a list)

::

    "/datasrting/path/`li`level #,file type`" 

File Reference type examples:

* directory, d
* file, f
* symlink, l
* raw-text, r
* tar-archive, t
* bzip2, 2
* zip, z
* gzip, g
* url, u
* pipe, p
* socket, s

**Filter by range unique (throws error or prompt user if not more than one
file in range):**

::

    "/datasrting/path/thing`ru`0-100`"

**Combine Filters:**

::

    "/datasrting/path/thing/`e`.fasta`r`75-94`"

    "/datasrting/path/thing/`r`25-30`r`50-80`"

HOPSTACK Output Formatter HOF:
--------------------------------

HOF is the inverse function of HDI. It takes the output of a station and
converts it into a single string that can be passed to the next LASO.

LASOF would take some output filter parameters defined in HDISS as input. It 
would then use thoes parameters to find the desired output files and create 
symlinks to them all in a neat LASO output directory whoes file path will be
passed to the next LASO in the pipeline.

HDISS Parameter Behavoir Settings:
---------------------------------

::

    `r-d`regex`     -- Only preforms regex on directories
    `r-d-L1`regex`  -- Only prefroms regex on directories in level one of the recursive call stack 
    `r-d-Lr5`regex` -- Same as above but throws errors if level 5 is not reached ('r' stands for required)
    `r-d-L1-P1`     -- Preforms regex on level one and is preformed first ('P' stands for priority)

Custom URL Schemes:
-------------------

* Previous LASO output
* Metro Shared Directory (workspace)

