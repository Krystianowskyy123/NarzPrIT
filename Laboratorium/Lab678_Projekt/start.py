import argparse
import json
import os

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

def main():
    parser = argparse.ArgumentParser(description='Verify if a file is a valid JSON file.')
    parser.add_argument('--verify-json', type=str, required=True, help='Path to the JSON file to be verified.')

    args = parser.parse_args()

    verify_json(args.verify_json)

if __name__ == '__main__':
    main()
