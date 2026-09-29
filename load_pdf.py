# get the pdf from the seniors first


#first ofall install the pdf plumber and os modules through pip, as : pip install pdfplubmer os
import pdfplubmer
import os
from cleanerf_for_loaded_text import clean_all_pages
def loader(path):
    #first lets check the pdf we are going to work with exists in th esame folder as the .py file
    if not os.path.exists(pdfpath):
        raise FileNotFoundError
        

    #                   the real thing is here
    all_text = []
    with pdfplumber.open(pdfpath) as pdf:
        #we are passing whatever is in pdfpath to the pdfplubmer and playing it with name pdf
        for pagenumber, page in enumerate(pdf.pages, start=1):
            #we can access everithing in the pdf object as .pages, and start=1 for enumerate function which iterates through and passes to variables page number and page
            text =page.extract_text()
            #from the page object obtained from each enumerate iterate, we extract the texts in it
            if text:
                #if there is text existing in the text indeed , we do
                all_text.append((page_num, text))
    final_text=clean_all_pages(all_text)
    return final_text
        
#just for confirmation lets do
print(f"Loaded this many pages succesfully: {len(loader(IS_456_2000.pdf))}")
