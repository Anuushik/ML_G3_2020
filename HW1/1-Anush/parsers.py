from object import TV


class Parser:


    def __init__(self, parser):
        self.parser = parser
        
    def parse_object(self, content):

        return TV(
            name=self.get_name(content),
            property_2=self.get_property_2(content),
            property_3=self.get_property_3(content),
            property_4=self.get_property_4(content),
            property_5=self.get_property_5(content)
        )

    def get_name(self, content):
        """ Finds a name in the content """
        return

    def get_property_2(self, content):
        return

    def get_property_3(self, content):
        return

    def get_property_4(self, content):
        return

    def get_property_5(self, content):
        return

