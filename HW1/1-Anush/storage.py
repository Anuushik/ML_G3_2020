from abc import ABC, abstractmethod
import csv
import os



class Persistor:
    """ A class that works with files"""

    def read_raw_data(self):
        raise NotImplementedError

    def save_raw_data(self, data, filename):
        """
        This function saves the content into the file as it is
        """

        with open(filename, 'w') as myFile:
            # write the data into myFile

            # writer = csv.writer(myFile)
            myFile.write(data)

    def save_csv(self, data):
        raise NotImplementedError

    def append_data(self, data):
        raise NotImplementedError


if __name__ == '__main__':
    # with open('csvexample.csv', 'w', newline='') as myFile:
    #     writer = csv.writer(myFile)

    # with open('csvexample.csv', 'r', newline='') as myFile:
    #     reader = csv.reader(myFile)
    #     row = "item, title, name\n"
    #     for row in reader:
    #         print(row)

    persistor = Persistor()
    persistor.save_raw_data("text","csvexample.csv")