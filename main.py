import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from Data_Getter import Data_Getter
import webbrowser
import os
import shutil
from tkinter import messagebox


def temp_goal_button():
    temp_goal_df = pd.read_csv("Results/Temperatures/Temperatures.csv")
    temp_goal_df.plot(x="Temperature", y=["Total Goal", "Home Goal", "Away Goal"], kind='bar')
    plt.show()


def temp_card_button():
    temp_card_df = pd.read_csv("Results/Temperatures/Temperatures.csv")
    temp_card_df.plot(x="Temperature", y=["Total Card", "Total Yellow Card", "Total Red Card"], kind='line')
    plt.show()


# Data taking by entry
def referee_goal_button():
    try:
        referee_goal_df = pd.read_csv(f"Results/Referees/{referee_title_entry.get()}.csv")
        referee_goal_df.plot(x="Temperature", y=["Total Goal", "Home Goal", "Away Goal"], kind='bar')
        plt.show()
    except:
        messagebox.showerror("showerror", "Error")


# Data taking by entry
def referee_card_button():
    try:
        referee_card_df = pd.read_csv(f"Results/Referees/{referee_title_entry.get()}.csv")
        referee_card_df.plot(x="Temperature", y=["Total Card", "Total Yellow Card", "Total Red Card"], kind='line')
        plt.show()
    except:
        messagebox.showerror("showerror", "Error")


# Data taking by entry
def home_goal_button():
    try:
        home_goal_df = pd.read_csv(f"Results/Teams/Home/{home_title_entry.get()}.csv")
        home_goal_df.plot(x="Temperature", y=["Total Goal", "Home Goal", "Away Goal"], kind='bar')
        plt.show()
    except:
        messagebox.showerror("showerror", "Error")


# Data taking by entry
def home_card_button():
    try:
        home_card_df = pd.read_csv(f"Results/Teams/Home/{home_title_entry.get()}.csv")
        home_card_df.plot(x="Temperature", y=["Total Card", "Total Yellow Card", "Total Red Card"], kind='line')
        plt.show()
    except:
        messagebox.showerror("showerror", "Error")


# Data taking by entry
def away_goal_button():
    try:
        away_goal_df = pd.read_csv(f"Results/Teams/Away/{away_title_entry.get()}.csv")
        away_goal_df.plot(x="Temperature", y=["Total Goal", "Home Goal", "Away Goal"], kind='bar')
        plt.show()
    except:
        messagebox.showerror("showerror", "Error")


# Data taking by entry
def away_card_button():
    try:
        away_card_df = pd.read_csv(f"Results/Teams/Away/{away_title_entry.get()}.csv")
        away_card_df.plot(x="Temperature", y=["Total Card", "Total Yellow Card", "Total Red Card"], kind='line')
        plt.show()
    except:
        messagebox.showerror("showerror", "Error")


# Simulation
def simulate_button():
    try:
        home_result = 0
        away_result = 0
        ycard_result = 0
        rcard_result = 0

        # Data taking from results.
        home_csv = pd.read_csv(f"Results/Teams/Home/{simulation_home_entry.get()}.csv")
        away_csv = pd.read_csv(f"Results/Teams/Away/{simulation_away_entry.get()}.csv")
        referee_csv = pd.read_csv(f"Results/Referees/{simulation_referee_entry.get()}.csv")

        # Printing for debug.
        print(home_csv)
        print(away_csv)
        print(referee_csv)

        # Result = (Home CSV Number + Away CSV Number + Referee Number)/3
        for index, row in home_csv.iterrows():
            if int(row["Temperature"]) == int(simulation_temp_entry.get()):
                print("Found")
                home_result += float(row["Home Goal"])
                away_result += float(row["Away Goal"])
                ycard_result += float(row["Total Yellow Card"])
                rcard_result += float(row["Total Red Card"])

        for index, row in away_csv.iterrows():
            if int(row["Temperature"]) == int(simulation_temp_entry.get()):
                print("Found")
                home_result += float(row["Home Goal"])
                away_result += float(row["Away Goal"])
                ycard_result += float(row["Total Yellow Card"])
                rcard_result += float(row["Total Red Card"])

        for index, row in referee_csv.iterrows():
            if int(row["Temperature"]) == int(simulation_temp_entry.get()):
                print("Found")
                home_result += float(row["Home Goal"])
                away_result += float(row["Away Goal"])
                ycard_result += float(row["Total Yellow Card"])
                rcard_result += float(row["Total Red Card"])

        home_result /= 3
        away_result /= 3
        ycard_result /= 3
        rcard_result /= 3

        home_result = "{:.2f}".format(home_result)
        away_result = "{:.2f}".format(away_result)
        ycard_result = "{:.2f}".format(ycard_result)
        rcard_result = "{:.2f}".format(rcard_result)

        simulation_home_label.config(text=home_result)
        simulation_away_label.config(text=away_result)
        simulation_ycard_label.config(text=ycard_result)
        simulation_rcard_label.config(text=rcard_result)

        print(f"Simulated "
              f"Temp = {simulation_temp_entry.get()} "
              f"HR = {home_result} "
              f"AR = {away_result} "
              f"YCR = {ycard_result} "
              f"RCR = {rcard_result}")
    except:
        messagebox.showerror("showerror", "Error")


