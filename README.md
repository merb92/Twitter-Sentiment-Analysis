# Twitter Sentiment Analysis

# Author: Michael Erb

# Problem

Company A will soon be releasing a new mobile phone. They are concerned about its reception in the market and would like a way to monitor it.

I will be building a Sentiment Analysis model to classify tweets as positive, negative or neutral.

# Data

The data is provided by [CrowdFlower](https://data.world/crowdflower) and is available for download from [data.world](https://data.world/crowdflower/brands-and-product-emotions)

It contains about 8500 instances.

# Methodology

* Exploratory Data Analysis to understand the data.


* Preprocess the text data: including removing unwanted punctuation, changing to lowercase and tokenization.


* Model Selection: A series of classification models were run on the data and evaluated on three metrics in descending order of importance: Average Macro Recall, a balanced Recall score for each class, and overall accuracy.

# Conclusion

* Using a Naive Bayes Classifier, I achieved an macro average recall score of 0.61, balanced recall scores of 0.61, 0.56 and 0.67 for Negative, Neutral and Positive classes respectively, and an overall accuracy of 60%


* While not the greatest accuracy, automating Twitter sentiment analysis will be a step in the right direction in terms of efficiently monitoring the sentiment of Twitter users towards Company A's new mobile phone.

# Recommendations

* I recommend that Company A use Twitter's API to filter tweets with hashtags and text deemed to be related to their mobile phone. These tweets can then be classified by the model and monitored to keep track of the current sentiment regarding their phone.


* Building upon the previous recommendation, an alert system can be created to monitor for changes in sentiment so that they can be addressed quickly.


* Use the model to monitor sentiment regarding the mobile phone industry in general, as well as the sentiment towards competing products.

# Future Work

* Acquire more labeled Tweets to improve the model

The dataset used to train this model is relatively small, about 8500 tweets.  Retraining the model on a larger dataset should improve its performance.

* Expand the scope of the sentiment analysis monitoring

There is plenty of other publicly available text data that can be acquired and monitored for sentiment.  This data may be on other social media platforms or public forums, or could be product reviews. While product reviews often have an associated rating, that rating may differ from the overall sentiment of the review.  Classifying this other data will require a new model because its structure would differ from a tweet.

* Add granularity to the sentiment analysis

Some text data is going to be more negative or more positive than others.  By creating a scale from very negative to somewhat negative to neutral to somewhat positive to very positive, more nuance will be able to be found in the sentiment analysis, and actions can be taken based on the severity of the situation.

# For Further Information

Please review the narrative of the analysis in the [Jupyter notebooks](01_project_summary.ipynb), review the [presentation](https://github.com/merb92/Twitter-Sentiment-Analysis/blob/master/Twitter%20Sentiment%20Analysis%20Presentation.pdf), or read the related [blog article](https://medium.com/analytics-vidhya/pre-processing-tweets-for-sentiment-analysis-a74deda9993e).
