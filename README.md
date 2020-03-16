# unsupervised-learning-course
Unsupervised Learning Course - Final work, Winter 2020, BIU

Project Structure: <br>
```
 README.md // YOU ARE HERE
├── requirements.txt // standard python requirements file
├── app.py // the main method for the python code
├── unsupervised.pdf // the paper summarizing the work that was done
├── data
│   └── netflix
│   <tab>    └── stage.json // the result of the data processing
│   <tab>   └── // original datasets used for the data processing
├── latex
│   └── // contains all the raw files and images making the pdf file
├── python_code // all the python code is here
│   ├── config.py
│   ├── data_prep
│   │   ├── // contains the code and the main for the data processing and preparation
│   ├── learning
│   │   ├── clustering
│   │   │   ├── // contains different algorithms used to cluster the data
│   │   ├── data_loader.py
│   │   ├── graph
│   │   │   ├── edges_logics
│   │   │   │   ├── // contains different logics used to construct the graph's edges from the data
│   │   │   ├── graph.py
│   │   └── stats
│   │       ├── // contains the hypothesis testing and the statistical analysis of the data and the clustering
```

Data was taken from:
1. https://www.kaggle.com/shivamb/netflix-shows/tasks?taskId=123
2. https://www.kaggle.com/ashirwadsangwan/imdb-dataset
3. https://www.kaggle.com/unanimad/the-oscar-award

The IMDB dataset couldn't be uploaded to this repository due to it's size,
so in order to rerun the entire data preparation process you need to download it manually
and place it in the `data/netflix/` folder

The results of the data preparation process are saved in `stage.json` so rerunning the entire workflow is unnecessary.