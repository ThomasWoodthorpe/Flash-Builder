import ctypes
import json
import os
import sys
import tkinter as tk
from math import sqrt
from time import sleep
from tkinter import filedialog, messagebox, ttk
import numpy as np
import pyqtgraph.opengl as gl
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QStyleFactory
from pyqtgraph import mkColor
import Ui_about
from customwidget import framecustomwidget, meshcustomwidget
from Ui_builder import Ui_MainWindow

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
APP_ID = "mitgobla.teamlightning.flashbuilder.beta"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)

_TRANSLATE = QtCore.QCoreApplication.translate

APP = QApplication([])
APP.setStyle(QStyleFactory.create('GTK+'))
WINDOW = QMainWindow()
ABOUT_DIALOG = QDialog()
ABOUT_DIALOG.setStyle(QStyleFactory.create('GTK+'))
ABOUT_UI = Ui_about.Ui_Dialog()
ABOUT_UI.setupUi(ABOUT_DIALOG)
UI = Ui_MainWindow()
UI.setupUi(WINDOW)


class Graphics:

    def __init__(self):
        self.display = UI.openGL_preview
        self.current_coordinates = [0, 0, 0]
        self.next_coordinates = [0, 0, 0]
        self.frame = framecustomwidget.CustomFrame(
            color=(0, 0, 0, 255))  # gl.GLBoxItem(color=(0, 0, 0, 255))

        self.grid_size = (5, 5)
        self.grid = None
        self.axis_lines = []
        self.frame.translate(0, 0, 0)
        self.display.addItem(self.frame)

        self.axis_x = np.array([
            [-0.1, -0.1, 0],
            [2, -0.1, 0]
        ])

        self.axis_y = np.array([
            [-0.1, -0.1, 0],
            [-0.1, 2, 0]
        ])

        self.axis_z = np.array([
            [-0.1, -0.1, 0],
            [-0.1, -0.1, 2]
        ])

        self.axis_colour = np.array([
            [0.1, 0.1, 0.1, 1],
            [0.1, 0.1, 0.1, 1]
        ])

        self.block_verts = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1]],
            dtype=float)

        self.block_faces = np.array([
            [0, 1, 2],
            [0, 2, 3],
            [0, 1, 4],
            [1, 5, 4],
            [1, 2, 5],
            [2, 5, 6],
            [2, 3, 6],
            [3, 6, 7],
            [0, 3, 7],
            [0, 4, 7],
            [4, 5, 7],
            [5, 6, 7],
        ])

    def add_grid(self):
        try:
            self.display.removeItem(self.grid)
            for axis in self.axis_lines:
                self.display.removeItem(axis)
            self.axis_lines = []
        except:
            pass
        self.grid = gl.GLGridItem(
            size=QtGui.QVector3D(self.grid_size[0]*2, self.grid_size[1]*2, 1))
        self.grid.setSpacing(
            spacing=QtGui.QVector3D(0.5, 0.5, 0.5))
        self.grid.translate(self.grid_size[0], self.grid_size[1], 0)

        line = gl.GLLinePlotItem(
            pos=self.axis_x, color=self.axis_colour, width=2, antialias=True)
        self.axis_lines.append(line)
        line = gl.GLLinePlotItem(
            pos=self.axis_y, color=self.axis_colour, width=2, antialias=True)
        self.axis_lines.append(line)
        line = gl.GLLinePlotItem(
            pos=self.axis_z, color=self.axis_colour, width=2, antialias=True)
        self.axis_lines.append(line)

        self.display.addItem(self.grid)
        for axis in self.axis_lines:
            self.display.addItem(axis)

    def update_frame(self):
        self.display.removeItem(self.frame)
        if self.next_coordinates[0] > ((self.grid_size[0]*2)-1) or self.next_coordinates[1] > ((self.grid_size[1]*2)-1):
            next_frame = framecustomwidget.CustomFrame(
                color=(255, 0, 0, 255))  # gl.GLBoxItem(color=(255, 0, 0, 255))
            UI.pushButton_place.setDisabled(True)
        elif self.next_coordinates[0] < 0 or self.next_coordinates[1] < 0:
            next_frame = framecustomwidget.CustomFrame(
                color=(255, 0, 0, 255))  # gl.GLBoxItem(color=(255, 0, 0, 255))
            UI.pushButton_place.setDisabled(True)
        elif self.next_coordinates[2] < 0:
            next_frame = framecustomwidget.CustomFrame(
                color=(255, 0, 0, 255))  # gl.GLBoxItem(color=(255, 0, 0, 255))
            UI.pushButton_place.setDisabled(True)
        else:
            next_frame = framecustomwidget.CustomFrame(
                color=(0, 0, 0, 255))  # gl.GLBoxItem(color=(0, 0, 0, 255))
            UI.pushButton_place.setEnabled(True)
        next_frame.translate(
            self.next_coordinates[0], self.next_coordinates[1], self.next_coordinates[2])
        self.frame = next_frame
        self.display.addItem(self.frame)
        self.current_coordinates = self.next_coordinates

    def add_box(self, colour):
        """Create a brick on the display

        Arguments:
            colour {tuple} -- RGBA of the brick
        """

        # box = gl.GLMeshItem(vertexes=self.block_verts,
        #                    faces=self.block_faces,
        #                    color=colour,
        #                    glOptions='opaque',
        #                    smooth=True)
        box = meshcustomwidget.CustomBox(vertexes=self.block_verts,
                                         faces=self.block_faces,
                                         color=colour,
                                         glOptions='opaque',
                                         smooth=True)

        box.translate(
            self.current_coordinates[0], self.current_coordinates[1], self.current_coordinates[2])

        self.display.addItem(box)
        return box

    def add_frame(self):
        """Create a frame on the display
        """

        # gl.GLBoxItem(color=(200, 200, 200, 255))
        frame = framecustomwidget.CustomFrame(
            color=(200, 200, 200, 255), linewidth=1)
        frame.translate(
            self.current_coordinates[0], self.current_coordinates[1], self.current_coordinates[2])

        self.display.addItem(frame)
        return frame


