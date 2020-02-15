import tkinter as tk
from math import cos, sin, pi
from time import time, sleep
from core.vector import Vector

root = tk.Tk()
width = 1280
height = 720
framerate = 30
camera = Vector(0, 0, 0)
rotation = Vector(0, 0, 0)
offset = Vector(0, 0, 0)

canvas = tk.Canvas(
    root,
    width = width,
    height = height,
    bg = "#000",
    highlightthickness = 0
)
canvas.pack(fill = "both", expand = True)

binds = {
	# Movement ............
	"forward": (87, "press"),
	"backward": (83, "press"),
	"up": (32, "press"),
	"down": (17, "press"),
	"speed": (16, "press"),
	"left": (81, "press"),
	"right": (69, "press"),
	# Camera Direction ....
	"look-left": (65, "press"),
	"look-right": (68, "press"),
	"look-up": (38, "press"),
	"look-down": (40, "press"),
	"tilt-left": (37, "press"),
	"tilt-right": (39, "press"),
	# Camera Offset .......
	"camoffset-left": (70, "press"),
	"camoffset-right": (72, "press"),
	"camoffset-up": (84, "press"),
	"camoffset-down": (71, "press"),
	# Gameplay ............
	"reset": (82, "press"),
}