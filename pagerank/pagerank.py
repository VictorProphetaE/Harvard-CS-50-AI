import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    #initialization of variables
    probability_dis = {}
    number_links = len(corpus[page])
    tam = len(corpus)
       
    if number_links != 0:
        for i in corpus:
            probability_dis[i] = (1 - damping_factor) / tam
        for i in corpus[page]:
            probability_dis[i] += damping_factor / number_links
    else:
        for i in corpus:
            probability_dis[i] = 1/tam
    return probability_dis


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #initialization of variables
    dictionary_page = {}
    for pages in corpus:
        dictionary_page[pages] = 0
    
    pages = random.choice(list(corpus.keys()))
    #calculation of probability of page, using the transition model to get next page
    for i in range(1,n):
        distribution = transition_model(corpus, pages, damping_factor)
        for j in dictionary_page.keys():
            dictionary_page[j] = ((i-1) * dictionary_page[j] + distribution[j]) / i
        
        pages = random.choices(list(dictionary_page.keys()), list(dictionary_page.values()))[0]    
    
    return dictionary_page

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #initialization of variables
    pages = len(corpus)
    pred_page = {}
    temp = {}
    for i in corpus:
        pred_page[i] = 1/pages
        temp[i] = None
        
    cond = True
    while cond:
        cond = False
        #calculation of the PageRank
        for actual_page in corpus:
            pagerank = (1 - damping_factor) / pages
            for keys, value in corpus.items():
                if value:
                    if keys != actual_page and actual_page in value:
                           pagerank += damping_factor * (pred_page[keys]/ len(corpus[keys]))
                else:
                    pagerank += damping_factor * (pred_page[keys]/ pages)
            
            temp[actual_page] = pagerank
        #verification to break the loop and to see if the iteration don't converge more
        for page in temp:
            dif = temp[page] - pred_page[page]
            if dif > 0.001:
                cond = True
        pred_page = temp.copy()
    
    return pred_page

if __name__ == "__main__":
    main()
