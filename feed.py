import yaml
import xml.etree.ElementTree as xml_tree
import xml.dom.minidom

with open('feed.yaml') as file:
    yml_data = yaml.safe_load(file)

rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:itunes': 'http://podcast-1-0.dtd',
    'xmlns:content': 'http://purl.org/rss/1.0/module/content'
})

channel_element = xml_tree.SubElement(rss_element, 'channel')
xml_tree.SubElement(channel_element, 'title').text = yml_data['title']
xml_tree.SubElement(channel_element, 'subtitle').text = yml_data['subtitle']
xml_tree.SubElement(channel_element, 'author').text = yml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yml_data['description']
xml_tree.SubElement(channel_element, 'image').text = yml_data['image']
xml_tree.SubElement(channel_element, 'language').text = yml_data['language']
xml_tree.SubElement(channel_element, 'category').text = yml_data['category']

for item in yml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(item_element, 'description').text = item['description']
    xml_tree.SubElement(item_element, 'pubDate').text = item['published']
    
    enclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': item['file'],
        'type': yml_data['format'],
        'length': str(item['length'])
    })
    
    xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']

# Pretty print the XML
rough_string = xml_tree.tostring(rss_element, 'utf-8')
reparsed = xml.dom.minidom.parseString(rough_string)
pretty_xml = reparsed.toprettyxml(indent="  ", encoding='utf-8')

with open('podcast.xml', 'wb') as f:
    f.write(pretty_xml)