class Builder:

    def __init__(self):
        self.graphics = Graphics()
        self.graphics.add_grid()

        self.model = {}
        self.model_frames = {}
        self.colours = {}
        self.current_colour = "Red"
        self.needToSave = False

    def calculate_print_time(self):
        seconds = 0
        distance = sqrt((sqrt((4)**2 + (1)**2))**2 + (1)**2)
        seconds += 1.7*distance

        for brick in self.model:
            distance = sqrt(
                (sqrt((4-brick[0])**2 + (1-brick[1])**2))**2 + (1-brick[2])**2)
            seconds += 1.7*(distance*2)
        seconds = int(seconds)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        seconds = "%d hours, %02d minutes, %02d seconds" % (h, m, s)
        UI.label_printtime.setText(_TRANSLATE(
            "MainWindow", "Estimated Print Time: "+seconds))

    def moving(self):
        UI.page_fileproperties.setDisabled(True)
        UI.label_status.setText(_TRANSLATE("MainWindow", "Updating..."))
        UI.label_secondstatus.setText(_TRANSLATE(
            "MainWindow", "Please wait"))

    def change_colour(self, colour):
        self.current_colour = colour
        UI.label_colour_selected.setText(_TRANSLATE(
            "MainWindow", "Current Colour: "+colour))
        if colour == "Red":
            UI.pushButton_red_brick.setChecked(True)
            UI.pushButton_blue_brick.setChecked(False)
            UI.pushButton_yellow_brick.setChecked(False)
        elif colour == "Blue":
            UI.pushButton_red_brick.setChecked(False)
            UI.pushButton_blue_brick.setChecked(True)
            UI.pushButton_yellow_brick.setChecked(False)
        elif colour == "Yellow":
            UI.pushButton_red_brick.setChecked(False)
            UI.pushButton_blue_brick.setChecked(False)
            UI.pushButton_yellow_brick.setChecked(True)

    def update(self):
        UI.lcdNumber_bricks.display(len(self.model))
        UI.lcdNumber_instructions.display(
            len(self.graphics.display.items))  # (len(self.model)*3)

        if self.needToSave:
            WINDOW.setWindowTitle(UI.lineEdit_filename.text()+"* - Team Lightning FLASH Software")
        else:
            WINDOW.setWindowTitle(UI.lineEdit_filename.text()+" - Team Lightning FLASH Software")

        if self.model:
            self.calculate_print_time()
        else:
            UI.label_printtime.setText(_TRANSLATE(
                "MainWindow", "Estimated Print Time: N/A seconds"))

    def reset_frame(self):
        self.graphics.next_coordinates = [0, 0, 0]
        self.graphics.update_frame()

    def move_frame(self, axis, displacement):
        self.graphics.next_coordinates[axis] = self.graphics.next_coordinates[axis] + displacement
        self.graphics.update_frame()

    def move_model(self, axis, displacement):
        self.moving()
        translation = (0, 0, 0)
        if axis == 0:
            translation = (displacement, 0, 0)
        elif axis == 1:
            translation = (0, displacement, 0)
        else:
            translation = (0, 0, displacement)

        moving_model = {}
        moving_model_frames = {}
        moving_colours = {}
        for brick in self.model:
            self.model[brick].translate(
                translation[0], translation[1], translation[2])
            self.model_frames[brick].translate(
                translation[0], translation[1], translation[2])

            moving_model[tuple(np.add(brick, translation))] = self.model[brick]
            moving_model_frames[tuple(
                np.add(brick, translation))] = self.model_frames[brick]
            moving_colours[tuple(np.add(brick, translation))
                           ] = self.colours[brick]

        self.model = moving_model
        self.model_frames = moving_model_frames
        self.colours = moving_colours

    def create_brick(self):
        self.moving()
        next_colour = (1, 0, 0, 1)
        next_colour_id = 1
        if self.current_colour == "Red":
            next_colour = (1, 0, 0, 1)
            next_colour_id = 1
        elif self.current_colour == "Blue":
            next_colour = (0, 0, 1, 1)
            next_colour_id = 2
        elif self.current_colour == "Yellow":
            next_colour = (1, 1, 0, 1)
            next_colour_id = 3

        if self.graphics.next_coordinates[0] > ((self.graphics.grid_size[0]*2)-1) or self.graphics.next_coordinates[1] > ((self.graphics.grid_size[1]*2)-1):
            return
        elif self.graphics.next_coordinates[0] < 0 or self.graphics.next_coordinates[1] < 0:
            return

        frame_coordinates = tuple(self.graphics.current_coordinates)

        if tuple(np.add(frame_coordinates, (0.5, 0, 0))) in self.model:
            return
        elif tuple(np.add(frame_coordinates, (-0.5, 0, 0))) in self.model:
            return
        elif tuple(np.add(frame_coordinates, (-0.5, -0.5, 0))) in self.model:
            return
        elif tuple(np.add(frame_coordinates, (0, -0.5, 0))) in self.model:
            return
        elif tuple(np.add(frame_coordinates, (0, 0.5, 0))) in self.model:
            return
        elif tuple(np.add(frame_coordinates, (0.5, -0.5, 0))) in self.model:
            return
        elif tuple(np.add(frame_coordinates, (-0.5, 0.5, 0))) in self.model:
            return
        elif tuple(np.add(frame_coordinates, (0.5, 0.5, 0))) in self.model:
            return

        try:
            self.graphics.display.removeItem(self.model[frame_coordinates])
            del self.model[frame_coordinates]
            self.graphics.display.removeItem(
                self.model_frames[frame_coordinates])
            del self.model_frames[frame_coordinates]
            del self.colours[frame_coordinates]
        except:
            pass
        self.model[frame_coordinates] = self.graphics.add_box(next_colour)
        self.model_frames[frame_coordinates] = self.graphics.add_frame()
        self.colours[frame_coordinates] = next_colour_id

    def delete_brick(self):
        self.moving()
        frame_coordinates = (
            self.graphics.current_coordinates[0], self.graphics.current_coordinates[1], self.graphics.current_coordinates[2])
        try:
            self.graphics.display.removeItem(self.model[frame_coordinates])
            del self.model[frame_coordinates]
            self.graphics.display.removeItem(
                self.model_frames[frame_coordinates])
            del self.model_frames[frame_coordinates]
            del self.colours[frame_coordinates]
        except:
            pass

    def update_grid(self):
        self.moving()
        self.graphics.grid_size = (
            UI.spinBox_grid_x.value()/2, UI.spinBox_grid_y.value()/2)
        self.graphics.add_grid()

    def on_key(self, event):
        if event == QtCore.Qt.Key_W:
            self.move_frame(1, 0.5)
        elif event == QtCore.Qt.Key_S:
            self.move_frame(1, -0.5)
        elif event == QtCore.Qt.Key_A:
            self.move_frame(0, -0.5)
        elif event == QtCore.Qt.Key_D:
            self.move_frame(0, 0.5)
        elif event == QtCore.Qt.Key_Q:
            self.move_frame(2, 1)
        elif event == QtCore.Qt.Key_E:
            self.move_frame(2, -1)
        elif event == QtCore.Qt.Key_Space:
            self.create_brick()
        elif event == QtCore.Qt.Key_1:
            self.change_colour("Red")
        elif event == QtCore.Qt.Key_2:
            self.change_colour("Blue")
        elif event == QtCore.Qt.Key_3:
            self.change_colour("Yellow")
        elif event == QtCore.Qt.Key_X:
            self.delete_brick()


