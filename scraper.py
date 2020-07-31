from helpers import *

import matplotlib.pyplot as plt




items = get_items("https://dhs.kerala.gov.in/%E0%B4%A1%E0%B5%86%E0%B4%AF%E0%B4%BF%E0%B4%B2%E0%B4%BF-%E0%B4%AC%E0%B5%81%E0%B4%B3%E0%B5%8D%E0%B4%B3%E0%B4%B1%E0%B5%8D%E0%B4%B1%E0%B4%BF%E0%B4%A8%E0%B5%8D%E2%80%8D/")
data=[]
for item in items[0:7]:
    pdf_link=get_doc_link(item[1])
     
    download_pdf(pdf_link,"out.pdf")    
    try:
        cases_per_day=data_extractor("out.pdf")
    except:
        continue
    print(item[0],cases_per_day)
    data.append(cases_per_day)
plt.plot(data)
plt.show()

# data=[]
# for item in items[:5]:
#     print(item)
#     pdf_link=get_doc_link(item[1])
    
#     download_pdf(pdf_link,"out.pdf")
#     try:
#         cases_per_day=data_extractor("out.pdf")
#     except:
#         continue
#     print(item[0],cases_per_day)
#     data.append(cases_per_day)
    
# plt.plot(data)
# plt.show()



