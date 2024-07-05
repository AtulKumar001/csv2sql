#!/usr/bin/python3
import csv, sys

if len(sys.argv) != 3:
    print(f"Uses: python3 {sys.argv[0]} <CSV_FILE_NAME> <TABLE_NAME>")
    print()
    exit()

file = open(sys.argv[1], newline='')
csvreader = csv.reader(file)

table_name = sys.argv[2]

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

'''
f = open(f"{table_name}.sql", "w")
f.write(sql_data)
f.close()

initial_data = f"INSERT INTO '{table_name}` {tuple(fields)} VALUES".replace("'", "`")
insert_data = ""
f = open(f"{table_name}.sql", "a")
while True:
    try:
        insert_data = f'{initial_data} {str(tuple(next(csvreader)))};\r\n'
        f.write(insert_data)
    except Exception as e:
        break
f.close()


file.close()
print(f"{table_name}.sql created Successfully.")
print()	