class Application:

    def __init__(self):
        self.builder = Builder()
        self.previous_model = {}
        self.coordinates = []
        self.check = True

    def update_status(self):
        if self.previous_model != self.builder.model:
            self.previous_model = self.builder.model
            self.builder.needToSave = True
            return True

        UI.label_status.setText(_TRANSLATE("MainWindow", "Updating..."))
        UI.label_secondstatus.setText(_TRANSLATE(
            "MainWindow", "Checking for errors."))

        if self.builder.model == {}:
            UI.label_status.setText(_TRANSLATE("MainWindow", "Not Ready"))
            UI.label_secondstatus.setText(
                _TRANSLATE("MainWindow", "No Bricks in model"))
            UI.page_fileproperties.setEnabled(True)
            UI.actionSave.setDisabled(True)
            UI.pushButton_printfile.setDisabled(True)
            return False

        self.coordinates = []
        for brick in self.builder.model:
            self.coordinates.append(brick)

        floating_brick = 0
        outside_brick = 0
        for brick in self.coordinates:
            if brick[2] == 0:
                pass
            elif tuple(np.add(brick, (-0.5, -0.5, -1))) in self.coordinates:
                pass
            elif tuple(np.add(brick, (0.5, -0.5, -1))) in self.coordinates:
                pass
            elif tuple(np.add(brick, (-0.5, 0.5, -1))) in self.coordinates:
                pass
            elif tuple(np.add(brick, (0.5, 0.5, -1))) in self.coordinates:
                pass
            elif tuple(np.add(brick, (0, 0, -1))) in self.coordinates:
                pass
            elif tuple(np.add(brick, (0.5, 0, -1))) in self.coordinates:
                pass
            elif tuple(np.add(brick, (-0.5, 0, -1))) in self.coordinates:
                pass
            elif tuple(np.add(brick, (0, 0.5, -1))) in self.coordinates:
                pass
            elif tuple(np.add(brick, (0, -0.5, -1))) in self.coordinates:
                pass
            else:
                floating_brick += 1

        if floating_brick > 0:
            UI.label_status.setText(_TRANSLATE("MainWindow", "Not Ready"))
            UI.label_secondstatus.setText(_TRANSLATE(
                "MainWindow", str(floating_brick)+" floating brick(s) in model"))
            UI.page_fileproperties.setEnabled(True)
            UI.actionSave.setDisabled(True)
            UI.pushButton_printfile.setDisabled(True)
            return False

        for brick in self.coordinates:
            if brick[0] < 0:
                outside_brick += 1
            elif brick[0] > (self.builder.graphics.grid_size[0]*2)-1:
                outside_brick += 1
            elif brick[1] < 0:
                outside_brick += 1
            elif brick[1] > (self.builder.graphics.grid_size[1]*2)-1:
                outside_brick += 1

        if outside_brick > 0:
            UI.label_status.setText(_TRANSLATE("MainWindow", "Not Ready"))
            UI.label_secondstatus.setText(_TRANSLATE(
                "MainWindow", str(outside_brick)+" brick(s) outside of print area"))
            UI.page_fileproperties.setEnabled(True)
            UI.actionSave.setDisabled(True)
            UI.pushButton_printfile.setDisabled(True)
            return False

        if not UI.lineEdit_filename.text():
            UI.label_status.setText(_TRANSLATE("MainWindow", "Not Ready"))
            UI.label_secondstatus.setText(_TRANSLATE(
                "MainWindow", "No filename provided"))
            UI.page_fileproperties.setEnabled(True)
            UI.actionSave.setDisabled(True)
            UI.pushButton_printfile.setDisabled(True)
            return False

        if not UI.plainTextEdit_filedescription.toPlainText():
            UI.label_status.setText(_TRANSLATE("MainWindow", "Not Ready"))
            UI.label_secondstatus.setText(_TRANSLATE(
                "MainWindow", "No file description provided"))
            UI.page_fileproperties.setEnabled(True)
            UI.actionSave.setDisabled(True)
            UI.pushButton_printfile.setDisabled(True)
            return False

        UI.label_status.setText(_TRANSLATE("MainWindow", "Ready"))
        UI.label_secondstatus.setText(_TRANSLATE(
            "MainWindow", "Ready to generate FLASH file"))

        UI.page_fileproperties.setEnabled(True)
        UI.actionSave.setEnabled(True)
        UI.pushButton_printfile.setEnabled(True)
        return True

    def newFile(self):
        if self.builder.needToSave:
            result = messagebox.askquestion(
                "New File", "You have unsaved changes.\nAre you sure?")
            if result == 'no':
                return
            self.builder.needToSave = False
        try:
            for item in self.builder.model:
                self.builder.graphics.display.removeItem(
                    self.builder.model[item])

            for item in self.builder.model_frames:
                self.builder.graphics.display.removeItem(
                    self.builder.model_frames[item])
        except ValueError:
            pass
        self.builder.model = {}
        self.builder.model_frames = {}
        self.previous_model = {}
        self.builder.graphics.next_coordinates = [0, 0, 0]
        self.builder.graphics.update_frame()
        self.builder.update()
        UI.openGL_preview.setCameraPosition(elevation=45, azimuth=225)
        UI.openGL_preview.opts['center'] = QtGui.QVector3D(
            BUILDER.graphics.grid_size[0]-2, BUILDER.graphics.grid_size[1]-2, 0)
        UI.openGL_preview.opts['distance'] = 40
        UI.openGL_preview.opts['fov'] = 20
        UI.lineEdit_filename.setText("Untitled Model")
        UI.plainTextEdit_filedescription.setPlainText("")

    def reset_camera(self):
        UI.openGL_preview.setCameraPosition(elevation=45, azimuth=225)
        UI.openGL_preview.opts['center'] = QtGui.QVector3D(
            BUILDER.graphics.grid_size[0]-2, BUILDER.graphics.grid_size[1]-2, 0)
        UI.openGL_preview.opts['distance'] = 40
        UI.openGL_preview.opts['fov'] = 20

    def toggle_dark_mode(self):
        if UI.actionToggleDarkMode.isChecked():
            UI.openGL_preview.setBackgroundColor(mkColor(55, 55, 55, 0))
        else:
            UI.openGL_preview.setBackgroundColor(mkColor(155, 155, 155, 0))


