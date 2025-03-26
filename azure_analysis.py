import pandas as pd

def read_csv():
    vm_table_data = pd.read_csv("vm_table_data_azure.csv", nrows = 10000000)
    return vm_table_data

def analysis():
    vm_table_data = read_csv()

analysis()