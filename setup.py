from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='asreview-multilingual-feature-extractor',
    version='0.1',
    description='A feature extractor based on distiluse-base-multilingual-cased-v1.',
    url='https://github.com/asreview/asreview-multilingual-feature-extractor',
    author='ASReview team',
    author_email='asreview@uu.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review multilingual feature extractor',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.6',
    install_requires=[
        'sklearn',
        'asreview>=0.13',
        'sentence_transformers'
    ],
    entry_points={
        'asreview.models.classifiers': [
            # define classifier algorithms
        ],
        'asreview.models.feature_extraction': [
            'multilingual = asreviewcontrib.models.distiluse_base_multilingual:MultilingualSentenceTransformer',
        ],
        'asreview.models.balance': [
            # define balance strategy algorithms
        ],
        'asreview.models.query': [
            # define query strategy algorithms
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/asreview/asreview-multilingual-feature-extractor/issues',
        'Source': 'https://github.com/asreview/asreview-multilingual-feature-extractor/',
    },
)