class ModelIO:

    def __init__(self, builder, app):
        self.app = app
        self.builder = builder
        self.window = tk.Tk()
        self.window.withdraw()
        self.window.wm_iconbitmap(SCRIPT_DIR+"\\flash-software-128.ico")

    def save(self):
        UI.actionSave.setDisabled(True)
        UI.lineEdit_filename.setDisabled(True)
        UI.plainTextEdit_filedescription.setDisabled(True)
        model = {
            "name": UI.lineEdit_filename.text(),
            "description": UI.plainTextEdit_filedescription.toPlainText(),
            "x": [],
            "y": [],
            "z": [],
            "c": [],
        }
        for block in self.builder.model:
            model["x"].append(block[0])
            model["y"].append(block[1])
            model["z"].append(block[2])
            model["c"].append(self.builder.colours[block])

        data = {
            "name": model["name"],
            "description": model["description"],
            "data": {
                "x": model["x"],
                "y": model["y"],
                "z": model["z"],
                "c": model["c"],
            },
            "grid": {
                "x": UI.spinBox_grid_x.value(),
                "y": UI.spinBox_grid_y.value(),
            },
        }
        file_to_save = filedialog.asksaveasfilename(defaultextension=".flash", filetypes=[
                                                    ('FLASH Model File', '.flash')],
                                                    title="Save Model")
        with open(file_to_save, 'w') as outfile:
            json.dump(data, outfile)

        messagebox.showinfo("Saved Successfully",
                            "Model saved as "+model["name"])
        UI.actionSave.setEnabled(True)
        UI.lineEdit_filename.setEnabled(True)
        UI.plainTextEdit_filedescription.setEnabled(True)
        self.app.builder.needToSave = False


    def open_file(self, openwith):
        file_to_open = filedialog.askopenfilename(defaultextension=".flash", filetypes=[
                                                  ('FLASH Model File', '.flash')],
                                                  title="Open Model")
        if not file_to_open:
            return
        data = {}
        with open(file_to_open) as json_file:
            data = json.load(json_file)
        try:
            UI.lineEdit_filename.setText(data["name"])
            UI.plainTextEdit_filedescription.setPlainText(data["description"])
        except:
            messagebox.showerror("Error", "Invalid FLASH file")
            return

        if data["grid"]["x"] > 50 or data["grid"]["y"] > 50:
            messagebox.showerror(
                "Error", "Invalid FLASH file.\nError: Grid size too large.")
            return

        if data["grid"]["x"] > UI.spinBox_grid_x.value() or data["grid"]["y"] > UI.spinBox_grid_y.value():
            result = messagebox.askquestion(
                "Grid Size", "The file has a larger grid size than your current settings.\nWould you like to update the grid size?", default=messagebox.YES)
            if result == 'yes':
                UI.spinBox_grid_x.setValue(data["grid"]["x"])
                UI.spinBox_grid_y.setValue(data["grid"]["y"])
                self.builder.update_grid()
        if not openwith:
            try:
                for item in self.builder.model:
                    self.builder.graphics.display.removeItem(
                        self.builder.model[item])

                for item in self.builder.model_frames:
                    self.builder.graphics.display.removeItem(
                        self.builder.model_frames[item])
            except ValueError:
                pass
            self.builder.model = {}
            self.builder.model_frames = {}
            self.builder.colours = {}
        self.builder.moving()
        model = data["data"]
        for block in range(len(model["x"])):
            if model["c"][block] == 1:
                self.builder.change_colour("Red")
            elif model["c"][block] == 2:
                self.builder.change_colour("Blue")
            if model["c"][block] == 3:
                self.builder.change_colour("Yellow")
            self.builder.graphics.current_coordinates = [
                model["x"][block], model["y"][block], model["z"][block]]
            if openwith:
                coordinates = (model["x"][block], model["y"]
                               [block], model["z"][block])
                if coordinates not in self.builder.model:
                    self.builder.create_brick()
            else:
                self.builder.create_brick()
        self.builder.change_colour("Red")
        self.builder.moving()


