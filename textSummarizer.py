from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import csv

fname = "./InputTextSummarization.txt"
fname2 = "./InputAnnualReport.csv"

records=[]
element = ""
i=0
with open(fname2, 'rt') as f:

    contents = csv.reader(f)
    for row in contents:
        # for element in row:
            
        text = row[2]
        i +=1
        print('Summary : ')
        print(summarize(text, word_count = 100))
        # print(text, i)





# with open(fname, 'r') as myfile:
#     text1 = myfile.read()

# print('Summary : ')
# print(summarize(text1, word_count = 100))

