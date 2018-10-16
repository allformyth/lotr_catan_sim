class Territory:
    def __init__(self, col_index, row_index, resource, number):
        self.col_index = col_index
        self.row_index = row_index
        self.resource = resource
        self.number = number
        self.is_mining = False
        #self.lands = lands
        #self.adjacents = dict()

    @property
    def cpm_num(self):
        result = self.col_index * 10 + self.row_index
        return result

    def __str__(self):
        return "zuobiaoshiiiii: " + str(self.col_index) + "," + str(self.row_index)

    def __repr__(self):
        return "zuobiaoshi: " + str(self.col_index) + "," + str(self.row_index)




class Land:
    def __init__(self, adjcents_territory:[]):
        self.adjcents_territory = sorted(adjcents_territory, key= lambda x: x.cpm_num)
        self.city = -1

