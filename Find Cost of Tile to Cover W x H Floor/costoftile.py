def cost_of_tile(height,width,cost_per_tile):
    return height*width*cost_per_tile

if __name__ == '__main__':
    height = float(input('Enter a height: '))
    width = float(input('Enter a width: '))
    cost_per_tile = float(input('Enter a cost per tile: '))
    print(f"Total cost of tile to cover a floor plan of {width} X {height} is {cost_of_tile(height,width,cost_per_tile)}.")