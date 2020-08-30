from datetime import datetime, timedelta

def seconds_ago(s,n):
    return (datetime.strptime(s, '%Y-%m-%d %H:%M:%S') - timedelta(seconds=n)).strftime('%4Y-%m-%d %H:%M:%S')

#https://www.codewars.com/kata/5a631508e626c5f127000055/train/python