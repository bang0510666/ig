import csv

with open('names.csv', newline='') as file:
    csv_reader = csv.reader(file)

    
    count_1_5 = 0
    count_6_10 = 0
    count_11_15 = 0
    count_over_15 = 0

    
    accounts_over_10 = []

    
    for row in csv_reader:
        account = row[0]  

        
        length = len(account)
        if length <= 5:
            count_1_5 += 1
        elif length <= 10:
            count_6_10 += 1
        elif length <= 15:
            count_11_15 += 1
        else:
            count_over_15 += 1

        
        if length > 10:
            accounts_over_10.append(account)

    print("1-5個字元：", count_1_5, "個")
    print("6-10個字元：", count_6_10, "個")
    print("11-15個字元：", count_11_15, "個")
    print("15個字元以上：", count_over_15, "個")

    with open('accounts_over_10.csv', 'w', newline='',encoding="utf-8") as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['帳號'])
        csv_writer.writerows([[account] for account in accounts_over_10])

    print("帳號字元數大於10的清單已寫入到accounts_over_10.csv文件中。")