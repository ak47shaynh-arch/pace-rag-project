#first find out if and how it needs to bring the loaded text to this .py file

#for this part i want to use the re module, which has amazing funtions to work with text
#as usual do pip install re 
import re

# lets write a def funtion and pass all the pages through that function
def clean_page_text(text):
    #basically we pass a page to this funtion it should give out the cleaned version


    # lets first remove page numbers (assuming common pattern: "Page 12")
    text = re.sub(r"Page\s+\d+", "", text)

    
    #and then strip extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    
    #ask seniors what all extra needed to be added and add those too 
    #like repeated information

    return text

cleaned_text = [(pg, clean_page_text(txt)) for pg, txt in all_text]
#the all_text is from the loader function