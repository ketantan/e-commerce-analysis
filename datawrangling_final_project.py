#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import sqlite3
import pandas as pd
import seaborn as sns


# In[2]:


#objective
#mencari tahu best and least performing products
#mendapatkan rekomendasi / follow-up actions dari hasil analisa tersebut.

#bikin koneksi ke db file
con = sqlite3.connect("olist.db")

#masukin dataset ke dataframe
df_geo = pd.read_sql_query("SELECT * FROM olist_geolocation_dataset", con)
df_sell = pd.read_sql_query("SELECT * FROM olist_sellers_dataset", con)
df_cust = pd.read_sql_query("SELECT * FROM olist_order_customer_dataset", con)
df_prod = pd.read_sql_query("SELECT * FROM olist_products_dataset", con)
df_order = pd.read_sql_query("SELECT * FROM olist_order_dataset", con)
df_order_items = pd.read_sql_query("SELECT * FROM olist_order_items_dataset", con)
df_order_pay = pd.read_sql_query("SELECT * FROM olist_order_payments_dataset", con)
df_order_rev = pd.read_sql_query("SELECT * FROM olist_order_reviews_dataset", con)
df_prod_name = pd.read_sql_query("SELECT * FROM product_category_name_translation", con)


# In[3]:


#cek isi dataframe
df_geo.head()


# In[4]:


df_sell.head()


# In[36]:


df_cust.head()


# In[6]:


df_prod.head()


# In[7]:


df_order.head()


# In[8]:


df_order_items.head()


# In[9]:


df_order_pay.head()


# In[10]:


df_order_rev.head()


# In[11]:


df_prod_name.head()


# In[12]:


#cek missing value
df_geo.isna().sum()


# In[13]:


df_sell.isna().sum()


# In[14]:


df_prod.isna().sum()


# In[15]:


df_prod.loc[df_prod["product_category_name"].isna()]
#banyak missing data, tapi karena ini table master, cukup sensitif untuk dihapus atau diedit.


# In[16]:


df_order.isna().sum()
#tanggal pengiriman tidak dihapus karena tergantung dari status ordernya


# In[17]:


df_order_items.isna().sum()


# In[18]:


df_order_pay.isna().sum()


# In[19]:


df_order_rev.isna().sum()


# In[20]:


df_prod_name.isna().sum()


# In[21]:


#cek outlier
df_order_items.describe()


# In[22]:


sns.histplot(data=df_order_items, x = "price", bins = 100)


# In[23]:


#batas atas data
batas_atas = df_order_items["price"].quantile(q=0.75) * 1.5

#nilai median
median_price = df_order_items["price"].median()

#mengubah nilai outlier dengan median
df_order_items.loc[df_order_items["price"] > batas_atas, "price"] = median_price


# In[24]:


sns.histplot(data=df_order_items, x = "price", bins = 100)


# In[25]:


sns.histplot(data=df_order_items, x = "freight_value", bins = 100)


# In[26]:


#batas atas data
batas_atas_freight = df_order_items["freight_value"].quantile(q=0.75) * 1.5

#nilai median
median_freight = df_order_items["freight_value"].median()

#mengubah nilai outlier dengan median
df_order_items.loc[df_order_items["freight_value"] > batas_atas_freight, "freight_value"] = median_freight


# In[27]:


sns.histplot(data=df_order_items, x = "freight_value", bins = 100)


# In[28]:


#cek duplikat
df_order_items[df_order_items.duplicated(keep=False)]


# In[29]:


#cek konsistensi format
df_prod["product_category_name"].unique()


# In[31]:


df_prod["product_category_name"].value_counts()


# In[32]:





# In[35]:


#gak sempet lagi T_T
df_geo.to_csv("bigh_geo.csv")
df_sell.to_csv("bigh_seller.csv")
df_cust.to_csv("bigh_customer.csv")
df_prod.to_csv("bigh_product.csv")
df_order.to_csv("bigh_order.csv")
df_order_items.to_csv("bigh_order_items.csv")
df_order_pay.to_csv("bigh_order_pay.csv")
df_order_rev.to_csv("bigh_order_rev.csv")
df_prod_name.to_csv("bigh_product_name.csv")

