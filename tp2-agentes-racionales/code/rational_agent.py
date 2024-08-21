import random

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
        return round(self.performance/(self.sizeX*self.sizeY)*100,1)
        # return round((self.performance/self.actions)*1000,1)

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
        # if perception["is_dirty"]:
        #     return self.suck()        
        # action = random.choice([self.up, self.down, self.left, self.right])
        action = random.choice([self.up, self.down, self.left, self.right, self.suck])
        return action()

if __name__ == "__main__":
   for i in range(7):
        size = 2**(i+1)
        print(f"\nEntorno de {size}x{size}")  
        for dirt_rate in [0.1,0.2,0.4,0.8,1.0]:
            print(f"\nRatio {dirt_rate}: ", end="")
            for j in range(10):
                posX = random.randint(0, size-1)
                posY = random.randint(0, size-1)
                env = Environment(size, size, posX, posY, dirt_rate)
                agent = Agent(env)
                for _ in range(1000):
                    agent.think()
                print(env.get_performance(), end=" ")
                #print(f"{env.get_performance()} ({env.performance}, {env.actions})", end=" ")
                if dirt_rate == 1.0 and j == 9: print()
'''
Resultados Ejercicio 4

Entorno de 2x2

Ratio 0.1: 0.0 0.0 0.0 25.0 0.0 0.0 0.0 25.0 0.0 0.0 
Ratio 0.2: 25.0 50.0 25.0 0.0 0.0 25.0 50.0 50.0 75.0 0.0 
Ratio 0.4: 50.0 25.0 25.0 25.0 50.0 75.0 75.0 25.0 25.0 0.0 
Ratio 0.8: 50.0 75.0 100.0 50.0 100.0 50.0 100.0 100.0 50.0 75.0 
Ratio 1.0: 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 

Entorno de 4x4

Ratio 0.1: 0.0 6.2 6.2 12.5 18.8 6.2 0.0 0.0 12.5 0.0 
Ratio 0.2: 25.0 18.8 25.0 31.2 12.5 31.2 0.0 18.8 6.2 25.0 
Ratio 0.4: 43.8 31.2 37.5 31.2 62.5 43.8 43.8 50.0 50.0 43.8 
Ratio 0.8: 81.2 87.5 87.5 87.5 62.5 68.8 87.5 87.5 81.2 75.0 
Ratio 1.0: 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 

Entorno de 8x8

Ratio 0.1: 17.2 12.5 9.4 9.4 10.9 9.4 12.5 12.5 9.4 6.2 
Ratio 0.2: 14.1 20.3 20.3 20.3 21.9 20.3 14.1 25.0 17.2 21.9
Ratio 0.4: 45.3 34.4 48.4 37.5 40.6 34.4 39.1 37.5 45.3 32.8 
Ratio 0.8: 81.2 70.3 78.1 87.5 71.9 78.1 84.4 82.8 84.4 78.1 
Ratio 1.0: 96.9 100.0 98.4 100.0 100.0 98.4 98.4 100.0 98.4 100.0

Entorno de 16x16

Ratio 0.1: 3.1 7.0 9.0 3.5 5.5 5.9 6.6 8.2 10.9 4.3 
Ratio 0.2: 18.4 7.4 12.9 15.6 15.2 18.4 14.1 14.5 15.2 12.5 
Ratio 0.4: 29.3 30.1 26.2 29.7 26.2 35.2 29.3 25.8 25.0 20.3 
Ratio 0.8: 54.7 63.3 57.0 44.1 36.7 50.4 57.0 40.6 63.7 56.6
Ratio 1.0: 78.5 65.2 71.1 71.9 85.5 62.9 72.3 55.9 43.4 78.1 

Entorno de 32x32

Ratio 0.1: 1.6 2.8 4.0 2.8 2.3 2.1 2.5 2.7 3.6 3.0 
Ratio 0.2: 3.9 5.7 4.6 5.8 6.0 4.1 3.4 6.2 5.2 3.5 
Ratio 0.4: 10.1 10.2 8.9 10.2 7.0 10.6 9.3 10.2 10.4 9.5
Ratio 0.8: 18.4 18.3 15.6 15.8 17.5 17.1 20.0 18.8 18.6 20.7 
Ratio 1.0: 24.3 19.3 23.7 21.9 19.9 25.3 23.5 20.8 19.8 26.7 

Entorno de 64x64

Ratio 0.1: 1.0 0.4 0.6 0.8 0.7 0.6 0.8 0.9 0.7 0.6 
Ratio 0.2: 1.8 1.5 1.3 1.4 1.5 1.6 1.3 1.6 1.4 2.1
Ratio 0.4: 1.2 2.3 3.3 3.3 2.9 2.5 2.2 2.0 3.8 2.3 
Ratio 0.8: 6.0 4.1 3.7 5.8 4.2 5.6 5.2 5.6 5.4 5.6 
Ratio 1.0: 4.9 7.3 7.3 6.6 6.8 6.6 5.2 6.6 6.8 6.6 

Entorno de 128x128

Ratio 0.1: 0.2 0.1 0.2 0.2 0.3 0.3 0.3 0.2 0.3 0.3 
Ratio 0.2: 0.4 0.4 0.3 0.4 0.4 0.5 0.2 0.4 0.4 0.4 
Ratio 0.4: 0.7 0.8 0.9 1.0 0.6 0.7 0.6 1.0 0.6 0.8 
Ratio 0.8: 1.2 1.2 1.4 1.3 1.2 1.0 0.9 1.2 1.5 1.3 
Ratio 1.0: 1.4 1.3 1.3 1.8 1.6 1.7 1.6 1.5 1.7 1.1

'''

