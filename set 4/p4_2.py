import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        dto = (self.x**2 + self.y**2)**0.5
        return dto

    def euclidean_distance(self, other):
        euc_dist = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return euc_dist

    def manhattan_distance(self, other):
        man_dist = abs(self.x - other.x) + abs(self.y - other.y)
        return man_dist

    def angle_between(self, other):
        vertical = other.y - self.y
        horizontal = other.x - self.x
        ang_bet = math.atan2(vertical, horizontal)
        return ang_bet

class Triangle():
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    def float_equal(self, n1, n2):
        if abs(n1 - n2) < 10 ** -6:
            return True
        
        else:
            return False

    def side_lengths(self):
        d_p1_p2 = self.p1.euclidean_distance(self.p2)
        d_p2_p3 = self.p2.euclidean_distance(self.p3)
        d_p3_p1 = self.p3.euclidean_distance(self.p1)
        lados = d_p1_p2, d_p2_p3, d_p3_p1
        return tuple(lados)
    
    def angles(self):
        lados = self.side_lengths()

        l1 = lados[0]
        l2 = lados[1]
        l3 = lados[2]

        a_r1_r2 = math.acos((l1 ** 2 + l2 ** 2 - l3 ** 2) / (2 * l1 * l2))
        a_r2_r3 = math.acos((l2 ** 2 + l3 ** 2 - l1 ** 2) / (2 * l2 * l3))
        a_r3_r1 = math.acos((l3 ** 2 + l1 ** 2 - l2 ** 2) / (2 * l3 * l1))

        angulos = a_r1_r2, a_r2_r3, a_r3_r1
        return tuple(angulos)

    def side_classification(self):
        lados = self.side_lengths()
        l1 = lados[0]
        l2 = lados[1]
        l3 = lados[2]
        
        if self.float_equal(l1, l2) and self.float_equal(l2, l3) and self.float_equal(l3, l1):
            return "equilateral"
        
        elif l1 != l2 != l3:
            return "scalene"
        
        else:
            return "isosceles"

    def angle_classification(self):
        if self.float_equal(max(self.angles()), math.pi/3):
            return "equiangular"

        elif max(self.angles()) < math.pi/2:
            return "acute"
        
        elif max(self.angles()) == math.pi/2:
            return "right"

        else:
            return "obtuse"

    def is_right(self):
        if self.angle_classification() == "right":
            return True
        else:
            return False

    def area(self):
        semi_p = self.perimeter()/2

        lados = self.side_lengths()
        l1 = lados[0]
        l2 = lados[1]
        l3 = lados[2]

        heron = (semi_p * (semi_p - l1) * (semi_p - l2) * (semi_p - l3)) ** 0.5
        return float(heron)

    def perimeter(self):
        return float(sum(self.side_lengths()))
