import pandas as pd
# word = raw_input("What is your Kickstarter name? ")
scrap = pd.read_csv('scraped_kickstarter_data_2.csv')
# # print word, scrap

# for index, row in scrap.iterrows():
#     loop.append(row[row[0].split() == word])
# print loop

loop = []
word = raw_input("What is your Kickstarter name? ")
for index, row in scrap.iterrows():
    if word in row[0].split():
        loop.append(row)
out = loop[0]
print out
# from IPython.display import Image, HTML
# HTML(out.to_html('search.html', escape=False, classes=['table', 'table-responsive',
#                                                                                'table-hover']))