import netflix_data_reader as reader

netflix_reader = reader.NetflixReader()
netflix_reader.read_netflix_data(file_path="./files/netflix_data.csv")
netflix_reader.preprocess()
netflix_reader.write_netflix_data('./files')

