import datetime
import xml.etree.cElementTree as ET
import xml.dom.minidom
import os
import argparse
import sys

def read_file():
    with open(args.input_file_path,'r') as file:
        list_of_urls = file.read()
        list_of_urls = list_of_urls.split('\n')
    return list_of_urls

def write_file(xml_template, XML_file_path):
    with open(XML_file_path,'w') as file:
        file.write(xml_template)

def format_xml(root):
    
    xml_string = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
    xml_string = os.linesep.join([s for s in xml_string.splitlines() if s.strip()])
    return xml_string

def generate_xml_template(root, url, last_mod_time, change_freq, priority):
    
    doc = ET.SubElement(root,"url")
    ET.SubElement(doc,"loc").text = url
    ET.SubElement(doc,"lastmod").text = last_mod_time
    ET.SubElement(doc,"changefreq").text = change_freq
    ET.SubElement(doc,"priority").text = priority

def generate_xml_file(list_of_urls):
    
    root = ET.Element('urlset')
    root.attrib['xmlns:xsi'] = "http://www.w3.org/2001/XMLSchema-instance"
    root.attrib['xsi:schemaLocation'] = "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
    root.attrib['xmlns'] = "http://www.sitemaps.org/schemas/sitemap/0.9"
    
    last_mod_time = datetime.datetime.now().strftime('%Y-%m-%d')
    change_freq = 'daily' 
    priority = '1.0'
    
    for i in range(len(list_of_urls)-1):
        url = args.base_url + list_of_urls[i]
        print(url)
        generate_xml_template(root, url, last_mod_time, change_freq, priority)
        
    xml_template = format_xml(root) 
    tree = ET.ElementTree(root)

    return xml_template

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description = "List of arguments")
    parser.add_argument ('--base_url', type = str, default="", help= 'Base URL for this site')
    parser.add_argument ('--input_file_path', type = str, required = True, help= 'File path of text file for list of URLs')
    parser.add_argument ('--xml_file_path', type = str, required = True, help= 'File path of XML file')
    args = parser.parse_args()
    
    xml_template = generate_xml_file(read_file())
    write_file(xml_template, args.xml_file_path)