import tkinter as tk
from tkinter import ttk
from datetime import datetime
import torch
import seaborn as sns
import matplotlib.pyplot as plt

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced CLOCK")

        self.label = ttk.Label(root, font=('calibri', 40, 'bold'), background="black", foreground="cyan")
        self.label.pack(anchor='center')
        self.update_time()

    
        self.torch_tensor_example()

        
        self.seaborn_visualization_example()

    def update_time(self):
        current_time = datetime.now().strftime('%H:%M:%S %p')
        self.label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def torch_tensor_example(self):
         tensor_example = torch.tensor([1, 2, 3, 4, 5])
        print("PyTorch Tensor Example:", tensor_example)

    def seaborn_visualization_example(self):
       
        sns.set_theme()
        data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
        df = sns.load_dataset("iris")
        sns.scatterplot(x='sepal_length', y='sepal_width', data=df)
        plt.title('Seaborn Scatter Plot Example')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    clock_app = ClockApp(root)
    root.mainloop()
