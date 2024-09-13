import markdown
from markdown.extensions.tables import TableExtension
import argparse

def read_contents(input_path: str) -> str:
    try:
        with open(input_path) as f:
            return f.read()
    except IOError as e:
        print(f"Error reading file {input_path}: {e}")
        raise

def write_contents(output_path: str, contents: str) -> None:
    try:
        with open(output_path, 'w') as f:
            f.write(contents)
    except IOError as e:
        print(f"Error writing file {output_path}: {e}")

def convert_markdown_to_html(markdown_contents: str) -> str:
    html = markdown.markdown(markdown_contents, extensions=[TableExtension(use_align_attribute=True)])
    return html

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Usage: converting markdown to html')
    parser.add_argument('input_path', help='input file path')
    parser.add_argument('output_path', help='output file path')

    return parser.parse_args()

def main() -> None:
    args = parse_arguments()
    markdown_contents = read_contents(args.input_path)
    html = convert_markdown_to_html(markdown_contents)
    write_contents(args.output_path, html)

if __name__ == "__main__":
    main()