import json


def read_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    
    print("First file:", data1)
    print("Second file:", data2)
    
    # В будущем здесь будет логика сравнения, пока возвращаем заглушку
    # return str(data1) + str(data2)


