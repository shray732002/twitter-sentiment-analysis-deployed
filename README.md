# twitter-sentiment-analysis-deployed(on heruko)

App link:- [Twitter-sentiment-analysis](https://app-twitter-sentiment-analysis.herokuapp.com/)

In this project i have made a simple app using flask and render template to it using html.

In this project you will get to know about major topics like:-
* Data preprocessing
* NLP(Natural language preprocessing)
* How to apply ML models(GaussianNB,XGBoost,RandomForest), then applied parameter tuning and compare it to get better(accurate) results
* Pickling the model

### Steps from beginning(from making a model) to end(deploying it on heroku)

* Make a conda environment :- conda create -n {env_name}
* After creating environment you need to activate it :- conda activate {env_name}
* try to download each and every library you need in your project
* then use pip freeze command to collect name and version of libraries in your requirements.txt file pip freeze > requirements.txt
* Make a flask app and add a Procfile so that heroku app will know where it has to search for your app in your github repository
* Then just go to heroku app and deploy your model

### Screenshots
* Racist/Sexist tweets:- 
 ![racist_tweets](https://github.com/shray732002/twitter-sentiment-analysis-deployed/blob/main/screenshots/Screenshot%20(10).png)
   * Result:-
    ![tweet_result](https://github.com/shray732002/twitter-sentiment-analysis-deployed/blob/main/screenshots/Screenshot%20(11).png)
* Non racist/sexist tweets:-
 ![non_racist_tweet](https://github.com/shray732002/twitter-sentiment-analysis-deployed/blob/main/screenshots/Screenshot%20(13).png)  
   * Result:-
    ![tweet_result](https://github.com/shray732002/twitter-sentiment-analysis-deployed/blob/main/screenshots/Screenshot%20(14).png)
