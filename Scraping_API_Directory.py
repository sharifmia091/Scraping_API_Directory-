#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import pandas as pd



np_api ={}
no_api = 0
i=0


while i<=753:
    
    url_text =  "https://www.programmableweb.com/apis/directory/api"+"?page="+str(i)
    
    response = requests.get(url_text)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    apis_odd= soup.find_all("tr", {"class","odd"})
    apis_even= soup.find_all("tr", {"class","even"})
    apis = apis_odd + apis_even
    i+=1
        

    for api in apis:
        api_name_tag = api.find("td",{"class":"views-field views-field-title col-md-3"})
        api_name = api_name_tag.text.strip() if api_name_tag  else "N/A"


        descrip_tag = api.find("td",{"class":"views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8"})
        descrip =  descrip_tag.text.strip() if api_name_tag  else "N/A"

        category_tag = api.find("td", {"class":"views-field views-field-field-article-primary-category"})
        category =category_tag.text.strip() if category_tag else "N/A"

        url_n =api.find("a").get("href")
        url_f ="https://www.programmableweb.com"+url_n

        date_tag = api.find("td", {"class":"views-field views-field-created"})
        date = date_tag.text.strip() if date_tag else "N/A"

        no_api +=1
        np_api[no_api] = [api_name,descrip,category,url_f, date]

        #print('API No: ', no_api, '\n\napi_name:',api_name, '\n\nDescrip:',descrip, '\n\ncategory:',category, '\n\nLink:',url_f, '\n\nDate:',date,'\n---')

    
        
print("Total api:", no_api)

no_api_df = pd.DataFrame.from_dict(np_api,orient = 'index', columns = ['API Name','Description','category', 'Link', 'Sub Date'])

no_api_df.head()
#no_api_df.to_csv('no_api_df_sharif_2.csv')




# In[ ]:





# In[ ]:




