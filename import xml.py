import xml.etree.ElementTree as ET

def import_xml(filename):
    try:
        tree = ET.parse(filename)  # Try to parse the file
        root = tree.getroot()       # Get the root element
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Use the corrected path without extra quotes
_data = import_xml('C:/Code_DataPre/Untilted-001.xml')
if _data:
    print(ET.tostring(_data, encoding='utf-8').decode('utf-8'))
else:
    print("No valid XML data found.")