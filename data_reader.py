import pandas as pd


class DataReader:
    pickle_file_path = "?"

    def read_netflix_data(self, file_path: str):
        """

        :return:
        """
        return pd.read_csv(file_path)

    def preprocess_netflix_data(self, data: pd.DataFrame):
        """

        :return:
        """
        print("WIP")

    def write_netflix_data(self, data_preprocessed: pd.DataFrame):
        """

        :return:
        """
        return data_preprocessed.to_pickle(self.pickle_file_path)
