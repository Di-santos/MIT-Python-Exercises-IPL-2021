class Vector:
    def __init__(self, nums):
        self.nums = nums

    def as_list(self):
        return list(self.nums)

    def size(self):
        return len(self.nums)

    def magnitude(self): 
        valor = 0
        for num in self.nums:
            valor += num ** 2
            
        mag = valor ** 0.5

        return mag

    def euclidean_distance(self, other):
        vectors_list = []
        euc_dist = 0

        for i in range(len(self.nums)):
            vls = self.nums[i]
            vlo = other.nums[i]
            par = [vls, vlo]
            vectors_list.append(par)
        
        for i in range(len(vectors_list)):
            euc_dist += (vectors_list[i][0] - vectors_list[i][1]) ** 2

        return euc_dist ** 0.5

    def normalized(self):
        magnitude = self.magnitude()
        normalizado = []

        for num in self.nums:
            normalizado.append(num / magnitude)

        return Vector(normalizado)

    def cosine_similarity(self, other):
        prod_escalar = self * other  
        return prod_escalar / (self.magnitude() * other.magnitude())

    def __add__(self, other):
        if isinstance(other, Vector) and len(self.nums) == len(other.nums):
            vectors_list = []

            for i in range(len(self.nums)):
                vls = self.nums[i]
                vlo = other.nums[i]
                par = [vls, vlo]
                vectors_list.append(par)
            
            for i in range(len(vectors_list)):
                vectors_list[i] = (vectors_list[i][0] + vectors_list[i][1])
            
            return Vector(vectors_list)
        
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Vector) and len(self.nums) == len(other.nums):
            vectors_list = []

            for i in range(len(self.nums)):
                vls = self.nums[i]
                vlo = other.nums[i]
                par = [vls, vlo]
                vectors_list.append(par)
            
            for i in range(len(vectors_list)):
                vectors_list[i] = (vectors_list[i][0] - vectors_list[i][1])
            
            return Vector(vectors_list)
        
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Vector) and len(self.nums) == len(other.nums):
            vectors_list = []
            valor = 0

            for i in range(len(self.nums)):
                vls = self.nums[i]
                vlo = other.nums[i]
                par = [vls, vlo]
                vectors_list.append(par)
            
            for i in range(len(vectors_list)):
                vectors_list[i] = (vectors_list[i][0] * vectors_list[i][1])
            
            return sum(vectors_list)
        
        elif isinstance(other, (int, float)):
            novo_vetor = []

            for num in self.nums:
                novo_vetor.append(num * other)  

            return Vector(novo_vetor)
            
        else:
            return None

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other,float):
            return self * (1 / other)  
        
        else:
            return None

