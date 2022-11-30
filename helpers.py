import pygame
from vosk import Model, KaldiRecognizer
from queue import Queue
import json
import requests
from variables import *
from data import *


# Microphone recording function
def record_microphone(chunk=1024):
    p = pyaudio.PyAudio()

    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=FRAME_RATE,
                    input=True,
                    frames_per_buffer=chunk)  # chunk - how often data will be fetched from the microphone

    frames = []  # a list for storing microphone recordings
    for i in range(0, int((FRAME_RATE * RECORD_SECONDS) / chunk)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    return frames


model = Model(model_name="vosk-model-small-pl-0.22")
rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)

# we create the 'values' queue, into which the coordinates will be put together with the number
values = Queue()


# A function that recognizes speech from the recording and replaces the transcript
# to the appropriate numeric values
def speech_recognition(frames):
    rec.AcceptWaveform(b''.join(frames))  # combining all the pieces into one file
    result = rec.Result()
    trans = json.loads(result)["text"]  # recording transcript
    try:
        row, = (row_map[x] for x in trans.split() if x in row_map.keys())
        col, val = (nums_map[x] for x in trans.split() if x in nums_map.keys())
        vals = (row, col, val)
        values.put(vals)  # we put the values into the queue
        return vals
    # if something is not recognized in the transcript, an appropriate message will be returned
    except:
        return "Wrong input! Please, try again."


# Sudoku API
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=medium")
grid = response.json()["board"]
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


# This function responsible for the button after pressing record
def start_recording(win):
    # button change when pressing record
    font = pygame.font.SysFont("Comic Sans MS", 25)
    label = font.render("Recording...", True, (255, 255, 255))
    pygame.draw.rect(win, background_color, (BUT_X - 60, BUT_Y + 60, 350, 50))
    pygame.draw.rect(win, (255, 0, 0), (BUT_X, BUT_Y, 150, 50))
    win.blit(label, (BUT_X + 10, BUT_Y + 5))
    pygame.display.update()

    # turn on recording and then speech recognition
    frames = record_microphone()
    vals = speech_recognition(frames)

    # displays a message in case of incorrect speech recognition
    if type(vals) == str:
        font = pygame.font.SysFont("Comic Sans MS", 20)
        label = font.render(vals, True, original_grid_element_color)
        pygame.draw.rect(win, background_color, (BUT_X + 20, BUT_Y + 50, 150, 50))
        win.blit(label, (BUT_X - 60, BUT_Y + 60))
        pygame.display.update()

    # the button returns to the initial state
    font = pygame.font.SysFont("Comic Sans MS", 25)
    label = font.render("Start", True, (255, 255, 255))
    pygame.draw.rect(win, (0, 0, 255), (BUT_X, BUT_Y, 150, 50))
    win.blit(label, (BUT_X + 40, BUT_Y + 5))
    pygame.display.update()


# Inserting a number into sudoku based on the commands
def insert(win, vals):
    i, j = vals[0], vals[1]
    value = vals[2]
    myfont = pygame.font.SysFont("Comic Sans MS", 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if (grid_original[i - 1][j - 1] != 0):
            return
        if (value == 0):
            grid[i - 1][j - i] = 0
            pygame.draw.rect(win, background_color,
                             (j * 50 + buffer + 100, i * 50 + buffer + 50, 50 - 2 * buffer, 50 - 2 * buffer))
            pygame.display.update()
            return
        if (0 < value < 10):
            pygame.draw.rect(win, background_color,
                             (j * 50 + buffer + 100, i * 50 + buffer + 50, 50 - 2 * buffer, 50 - 2 * buffer))
            text = myfont.render(str(value), True, (0, 0, 255))
            win.blit(text, (j * 50 + 115, i * 50 + 50))
            grid[i - 1][j - 1] = value
            pygame.display.update()
            return
