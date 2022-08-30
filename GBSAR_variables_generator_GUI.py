from tkinter import  *
import tkinter.messagebox as msgbox
import os
import pandas as pd

gui = Tk()
gui.title("GBSAR Parameters Generator ver0.5")
gui.geometry("700x630")

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

# def help_ftn():
#     help_photo = PhotoImage(file = 'GUI/example.PNG')
#     msgbox.showinfo('Example', help_photo)

def save():
    response = msgbox.askyesno("Save", "Did you check the parameter clearly?")
    if response == 1:
        value1 = data_dir_entry.get()
        value2 = file_head_entry.get()
        value3 = nline_skip_entry.get()
        value4 = num_channel_entry.get()
        value5 = channel_head_entry.get()
        value6 = freq_entry.get()
        value7 = antenna_azi_entry.get()
        value8 = rail_mm_entry.get()
        value9 = rail_filename_entry.get()
        value10 = FFT_entry.get()
        value11 = azi_TD_entry.get()
        value12 = Rcenter_entry.get()
        value13 = Focusing_selection_entry.get()
        value14 = VNA_entry.get()
        value15 = baseline_entry.get()
        value16 = _1s1m_station_entry.get()
        value17 = _1s1m_beam_entry.get()

        parameters = {'parms' : [value1,value2,value3,value4,value5,value6,value7,value8,value9,value10,value11,value12,value13,value14,value15,value16,value17],
                        'dummies' : ['data_directory', 'output_file_head(fohead)', 'nline_skip', 'number_of_channel',
                        'output_channel_head', 'frequency(start,stop)[GHz],number','Antenna_azimuth[m]', 'Rail(start,stop,step)[mm]',
                        'Rail(start,stop,step)[filename]', 'FFT_fold(interpolation)', 'mazimuth_TD(Azimuth_Width_Fold_TD)', 'R_center',
                        'Focusing_selection', 'Rcut_for_VNA_Port_length[m]', 'Baseline_of_Tx_and_Rx[m]', '1s1m_location_of_stationary_antenna(sx,sy)[m]',
                        '1s1m_location_of_beam_center(bx,by)[m]']}

        df = pd.DataFrame(parameters)
        df.to_csv(file_name_entry.get() + ".pam", mode = 'a', index = False, header = False, sep = '\t')
        msgbox.showinfo("Complete", "The file has been generated")


gui_gen = GUIGenerator()

file_name_label = gui_gen.label_generator("File Name", 30, 0)
file_name_entry = Entry(gui, width = 30)
file_name_entry.place(x = 250, y = 0)
file_name_entry.insert(0, 'Output File Name')
file_name_desc = gui_gen.description("The file will be named via this entry", 480, 0)

# entry는 class 말고 따로 지정 할 것
data_dir_label = gui_gen.label_generator("Data Directory", 30, 30)
data_dir_entry = Entry(gui, width = 30)
data_dir_entry.place(x = 250, y = 30)
data_dir_entry.insert(0, '../1')

file_head_label = gui_gen.label_generator("Output File Head", 30, 60)
file_head_entry = Entry(gui, width = 30)
file_head_entry.place(x = 250, y = 60)
file_head_entry.insert(0, 'a1')

nline_skip_label = gui_gen.label_generator("nLine Skip", 30, 90)
nline_skip_entry = Entry(gui, width = 30)
nline_skip_entry.place(x = 250, y = 90)
nline_skip_entry.insert(0, '22')

num_channel_label = gui_gen.label_generator("Number of Channel", 30, 120)
num_channel_entry = Entry(gui, width = 30)
num_channel_entry.place(x = 250, y = 120)
num_channel_entry.insert(0, '1')

channel_head_label = gui_gen.label_generator("Output Channel Head", 30, 150)
channel_head_entry = Entry(gui, width = 30)
channel_head_entry.place(x = 250, y = 150)
channel_head_entry.insert(0, 'VV')

freq_label = gui_gen.label_generator("Frequency", 30, 180)
freq_entry = Entry(gui, width = 30)
freq_entry.place(x = 250, y = 180)
freq_entry.insert(0, '5.2 5.4 4001')
freq_desc = gui_gen.description('(Start, Stop)[GHz], Number', 480, 180)

