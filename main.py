import os, time, sys
from colorama import Fore

class LangtonAnt:
    def __init__(self, width=50, height=30):
        self.width = width
        self.height = height
        self.visited = set() 
        self.ant_x = width // 2
        self.ant_y = height // 2
        self.direction = 0  # 0=up, 1=right, 2=down, 3=left
        self.step = 0
        
    def is_visited(self, x, y):
        return (x, y) in self.visited
    
    def toggle_cell(self, x, y):
        pos = (x, y)
        if pos in self.visited:
            self.visited.remove(pos)
        else:
            self.visited.add(pos)
    
    def move_forward(self):
        self.ant_x += (1 if self.direction == 1 else -1 if self.direction == 3 else 0)
        self.ant_y += (1 if self.direction == 2 else -1 if self.direction == 0 else 0)
    
    def turn_right(self):
        self.direction = (self.direction + 1) % 4
    
    def turn_left(self):
        self.direction = (self.direction - 1) % 4
    
    def display(self):
        buffer = "\x1b[H\x1b[2J"  # Cursor home + clear screen
        
        for y in range(self.height):
            for x in range(self.width):
                if x == self.ant_x and y == self.ant_y:
                    buffer += Fore.RED + "@"
                elif self.is_visited(x, y):
                    buffer += Fore.GREEN + "O"
                else:
                    buffer += Fore.WHITE + "."
            buffer += "\n"
        
        print(buffer, end="", flush=True)
    
    def run(self, steps):
        
        try:
            for _ in range(steps):
                if self.is_visited(self.ant_x, self.ant_y):
                    self.turn_left()
                else:
                    self.turn_right()
                
                self.toggle_cell(self.ant_x, self.ant_y)
                self.move_forward()
                self.step += 1
                
                self.display()
                time.sleep(0.05)

        except KeyboardInterrupt:
            print("\nProgram ended")


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        steps = 10000
    else: 
        steps = int(sys.argv[1])
    
    langton = LangtonAnt(width=40, height=20)
    langton.run(steps)