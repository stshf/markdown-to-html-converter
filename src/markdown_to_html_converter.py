import markdown
from markdown.extensions.tables import TableExtension
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def read_contents(input_path: str) -> str:
    try:
        with open(input_path, 'r') as f:
            return f.read()
    except IOError as e:
        logger.error(f"Error reading file {input_path}: {e}")
        return None

def write_contents(output_path: str, contents: str) -> bool:
    try:
        with open(output_path, 'w') as f:
            f.write(contents)
        return True
    except IOError as e:
        logger.error(f"Error writing file {output_path}: {e}")
        return False

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
    if markdown_contents is None:
        return

    html = convert_markdown_to_html(markdown_contents)
    if write_contents(args.output_path, html):
        logger.info(f"Successfully converted {args.input_path} to {args.output_path}")
    else:
        logger.error(f"Failed to write to {args.output_path}")

if __name__ == "__main__":
    main()