
# Sitemap Generator







1. To generate a sitemap use the following command

```bash
  python main.py --option <option_value> --input_file_path <filepath> --base_url <base_url> --changefreq <change_frequency> --last_mod <last_modified_date> --priority <priority> 
```
### option_value

- It is a required argument. For this option_value is 1
Example-

```javascript
python main.py --option 1 --input_file_path <input_file_path>
```

### input_file_path
- It is a required argument. give file path of text file which contains all the site urls. Filepath should be in inverted commas("")
Example-

```javascript
python main.py --option 1 --input_file_path "c:\\Users\\91704\\Desktop\\urls.txt"
```
### base_url
- It is an optional argument. give base_url of the website only if the urls in the text file does not contain base url. It should be in inverted commas("")
Example-

```javascript
python main.py --option 1 --input_file_path "c:\\Users\\91704\\Desktop\\urls.txt" --base_url "https://deltafaucet.in"
```
### change_frequency
- It is an optional argument. give change_frequency of the website if it is needed in your Sitemap. It should be in inverted commas("")
Example-

```javascript
python main.py --option 1 --input_file_path "c:\\Users\\91704\\Desktop\\urls.txt" --changefreq "daily"
```
### last_modified_date
- It is an optional argument. give last modified date of the website if it is needed in your Sitemap. It should be in inverted commas("")
Example-

```javascript
python main.py --option 1 --input_file_path "c:\\Users\\91704\\Desktop\\urls.txt" --last_mod "07/05/2022"
```
### priority
- It is an optional argument. give priority if it is needed in your Sitemap. It should be in inverted commas("")
Example-

```javascript
python main.py --option 1 --input_file_path "c:\\Users\\91704\\Desktop\\urls.txt" --priority "1.0" 
```
2. To generate a csv file from a given sitemap file, Use the following command. it will contain all the data from the sitemap.
```bash
  python main.py --option <option_value> --xml_file_path <sitemap_file_path>
```
### option_value

- It is a required argument. For this option_value is 2
Example-

```javascript
python main.py --option 2 --xml_file_path <sitemap_file_path>
```
### sitemap_file_path
- It is a reruired argument. give sitemap file path. It should be in inverted commas("")
Example-

```javascript
python main.py --option 2 --xml_file_path "c:\\Users\\91704\\Desktop\\sitemap.xml"
```
3. To generate a text file of urls from two given text file of urls. It will return all the urls which are not common in those two url files.  use the following command
```bash
  python main.py --option <option_value> --list1_file_path <file_path> --list2_file_path <file_path>
```
### option_value

- It is a required argument. For this option_value is 3
Example-

```javascript
python main.py --option 3 --list1_file_path <file_path> --list2_file_path <file_path>
```
### file_path
- It is a reruired argument. give file path of two text files. It should be in inverted commas("")
Example-

```javascript
python main.py --option 3 --list1_file_path "c:\\Users\\91704\\Desktop\\urls.txt" --list2_file_path "c:\\Users\\91704\\Desktop\\urls-3.txt"
```