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
        self._data_split_ratios = {"train": 0.8, "val": 0.2, "test": 0}
        self.data_leakage_warning = False

    def set_data_split_ratio(self, new_split_ratios: dict):
        pass


    def read_netflix_data(self, file_path: str):
        loaded_csv = pd.read_csv(file_path,sep="<")
        return loaded_csv

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
        pass

    def _set_types(self):
        pass

    @staticmethod
    def _convert_string_to_list(str_list: str):
        pass

    def _convert_list_do_bool(self, column_to_distribute: str):
        pass

    def _split_data(self):
        pass

    def _is_data_leakage(self):
        pass

