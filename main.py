import netflix_data_reader as reader

netflix_reader = reader.NetflixReader()
netflix_reader.read_netflix_data(file_path="./files/netflix_data.csv")
print(netflix_reader.netflix_data_raw)