'''
Resultados Ejercicio 5

Entorno de 2x2

Ratio 0.1: 50.0 0.0 0.0 0.0 0.0 0.0 25.0 0.0 0.0 0.0 
Ratio 0.2: 0.0 50.0 50.0 50.0 25.0 50.0 0.0 0.0 0.0 25.0 
Ratio 0.4: 25.0 75.0 75.0 25.0 50.0 50.0 25.0 50.0 50.0 25.0 
Ratio 0.8: 50.0 75.0 75.0 100.0 100.0 100.0 75.0 50.0 100.0 100.0 
Ratio 1.0: 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 

Entorno de 4x4

Ratio 0.1: 12.5 6.2 12.5 12.5 18.8 12.5 12.5 6.2 12.5 6.2 
Ratio 0.2: 12.5 6.2 12.5 25.0 25.0 12.5 18.8 18.8 18.8 18.8 
Ratio 0.4: 56.2 37.5 25.0 43.8 25.0 43.8 43.8 62.5 12.5 43.8 
Ratio 0.8: 75.0 75.0 75.0 68.8 87.5 75.0 62.5 87.5 93.8 87.5 
Ratio 1.0: 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 100.0 

Entorno de 8x8

Ratio 0.1: 6.2 14.1 14.1 4.7 17.2 9.4 10.9 15.6 10.9 6.2 
Ratio 0.2: 14.1 20.3 6.2 14.1 9.4 21.9 15.6 21.9 21.9 17.2 
Ratio 0.4: 26.6 32.8 31.2 32.8 39.1 40.6 35.9 28.1 23.4 37.5
Ratio 0.8: 73.4 68.8 70.3 67.2 65.6 67.2 71.9 73.4 64.1 62.5 
Ratio 1.0: 84.4 87.5 89.1 78.1 85.9 81.2 93.8 75.0 84.4 78.1 

Entorno de 16x16

Ratio 0.1: 1.6 3.9 3.1 5.1 3.5 4.7 3.1 1.6 5.5 5.9
Ratio 0.2: 9.8 9.0 12.9 8.2 9.8 9.0 7.8 7.0 7.4 9.4 
Ratio 0.4: 15.6 16.0 14.5 9.8 14.5 16.4 18.8 10.2 14.8 15.6 
Ratio 0.8: 27.3 30.5 23.4 30.5 31.6 31.6 32.0 26.6 24.6 32.4 
Ratio 1.0: 35.9 28.9 43.0 34.4 37.9 38.3 37.5 29.3 38.7 35.9

Entorno de 32x32

Ratio 0.1: 0.8 1.0 1.4 0.7 0.4 0.6 0.9 0.9 1.1 0.8 
Ratio 0.2: 1.7 1.3 2.2 2.5 1.6 2.0 2.0 2.2 2.0 2.3 
Ratio 0.4: 5.1 4.8 4.2 3.8 4.1 3.7 4.2 4.8 4.2 3.5 
Ratio 0.8: 8.3 8.8 7.7 7.6 8.0 8.8 10.1 8.5 7.4 8.5
Ratio 1.0: 10.9 11.8 11.9 10.0 10.6 8.7 10.4 11.1 11.6 12.3 

Entorno de 64x64

Ratio 0.1: 0.3 0.3 0.2 0.1 0.3 0.4 0.5 0.1 0.4 0.2 
Ratio 0.2: 0.6 0.5 0.6 0.5 0.6 0.4 0.7 0.5 0.8 0.5 
Ratio 0.4: 1.0 1.0 1.2 1.2 1.0 0.9 1.1 1.1 1.5 1.1 
Ratio 0.8: 2.2 2.5 2.2 2.4 2.1 2.1 2.6 2.2 2.4 2.2 
Ratio 1.0: 2.9 3.0 3.0 3.0 3.1 2.8 2.8 2.9 2.9 2.8 

Entorno de 128x128

Ratio 0.1: 0.1 0.0 0.0 0.1 0.1 0.1 0.1 0.1 0.1 0.1 
Ratio 0.2: 0.1 0.2 0.1 0.1 0.1 0.1 0.1 0.1 0.2 0.2 
Ratio 0.4: 0.3 0.3 0.3 0.3 0.3 0.2 0.3 0.3 0.4 0.3 
Ratio 0.8: 0.7 0.7 0.6 0.6 0.5 0.5 0.7 0.7 0.5 0.6 
Ratio 1.0: 0.7 0.8 0.8 0.9 0.6 0.6 0.8 0.8 0.7 0.7 

'''

