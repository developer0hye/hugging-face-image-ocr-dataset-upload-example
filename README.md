# hugging-face-image-ocr-dataset-upload-example

https://huggingface.co/datasets/developer0hye/korocr

![teaser](teaser.png)

Refer to the [official documentation](https://huggingface.co/docs/datasets/image_dataset) to ensure you don't spend more than 12 hours uploading your dataset to Hugging Face Datasets.


Familiarize yourself with the code and dataset directory structure.

```
dataset/
  train/
    *.jpg
    metadata.csv
  validation/
    *.jpg
    metadata.csv
```
- The text files(*.txt) contain essential ground truth information, but to upload the dataset to Hugging Face Datasets, this information must be matched with its corresponding image file in the `metadata.csv` file. This process is automatically executed in upload.py.

# Run

```
git clone https://github.com/developer0hye/hugging-face-image-ocr-dataset-upload-example.git
cd hugging-face-image-ocr-dataset-upload-example
```

Replace the highlighted lines in `upload.py` with [your new repository](https://huggingface.co/new-dataset).
![repo](repo.png)

```
python upload.py
```
