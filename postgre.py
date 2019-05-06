import psycopg2
conn = psycopg2.connect(database="Common", user="postgres", password="123456", host="127.0.0.1", port="5432")
import csv
'''
with open('test.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    l = list(zip(reader))
    second_level = dict()
    l[0][0][0] = '1'
    #print(l)
    for i in l:
        k = list(second_level.keys())
        if i[0][1] not in k:
            second_level.update({i[0][1]:[i[0][0]]})
        else:
            second_level[i[0][1]].append(i[0][0])
print(second_level)
'''

cur = conn.cursor()
while True:
    a = input('输入二级分类: ')
    b = input('输入城市（e.g. 635 - 北京， 637 - 上海）：')
    c = input('输入教育程度(e.g. 2 - 本科， 3 - 硕士， 4 - 博士)：')
    d = input('输入经验：')
    '''
    cur.execute("select id from cities where en = '" + b + "'")
    rows = cur.fetchall()
    if rows == []:
        print('没有这个城市')
        exit(0)
    #print(rows)
    for row in rows:
        cid = str(rows[0][0])
    cid = '*'
    '''
    profession_id = second_level[a]
    query_id = ""
    flag = True
    for i in profession_id:
        if flag:
            query_id = query_id + " profession_id = " + str(i)
            flag = False
        else:
            query_id = query_id + " or profession_id = " + str(i)
    base_query = "select salary_min from recruit_infos where" + query_id

    query_city = " and city_id = " + b
    query_edu = " and degree_id = " + c
    query_exp = " and experience_min <= " + d

    Q = base_query
    if b != '':
        Q = Q + query_city
    if c != '':
        Q = Q + query_edu
    if d != '':
        Q = Q + query_exp

    cur.execute(Q)
    rows = cur.fetchall()
    count = 0
    salary = 0
    mi = list()
    for row in rows:
        if row[0] is not None:
            count += 1
            salary += row[0]
            mi.append(row[0])
    if count == 0:
        print('最小工资数据量不足\n')
        continue
    ave_salary_min = salary/count
    print('最小工资平均数：', int(ave_salary_min))
    mi.sort()
    l = len(mi)
    print('最小工资中位数：', mi[int((l-1)/2)])
    print('数据量：', count)
    base_query = "select salary_max from recruit_infos where" + query_id

    Q = base_query
    if b != '':
        Q = Q + query_city
    if c != '':
        Q = Q + query_edu
    if d != '':
        Q = Q + query_exp

    cur.execute(Q)
    rows = cur.fetchall()
    count = 0
    salary = 0
    ma = list()
    for row in rows:
        if row[0] is not None:
            count += 1
            salary += row[0]
            ma.append(row[0])
    if count == 0:
        print('最大工资数据量不足\n')
        continue
    ave_salary_min = salary/count
    print('最大工资平均数：', int(ave_salary_min))
    ma.sort()
    l = len(ma)
    print('最大工资中位数：', ma[int((l-1)/2)])
    print('数据量：', count)
    print('\n')
