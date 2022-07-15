#Inflam
![Continuous Integration build in GitHub Actions](https://github.com/lionandjelka/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)
Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit tes


Installation/deployment: 
Requirements

Python>3.7
cycler==0.11.0
fonttools==4.28.1
kiwisolver==1.3.2
matplotlib==3.5.0
numpy==1.21.4
packaging==21.2
Pillow==8.4.0
pyparsing==2.4.7
python-dateutil==2.8.2
setuptools-scm==6.3.2
six==1.16.0
tomli==1.2.2

In command prompt type

>python3 inflammation-analysis.py


Basic usage: 

for testing install pytest

>pip3 install pytest

>pytest tests/test_models.py


basic usage in Python shell:

>import inflammation
>from inflammation import  models, serializers,views


Contributing: 
Contributors  to open source are sought, with emphasize on statitistical analysis and vizualization 


Contact information/getting help: 

E: SER-SAG.Team@math.rs


Credits/Acknowledgements: 

Southempton University


Citation:

https://github.com/lionandjelka/python-intermediate-inflammation/blob/main/CITATION.cff

 
Licence: open source