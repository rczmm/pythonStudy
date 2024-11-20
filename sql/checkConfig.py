import csv

configs = []

with open('config.csv', 'r', encoding='utf-8') as f:
    config = csv.reader(f)
    for row in config:
        data = row[0].split(" ")
        tenant_id = data[2]
        name = data[5]
        level = data[8]
        sc_type = data[9]
        common = data[10]
        photo_flag = data[11]
        photo_num = data[12]
        inhabitant_flag = data[13]
        advise = data[14]
        process_time = data[16]
        config = {
            "name": name,
            "level": level,
            "sc_type": sc_type,
            "common": common,
            "photo_flag": photo_flag,
            "photo_num": photo_num,
            "flag": inhabitant_flag,
            "advise": advise,
            "process_time": process_time,
            "pid": 0

        }
        configs.append(config)

sqls = []

commons = set()

for config in configs:
    commons.add(config['common'])

sqls = []

for config in configs:
    pids = {
        '燃气软管': 168,
        '表后管道': 169,
        '燃气阀门': 170,
        '户内燃气管道': 171,
        '燃气表': 172,
        '表前管道': 173,
        '其他': 174,
        '燃气设备': 175,
    }
    sql = f'''
    INSERT into "JHC-MH-SC"."check_config"("tenant_id","name","sc_level","sc_type","common","photo_flag","photo_num","inhabitant_flag","sc_advise","sc_process_time","pid","order_R")
VALUES ('jytbrq','{config['name']}','{config['level']}','{config['sc_type']}','{config['common']}',{config['photo_flag']},{config['photo_num']},'{config['flag']}','{config['advise']}','{config['process_time']}','{pids[config['common']]}',0);'''
    sqls.append(sql)

com = []

for common in commons:
    sql = f'''INSERT INTO "JHC-MH-SC"."check_config"("tenant_id","common","photo_flag","photo_num","inhabitant_flag","pid","order_R")
VALUES('jytbrq','{common}','0','0','居民','0',0)
                '''
    com.append(sql)

for i in com:
    print(i)

for i in sqls:
    print(i)

if __name__ == '__main__':
    pass
