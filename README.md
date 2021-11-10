# ASReview multilingual feature extractor

This extension to ASReview implements a multilingual feature extractor algorithm.
This algorithm allows for the usage of records in multiple languages. These 
languages are:

Arabic, Chinese, Dutch, English, French, German, Italian, Korean, Polish, Portuguese, Russian, Spanish, Turkish. 

The extension implements [`sentence-transformers/distiluse-base-multilingual-cased-v1`](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1).
This is a sentence-transformers model and maps sentences to a 512 dimensional dense
vector space and is multilingual. For more information about the feature extraction
method, see 

> Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. ArXiv, abs/1908.10084. https://arxiv.org/abs/1908.10084


## Installation

Install the multilingual feature extractor with:

```bash
pip install .
```

or

```bash
pip install git+https://github.com/asreview/asreview-multilingual-feature-extractor.git
```

## Usage

### ASReview LAB

ASReview LAB users can select the model in the
[Model Selection](https://asreview.readthedocs.io/en/latest/features/pre_screening.html#select-model)
step of the project setup. Select "Multilingual Sentence Transformer" under
"Feature extraction". 

### Simulation

The new feature extractor `Multilingual Sentence Transformer` is defined in
[`asreviewcontrib/models/distiluse-base-multilingual.py`](asreviewcontrib/models/distiluse-base-multilingual.py) 
and can be used in a simulation.

```bash
asreview simulate example_data_file.csv -e multilingual
```

Test the feature extractor with:

```bash
asreview simulate benchmark:van_de_Schoot_2017 -e multilingual -m svm
```

## License

[MIT license](/LICENSE)

## Contact

For any questions or remarks, please send an email to asreview@uu.nl or open an issue.
