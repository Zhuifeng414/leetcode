# def complete_info():
#     return
###############################################################################
# coding:utf-8
# cat_cross.py
# from odps.udf import annotate
# from odps.udf import BaseUDTF
# @annotate('string,string,string -> string,string,string')
# class deal_cat_cross(BaseUDTF):
#     # 将string按逗号分隔输出成多条记录。
#     def process(self, profitcentername, user_id, cat_set_str):
#         cat_set_list = cat_set_str.split(',')
#         cat_set_list.sort()
#         for i in range(len(cat_set_list)):
#             for j in range(i + 1, len(cat_set_list)):
#                 cat_cross_item = cat_set_list[i] + '&' + cat_set_list[j]
#                 # print user_id, cat_cross_item
#                 self.forward(profitcentername, user_id, cat_cross_item)
###############################################################################
# import json
# from odps.udf import annotate
# @annotate('string->string')
# class Transform(object):
#     def evaluate(self, x):
#         columns = list('abc')
#         d = dict(zip(columns, x.split(',')))
#         return json.dumps(d)
###############################################################################
#from odps.udf import annotate

#@annotate("string->string")
#class regxp_sign(object):
# import re
# def evaluate(charge_account):
#     #phone_res = re.findall('(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', charge_account)
#     phone_res = re.findall('(\d{3}\*\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', charge_account)
#     return phone_res
#
#
# print(evaluate('wqng13296618414lei13071288614lei132***18414'))
###############################################################################