# Gets the data via entry parameters.
def get_data_button():
    try:
        # Deleting old data.
        folder_path = "Results"
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            print("Folder deleted successfully.")
        else:
            print("Folder does not exist.")

        # Creating new files.
        os.mkdir(folder_path)
        folder_path = "Results/Referees"
        os.mkdir(folder_path)
        folder_path = "Results/Teams"
        os.mkdir(folder_path)
        folder_path = "Results/Teams/Away"
        os.mkdir(folder_path)
        folder_path = "Results/Teams/Home"
        os.mkdir(folder_path)
        folder_path = "Results/Temperatures"
        os.mkdir(folder_path)

        # Getting new data
        if int(data_end_entry.get()) <= int(data_start_entry.get()) or int(data_end_entry.get()) > 18 \
                or int(data_start_entry.get()) < 0:
            messagebox.showerror("showerror", "Error")
        else:
            data_getter = Data_Getter(int(data_start_entry.get()),int(data_end_entry.get()) - int(data_start_entry.get()))
            data_getter.main_function()
    except:
        messagebox.showerror("showerror", "Error")


def doc_button():
    try:
        os.startfile("Documents.docx")
    except:
        messagebox.showerror("showerror", "Error")


def site_button():
    try:
        webbrowser.open("https://bskorkmaz.wordpress.com/temperature-of-premier-league/")
    except:
        messagebox.showerror("showerror", "Error")


def github_button():
    try:
        webbrowser.open("https://github.com/sehaaz")
    except:
        messagebox.showerror("showerror", "Error")


def linkedin_button():
    try:
        webbrowser.open("https://www.linkedin.com/in/bahadır-semih-korkmaz-88557221b/")
    except:
        messagebox.showerror("showerror", "Error")


final_frame = pd.read_csv("Results/Temperatures/Temperatures.csv")

print(final_frame)


window = tk.Tk()
window.title("Temperature of PL")
window.geometry("550x500")

for i in range(19):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)


general_label = tk.Label(window, text="Temperature")
general_goal_button = tk.Button(window, text="Goal", command=temp_goal_button, height=3, width=12)
general_card_button = tk.Button(window, text="Card", command=temp_card_button, height=3, width=12)
general_label.grid(row=1, column=1, columnspan=8, rowspan=2)
general_goal_button.grid(row=3, column=1, columnspan=4, rowspan=2)
general_card_button.grid(row=3, column=5, columnspan=4, rowspan=2)

referee_label = tk.Label(window, text="Referee")
referee_title_label = tk.Label(window, text="Title")
referee_title_entry = tk.Entry(window)
referee_goal_button = tk.Button(window, text="Goal", command=referee_goal_button, height=3, width=12)
referee_card_button = tk.Button(window, text="Card", command=referee_card_button, height=3, width=12)
referee_label.grid(row=1, column=11, columnspan=4, rowspan=2)
referee_title_label.grid(row=1, column=15, columnspan=4, rowspan=1)
referee_title_entry.grid(row=2, column=15, columnspan=4, rowspan=1)
referee_goal_button.grid(row=3, column=11, columnspan=4, rowspan=2)
referee_card_button.grid(row=3, column=15, columnspan=4, rowspan=2)

home_label = tk.Label(window, text="Home")
home_title_label = tk.Label(window, text="Title")
home_title_entry = tk.Entry(window)
home_goal_button = tk.Button(window, text="Goal", command=home_goal_button, height=3, width=12)
home_card_button = tk.Button(window, text="Card", command=home_card_button, height=3, width=12)
home_label.grid(row=6, column=1, columnspan=4, rowspan=2)
home_title_label.grid(row=6, column=5, columnspan=4, rowspan=1)
home_title_entry.grid(row=7, column=5, columnspan=4, rowspan=1)
home_goal_button.grid(row=8, column=1, columnspan=4, rowspan=2)
home_card_button.grid(row=8, column=5, columnspan=4, rowspan=2)

