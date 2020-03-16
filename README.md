# unsupervised-learning-course
Unsupervised Learning Course - Final work, Winter 2020, BIU

Project Structure: <br>
├── README.md // YOU ARE HERE <br>
├── requirements.txt // standard python requirements file <br>
├── app.py // the main method for the python code <br>
├── unsupervised.pdf // the paper summarizing the work that was done <br>
├── data <br>
│   └── netflix <br>
│       └── stage.json // the result of the data processing <br>
│       └── // original datasets used for the data processing <br>
├── latex <br>
│   └── // contains all the raw files and images making the pdf file <br>
├── python_code // all the python code is here <br>
│   ├── config.py <br>
│   ├── data_prep <br>
│   │   ├── // contains the code and the main for the data processing and preparation <br>
│   ├── learning <br>
│   │   ├── clustering <br>
│   │   │   ├── // contains different algorithms used to cluster the data <br>
│   │   ├── data_loader.py <br>
│   │   ├── graph <br>
│   │   │   ├── edges_logics <br>
│   │   │   │   ├── // contains different logics used to construct the graph's edges from the data <br>
│   │   │   ├── graph.py <br>
│   │   └── stats <br>
│   │       ├── // contains the hypothesis testing and the statistical analysis of the data and the clustering <br>


Data was taken from:
1. https://www.kaggle.com/shivamb/netflix-shows/tasks?taskId=123
2. https://www.kaggle.com/ashirwadsangwan/imdb-dataset
3. https://www.kaggle.com/unanimad/the-oscar-award

The IMDB dataset couldn't be uploaded to this repository due to it's size,
so in order to rerun the entire data preparation process it is must be downloaded manually
and placed in the `data/netflix/` folder

The results of the data preparation process are saved in `stage.json` so rerunning the entire workflow is unnecessary.