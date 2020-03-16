from IPython.core.display import display

from python_code.data_prep.data_prep import data_prep

if __name__ == "__main__":
    df = data_prep()
    display(df)
