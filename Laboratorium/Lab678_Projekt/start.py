import argparse
import json
import os
import yaml
import xml.etree.ElementTree as ET

def verify_json(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False

    try:
        with open(file_path, 'r') as file:
            json.load(file)
        print(f"Success: File '{file_path}' is a valid JSON file.")
        return True
    except json.JSONDecodeError as e:
        print(f"Error: File '{file_path}' is not a valid JSON file. {e}")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred while processing '{file_path}'. {e}")
        return False

def verify_yml(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False

    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        print(f"Success: File '{file_path}' is a valid YAML file.")
        return True
    except yaml.YAMLError as e:
        print(f"Error: File '{file_path}' is not a valid YAML file. {e}")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred while processing '{file_path}'. {e}")
        return False

def verify_xml(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False

    try:
        tree = ET.parse(file_path)
        tree.getroot()
        print(f"Success: File '{file_path}' is a valid XML file.")
        return True
    except ET.ParseError as e:
        print(f"Error: File '{file_path}' is not a valid XML file. {e}")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred while processing '{file_path}'. {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Verify if a file is a valid JSON, YAML, or XML file.')
    parser.add_argument('--verify-json', type=str, help='Path to the JSON file to be verified.')
    parser.add_argument('--verify-yml', type=str, help='Path to the YAML file to be verified.')
    parser.add_argument('--verify-xml', type=str, help='Path to the XML file to be verified.')

    args = parser.parse_args()

    if args.verify_json:
        verify_json(args.verify_json)
    elif args.verify_yml:
        verify_yml(args.verify_yml)
    elif args.verify_xml:
        verify_xml(args.verify_xml)
    else:
        print("Error: No file specified for verification. Use --verify-json, --verify-yml, or --verify-xml.")

if __name__ == '__main__':
    main()
