import requests                                                                                                 #Library for sending HTTP requests to fetch web pages
from bs4 import BeautifulSoup                                                                                   #Library for parsing and extracting data from HTML documents
import random                                                                                                   #Library for generating random selections
import sys                                                                                                      #Library for accessing command-line arguments and interacting with the system
import re                                                                                                       #Library for using regular expressions to match patterns in strings

#Run the command: py.exe .\html-uri-crawler.py {starting seed URI} {number of links wanted}

def findLinks(seedURl, targetAmount):                           
    '''
    Definition for a function that collects the desired amount of web pages starting from a seed URL.

    Args:
        seedURl (str): The starting HTML seed used for crawling.
        targetAmount (int): The total number of HTML links to collect.

    Returns:
        collectedLinks (set): A set of unique HTML URIs collected during the crawl.
    '''
    collectedLinks = set([seedURl])                                                                             #Set is used to store unique pages
    queue = [seedURl]                                                                                           #Queue of links waiting to be processed
    pattern = re.compile(r'^https?://.+', re.IGNORECASE)                                                        #Regex filters for http/https https://stackoverflow.com/questions/4643142/regex-to-test-if-string-begins-with-http-or-https
    printedEnoughLinksFound = False                                                                             #Tracks whether "enough links found" was printed 

    while queue:                                                                                                #Loop until all links are visited
        if len(collectedLinks) >= targetAmount:                                                                 #When the set has the required number of links. . .
            break                                                                                               #Stop visiting links

        currentLink = random.choice(queue)                                                                      #Pick a random link in the queue
        queue.remove(currentLink)                                                                               #Remove it so it isn't selected again
        
        try:

            response = requests.get(currentLink, allow_redirects=True, timeout=5)                               #Request the page, allowing redirects
            contentType = response.headers.get("Content-Type", "")                                              #Get content type
            contentLength = response.headers.get("Content-Length")                                              #Get content length
            
            if "text/html" in contentType and (contentLength is None or int(contentLength) > 1000):             #Only keep pages that are HTML and larger than 1000 bytes
               
                soup = BeautifulSoup(response.text, "html.parser")                                              #Parse the HTMl and extract all <a href=""> links

                linksFound = 0                                                                                  #Counts the number of links produced from the seed

                for link in soup.find_all("a"):                                                                 #Loop through all hyperlinks
                    href = link.get("href")                                                                     #Extract the href attribute
                    if not href:                                                                                #If there isn't a href attribute. . .
                        continue                                                                                #Skip

                    m = pattern.match(href)                                                                     #Check if href matches the pattern

                    if m:                                                                                       #If it does. . .
                        abs_url = m.group(0)                                                                    #Get the full URL from the match
                        
                        if abs_url not in collectedLinks:                                                       #If the full URL has not been added to the collection already. . .
                            collectedLinks.add(abs_url)                                                         #Add it to the collection
                            queue.append(abs_url)                                                               #Remove it from the queue
                            linksFound+= 1                                                                      #Adds one to the count for every good link found by that seed

                            if len(collectedLinks) == targetAmount:                                             #When the target amount is reached. . .
                                break                                                                           #Stop

                foundCount = len(collectedLinks)                                                                #Holds total amount of links collected so far
                stillNeed = max(0, targetAmount - foundCount)                                                   #Holds number of links needed to still hit the target amount

                print(f"Seed URI: {response.url}")                                                              #Outputs the seed URI used
                
                if stillNeed > 0:                                                                               #If more links are still needed. . .
                    print(f"Found: {foundCount} links\tNeed: {stillNeed} more links")                           #Outputs number of links found by the seed and how many more are needed
                    print("\tGrabbing random seed. . .\n")                                                      #Output that another random seed will be selected

                elif stillNeed == 0 and not printedEnoughLinksFound:                                            #If target amount reached and message not yet printed. . .
                    print(f"Found: {foundCount} links\tEnough links found!\n")                                  #Output that enough links have been found
                    printedEnoughLinksFound = True                                                              #Mark that the message has been printed so it does not repeat
            
            else:                                                                                               #If it’s not valid HTML or is too small. . .                                                                               
                continue                                                                                        #Skip

        except Exception:                                                                                       #If any errors occur. . .
            continue                                                                                            #Skip page

    return collectedLinks                                                                                       #Return all collected links


if __name__ == "__main__":                                                                                      #Start of main function
    if len(sys.argv) < 3:                                                                                       #If required arguments are missing. . .
        print("Usage: py.exe html-uri-crawler.py <seedURI> <number_of_links>")                                  #Show usage
        sys.exit(1)                                                                                             #Exit program

    seedURI = sys.argv[1]                                                                                       #The first command-line argument from the user is the seed URI
    
    try:
        targetAmount = int(sys.argv[2])                                                                         #The second command-line argument from the user is the number of links the user wants to grab
    except ValueError:                                                                                          #If a non-integer number is entered. . .
        print("Error: <number_of_links> must be an integer.")                                                   #Warn user about invalid integer
        sys.exit(1)                                                                                             #Exit program

    collectedLinks = findLinks(seedURI, targetAmount)                                                           #Call the function to start finding links 

    outputFile = input("Save the file containing the links as: ").strip()                                       #Prompt the user to enter a name for the file containing the links

    if not outputFile:                                                                                          #If the user presses Enter with no name. . .
        outputFile = "Crawled-Links.txt"                                                                        #The file is named "Crawled-Links.txt" by default

    elif not outputFile.lower().endswith(".txt"):                                                               #If user-provided name does not end with ".txt"
        outputFile += ".txt"                                                                                    #Automatically append the .txt extension so all output files are consistent

    with open(outputFile, "w", encoding="utf-8") as f:                                                          #Open/create a file in write mode that can handle special characters for the links 
        for url in collectedLinks:                                                                              #For each URL in the collection created
            f.write(url + "\n")                                                                                 #Write it to the file with each link starting on a new line
    
    print()                                                                                                     #Outputs a blank line
    print(f"A list of all the unique URIs grabbed has been saved to {outputFile}")                              #Outputs a message to the terminal once the file is done being written
