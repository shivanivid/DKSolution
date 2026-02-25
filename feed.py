import yaml
import xml.etree.ElementTree as xml_tree
with open('feed.yaml') as file:
    yml_data = yaml.safe_load(file)

rss_element = xml_tree.Element('rss',{'version' : '2.0',
 'xmlns:itunes':'http://podcast-1-0.dtd',
 'xmlns:content':'http://purl.org/rss/1.0/module/content'
 })


channel_element = xml_tree.SubElement(rss_element, 'channel')
xml_tree.SubElement(channel_element, 'title').text = yml_data['title']
xml_tree.SubElement(channel_element, 'subtitle').text = yml_data['subtitle']
xml_tree.SubElement(channel_element, 'author').text = yml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yml_data['description']

xml_tree.SubElement(channel_element, 'image').text = yml_data['image']
xml_tree.SubElement(channel_element, 'language').text = yml_data['title']
xml_tree.SubElement(channel_element, 'title').text = yml_data['title']
xml_tree.SubElement(channel_element, 'title').text = yml_data['title']




output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='utf-8',xml_declaration = True)