from abc import ABC, abstractmethod
import csv
import os



class Persistor(ABC):

    @abstractmethod
    def read_raw_data(self):
        raise NotImplementedError

    @abstractmethod
    def save_raw_data(self, data):
        raise NotImplementedError

    @abstractmethod
    def save_csv(self, data):
        raise NotImplementedError

    @abstractmethod
    def append_data(self, data):
        raise NotImplementedError

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'csvexample.csv')


with open(my_file,'w', newline='') as myFile:
    reader = csv.reader(myFile)
    writer = csv.writer(myFile)
    row = "item, title, name\n"
   # for row in reader:
   # print(row)
