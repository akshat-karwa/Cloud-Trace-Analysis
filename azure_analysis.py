import matplotlib.pyplot as plt
import pandas as pd

def read_csv():
    vm_table_data = pd.read_csv("vm_table_data_azure.csv")
    return vm_table_data

def graph_utilization_rates(metric):
    vm_table_data = read_csv()
    plt.figure(figsize = (10, 6)) # @Akshat, change as neeeded, we can finalize upon one
    plt.hist(vm_table_data[metric], bins = 20, rwidth = 0.95, color = "green")
    plt.title("Distribution of " + str(metric) + " CPU values, for Azure")
    plt.ylabel("Number of VMs")
    plt.xlabel("Percentage (%) Utilization")
    plt.show()

graph_utilization_rates("max_cpu")
graph_utilization_rates("avg_cpu")
graph_utilization_rates("p95_max_cpu")