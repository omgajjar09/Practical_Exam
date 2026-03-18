import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class FitnessTracker:

    def __init__(self):
        self.df=None

    def load_data(self):
        try:
            print("\n== Load Dataset ==")
            data_frame=input("Enter the path of the dataset (csv file): ").strip()
            self.df=pd.read_csv(data_frame)
            print("\nDataset loaded Successfully!\n")
        except FileNotFoundError:
            print("\nError: File not found. Please check the file path.\n")

    def Metrics(self):
        try:
            print("\nFitness Metrics:")
            total_calories = self.df["Calories_Burned"].sum()
            avg_duration = self.df["Duration"].mean()
            print(f"Total Calories Burned: {total_calories}")
            print(f"Average Duration: {avg_duration:.2f} minutes")
            print("\nActivity Frequency:")
            print(self.df["Activity_Type"].value_counts())
        except Exception as e:
            print("Error :",e)

#---------- Generate Report -----------
    def generate_report(self):
        print("\nSummary Report:")
        print(self.df.describe())

# ---------- Filter ----------
    def filter_by_Activity(self):
        try:
            activity = input("Enter Activity Type (e.g., Running): ")
            filtered = self.df[self.df["Activity_Type"] == activity]
            print("\nFiltered Data:\n")
            print(filtered)
        except Exception as e:
            print("Error : ",e)

# ----------Visulaization Data ---------
    def bar_chart(self):
        print("\n== Bar Plot ==")
        print("Generating Bar plot...")
        self.df.groupby("Activity_Type")["Duration"].sum().plot(kind="bar")
        plt.title("Bar Plot")
        plt.xlabel("Activity_Type")
        plt.ylabel("Duration")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        print("Bar plot displayed successfully!")

    def line_graph(self):
        print("\n== Line Plot ==")
        print("Generating line plot...")
        plt.plot(self.df["Date"], self.df["Calories_Burned"], marker='o', color="blue")
        plt.xlabel("Date")
        plt.ylabel("Calories_Burned")
        plt.title("Line Plot")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        print("Line plot displayed successfully!")

    def pie_chart(self):
        print("\n== Pie Chart ==")
        print("Generating pie chart...")
        self.df["Activity_Type"].value_counts().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Activity Distribution")
        plt.ylabel("")
        plt.show()
        print("Pie chart displayed successfully!")

    def heatmap(self):
        print("\n== Heatmap ==")
        print("Generating Heatmap...")
        sns.heatmap(self.df[["Duration", "Calories_Burned"]].corr(), annot=True)
        plt.title("Heatmap")
        plt.show()
        print("Heatmap displayed successfully!")

    def __del__(self):
        pass

ft=FitnessTracker()

while True:
    try:
        print("\n===== Fitness Tracker Menu =====")
        print("1. Load Dataset")
        print("2. View Metrics")
        print("3. Filter Activities")
        print("4. Generate Report")
        print("5. Visualize Data")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            ft.load_data()

        elif choice == 2:
            ft.Metrics()

        elif choice == 3:
            ft.filter_by_Activity()

        elif choice == 4:
            ft.generate_report()

        elif choice == 5:
            try:
                while True:
                    print("\nVisualize Data")
                    print("1. Bar Chart")
                    print("2. Line Graph")
                    print("3. Pie Chart")
                    print("4. Heatmap")
                    print("5. Go Back")
                    vchoice=int(input("Enter your choice: "))
                    if vchoice==1:
                        ft.bar_chart()
                    elif vchoice==2:
                        ft.line_graph()
                    elif vchoice==3:
                        ft.pie_chart()
                    elif vchoice==4:
                        ft.heatmap()
                    elif vchoice==5:
                        print("\nReturning to Main Menu....\n")
                        break
                    else:
                        print("\nInvalided Choice\n")
            except Exception as e:
                print("Error :",e)

        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("\nInvalided choice!")

    except Exception as e:
        print("Error :",e)