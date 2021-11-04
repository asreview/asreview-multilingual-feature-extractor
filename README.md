# ASReview plugin implementing a multilingual feature extractor
This repo contains a plugin implementing 
[`sentence-transformers/distiluse-base-multilingual-cased-v1`](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1).

This special sentence tranformer allows for the usage of records in multiple languages.

## Getting started

To install the new feature extractor use:

```bash
pip install .
```

or

```bash
pip install git+https://github.com/asreview/asreview-multilingual-feature-extractor.git
```


## Usage

The new feature extractor `Multilingual Sentence transformer` is defined in
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

MIT license
