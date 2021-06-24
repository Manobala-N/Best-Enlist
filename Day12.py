#!/usr/bin/env python
# coding: utf-8

# In[14]:


f =open("30_days_30_hour_operations.txt","w+")
f.write("I have completed 10 days successfully")
f.close()
f1 =open("30_days_30_hour_operations.txt","a+") 
f1.writelines(" Manobala.N")
f1 =open("30_days_30_hour_operations.txt","r") 
print(f1.read())
f1.close()

#OUTPUT
#I have completed 10 days successfully Manobala.N ECE

