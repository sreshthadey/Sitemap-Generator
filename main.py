import argparse
from sitemap_generator import generate_xml_file, read_text_file, read_xml_file, write_xml_file, write_text_file, write_csv_file_from_list_of_dictionary, generate_xml_template, generate_xml_file, find_difference_between_two_lists

if __name__ == '__main__':
     
    parser = argparse.ArgumentParser(description = "List of arguments")
    parser.add_argument ('--option', type = int, required = True, help= 'give option which you want to execute')
    parser.add_argument ('--base_url', type = str, default="", help= 'Base URL for this site')
    parser.add_argument ('--input_file_path', type = str, required = False, help= 'File path of text file for list of URLs')
    parser.add_argument ('--xml_file_path', type = str, required = False, help= 'File path of XML file')
    parser.add_argument ('--changefreq', type = str, required = False, help= 'change frequency')
    parser.add_argument ('--last_mod', type = str, required = False, help= 'last modified date')
    parser.add_argument ('--priority', type = str, required = False, help= 'Priority')
    parser.add_argument ('--list1_file_path', type = str, required = False, help= 'File path of rest of the urls')
    parser.add_argument ('--list2_file_path', type = str, required = False, help= 'File path of rest of the urls')

    args = parser.parse_args()

    if args.option == 1:
        xml_template = generate_xml_file(read_text_file(args.input_file_path), args.base_url, args.last_mod, args.changefreq, args.priority)
        write_xml_file(xml_template) 

    elif args.option == 2:
        url_data = read_xml_file(args.xml_file_path)
        write_csv_file_from_list_of_dictionary(url_data)

    elif args.option == 3:
        list1 = read_text_file(args.list1_file_path)
        list2 = read_text_file(args.list2_file_path)
        rest_of_urls = find_difference_between_two_lists(list1, list2)
        write_text_file(rest_of_urls)