APPLICATION = Application()
WINDOW.setWindowIcon(QtGui.QIcon(SCRIPT_DIR+'\\flash-software-128.png'))
BUILDER = APPLICATION.builder

SAVE_IO = ModelIO(BUILDER, APPLICATION)

APPLICATION.update_status()
TIMER = QtCore.QTimer()
TIMER.timeout.connect(APPLICATION.update_status)
TIMER.start(1000)

BUILD_TIMER = QtCore.QTimer()
BUILD_TIMER.timeout.connect(BUILDER.update)
BUILD_TIMER.start(50)

UI.openGL_preview.setCameraPosition(elevation=45, azimuth=225)
UI.openGL_preview.opts['center'] = QtGui.QVector3D(
    BUILDER.graphics.grid_size[0]-2, BUILDER.graphics.grid_size[1]-2, 0)
UI.openGL_preview.opts['fov'] = 20
UI.openGL_preview.opts['distance'] = 40
UI.label_colour_selected.setText(_TRANSLATE(
    "MainWindow", "Current Colour: "+BUILDER.current_colour))
UI.pushButton_red_brick.clicked.connect(lambda: BUILDER.change_colour("Red"))
UI.pushButton_blue_brick.clicked.connect(lambda: BUILDER.change_colour("Blue"))
UI.pushButton_yellow_brick.clicked.connect(
    lambda: BUILDER.change_colour("Yellow"))