antenna_azi_label = gui_gen.label_generator("Antenna Azimuth", 30, 210)
antenna_azi_entry = Entry(gui, width = 30)
antenna_azi_entry.place(x = 250, y = 210)
antenna_azi_entry.insert(0, '0.25')
antenna_azi_desc = gui_gen.description('[m]', 480, 210)

rail_mm_label = gui_gen.label_generator("Rail", 30, 240)
rail_mm_entry = Entry(gui, width = 30)
rail_mm_entry.place(x = 250, y = 240)
rail_mm_entry.insert(0, '-3000 3000 30')
rail_mm_desc = gui_gen.description('(Start, Stop, Step)[mm]', 480, 240)

rail_filename_label = gui_gen.label_generator("Rail", 30, 270)
rail_filename_entry = Entry(gui, width = 30)
rail_filename_entry.place(x = 250, y = 270)
rail_filename_entry.insert(0, '0 6000 30')
rail_filename_desc = gui_gen.description('(Start, Stop, Step) Filename', 480, 270)

FFT_label = gui_gen.label_generator("FFT Fold", 30, 300)
FFT_entry = Entry(gui, width = 30)
FFT_entry.place(x = 250, y = 300)
FFT_entry.insert(0, '2 2')
FFT_desc = gui_gen.description('Interpolation', 480, 300)

azi_TD_label = gui_gen.label_generator("mAzimuth TD", 30, 330)
azi_TD_entry = Entry(gui, width = 30)
azi_TD_entry.place(x = 250, y = 330)
azi_TD_entry.insert(0, '2')
azi_TD_desc = gui_gen.description("Azimuth Width Fold TD", 480, 330)

Rcenter_label = gui_gen.label_generator("R center", 30, 360)
Rcenter_entry = Entry(gui, width = 30)
Rcenter_entry.place(x = 250, y = 360)
Rcenter_entry.insert(0, '0.')

Focusing_selection_label = gui_gen.label_generator("Focusing Selection", 30, 390)
Focusing_selection_entry = Entry(gui, width = 30)
Focusing_selection_entry.place(x = 250, y = 390)
Focusing_selection_entry.insert(0, '5')

VNA_label = gui_gen.label_generator("Rcut for VNA Port Length", 30, 420)
VNA_entry = Entry(gui, width = 30)
VNA_entry.place(x = 250, y = 420)
VNA_entry.insert(0, '6.0')
VNA_desc = gui_gen.description("[m]", 480, 420)

baseline_label = gui_gen.label_generator("Baseline of Tx and Rx", 30, 450)
baseline_entry = Entry(gui, width = 30)
baseline_entry.place(x = 250, y = 450)
baseline_entry.insert(0, '1.0')
baseline_desc = gui_gen.description("[m]", 480, 450)

_1s1m_station_label = gui_gen.label_generator("1s1m Location of Stationary Antenna", 30, 480)
_1s1m_station_entry = Entry(gui, width = 30)
_1s1m_station_entry.place(x = 250, y = 480)
_1s1m_station_entry.insert(0, '0. 0.')
_1s1m_station_desc = gui_gen.description("(sx, sy) [m]", 480, 480)

_1s1m_beam_label = gui_gen.label_generator("1s1m Location of Beam Center", 30, 510)
_1s1m_beam_entry = Entry(gui, width = 30)
_1s1m_beam_entry.place(x = 250, y = 510)
_1s1m_beam_entry.insert(0, '0. 10.')
_1s1m_beam_desc = gui_gen.description("(bx, by) [m]", 480, 510)

quit_btn = Button(gui, width = 15, text = "Quit", command = quit)
quit_btn.place(x = 550, y = 550)

run_btn = Button(gui, width = 15, text = "Save", command = save)
run_btn.place(x = 300, y = 550)

sign_label = Label(gui, text = "© Created by Lee and Sung. 2021")
sign_label.place(x = 500, y = 580)

gui.mainloop()