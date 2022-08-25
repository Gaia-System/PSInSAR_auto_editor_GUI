# This GUI was written in order to edit the generated csv files through StaMPS.
# It can be used when you wanna cut only a local area in a large area.
# You can edit your csv files via excel directly, but I think a large csv file will be slow when it open. So I made this GUI.
# If you wanna use this script, you will use via 'visual studio code'.
# This script is no copyright.

from tkinter import *
import tkinter.messagebox as msgbox
import os
import pandas as pd

gui = Tk()
gui.title("PSInSAR csv Auto Editor ver.1.0.0")
gui.geometry("750x530")

class GUIGenerator:
    def label_generator(self, text, x_coor, y_coor):
        self.text = text
        self.label = Label(gui, text = text)
        self.label.place(x = x_coor, y = y_coor)

    def description(self, text, x_coor, y_coor):
        self.text = text
        self.label = Label(gui, text = text)
        self.label.place(x = x_coor, y = y_coor)

def quit():
    response = msgbox.askyesno("Quit", "Are you sure?")
    if response == 1: gui.quit()

def edit():
    response = msgbox.askyesno("Save", "Did you check the parameter clearly?")
    try:
        if response == 1:
            table = pd.read_csv(in_name_entry.get() + ".csv")
            filt_lon = (table.export_res_1 >= float(W_lon_entry.get())) & (table.export_res_1 < float(E_lon_entry.get()))
            filt_lat = (table.export_res_2 >= float(S_lat_entry.get())) & (table.export_res_2 < float(N_lat_entry.get()))

            time_row = table.iloc[:1,:]

            filted_table = table.loc[filt_lon,:]
            filted_table = filted_table.loc[filt_lat,:]
            filted_table = time_row.append(filted_table)
            print(filted_table)

            filted_table.to_csv(out_name_entry.get() + '.csv', mode = 'a', index = False)
            msgbox.showinfo("Complete", "The file has been generated")
    except ValueError:
        msgbox.showerror("Error", "Check your boundary bars if some symbols is occupying the bars or not.")

gui_gen = GUIGenerator()

title = Label(gui, text = "PSInSAR csv Auto Editor", font = ("times new roman", 30, "bold"))
title.pack()

caution = Label(gui, text = "CAUSIONS\nPlease locate this program with your csv files in same diretory.\nYou can insert only decimal numbers into the boundary bars.\nPlease install the 'pandas' in your computer via terminal or IDE.",
                font = ("times new roman", 15, "bold"), fg = "red")
caution.place(x = 87, y = 350)

in_name_label = gui_gen.label_generator("Input File Name", 30, 50)
in_name_entry = Entry(gui, width = 30)
in_name_entry.place(x = 250, y = 50)
in_name_entry.insert(0, 'Input File Name')
in_name_desc = gui_gen.description("Insert your input file name", 480, 50)

out_name_label = gui_gen.label_generator("Output File Name", 30, 80)
out_name_entry = Entry(gui, width = 30)
out_name_entry.place(x = 250, y = 80)
out_name_entry.insert(0, 'Output File Name')
out_name_desc = gui_gen.description("The output file will be named via this bar", 480, 80)

sep_label = Label(gui, text = '----------------------------------------------------------------------------------------------------------------------------------------')
sep_label.place(x = 30, y = 110)

W_lon_label = gui_gen.label_generator("Western Boundary", 30, 140)
W_lon_entry = Entry(gui, width = 30)
W_lon_entry.place(x = 250, y = 140)
W_lon_entry.insert(0, 'Western Boundary')

E_lon_label = gui_gen.label_generator("Eastern Boundary", 30, 170)
E_lon_entry = Entry(gui, width = 30)
E_lon_entry.place(x = 250, y = 170)
E_lon_entry.insert(0, 'Eastern Boundary')

N_lat_label = gui_gen.label_generator("Northern Boundary", 30, 200)
N_lat_entry = Entry(gui, width = 30)
N_lat_entry.place(x = 250, y = 200)
N_lat_entry.insert(0, 'Northern Boundary')

S_lat_label = gui_gen.label_generator("Southern Boundary", 30, 230)
S_lat_entry = Entry(gui, width = 30)
S_lat_entry.place(x = 250, y = 230)
S_lat_entry.insert(0, 'Southern Boundary')


quit_btn = Button(gui, width = 15, text = "Quit", command = quit)
quit_btn.place(x = 425, y = 300)

edit_btn = Button(gui, width = 15, text = "Edit", command = edit)
edit_btn.place(x = 175, y = 300)

sign_label = Label(gui, text = "Created by Gaia-Archive. 2021")
sign_label.place(x = 470, y = 450)

gui.mainloop()