UI.lineEdit_filename.setText("Untitled Model")
WINDOW.setWindowTitle(_TRANSLATE(
    "MainWindow", UI.lineEdit_filename.text()+" - Team Lightning FLASH Software"))
UI.plainTextEdit_filedescription.setPlainText("")


UI.openGL_preview.keyPressed.connect(BUILDER.on_key)

UI.pushButton_left_x.clicked.connect(lambda: BUILDER.move_frame(0, -0.5))
UI.pushButton_right_x.clicked.connect(lambda: BUILDER.move_frame(0, 0.5))

UI.pushButton_down_y.clicked.connect(lambda: BUILDER.move_frame(1, -0.5))
UI.pushButton_up_y.clicked.connect(lambda: BUILDER.move_frame(1, 0.5))

UI.pushButton_down_z.clicked.connect(lambda: BUILDER.move_frame(2, -1))
UI.pushButton_up_z.clicked.connect(lambda: BUILDER.move_frame(2, 1))

UI.pushButton_move_left_x.clicked.connect(lambda: BUILDER.move_model(0, -0.5))
UI.pushButton_move_right_x.clicked.connect(lambda: BUILDER.move_model(0, 0.5))

UI.pushButton_move_down_y.clicked.connect(lambda: BUILDER.move_model(1, -0.5))
UI.pushButton_move_up_y.clicked.connect(lambda: BUILDER.move_model(1, 0.5))

