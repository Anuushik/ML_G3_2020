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

with open('csvexample.csv', 'w', newline='') as myFile:
    writer = csv.writer(myFile)

with open('csvexample.csv', 'r', newline='') as myFile:
    reader = csv.reader(myFile)
    row = "item, title, name\n"
    for row in reader:
        print(row)