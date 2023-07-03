from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from rest_framework import status
import json
from rest_framework.response import Response
# Create your views here.

class AppData(APIView):
    def get(self,request,pk):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode
        chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
        driver = webdriver.Chrome(options=chrome_options)
        try:
            driver.get(f'https://play.google.com/store/apps/details?id={pk}')
            
            # Find an element by its ID and interact with it
            about_click = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='See more information on About this game']"))
            )
            about_click.click()

            tabel_data = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '''//div[@role='dialog']//div[@class="G1zzid"]'''))
            )
            # tabel_data.text
            scrape_data = tabel_data.text.split('\n')
            l1=[]
            l2=[]
            for i in range(len(scrape_data)):
                if i%2==0:
                    l1.append(scrape_data[i])
                else:
                    l2.append(scrape_data[i])
            
            dict_data = dict(zip(l1,l2))

            print(dict_data)
        except:
            pass
        if dict_data:
            return Response(dict_data,status=status.HTTP_200_OK)
        return Response({'msg':'not found !!'}, status=status.HTTP_400_BAD_REQUEST)

        