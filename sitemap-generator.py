import datetime
#from jinja2 import Template
#import pandas as pd
import xml.etree.cElementTree as ET
#from lxml import etree
import xml.dom.minidom
import os
import argparse
import sys

def generate_xml_template(root, url, lastModTime, changeFreq, priority):
    
    doc = ET.SubElement(root,"url")
    ET.SubElement(doc,"loc").text = url
    ET.SubElement(doc,"lastmod").text = lastModTime
    ET.SubElement(doc,"changefreq").text = changeFreq
    ET.SubElement(doc,"priority").text = priority
    #xml_template = pretty_print_xml(doc) 
    #return xml_template

def format_xml(root):
    
    xml_string = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
    xml_string = os.linesep.join([s for s in xml_string.splitlines() if s.strip()])
    return xml_string

def generate_xml_file(list_of_urls, XML_file_path):
    
    root = ET.Element('urlset')
    root.attrib['xmlns:xsi'] = "http://www.w3.org/2001/XMLSchema-instance"
    root.attrib['xsi:schemaLocation'] = "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    root.attrib['xmlns'] = "http://www.sitemaps.org/schemas/sitemap/0.9"
    
    lastModTime = datetime.datetime.now().strftime('%Y-%m-%d')
    changeFreq = 'daily' 
    priority = '1.0'
    
    for url in list_of_urls:
        url = args.baseURL + url
        generate_xml_template(root, url, lastModTime, changeFreq, priority)
        
    xml_template = format_xml(root) 
    tree = ET.ElementTree(root)
    
    print(xml_template)
    
    with open(XML_file_path,'w') as file:
        file.write(xml_template)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description = "List of arguments")
    parser.add_argument ('baseURL', type = str, help= 'Base URL for this site')
    parser.add_argument ('input_file_path', type = str, help= 'File path of text file for list of URLs')
    parser.add_argument ('XML_file_path', type = str, help= 'File path of XML file')
    args = parser.parse_args()
    print(args.baseURL)
    
    with open(args.input_file_path,'r') as file:
        list_of_urls = file.read()
        list_of_urls = list_of_urls.split('\n')
    
    generate_xml_file(list_of_urls, args.XML_file_path)