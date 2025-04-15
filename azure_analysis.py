import matplotlib.pyplot as plt
import pandas as pd

def read_csv():
    vm_table_data = pd.read_csv("vm_table_data_azure.csv")
    return vm_table_data

def plot_resource_analysis(dataframe, col_name):
    plt.figure(figsize = (10, 6))
    plt.hist(dataframe[col_name], bins = 40, rwidth = 0.85, color = "dodgerblue")
    heading = ""
    if col_name == "max_cpu":
        heading = "Max"
    elif col_name == "avg_cpu":
        heading = "Average"
    else:
        heading = "P95 Max"
    plt.title("Distribution of " + str(heading) + " CPU Utilization Percentage Values for Azure")
    plt.xlabel("CPU Utilization (%)")
    plt.ylabel("Number of Virtual Machines")
    plt.grid(True)
    plt.savefig(f'azure_{col_name}_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

vm_table_data = read_csv()
print(vm_table_data["avg_cpu"].mean())
#plot_resource_analysis(vm_table_data, "max_cpu")
#plot_resource_analysis(vm_table_data, "avg_cpu")
#plot_resource_analysis(vm_table_data, "p95_max_cpu")