import random
import copy

# Ejercicio 2

class Environment:
    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = init_posX
        self.posY = init_posY
        self.dirt_rate = dirt_rate
        self.grid = [[random.random() < dirt_rate for _ in range(sizeX)] for _ in range(sizeY)]
        self.performance = 0
        self.actions = 0

    def accept_action(self, action):
        self.actions += 1        
        if action == "Arriba" and self.posY > 0:
            self.posY -= 1
        elif action == "Abajo" and self.posY < self.sizeY - 1:
            self.posY += 1
        elif action == "Izquierda" and self.posX > 0:
            self.posX -= 1
        elif action == "Derecha" and self.posX < self.sizeX - 1:
            self.posX += 1
        elif action == "Limpiar" and self.is_dirty():
            self.performance += 1
            self.grid[self.posY][self.posX] = False
        
    def is_dirty(self):
        return self.grid[self.posY][self.posX]

    def get_performance(self):
        # return round(self.performance/(self.sizeX*self.sizeY)*100,1)
        return self.performance

    def print_environment(self):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                if x == self.posX and y == self.posY:
                    print("A", end=" ")
                elif self.grid[y][x]:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()
        print(f"VecesLimpia: {self.performance}, NroTotalAcciones: {self.actions}")

# Ejercicio 3

class Agent:
    def __init__(self, env):
        self.env = env
    def up(self):
        self.env.accept_action("Arriba")
    def down(self):
        self.env.accept_action("Abajo")
    def left(self):
        self.env.accept_action("Izquierda")
    def right(self):
        self.env.accept_action("Derecha")
    def suck(self):
        self.env.accept_action("Limpiar")
    def idle(self):
        self.env.accept_action("NoHacerNada")

    def perspective(self, env):
        return {
            "posX": env.posX, # no usado
            "posY": env.posY, # no usado
            "is_dirty": env.is_dirty()
        }
    
    def think(self):
        perception = self.perspective(self.env)       
        if perception["is_dirty"]:
            return self.suck()        
        action = random.choice([self.up, self.down, self.left, self.right])
        return action()
            
    def thinkRandom(self):
        action = random.choice([self.up, self.down, self.left, self.right, self.suck])
        return action()

if __name__ == "__main__":
    for dirt_rate in [0.1,0.2,0.4,0.8]:  
        for i in range(7):
            size = 2**(i+1)
            print(f"\nEntorno de {size}x{size}")
            list_reflexivo = []
            list_random = []
            for _ in range(10):
                posX = random.randint(0, size-1)
                posY = random.randint(0, size-1)
                env = Environment(size, size, posX, posY, dirt_rate)
                env1 = copy.deepcopy(env)
                env2 = copy.deepcopy(env)
                agent1 = Agent(env1)
                agent2 = Agent(env2)
                for _ in range(1000):
                    agent1.think()
                    agent2.thinkRandom()
                list_reflexivo.append(env1.get_performance())
                list_random.append(env2.get_performance())               
            print(f"\nRatio {dirt_rate} reflexivo simple: {list_reflexivo}", end="")
            print(f"\nRatio {dirt_rate} aleatorio: {list_random}")
                