away_label = tk.Label(window, text="Away")
away_title_label = tk.Label(window, text="Title")
away_title_entry = tk.Entry(window)
away_goal_button = tk.Button(window, text="Goal", command=away_goal_button, height=3, width=12)
away_card_button = tk.Button(window, text="Card", command=away_card_button, height=3, width=12)
away_label.grid(row=6, column=11, columnspan=4, rowspan=2)
away_title_label.grid(row=6, column=15, columnspan=4, rowspan=1)
away_title_entry.grid(row=7, column=15, columnspan=4, rowspan=1)
away_goal_button.grid(row=8, column=11, columnspan=4, rowspan=2)
away_card_button.grid(row=8, column=15, columnspan=4, rowspan=2)

simulation_home_entry_label = tk.Label(window, text="Home")
simulation_away_entry_label = tk.Label(window, text="Away")
simulation_temp_entry_label = tk.Label(window, text="Temperature")
simulation_referee_entry_label = tk.Label(window, text="Referee")
simulation_home_entry = tk.Entry(window)
simulation_away_entry = tk.Entry(window)
simulation_temp_entry = tk.Entry(window)
simulation_referee_entry = tk.Entry(window)
simulation_simulate_button = tk.Button(window, text="Simulate", command=simulate_button, height=3, width=30)
simulation_home_label = tk.Label(window, text=0)
simulation_away_label = tk.Label(window, text=0)
simulation_ycard_label = tk.Label(window, text=0)
simulation_rcard_label = tk.Label(window, text=0)
simulation_home_entry_label.grid(row=11, column=1, columnspan=4, rowspan=1)
simulation_away_entry_label.grid(row=11, column=5, columnspan=4, rowspan=1)
simulation_temp_entry_label.grid(row=13, column=1, columnspan=4, rowspan=1)
simulation_referee_entry_label.grid(row=13, column=5, columnspan=4, rowspan=1)
simulation_home_entry.grid(row=12, column=1, columnspan=4, rowspan=1)
simulation_away_entry.grid(row=12, column=5, columnspan=4, rowspan=1)
simulation_temp_entry.grid(row=14, column=1, columnspan=4, rowspan=1)
simulation_referee_entry.grid(row=14, column=5, columnspan=4, rowspan=1)
simulation_simulate_button.grid(row=15, column=1, columnspan=8, rowspan=2)
simulation_home_label.grid(row=17, column=1, columnspan=2, rowspan=2)
simulation_away_label.grid(row=17, column=3, columnspan=2, rowspan=2)
simulation_ycard_label.grid(row=17, column=5, columnspan=2, rowspan=2)
simulation_rcard_label.grid(row=17, column=7, columnspan=2, rowspan=2)

data_start_entry_label = tk.Label(window, text="Start")
data_end_entry_label = tk.Label(window, text="End")
data_start_entry = tk.Entry(window)
data_end_entry = tk.Entry(window)
data_get_button = tk.Button(window, text="Get Data", command=get_data_button, height=3, width=30)
data_start_entry_label.grid(row=11, column=11, columnspan=4, rowspan=1)
data_end_entry_label.grid(row=11, column=15, columnspan=4, rowspan=1)
data_start_entry.grid(row=12, column=11, columnspan=4, rowspan=1)
data_end_entry.grid(row=12, column=15, columnspan=4, rowspan=1)
data_get_button.grid(row=13, column=11, columnspan=8, rowspan=2)

credit_github_button = tk.Button(window, text="GitHUB", command=github_button, height=2, width=30)
credit_linkedin_button = tk.Button(window, text="LinkedIN", command=linkedin_button, height=2, width=30)
credit_doc_button = tk.Button(window, text="Documents", command=doc_button, height=2, width=30)
credit_site_button = tk.Button(window, text="Site", command=site_button, height=2, width=30)
credit_github_button.grid(row=17, column=11, columnspan=8, rowspan=1)
credit_linkedin_button.grid(row=16, column=11, columnspan=8, rowspan=1)
credit_doc_button.grid(row=15, column=11, columnspan=8, rowspan=1)
credit_site_button.grid(row=18, column=11, columnspan=8, rowspan=1)

window.mainloop()
