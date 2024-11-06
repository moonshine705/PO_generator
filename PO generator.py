import tkinter as tk

def main():
    lines = input_box.get("1.0","end-1c").splitlines()

    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")

    for i in range(len(lines)):
        converter(lines[i])

def converter(line):
    new_line = ["1260", "", "APN", "Des", "Cost", "Unit Price", "Price break", "","","", "MFR", "MPN","Workorder","G/L account"]

    new_line[2] = line[0]
    new_line[3] = line[1]
    new_line[4] = line[2]

    new_line[5] = line[3] #need to shift the decimal point
    
    new_line[10] = line[4]
    new_line[11] = line[5]
    new_line[12] = line[6]

    x,y = new_line[5].split(".")
    len_y = len(y)

    if len_y <= 6:
        powers_div = 10**(len_y-2)

        if len_y == 1:
            powers_div = 1

        converted_nums = f"{powers_div*float(new_line[5]):.2f}"
        powers_div = str(powers_div)

    new_line[5] = converted_nums
    new_line[6] = powers_div
    
    result_box.insert("1.0", "\t".join(new_line)+"\n")

window = tk.Tk()
window.title("PO Excel Converter")

input_box = tk.Text(window, height = 3, width= 150)
input_box.pack()

input_box_button = tk.Button(window, text = "Generate", command = main)
input_box_button.pack()

result_box = tk.Text(window, height = 3, width = 150)
result_box.pack()



window.mainloop()
