# html-uri-crawler

A randomized web crawler that collects unique HTML URIs that are larger than 1000 bytes, starting from a given seed page.

<br />


# Project Overview

This program is an improved version of the CS432: Web Science - Homework 1, Question 3 randomized web crawler implementation originally created by Prof. Nasreen Arif at Old Dominion University.
It was enhanced to provide better error handling, user interaction, and link filtering.

The crawler starts from a single seed URI and continues to discover and follow random hyperlinks obtained from a previously crawled page until a specified number of valid, unique HTML pages are collected.


## Original Assignment Requirements

* Take the URI of a seed webpage as a command-line argument.
* Extract all the links from the page's HTML.
* For each link, request the URI and use the `Content-Type` HTTP response header to determine if the link references an HTML file (`text/html`);
    * if it does, use the `Content-Length` HTTP response header to determine if it contains more than 1000 bytes
       * if it does, then print the final URI (after any redirects) 
* Must use BeautifulSoup4 and Regex as demonstrated in lecture.
* Randomly select discovered hyperlinks to continue crawling.
* Collect a specified number of unique HTML URIs.
* Ensure collected pages are text/html and larger than 1000 bytes.


## Added Improvements

* **File saving** - Collected URIs are saved in a text document the user names during execution and automatically adds the proper file extension if not included by the user.
* **Error handling** — Skips unreachable or invalid pages instead of crashing.
*  **Content filtering** — validates Content-Type and Content-Length headers to ensure only full HTML pages are included.
* **Dynamic crawling** — Uses a queue and random selection for more organic traversal of the web graph.
*  **Regex-based validation** — ensures only proper HTTP/HTTPS URIs are collected.
* **Progress reporting** — displays number of links found and how many are still needed until completion.
  

<br />


# Getting Started
## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a Windows/Linux/MacOS system with Python installed
* You have installed the required libraries with: 

        pip install requests beautifulsoup4


## Installing

* To install this program, clone or download this repository:

        git clone https://github.com/emxily/html-uri-crawler.git
* Then, navigate into the project directory:

        cd html-uri-crawler


## Executing program

* To run the program from the terminal:

        python.exe .\html-uri-crawler.py <seed_URI> <number_of_links>



### <u>Example Output</u>

```python.exe .\html-uri-crawler.py https://www.odu.edu 100```
```
Seed URI: https://www.odu.edu/
Found: 48 links Need: 52 more links
        Grabbing random seed. . .

Seed URI: https://www.evms.edu/education/school_of_medicine/
Found: 68 links Need: 32 more links
        Grabbing random seed. . .

Seed URI: https://online.odu.edu/summer-studies
Found: 99 links Need: 1 more links
        Grabbing random seed. . .

Seed URI: https://catalog.odu.edu/
Found: 100 links        Enough links found!

Save the file containing the links as:

A list of all the unique URIs grabbed has been saved to Crawled-Links.txt
```


<br />


# Version History

* 0.1
    * Initial Release

*This program was tested and developed on Windows 10+ using Python 3.13.9*


<br />


# Authors

**Author:** Emily Nowak

*Based on **"Homework 1 - Web Science Intro."** by **Prof. Nasreen Arif** for CS:432 Web Science, at Old Dominion University* 


<br />



# Acknowledgments

## Original Assignment

[HW1 - Web Science Intro. - Question 3 Original Instructions](https://github.com/emxily/html-uri-crawler/blob/cec0cd57c59a0b7e5bf42890bf14d824860829a8/original-assignment-intructions.md)

* ***Note:**  Only Question 3 applies to this program implementation.*

## References
* Markdown Syntax: <https://www.markdownguide.org/basic-syntax/#headings>
* HTML Syntax: <https://www.w3schools.com/tags>
* Beautiful Soup Documentation: <https://www.crummy.com/software/BeautifulSoup/bs4/doc>
* Regex for http/https: <https://stackoverflow.com/questions/4643142/regex-to-test-if-string-begins-with-http-or-https>
