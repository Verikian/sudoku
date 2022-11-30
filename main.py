import platform
import os
from helpers import *
from variables import *


# Main function
def sudoku():
    if platform.system() == 'Windows':
        os.environ['SDL_VIDEODRIVER'] = 'windib'
    else:
        pass
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))  # creates a window
    pygame.display.set_caption("Sudoku")  # title
    win.fill(background_color)  # background color
    myfont = pygame.font.SysFont("Comic Sans MS", 35)  # font

    # the grid creation
    for i in range(0, 10):
        if (i % 3 == 0):
            # vertical lines of blocks 3x3
            pygame.draw.line(win, original_grid_element_color, (150 + 50 * i, 100), (150 + 50 * i, 550), 4)
            # horizontal lines of blocks 3x3
            pygame.draw.line(win, original_grid_element_color, (150, 100 + 50 * i), (600, 100 + 50 * i), 4)
        # vertical lines
        pygame.draw.line(win, original_grid_element_color, (150 + 50 * i, 50), (150 + 50 * i, 550), 2)
        # horizontal lines
        pygame.draw.line(win, original_grid_element_color, (15, 100 + 50 * i), (600, 100 + 50 * i), 2)

    pygame.display.update()

    # enter the output numbers for sudoku
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j + 1) * 50 + 115, (i + 1) * 50 + 50))

    # enter the coordinates X
    for i in range(0, len(grid[0])):
        value = myfont.render(str(i + 1), True, coords_color)
        win.blit(value, ((i + 1) * 50 + 115, 50))

        # enter the coordinates Y (the names keywords)
    for i, name in zip(range(0, len(grid[0])), row_map.keys()):
        value = myfont.render(name.capitalize(), True, coords_color)
        win.blit(value, (15, (i + 1) * 50 + 50))

    # button Start
    font = pygame.font.SysFont("Comic Sans MS", 25)
    label = font.render("Start", 1, (255, 255, 255))
    pygame.draw.rect(win, (0, 0, 255), (BUT_X, BUT_Y, 150, 50))
    win.blit(label, (BUT_X + 40, BUT_Y + 5))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            # if the button has been clicked, the function with recording is activated
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(BUT_X, BUT_Y, 150, 50).collidepoint(pygame.mouse.get_pos()):
                    start_recording(win)
                    # if X (exit from the application) is clicked, everything is turned off
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                return

        # if the 'values' queue is not empty, we fetch data from it
        while not values.empty():
            vals = values.get()
            insert(win, vals)  # execute the insert() function


# execution
sudoku()
