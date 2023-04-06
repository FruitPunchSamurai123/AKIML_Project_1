import pandas as pd


class NetflixReader:
    def __init__(self):
        self.netflix_data_raw = pd.DataFrame()
        self.netflix_data = pd.DataFrame()
        self.train_data = pd.DataFrame()
        self.val_data = pd.DataFrame()
        self.test_data = pd.DataFrame()
        self._type_dict = {"index": "int",
                           "id": "string",
                           "title": "string",
                           "type": "category",
                           "runtime": "int",
                           "genres": "string",
                           "production_countries": "string",
                           "imdb_id": "string",
                           "imdb_score": "float",
                           "imdb_votes": "int"
                           }
        self._data_split_ratios = {"train": 0.4, "val": 0.3, "test": 0.3}
        self.data_leakage_warning = False

    def set_data_split_ratio(self, new_split_ratios: dict):
        self._data_split_ratios = new_split_ratios

    def read_netflix_data(self, file_path: str):
        self.netflix_data_raw = pd.read_csv(file_path, sep=">")

    def preprocess(self):
        self.netflix_data_raw.drop(columns="seasons", inplace=True)
        self.netflix_data_raw.drop(columns="age_certification", inplace=True)
        self._drop_missing_values()
        self._set_types()
        self.netflix_data.drop(columns="production_countries", inplace=True)
        self._convert_list_do_bool("genres")
        self.netflix_data.drop(columns="genres", inplace=True)
        self._split_data()
        self.data_leakage_warning = self._is_data_leakage()

    def write_netflix_data(self, file_path: str):
        pass

    def _drop_missing_values(self):
        self.netflix_data = self.netflix_data_raw.dropna()

    def _set_types(self):
        self.netflix_data = self.netflix_data.astype(self._type_dict)

    @staticmethod
    def _convert_string_to_list(str_list: str):
        pass

    def _convert_list_do_bool(self, column_to_distribute: str):
        """
        This function splits a column into multiple columns of each value in the dataframe. These columns
        then contain only boolean values. if the previous row contained the specific value the new column will .
        return true.
        :param column_to_distribute: name of the column that should be split
        :return:
        """
        genre_dummies = self.netflix_data[column_to_distribute].str.get_dummies(sep="'")
        genre_dummies.columns = genre_dummies.columns.str.replace(" ", "")
        genre_dummies.drop(columns=[",", "[]", "]", "["], inplace=True)
        self.netflix_data = pd.concat([self.netflix_data_raw, genre_dummies])

    def _split_data(self):
        #shuffle the rows so that the data is not ordered by any column
        data_shuffled = self.netflix_data_raw.sample(frac=1)

        #calculate the number of rows for each split based on the split ratios
        train_rows = int(data_shuffled.shape[0] * self._data_split_ratios["train"])
        val_rows = int(data_shuffled.shape[0] * self._data_split_ratios["val"])
        test_rows = int(data_shuffled.shape[0] * self._data_split_ratios["test"])

        #take the rows acording to the split ratios and fill the dataframes
        self.train_data = data_shuffled.iloc[:train_rows]   
        self.val_data = data_shuffled.iloc[train_rows:train_rows + val_rows]
        self.test_data = data_shuffled.iloc[train_rows + val_rows:]

    def _is_data_leakage(self):
        pass
