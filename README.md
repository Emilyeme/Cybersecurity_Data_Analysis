# Overview

As a software developer interested in cybersecurity and data analysis, I wanted to develop practical skills in using Python to examine network traffic data and identify patterns that may be useful in understanding cybersecurity activities.

This project analyses a subset of the CIC-IDS2017 cybersecurity dataset.The dataset contains network traffic records with 70 columns including flow duration, packet clumns, datatransfer rates and traffic labels. The selected dataset contains two taffic categories: BENGN and PortScan.

Dataset: CIC-IDS2017
Dataset source

The purpose of this software is to use Python and data anlysis libraries to investigate network traffic, compare traffic categories, identifying patterns and present findings through statistical summaries and visualisations. It also demostrates data ccleaning by identifying and removing duplicate records and rows containing missing values before performing further analysis.

[Software Demo Video](https://www.loom.com/share/3a33be2e2c1e4f91badae3399f3ffe8b)

# Data Analysis Results

1 Which network traffic category has the highest number of records?

Before cleaning, the dataset contained 286,467 records:

PortScan: 158,930 records (55.48%).

BENIGN: 127,537 records (44.52%).

After removing duplicate records and rows with missing values, 214,099 records remained:

BENIGN: 123,280 records (57.58%).

PortScan: 90,819 records (42.42%).

The results show that BENIGN was the most frequent traffic category after data cleaning.

2 What differences can be observed between BENIGN and PortScan network traffic?

I compared four network traffic characteristics using the median values.
The results show that BENIGN traffic had a longer median flow duration and higher median forward and backward packet counts. PortScan traffic had a considerably higher median flow byte rate.

These findings demonstrate differences in the characteristics of the two traffic categories in the selected dataset.

Data cleaning: The original dataset contained 72,353 duplicate records and 15 missing values. After removing duplicates and rows with missing values, the dataset contained 214,099 records.

Visualisations:

traffic_analysis.png – Shows traffic categories before data cleaning.

cleaned_traffic_analysis.png – Shows traffic categories after data cleaning.

# Development Environment

The software was developed using the following tools:

Windows operating system.

Windows PowerShell for executing the Python program.

Python 3.14.

A local project folder for storing the program, dataset, and visualisations.

Programming Language and Libraries

Python was used as the main programming language.

The following libraries were used:

Pandas: Used to load, explore, clean, group, count, and analyse the dataset.

Matplotlib: Used to create bar charts showing network traffic categories before and after data cleaning.

PyArrow: Used to read the Parquet dataset format.

# Useful Websites

[Pandas Documentation](https://dataanalysispython.readthedocs.io/en/latest/pandas.html)
[Matplotlib Documentation](https://matplotlib.org/stable/index.html)
[Python Documentation](https://docs.python.org/3/)
[Hugging Face](https://huggingface.co/datasets/bvsam/cic-ids-2017/blob/refs%2Fconvert%2Fparquet/machine_learning/train/0001.parquet)

# Future Work

Investigate additional network traffic categories to expand the analysis.

Explore datasets containing timestamps to investigate changes in network traffic over time.

Improve the visualisations by adding more detailed comparisons and labels.

Add more statistical analysis to identify additional patterns in network traffic.

Improve the program's ability to handle different datasets and missing values.