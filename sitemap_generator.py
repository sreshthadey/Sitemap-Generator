from asyncio.windows_events import NULL
import datetime
from posixpath import split
import string
import xml.etree.cElementTree as ET
import xml.dom.minidom
import os
import argparse
import csv
import sys
from bs4 import BeautifulSoup

def read_text_file(input_file_path) -> list:
    with open(input_file_path,'r') as file:
        list_of_urls = file.read()
        list_of_urls = list_of_urls.split('\n')
        list_of_urls = [url for url in list_of_urls if url]
                
    return list_of_urls

def read_xml_file(existed_xml_file_path: str) -> list:
    
    with open(existed_xml_file_path,'r') as file:
        data = file.read()
    bs_data = BeautifulSoup(data, features="xml")
    bs_data_url = bs_data.find_all('url')
    url_data = list()
    for data in bs_data_url:
        temp_dic = dict()
        url = data.loc.string
        count = 0
        position = 0
        for i in range(len(url)):
            if url[i] == '/':
                count += 1
            if(count == 3):
                position = i
                break
        #url_list.append(url[length_base_url:])
        temp_dic['url'] = url[position:]
        if(data.lastmod):
            temp_dic['lastmod'] = data.lastmod.string
        if(data.changefreq):
            temp_dic['change_frequency'] = data.changefreq.string
        if(data.priority):
            temp_dic['priority'] = data.priority.string
        url_data.append(temp_dic)
    
    return url_data

def write_xml_file(xml_template: str):
    with open("sitemap.xml",'w') as file:
        file.write(xml_template)

def write_text_file(urls_list: list):
    with open("output.txt",'w') as file:
        for item in urls_list:
            file.write( "%s\n" %item)

def write_csv_file_from_list_of_dictionary(url_data:dict):

    header = list(url_data[0].keys())
    with open("csv_file.csv",'w', newline = '') as file:
        dict_writer = csv.DictWriter(file, header)
        dict_writer.writeheader()
        dict_writer.writerows(url_data)

def format_xml(root: object) -> string:
    
    xml_string = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
    xml_string = os.linesep.join([s for s in xml_string.splitlines() if s.strip()])
    xml_string = xml_string.replace("\n", "")
    return xml_string

def generate_xml_template(root: object, url: str, last_mod: str, changefreq: str, priority: str):
    
    doc = ET.SubElement(root,"url")
    ET.SubElement(doc,"loc").text = url
    if last_mod:
        ET.SubElement(doc,"lastmod").text = last_mod
    if changefreq:
        ET.SubElement(doc,"changefreq").text = changefreq
    if priority:
        ET.SubElement(doc,"priority").text = priority

def generate_xml_file(list_of_urls: list, base_url: str, last_mod: str, changefreq: str, priority: str):
    
    root = ET.Element('urlset')
    root.attrib['xmlns:xsi'] = "http://www.w3.org/2001/XMLSchema-instance"
    root.attrib['xsi:schemaLocation'] = "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    root.attrib['xmlns'] = "http://www.sitemaps.org/schemas/sitemap/0.9"
    
    #last_mod_time = datetime.datetime.now().strftime('%Y-%m-%d')

    last_mod_time = NULL
    
    for i in range(len(list_of_urls)):
        if(base_url):
            url = base_url + list_of_urls[i]
        else:
            url = list_of_urls[i]
        generate_xml_template(root, url, last_mod, changefreq, priority)
        
    xml_template = format_xml(root) 
    tree = ET.ElementTree(root)

    return xml_template

def find_difference_between_two_lists(list1:list, list2:list) -> list:
    rest_urls = list()
    for url in list1:
        if url not in list2:
           #if '/product' not in url:
                rest_urls.append(url)
        else:
            continue
    for url in list2:
        if url not in list1:
            #if '/product' not in url:
                rest_urls.append(url)
        else:
            continue
    return rest_urls

