import pyaudio

CHANNELS = 1
FRAME_RATE = 16000       # sampling
RECORD_SECONDS = 7       # every how many seconds audio will be sent for transcription
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2


# dimensions and colors for sudoku window
WIDTH = 650
HEIGHT = 700
BUT_X = WIDTH - 400
BUT_Y = HEIGHT - 100
background_color = (255, 255, 255)
original_grid_element_color = (0, 0, 0)
coords_color = (170, 74, 68)
buffer = 5