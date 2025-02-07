import pathlib
import sys

def validate_label_format(txt_file: pathlib.Path) -> bool:
    """Validate if the label starts with '[' and ends with ']'"""
    with open(txt_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        if not (content.startswith('[') and content.endswith(']')):
            print(f"Error in {txt_file}: Content should start with '[' and end with ']'")
            print(f"Current content: {content}")
            return False
    return True

def check_missing_labels(root: pathlib.Path) -> bool:
    """Check if all image files have corresponding txt files"""
    all_valid = True
    image_extensions = {'.jpg', '.jpeg', '.png'}
    
    for img_file in root.rglob('*'):
        if img_file.suffix.lower() in image_extensions:
            txt_file = img_file.with_suffix('.txt')
            if not txt_file.exists():
                print(f"Error: Missing label file for {img_file}")
                all_valid = False
    
    return all_valid

def main():
    root = pathlib.Path('data')
    all_valid = True
    
    # Check all txt files format
    for txt_file in root.rglob('*.txt'):
        if not validate_label_format(txt_file):
            all_valid = False
    
    # Check for missing label files
    if not check_missing_labels(root):
        all_valid = False
    
    if not all_valid:
        sys.exit(1)
    print("All labels are properly formatted and all images have corresponding label files!")
    sys.exit(0)

if __name__ == '__main__':
    main() 