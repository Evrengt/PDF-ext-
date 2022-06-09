#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tabula-py --force-reinstall --user


# In[2]:


import tabula
import pandas as pd


# In[3]:


pdf_in = "c:/siftah/YPL Nisan 2022 Dağılım Raporu.pdf"


# In[4]:


PDF = tabula.read_pdf(pdf_in, pages='all', multiple_tables=True)


# In[5]:


print ('\nTables from PDF file\n'+str(PDF))


# In[6]:


pdf_out_xlsx = "C:\siftah\From_PDF.xlsx"
pdf_out_csv = "C:\siftah\From_PDF.csv"


# In[7]:


tabula.convert_into("YPL Nisan 2022 Dağılım Raporu.pdf", "YPL Nisan 2022 Dağılım Raporu.csv", output_format="csv", pages='all')
print(df)


# In[ ]:


PDF = pd.DataFrame(PDF)
PDF.to_excel(pdf_out_xlsx,index=False) 


# In[9]:


tabula.convert_into (input_PDF, pdf_out_csv, pages='all',multiple_tables=True)
print("Done")