UI.pushButton_move_down_z.clicked.connect(lambda: BUILDER.move_model(2, -1))
UI.pushButton_move_up_z.clicked.connect(lambda: BUILDER.move_model(2, 1))

UI.pushButton_place.clicked.connect(BUILDER.create_brick)
UI.pushButton_delete.clicked.connect(BUILDER.delete_brick)

UI.actionAbout.triggered.connect(ABOUT_DIALOG.show)
UI.actionNew.triggered.connect(APPLICATION.newFile)
UI.actionSave.triggered.connect(SAVE_IO.save)
UI.pushButton_printfile.clicked.connect(SAVE_IO.save)
UI.actionOpen.triggered.connect(lambda: SAVE_IO.open_file(False))
UI.actionOpenWith.triggered.connect(lambda: SAVE_IO.open_file(True))
UI.actionResetCamera.triggered.connect(APPLICATION.reset_camera)
UI.actionResetPlacer.triggered.connect(BUILDER.reset_frame)
UI.actionToggleDarkMode.triggered.connect(APPLICATION.toggle_dark_mode)

ABOUT_UI.pushButton.clicked.connect(ABOUT_DIALOG.close)

UI.spinBox_grid_x.valueChanged.connect(BUILDER.update_grid)
UI.spinBox_grid_y.valueChanged.connect(BUILDER.update_grid)


#PAUSE_TIMER = QtCore.QTimer()
#
#def loading():
#    LOADING_DIALOG.close()
#    WINDOW.show()
#    PAUSE_TIMER.stop()
#
#PAUSE_TIMER.timeout.connect(loading)
#PAUSE_TIMER.start(5000)

WINDOW.show()

sys.exit(APP.exec_())
