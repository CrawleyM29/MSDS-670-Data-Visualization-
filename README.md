# Practicing Matplotlib with Mushroom Analysis

This project is for the MSDS 670-Data Visualization class, taught at Regis University by Professor John Koening.  We are to practice using 'Matplotlib' using Python language to showcase visualization.  I used the mushroom project provided on a list of data we can use to showcase visualization for week 5.  Included will be week 6 project in which we place our visuals on powerpoint.

You can find my code in 'Week 5' folder.  I also cleaned the data prior to capturing the story of the dataset.

## Violin Plot

First visual will be a violin plow that shows the distribution of classification characterstics.  The most important data to know about mushrooms are the 'gill-color' of the mushroom which breaks down into two parts: below 3 and above 3.  This may contribute to the classification of our mushrooms.

![Violin Plot](https://github.com/CrawleyM29/MSDS-670-Data-Visualization-/blob/data-engineering/Week5/savefig/ViolinChart.JPG)

We can see that the gill-color has the most data while gill-spacing has the least.

## Bar Chart: Number of Poisonous and Edible Mushrooms (0 = Edible, 1 = Poisonous)

The following barchart captures the balance in the dataset when it comes to poisonous mushrroms vs edible mushrooms:

![Bar Chart](https://github.com/CrawleyM29/MSDS-670-Data-Visualization-/blob/data-engineering/Week5/savefig/Barchart-poisonous-vs-nonPoisonous.JPG)

Results show that our dataset is pretty balanced between poisonous and edible mushrooms.  This would be a great dataset for machine learning to showcase poinonous versus edible mushrooms via pictures.  We have a little over 4,000 edible mushrooms in our dataset, and approximetly 3,600 poisonous mushrooms.

## Heat Map

To practice analytical skills while showing a visual, I wanted to create a heatmap to know which variable is the least correlating variable as this is the most important one for classification to take a closer look at it and why it's the lowest variable.


![Heat Map](https://github.com/CrawleyM29/MSDS-670-Data-Visualization-/blob/data-engineering/Week5/savefig/heatmap.JPG)

According to our heatmap, 'gill-color' is the least correlating variable with a -0.53. If I were to continue my analysis, I would create a decision tree classifier to help redict a quality response versus a regression tree that predicts quantitive response.

## Conclusion

Results show that our gill-color has a lot of big data unlike the gill-spacing, which has smaller data. The bar chart concluded that the dataset is very balanced for future deep learning and AI capabilities, edible mushrooms having more data with 4,000 edible mushrooms and approximently 3,600 poisonous mushrooms in our dataset.  Ending with the results of our heatmap that shows the least correlated variable being gill-color in which we need to focus on why for future analysis.  
