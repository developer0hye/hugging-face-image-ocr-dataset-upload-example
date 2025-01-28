import pathlib
import pandas as pd
import tqdm
from huggingface_hub import login
from datasets import load_dataset

def read_label_file(txt_file: pathlib.Path) -> str:
    """Read and clean label from text file"""
    with open(txt_file, 'r', encoding='utf-8') as f:
        return f.read().rstrip()

def process_split(root: pathlib.Path, split: str, query: str) -> pd.DataFrame:
    """Process a single data split"""
    # Create lists to store the data
    file_names = []
    queries = []
    labels = []
    
    jpg_files = sorted(root.glob(f'{split}/*.jpg'))
    print(f'Processing {len(jpg_files)} files in {split} split')
    for jpg_file in tqdm.tqdm(jpg_files):
        
        txt_file = jpg_file.with_suffix('.txt')
        if not txt_file.exists():
            continue
        label = read_label_file(txt_file)
        
        # Append to lists instead of creating individual DataFrames
        file_names.append(jpg_file.name)
        queries.append(query)
        labels.append(label)
    
    # Create DataFrame once with all the data
    return pd.DataFrame({
        'file_name': file_names,
        'query': queries,
        'label': labels
    })

def main():
    root = pathlib.Path('data')
    huggingface_id = 'developer0hye'
    huggingface_dataset_name = 'korocr'

    query = '이미지의 모든 문자를 인식하세요. 반환 포맷: ["문자 1", "문자 2", ..., "문자 n"] 인식된 문자가 없는 경우 [] 를 반환하세요.'
    
    for split in ['train', 'validation']:
        df = process_split(root, split, query)
        df.to_csv(f'{root}/{split}/metadata.csv', index=False)
        
    dataset = load_dataset('imagefolder', data_dir=root)
    dataset.push_to_hub(f'{huggingface_id}/{huggingface_dataset_name}')

if __name__ == '__main__':
    main()