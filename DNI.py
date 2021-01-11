class DNI:
    
    @staticmethod
    def function(cost):
        if cost == True:
            return cost
        else:
            return "Tus muertos"

    @staticmethod
    def numCount(dni):
        if type(dni) == object:
            cont = 0
            for char in dni.dni:
                if char in dni.nums:
                    cont += 1
                elif char in dni.leters:
                    cont += 1
            if cont == len(dni.dni):
                return True
        return False
    
    def __init__(self, dni):
        if type(dni) == str:
            self.dni = dni
            self.leters = "ABCDEFGHJKLMNPQRSTVWXYZ"
            self.nums = "0123456789"

    def verifyDNI(self):
        return 0

    def get_num(self):
        if len(self.dni) > 0:
            for let in self.dni[ : len(self.dni) - 1]:
                if let not in self.nums:
                    return "DNI format incorrect."
            return self.dni[ : len(self.dni) - 1]
        else:
            return "DNI format incorrect."