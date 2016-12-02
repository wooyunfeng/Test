#coding: utf-8
import cx_Oracle
#db=cx_Oracle.connect('username','password','ip地址:1521/service name')
db=cx_Oracle.connect('system/123456@localhost/ora11g') 
print db.version
