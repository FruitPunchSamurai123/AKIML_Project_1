import netflix_data_reader as reader

netflix_reader = reader.NetflixReader()
netflix_reader.read_netflix_data(file_path="./files/netflix_data.csv")
netflix_reader.preprocess()
if netflix_reader.data_leakage_warning:
    print('data leakage!')
netflix_reader.write_netflix_data('./files')
