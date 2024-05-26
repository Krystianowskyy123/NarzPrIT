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


def detect_file_type(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower()


def convert_file(input_path, output_path):
    input_type = detect_file_type(input_path)
    output_type = detect_file_type(output_path)

    if input_type not in ['.json', '.yml', '.yaml', '.xml']:
        print(f"Error: Unsupported input file type '{input_type}'.")
        return False

    if output_type not in ['.json', '.yml', '.yaml', '.xml']:
        print(f"Error: Unsupported output file type '{output_type}'.")
        return False

    # Load the input file
    try:
        if input_type == '.json':
            with open(input_path, 'r') as file:
                data = json.load(file)
        elif input_type in ['.yml', '.yaml']:
            with open(input_path, 'r') as file:
                data = yaml.safe_load(file)
        elif input_type == '.xml':
            tree = ET.parse(input_path)
            data = tree.getroot()
    except Exception as e:
        print(f"Error: Failed to read input file '{input_path}'. {e}")
        return False

    # Write to the output file
    try:
        if output_type == '.json':
            with open(output_path, 'w') as file:
                json.dump(data, file, indent=4)
        elif output_type in ['.yml', '.yaml']:
            with open(output_path, 'w') as file:
                yaml.dump(data, file, default_flow_style=False)
        elif output_type == '.xml':
            def dict_to_xml(tag, d):
                elem = ET.Element(tag)
                for key, val in d.items():
                    child = ET.Element(key)
                    child.text = str(val)
                    elem.append(child)
                return elem

            root = dict_to_xml('root', data)
            tree = ET.ElementTree(root)
            tree.write(output_path)
    except Exception as e:
        print(f"Error: Failed to write output file '{output_path}'. {e}")
        return False

    print(f"Success: Converted '{input_path}' to '{output_path}'.")
    return True


def main():
    parser = argparse.ArgumentParser(description='Verify and convert JSON, YAML, or XML files.')
    parser.add_argument('--verify-json', type=str, help='Path to the JSON file to be verified.')
    parser.add_argument('--verify-yml', type=str, help='Path to the YAML file to be verified.')
    parser.add_argument('--verify-xml', type=str, help='Path to the XML file to be verified.')
    parser.add_argument('--convert', nargs=2, help='Convert file1 to file2. Detects file types by extension.')

    args = parser.parse_args()

    if args.verify_json:
        verify_json(args.verify_json)
    elif args.verify_yml:
        verify_yml(args.verify_yml)
    elif args.verify_xml:
        verify_xml(args.verify_xml)
    elif args.convert:
        input_path, output_path = args.convert
        input_type = detect_file_type(input_path)
        if input_type == '.json':
            if verify_json(input_path):
                convert_file(input_path, output_path)
        elif input_type in ['.yml', '.yaml']:
            if verify_yml(input_path):
                convert_file(input_path, output_path)
        elif input_type == '.xml':
            if verify_xml(input_path):
                convert_file(input_path, output_path)
        else:
            print(f"Error: Unsupported file type '{input_type}' for input file '{input_path}'.")
    else:
        print("Error: No operation specified. Use --verify-json, --verify-yml, --verify-xml, or --convert.")


if __name__ == '__main__':
    main()
