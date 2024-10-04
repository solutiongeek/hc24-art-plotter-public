import xml.etree.ElementTree as ET
from svgpathtools import parse_path

def parse_file(file_path: str) -> list:
    """
    Parse an SVG file and extract path data and attributes.
    
    Args:
        file_path (str): The path to the SVG file.
    
    Returns:
        list: A list of tuples, each containing a path's 'd' attribute and other attributes.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        raise ValueError(f"Error parsing SVG: {e}")
    
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    paths = []
    
    # Get the 'd' attribute from each path element
    # this attribute defines a path to be drawn.
    for path_element in root.findall('.//svg:path', namespaces=ns):
        path_data = path_element.attrib.get('d')
        if path_data:
            paths.append((path_data, path_element.attrib))
    
    return paths

def parse_paths(path_data_list: list) -> list:
    """
    Convert the SVG path data into Path objects.
    
    Args:
        path_data_list (list): A list of tuples (path_data, attributes) from the SVG file.
    
    Returns:
        list: A list of svgpathtools Path objects for further processing.
    """
    return [parse_path(path_data) for path_data, _ in path_data_list]