'''
Entorno de 2x2

Ratio 0.1 reflexivo simple: [1, 1, 0, 1, 0, 0, 0, 0, 0, 1]
Ratio 0.1 aleatorio: [1, 1, 0, 1, 0, 0, 0, 0, 0, 1]

Entorno de 4x4

Ratio 0.1 reflexivo simple: [1, 1, 0, 4, 1, 1, 1, 2, 1, 1]
Ratio 0.1 aleatorio: [1, 1, 0, 4, 1, 1, 1, 2, 1, 1]

Entorno de 8x8

Ratio 0.1 reflexivo simple: [12, 5, 4, 7, 8, 6, 11, 4, 7, 5]
Ratio 0.1 aleatorio: [10, 5, 4, 6, 4, 4, 9, 3, 7, 5]

Entorno de 16x16

Ratio 0.1 reflexivo simple: [10, 20, 17, 17, 20, 19, 23, 20, 16, 21]
Ratio 0.1 aleatorio: [6, 9, 7, 9, 12, 16, 13, 5, 8, 11]

Entorno de 32x32

Ratio 0.1 reflexivo simple: [19, 23, 32, 30, 28, 26, 31, 20, 29, 37]
Ratio 0.1 aleatorio: [7, 12, 8, 11, 6, 11, 10, 14, 9, 10]

Entorno de 64x64

Ratio 0.1 reflexivo simple: [17, 22, 42, 32, 31, 22, 37, 39, 30, 24]
Ratio 0.1 aleatorio: [11, 7, 11, 11, 17, 18, 12, 11, 11, 8]

Entorno de 128x128

Ratio 0.1 reflexivo simple: [34, 27, 38, 26, 29, 45, 26, 19, 23, 29]
Ratio 0.1 aleatorio: [10, 15, 11, 14, 13, 6, 10, 23, 6, 14]

Entorno de 2x2

Ratio 0.2 reflexivo simple: [0, 1, 0, 0, 0, 1, 0, 2, 1, 0]
Ratio 0.2 aleatorio: [0, 1, 0, 0, 0, 1, 0, 2, 1, 0]

Entorno de 4x4

Ratio 0.2 reflexivo simple: [3, 5, 4, 2, 5, 5, 2, 4, 3, 4]
Ratio 0.2 aleatorio: [3, 5, 4, 2, 5, 5, 2, 4, 3, 4]

Entorno de 8x8

Ratio 0.2 reflexivo simple: [13, 16, 9, 8, 8, 21, 12, 14, 5, 9]
Ratio 0.2 aleatorio: [13, 14, 9, 7, 6, 17, 10, 13, 4, 8]

Entorno de 16x16

Ratio 0.2 reflexivo simple: [36, 33, 32, 40, 39, 25, 34, 26, 41, 36]
Ratio 0.2 aleatorio: [19, 14, 27, 18, 18, 20, 26, 12, 21, 18]

Entorno de 32x32

Ratio 0.2 reflexivo simple: [40, 54, 47, 37, 63, 54, 58, 44, 60, 50]
Ratio 0.2 aleatorio: [21, 26, 14, 19, 22, 19, 18, 16, 22, 21]

Entorno de 64x64

Ratio 0.2 reflexivo simple: [59, 47, 43, 59, 61, 54, 73, 45, 68, 71]
Ratio 0.2 aleatorio: [25, 25, 22, 23, 14, 20, 31, 23, 22, 26]

Entorno de 128x128

Ratio 0.2 reflexivo simple: [69, 78, 68, 67, 70, 54, 71, 68, 88, 58]
Ratio 0.2 aleatorio: [26, 14, 25, 16, 19, 24, 19, 24, 33, 29]

Entorno de 2x2

Ratio 0.4 reflexivo simple: [2, 2, 0, 4, 0, 1, 3, 2, 2, 1]
Ratio 0.4 aleatorio: [2, 2, 0, 4, 0, 1, 3, 2, 2, 1]

Entorno de 4x4

Ratio 0.4 reflexivo simple: [8, 8, 8, 7, 8, 5, 6, 9, 5, 5]
Ratio 0.4 aleatorio: [8, 8, 8, 7, 8, 5, 6, 9, 5, 5]

Entorno de 8x8

Ratio 0.4 reflexivo simple: [16, 25, 24, 29, 24, 17, 31, 24, 30, 26]
Ratio 0.4 aleatorio: [11, 21, 19, 29, 19, 16, 21, 20, 26, 25]

Entorno de 16x16

Ratio 0.4 reflexivo simple: [61, 85, 65, 82, 63, 66, 71, 58, 83, 61]
Ratio 0.4 aleatorio: [34, 29, 34, 41, 37, 35, 28, 31, 43, 24]

Entorno de 32x32

Ratio 0.4 reflexivo simple: [112, 123, 100, 74, 113, 123, 109, 120, 75, 103]
Ratio 0.4 aleatorio: [45, 45, 39, 44, 59, 49, 53, 51, 43, 48]

Entorno de 64x64

Ratio 0.4 reflexivo simple: [114, 137, 84, 105, 98, 145, 120, 125, 155, 101]
Ratio 0.4 aleatorio: [43, 46, 40, 55, 52, 44, 54, 42, 51, 47]

Entorno de 128x128

Ratio 0.4 reflexivo simple: [116, 136, 128, 135, 103, 113, 106, 127, 114, 125]
Ratio 0.4 aleatorio: [63, 52, 51, 53, 39, 50, 51, 49, 52, 39]

Entorno de 2x2

Ratio 0.8 reflexivo simple: [2, 4, 3, 4, 4, 4, 3, 3, 2, 3]
Ratio 0.8 aleatorio: [2, 4, 3, 4, 4, 4, 3, 3, 2, 3]

Entorno de 4x4

Ratio 0.8 reflexivo simple: [13, 13, 13, 10, 13, 12, 11, 12, 12, 12]
Ratio 0.8 aleatorio: [13, 13, 13, 10, 13, 12, 11, 12, 12, 12]

Entorno de 8x8

Ratio 0.8 reflexivo simple: [51, 55, 52, 53, 51, 50, 46, 47, 51, 51]
Ratio 0.8 aleatorio: [38, 48, 46, 47, 37, 44, 38, 40, 46, 46]

Entorno de 16x16

Ratio 0.8 reflexivo simple: [130, 143, 146, 177, 150, 117, 162, 117, 103, 119]
Ratio 0.8 aleatorio: [84, 72, 77, 64, 76, 66, 74, 87, 70, 78]

Entorno de 32x32

Ratio 0.8 reflexivo simple: [145, 200, 213, 230, 230, 207, 206, 201, 256, 217]
Ratio 0.8 aleatorio: [85, 93, 83, 87, 89, 57, 99, 85, 75, 93]

Entorno de 64x64

Ratio 0.8 reflexivo simple: [212, 184, 231, 219, 233, 264, 197, 265, 238, 244]
Ratio 0.8 aleatorio: [98, 96, 98, 99, 78, 84, 89, 90, 106, 84]

Entorno de 128x128

Ratio 0.8 reflexivo simple: [250, 217, 226, 246, 219, 169, 184, 213, 214, 251]
Ratio 0.8 aleatorio: [85, 91, 101, 100, 76, 85, 87, 98, 94, 89]
'''