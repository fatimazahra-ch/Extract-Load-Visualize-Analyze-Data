
from textblob import TextBlob
from telnetlib import EC
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException,TimeoutException

import numpy as np
import pandas as pd
import re

import requests
import csv
import os, random, sys, time


def  facebook(name):
    username='abdeallahmaachi703@gmail.com'
    password='Lang$1991'
    url='https://www.facebook.com/'
    try:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)

        #action = webdriver.ActionChains(driver)
        #pour vider les fichiers---------------------------------------------------------------------------
        mon_fichier = open("fichier.txt", "w", encoding="utf-8")
        mon_fichier.write("")
        mon_fichier.close()

        facebook_dict = {
            "photos": "None",
            "videos": "None",
            "sports": "None",
            "music": "None",
            "books": "None",
            "likes": "None"
        }

        try:
            driver.get(url)
            #etape d'authentification---------------------------------------------------------------------------
            #----------------------------------------------------------------------------------------------------
            driver.find_element_by_id('email').send_keys(username)
            driver.find_element_by_id('pass').send_keys(password)
            driver.find_element_by_id('loginbutton').click()
        except(NoSuchElementException, WebDriverException, StaleElementReferenceException):
            driver.close()
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications" : 2}
            chrome_options.add_experimental_option("prefs",prefs)
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get(url)
            #etape d'authentification---------------------------------------------------------------------------
            #----------------------------------------------------------------------------------------------------
            driver.find_element_by_id('email').send_keys(username)
            driver.find_element_by_id('pass').send_keys(password)
            driver.find_element_by_id('loginbutton').click()
        finally:
            pass
        #etape de recherche---------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------
        wait = WebDriverWait(driver, 30)
        wait.until( EC.presence_of_element_located((By.XPATH,"//input[@data-testid='search_input' or @name='q']")))
        element=driver.find_element_by_xpath("//input[@data-testid='search_input' or @name='q']")
        element.send_keys('bassma maachi')
        driver.find_element_by_xpath("//button[@data-testid='facebar_search_button']").click()
        wait.until( EC.element_to_be_clickable((By.XPATH,"//a[@data-testid='see_more_header-ENTITY_USER-user']")))
        driver.find_element_by_xpath("//a[@data-testid='see_more_header-ENTITY_USER-user']").click()
        #etape de cibler les resultats---------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------
        #wait.until( EC.presence_of_element_located((By.XPATH,"//div[@class='clearfix pbm']")))
        element_from=driver.find_element_by_xpath("//div[@class='clearfix pbm']")

        wait.until( EC.presence_of_element_located((By.XPATH,"//div[@class='_1qkq _1qkx']")))
        element_from1=element_from.find_element_by_xpath("//div[@class='_1qkq _1qkx']")

        wait.until( EC.presence_of_element_located((By.XPATH,"//div[@class='_1yt' or @id='BrowseResultsContainer']")))
        element_from2=element_from1.find_element_by_xpath("//div[@class='_1yt' or @id='BrowseResultsContainer']")
        wait.until( EC.presence_of_element_located((By.XPATH,"//div[@class='_4p2o _87m1']")))
        try:
            wait.until( EC.presence_of_element_located((By.XPATH,"//div[@class='_4p2o _87m1']")))
            wait.until( EC.presence_of_element_located((By.XPATH,"//div[@class='_4p2o _87m1']")))
            list=element_from2.find_elements_by_xpath("//div[@class='_4p2o _87m1']")
        except(StaleElementReferenceException):
            driver.get(driver.current_url)
            list=element_from2.find_elements_by_xpath("//div[@class='_4p2o _87m1']")
        finally:
            pass
        #etape de stockage---------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------
        mon_fichier = open("fichier.txt", "a", encoding="utf-8")
        for i in range(len(list)):
            element_from3=list[i]
            WebDriverWait(driver, 150).until( EC.presence_of_element_located((By.TAG_NAME,"span")))
            spane=(element_from3.find_elements_by_tag_name('span'))[0]
            s_text=spane.text
            mon_fichier.write(s_text+"\n")
            WebDriverWait(driver, 150).until( EC.presence_of_element_located((By.TAG_NAME,"img")))
            image=((element_from3.find_elements_by_tag_name('img'))[0]).get_attribute("src")
            mon_fichier.write(image+"\n")
        mon_fichier.close()
        #etape :choix de profil---------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------
        profile=list[0]
        profile_elem=profile.find_element_by_xpath("//a[@class='_32mo']")
        profile_elem.click()
        print(driver.current_url)
        WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//div[@class='clearfix _ikh _3-8y']")))
        element=driver.find_element_by_xpath("//div[@class='clearfix _ikh _3-8y']")
        element1=element.find_element_by_xpath("//div[@class='_3-96']")
        profile_barre=element1.find_element_by_xpath("//ul[@class='uiList _3-8x _2pic _4kg' or @id='u_0_1n']")
        barre_infos=profile_barre.find_elements_by_tag_name('li')
        print(len(barre_infos))
        #etape :stockage dans le fichier---------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------
        file_infos = open("scrapping.csv", "w", encoding='utf-8')
        try:
            writer = csv.writer(file_infos)
            writer.writerow( ['information-----------------------'] )
            for i in range(len(barre_infos)):
                writer.writerow( [barre_infos[i].text] )
                print(barre_infos[i].text)
            writer.writerow( ['----------------------------------'] )
        finally:
            file_infos.close()
        #etape :about page---------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------------------
        profile_barre=driver.find_element_by_xpath("//div[@class='clearfix' or @id='fbTimelineHeadline']")
        profile_ul=profile_barre.find_element_by_xpath("//ul[@class='_6_7 clearfix' or @id='u_0_12']")
        list=profile_ul.find_elements_by_tag_name('li')
        barre_infos=list[1].find_element_by_tag_name('a')
        barre_infos.click()
        print(driver.current_url)
        #on est dans la page about-----------------------------on va cibler la partir 'mention de j'aime'-----------------
        WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//div[@class='fb_content clearfix'  or @id='content']")))
        body=driver.find_element_by_xpath("//div[@class='fb_content clearfix'  or @id='content']")
        bodyA=body.find_element_by_xpath("//div[@id='mainContainer']")
        bodyB=bodyA.find_element_by_xpath("//div[@class='clearfix'  or @id='contentCol']")
        html = driver.find_element_by_tag_name('html')
        i=1
        while(i<5):
            html.send_keys(Keys.PAGE_DOWN)
            i=i+1

        try:
            WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//div[@id='pagelet_main_column_personal']")))
            bodyC=bodyB.find_element_by_xpath("//div[@id='pagelet_main_column_personal']")
            WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//div[@class='_36d' or @id='timeline-medley']")))
            bodyD=bodyC.find_element_by_xpath("//div[@class='_36d' or @id='timeline-medley']")#fine
            WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//div[@class='_2w3']")))
            bodyDD=bodyD.find_element_by_xpath("//div[@class='_2w3']")
        except(StaleElementReferenceException):
            driver.get(driver.current_url)
            WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//div[@id='pagelet_main_column_personal']")))
            bodyC=bodyB.find_element_by_xpath("//div[@id='pagelet_main_column_personal']")
            WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//div[@class='_36d' or @id='timeline-medley']")))
            bodyD=bodyC.find_element_by_xpath("//div[@class='_36d' or @id='timeline-medley']")#fine
            WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//div[@class='_2w3']")))
            bodyDD=bodyD.find_element_by_xpath("//div[@class='_2w3']")
        finally:
            pass
        #------photos-------------------------------------------------------------------------------------------------------------
        html.send_keys(Keys.PAGE_DOWN)

        try:
            WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//div[@id='pagelet_timeline_medley_photos']")))
            element=bodyDD.find_element_by_xpath("//div[@id='pagelet_timeline_medley_photos']")
            facebook_dict["photos"] = element
            action.move_to_element(element).perform()
        except (NoSuchElementException, WebDriverException, StaleElementReferenceException,TimeoutException):
            print('photos none')
            element = 'None'
        finally:
            pass
        #------videos-------------------------------------------------------------------------------------------------------------
        facebook_dict["videos"] = "None" # Y a pas de block consernant les video
        #-----sports-------------------------------------------------------------------------------------------------------------
        html.send_keys(Keys.PAGE_DOWN)
        try:
            WebDriverWait(driver, 50).until( EC.presence_of_element_located((By.XPATH,"//div[@id='pagelet_timeline_medley_sports']")))
            element=bodyDD.find_element_by_xpath("//div[@id='pagelet_timeline_medley_sports']")
            facebook_dict["sports"] = element
            action.move_to_element(element).perform()
        except (NoSuchElementException, WebDriverException, StaleElementReferenceException,TimeoutException):
            print('sports none')
            element = 'None'
        finally:
            pass

        #-----music-------------------------------------------------------------------------------------------------------------
        i=1
        while(i<5):
            html.send_keys(Keys.PAGE_DOWN)
            i=i+1
        try:
            WebDriverWait(driver, 150).until( EC.presence_of_element_located((By.XPATH,"//div[@id='pagelet_timeline_medley_music']")))
            element=bodyDD.find_element_by_xpath("//div[@id='pagelet_timeline_medley_music']")
            facebook_dict["music"] = element
            action.move_to_element(element).perform()
        except (NoSuchElementException, WebDriverException, StaleElementReferenceException,TimeoutException):
            print('music none')
            element = 'None'
        finally:
            pass

        #-----book-------------------------------------------------------------------------------------------------------------
        i=1
        while(i<5):
            html.send_keys(Keys.PAGE_DOWN)
            i=i+1
        try:
            WebDriverWait(driver, 150).until( EC.presence_of_element_located((By.XPATH,"//div[@id='pagelet_timeline_medley_books']")))
            element=bodyDD.find_element_by_xpath("//div[@id='pagelet_timeline_medley_books']")
            facebook_dict["books"] = element
            action.move_to_element(element).perform()
        except (NoSuchElementException, WebDriverException, StaleElementReferenceException,TimeoutException):
            print('books none')
            element = 'None'
        finally:
            pass    
        #-------ce block pour telecharger la page
        i=1
        while(i<5):
            html.send_keys(Keys.PAGE_DOWN)
            i=i+1
        #-----likes-------------------------------------------------------------------------------------------------------------

        try:
            WebDriverWait(driver, 200).until( EC.presence_of_element_located((By.XPATH,"//div[@id='pagelet_timeline_medley_likes']")))
            element=bodyDD.find_element_by_xpath("//div[@id='pagelet_timeline_medley_likes']")
            facebook_dict["likes"] = element
            action.move_to_element(element).perform()
        except (NoSuchElementException, WebDriverException, StaleElementReferenceException,TimeoutException):
            print('likes none')
            element = 'None'
        finally:
            pass  
        html.send_keys(Keys.PAGE_DOWN)

        if(element !='None'):
            element=element.find_element_by_xpath("//div[@class='_5h60 _30f']")
            WebDriverWait(driver, 400).until( EC.presence_of_element_located((By.XPATH,"//ul[@class='uiList _153e _5k35 _620 _509- _4ki']")))
            list=element.find_element_by_xpath("//ul[@class='uiList _153e _5k35 _620 _509- _4ki']")
            list=list.find_elements_by_tag_name('li')
            print(len(list))
            for i in range(len(list)):
                case=list[i].find_elements_by_tag_name('div')
                print(case[6].text)
                print(case[7].text)
                print('------------')

            file_infos = open("scrapping.csv", "a", encoding='utf-8')
            try:
                fieldnames = ['page_name', 'page_genre']
                writer = csv.DictWriter(file_infos , fieldnames=fieldnames)
                writer.writeheader()
                for i in range(len(list)):
                    case=list[i].find_elements_by_tag_name('div')
                    writer.writerow({'page_name' :case[6].text, 'page_genre' :case[7].text})
                writer.writerow({'page_name' :'-----------------------------------------', 'page_genre' :'-----------------------------------------'})
            finally:
                file_infos.close()
        else:
            print('element is null')
        driver.close()
    except(WebDriverException):
        print('le driver est ferme forcement')
    return facebook_dict


