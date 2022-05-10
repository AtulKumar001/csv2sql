import csv

table_name = input("Enter File name: ")
file = open(input("Enter CSV File Path: "), newline='')
csvreader = csv.reader(file)

fields = next(csvreader)
table = f"CREATE TABLE IF NOT EXISTS `{table_name}` (\r\n"
i = 0
for r in fields:
    if len(fields) == i+1:
        table += f"\t`{r}` varchar(255) DEFAULT NULL\r\n"
    else:
        table += f"\t`{r}` varchar(255) DEFAULT NULL,\r\n"
    i += 1
table += ");\r\n"

insert_data = f"INSERT INTO '{table_name}` {tuple(fields)} VALUES \r\n".replace("'", "`")
while True:
    try:
        insert_data += str(tuple(next(csvreader)))+",\r\n"
    except Exception as e:
        break
list_insert_data = list(insert_data)
del list_insert_data[-1]
del list_insert_data[-1]
del list_insert_data[-1]
list_insert_data.append(";")

insert_data  = "".join(list_insert_data)

sql_data = f'''

--
-- Convert Csv to Sql
--

-- --------------------------------------------------------

--
-- Table structure for table `{table_name}`
--
{table}

--
-- Dumping data for table `{table_name}`
--

{insert_data}
'''
file.close()
f = open(f"{table_name}.sql", "w")
f.write(sql_data)
f.close()
print(f"{table_name}.sql created Successfully.")