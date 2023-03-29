import netflix_data_reader as reader

netflix_reader = reader.NetflixReader()
print(netflix_reader.read_netflix_data(file_path="./files/netflix_data.csv"))