def  linkdin(name):
    browser = webdriver.Chrome('chromedriver.exe')
    wait = WebDriverWait(browser, 30)
    browser.get('https://www.linkedin.com/uas/login')
    username = "fatimazahracharjane@gmail.com"
    password      = "mama&baba:2021"
    search_item   = name
    elementID = browser.find_element_by_id('username')
    elementID.send_keys(username)
    elementID = browser.find_element_by_id('password')
    elementID.send_keys(password)
    elementID.submit()
    wait.until(EC.element_to_be_clickable((By.ID, "nav-typeahead-wormhole")))
    browser.find_element_by_css_selector("div.nav-search-typeahead input").send_keys(search_item)
    browser.find_element_by_css_selector("div.nav-search-typeahead input").send_keys(Keys.ENTER)
    profilesQueued = []
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.name.actor-name")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3.search-results__total")))  # Pour ne pas avoir aucun resultats
    scheight = .1
    while scheight < 1.0:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
        scheight += .1
    try:
        print(browser.find_element_by_css_selector('div.search-result__wrapper').text)
    except(NoSuchElementException):
        print('No div.div.search-result__wrapper')
    finally:
        pass
    profils = browser.find_elements_by_css_selector("div.search-result__wrapper")
    name_location = profils[0].find_element_by_css_selector("span.name.actor-name")
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});", name_location)
    name = name_location.text.encode('utf-8')
    #name = name.lower()
    name = name.decode()
    if search_item in name:
        url_profil = profils[0].find_element_by_css_selector("a.search-result__result-link").get_attribute('href')
        profilesQueued.append(url_profil)
    infoo = {
        "name_linkdin": "None",
        "profile_title_linkdin": "None",
        "loc": "None",
        "information": "None"
    }
    educationn = {
        "college_name": "None",
        "degree_name": "None",
        "degree_year": "None"
    }
    experiencee = {
        "company_name": "None",
        "job_title": "None",
        "joining_date": "None",
        "exp": "None"
    }
    linkdin_dict = {
        "info": "None",
        "education": "None",
        "experience": "None",
        "competences": "None"
    }
    if (len(profilesQueued) == 1):
        fullLink = profilesQueued.pop()
        browser.get(fullLink)
        SCROLL_PAUSE_TIME = 5
        last_height = browser.execute_script("return document.body.scrollHeight")
        # Get scroll height
        for i in range(3):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        ## Info
        soup = BeautifulSoup(browser.page_source, "html.parser")
        name_div = soup.find('div', {'class': 'flex-1 mr5'})
        if name_div is not None:
            name_loc = name_div.find_all('ul')
            if name_loc is not None:
                name = name_loc[0].find('li').get_text().strip()
                loc = name_loc[1].find('li').get_text().strip()
                infoo["name_linkdin"] = name
                infoo["loc"] = loc  
            else:
                name_loc = 'None'
            profile_title = name_div.find('h2').get_text().strip()
            infoo["profile_title_linkdin"] = profile_title
        else:
            name_div = 'None'   

        ##Information
        name_information = soup.find('div', {'class': 'pv-oc ember-view'})
        if name_information is not None:
            content_information = name_information.find('p')
            if content_information is not None:
                content_information = content_information.get_text().strip()
                content_information = content_information.replace('\n','')
                content_information = content_information.replace('voir plus','')
                infoo["information"] = content_information
            else:
                content_information = 'None'
                infoo["information"] = content_information
        linkdin_dict["info"] = infoo


        ## Experience              
        # testExp = exp_section.get_text().strip()
        # info.append(testExp) 
        try:          
            exp_section = soup.find('section', {'id': 'experience-section'})
            try:
                exp_section = exp_section.find('ul')
                try:
                    li_tags = exp_section.find('div')
                    try:
                        a_tags = li_tags.find('a')
                        try:
                            job_title = a_tags.find('h3').get_text().strip()
                        except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                            job_title = 'None'
                        finally:
                            pass
                        experiencee["job_title"] = job_title
                        try:
                            company_name = a_tags.find_all('p')[1].get_text().strip()
                        except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                            company_name = 'None'
                        finally:
                            pass
                        experiencee["company_name"] = company_name
                        try:
                            joining_date = a_tags.find_all('h4')[0].find_all('span')[1].get_text().strip() 
                        except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                            joining_date ='None'
                        finally:
                            pass
                        experiencee["joining_date"] = joining_date
                        try:
                            exp = a_tags.find_all('h4')[1].find_all('span')[1].get_text().strip() 
                        except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                            exp = 'None'
                        finally:
                            pass
                        experiencee["exp"] = exp
                    except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                        a_tags = 'None'
                    finally:
                        pass
                except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                    li_tags = 'None'
                finally:
                    pass
            except (AttributeError, NoSuchElementException, WebDriverException, StaleElementReferenceException):
                exp_section = 'None'
            finally:
                    pass
        except (AttributeError, NoSuchElementException, WebDriverException, StaleElementReferenceException):
            exp_section = 'None'
        finally:
                pass
        linkdin_dict["experience"] = experiencee

        ## Formation
        browser.page_source
        scheight = .1
        while scheight < 1.0:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
            scheight += .1
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section#education-section')))
            try:
                edu_section = browser.find_element_by_css_selector("section#education-section")
                # testExp = edu_section.text
                # info.append(testExp)
                try:
                    college_name = edu_section.find_element_by_css_selector('h3.pv-entity__school-name.t-16.t-black.t-bold').text
                except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                    college_name = 'None'
                finally:
                    pass
                educationn["college_name"] = college_name
                try:
                    degree_name = edu_section.find_element_by_css_selector('p.pv-entity__secondary-title.pv-entity__degree-name.t-14.t-black.t-normal').text
                except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                    degree_name = 'None'
                finally:
                    pass
                educationn["degree_name"] = degree_name
                try:
                    degree_year = edu_section.find_element_by_css_selector('p.pv-entity__dates.t-14.t-black--light.t-normal')
                    degree_year = degree_year.find_element_by_css_selector('span:nth-child(2)').text
                except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                    degree_year = 'None'
                finally:
                    pass
                educationn["degree_year"] = degree_year
            except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                edu_section = 'None'
            finally:
                pass
        except:
            print('No education')
        finally:
            pass
        linkdin_dict["education"] = educationn

        # Competences Professionnelles
        browser.page_source
        scheight = .1
        while scheight < 1.0:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
            scheight += .1
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'section.pv-profile-section.pv-skill-categories-section.artdeco-container-card.ember-view')))
            try:
                competence_section = browser.find_element_by_css_selector('section.pv-profile-section.pv-skill-categories-section.artdeco-container-card.ember-view')
                button_skills = competence_section.find_element_by_css_selector('button.pv-profile-section__card-action-bar.pv-skills-section__additional-skills.artdeco-container-card-action-bar.artdeco-button.artdeco-button--tertiary.artdeco-button--3.artdeco-button--fluid')
                button_skills.send_keys(Keys.ENTER)
                competence_section = browser.find_element_by_css_selector('section.pv-profile-section.pv-skill-categories-section.artdeco-container-card.ember-view')                           
                try:
                    competence_section_1 = competence_section.find_element_by_css_selector('ol.pv-skill-categories-section__top-skills.pv-profile-section__section-info.section-info.pb1')
                    competence_section_1 = competence_section_1.text.split(",")

                except:
                    competence_section_1 = 'None'
                finally:
                    pass
                try:
                    competence_section_2 = competence_section.find_element_by_css_selector('div#skill-categories-expanded')
                    competence_div = competence_section_2.find_element_by_css_selector('div.pv-skill-category-list.pv-profile-section__section-info.mb6.ember-view')
                    competence_ol = competence_div.find_element_by_css_selector('ol.pv-skill-category-list__skills_list.list-style-none')
                    competence_ol = competence_ol.text.split(",")
                    competence_section_1 = competence_ol + competence_section_1
                except:
                    competence_section_2 = 'None'
                finally:
                    pass
            except:
                competence_section = 'None'
                competence_section_1 = 'None'
            finally:
                pass  
        except:
            print('No skills')
            competence_section_1 = 'None'
        finally:
            pass      
        linkdin_dict["competences"] = competence_section_1
    else:
        message='No profil fineded'
    print(linkdin_dict)
    browser.close()
    return linkdin_dict

