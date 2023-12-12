<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Lewis98/Covid_AI">
    <img src="readme.ico" alt="Logo" width="80" height="80">
  </a>
  
<h3 align="center">AI Detection of Covid-19 in Chest X-Rays</h3>

  <p align="center">
    Use of Logistic Regression and Support Vector Classification machine learning models, for use in detecting Covid-19 in Chest X-Rays.<br/>
    This project was submitted as part of the 6006CEM Machine Learning and Related Applications module.

  </p>


<!-- ABOUT THE PROJECT -->
## About The Project

The dataset has not been included in the repository, but is freely accessible from: 
https://www.kaggle.com/datasets/prashant268/chest-xray-covid19-pneumonia

The repository consists of two Jupyter Notebook files (.ipynb) and two vanilla python files (.py). 
Both sets of files are identical in contents, with the python files containing block comments denoting
the cell divisions within the Notebook files. This has been done to improve overall readability and accessibility 
of the project.

### Data Pre-Processing

Prior to being used, the images from the dataset were converted to greyscale and resized to a 512x512 resolution.
This was done to reduce the total amount of features per image, and simplify the process of converting the 
image to a computer readable format. The main motivation for this was to reduce development and processing time 
required due to time constraints.

As the image filenames were prefxed by their target (I.E: 'COVID' & 'NORMAL'), the targets could be generated whilst 
iterating over the images for pre-processing.

### Results

The results display a ~95% accuracy rating for both Logistic Regresson and SVM models.

However, there are some concerns with regards to overfitting and sanitisation of data. 
Primarily, some Covid positive samples contain artifacts such as arrows and circles 
(presumably from radiologists identifying the disease). These artifacts are a major issue, 
in that they enable the model to 'cheat' by using the marks to identify covid positive samples,
without requiring analysis of the imaged chest. 

Additionally, the balance between Covid positive and negative 
chest X-Ray images within the dataset is imperfect, this is due to the lack of availability of Covid-19 
Positive X-Rays at the time the project was completed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [Python](https://www.python.org/)
* [Jupyter Notebook](https://jupyter.org/)
* [NumPy](https://numpy.org/)
* [SciKit Image](https://scikit-image.org/)
* [SciKit Learn](https://scikit-learn.org/)
* [Pandas](https://pandas.pydata.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Prashant Patel](https://www.kaggle.com/prashant268) for the [Dataset](https://www.kaggle.com/datasets/prashant268/chest-xray-covid19-pneumonia) used to train and test the model

<p align="right">(<a href="#readme-top">back to top</a>)</p>
