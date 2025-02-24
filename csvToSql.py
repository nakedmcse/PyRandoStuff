with open('/Users/walker/Downloads/effdates.csv') as csvfile:
    splits = csvfile.read().splitlines()
    for row in splits:
        splitrow = row.split(',')
        print(f"update NA set EDate = '{splitrow[1]}', XDate = '{splitrow[2]}' where NAID = (select NAID from SNumbers where SNumber = {splitrow[0]});")