def  twitter(name):
    def waiting_func(by_variable, attribute):
        try:
            WebDriverWait(driver, 10).until(lambda x: x.find_element(by=by_variable, value=attribute))
        except (NoSuchElementException, TimeoutException):
            print('{} {} not found'.format(by_variable, attribute))
        finally:
            pass  
    #first_name,last_name=name.split(' ')
    url = r'https://twitter.com/'+name#first_name+'_'+last_name
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    twitter_dict = {
        "Profile_Name": "None",
        "User_Name": "None",
        "Biographie": "None",
        "Following": "None",
        "Followers": "None",
        "tweets": "None"
    }
    i = 0
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    while(match == False):
        lastCount = lenOfPage
        sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match = True
    try:
        waiting_func('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/span[1]/span')
        p1 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/span[1]/span')
        profile_name = p1.text
        twitter_dict["Profile_Name"] = profile_name
        waiting_func('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/span')
        p2 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/span')
        user_name = p2.text
        twitter_dict["User_Name"] = user_name
        waiting_func('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div/span')
        p3 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div/span')
        biographie = p3.text
        twitter_dict["Biographie"] = biographie
        waiting_func('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[5]/div[1]/a/span[1]/span')
        p4 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[5]/div[1]/a/span[1]/span')
        following = p4.text
        twitter_dict["Following"] = following
        waiting_func('xpath','//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span')
        p5 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span')
        followers = p5.text
        twitter_dict["Followers"] = followers
        waiting_func('xpath',"//div[@data-testid='tweet']//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0']")
        tweet = driver.find_elements_by_xpath("//div[@data-testid='tweet']//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0']")   
        tweets = []
        for i in range(len(tweet)):
            str = tweet[i].text
            stri1 = profile_name
            stri2 = user_name
            stri3 = "."
            if str != stri1 and str!=stri2 and str!=stri3 and not(len(str)<=3) and "#" not in str and "@" not in str and "k" not in str:
                tweets.append(str)
                twitter_dict["tweets"] = tweets
    except:
        print('error')
    finally:
        pass
    driver.close()
    return twitter_dict

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-a0-9]+)|([^0-9A-Za-z\t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyze_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0 
    else:
        return -1

def analyze_sentiment_twitter(tweets):
    df = pd.DataFrame(data=[tweet for tweet in tweets], columns=['tweets'])
    sentiment = np.array([analyze_sentiment(tweet) for tweet in df['tweets']])
    return sentiment