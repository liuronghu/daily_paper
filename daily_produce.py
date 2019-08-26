# -*- coding: utf-8 -*- 
import pandas as pd
start_date = '28/6/2019'
end_date = '31/7/2019'
target_file = 'daily_file'
source_file = 'daily_template.conf'
source_data = open(source_file, 'rt',encoding='UTF-8').read()
target_data = open(target_file, 'wt',encoding='UTF-8')
date_value = pd.date_range(start_date, end_date)
for date in date_value:
    source_data_copy = source_data
    source_data_copy = source_data_copy.replace("{year}",str(date.year))
    source_data_copy = source_data_copy.replace('{month}',str(date.month))
    source_data_copy = source_data_copy.replace('{day}',str(date.day))
    target_data.write(source_data_copy)