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
test_str = '''15556798106	155****8106	ゾ词穷		15556798106
13413066327	134****6327	tb137491002		13413066327
cjh1314520mh	131****0608	tb085325108		cjh1314520mh
xxbb9966	139****5733	陌陌929999		xxbb9966
13922721185	139****1185	aaa13922721185		13922721185
489986441	152****0692	一条街42		489986441
pyx1760359697	***0359697@qq.com	t_1499264979205_0303	1760359697@qq.com	pyx1760359697
18826289009	188****9009	杜广猛		18826289009
13922508836	139****8836	yuyudai76		13922508836
13435399717	134****9717	叶景锋18	1044524700@qq.com	13435399717
limengqing+21793984	181****0649	lmq891121		limengqing+21793984
189728333207z	***kfl549511@163.com	云霄波克	rrekfl549511@163.com	189728333207z
15886179799	158****9799	wang154885539		15886179799
2426523993	***6890462@qq.com	正方形大门一串3	2986890462@qq.com	2426523993
2293425912	173****1844	t_1510299717918_0279		2293425912
625235964	***645044@qq.com	何处不是花	814645044@qq.com	625235964;安卓客户端
2200409030	***8164245@qq.com	tb372004034		2200409030
1112577602	151****3666	huxin84714	9335549@qq.com	1112577602
836498101	***2220609@qq.com	唐军19790219	1312220609@qq.com	836498101
18813618212	188****8212	t0882205040		18813618212
1013156910	***3156910@qq.com	wangyayun12345	1013156910@qq.com	1013156910
18958374737	136****9384	猪鼻子的雯雯		18958374737
13509836298	135****6298	t_1485603144615_0630		13509836298
17688679089	176****9089	春天的梦欣欣1		17688679089;苹果客户端
2673864818	852*****6257	tb375186738		2673864818
13168928295	***5549237@qq.com	lzp11255	1125549237@qq.com	13168928295
19806785871	139****4642	tb960991826		19806785871
13821011830	***gqiyang5193@163.com	dongqiyang520	dongqiyang5193@163.com	13821011830
15958143717	159****3717	我是整颗心呀		15958143717
1137398003	***kxia1982@126.com	gege19890508	jackxia1982@126.com	1137398003
dyya1zhvogj7	188****6081	tb608427452		dyya1zhvogj7
974491351	151****8935	t_1493111827436_0778		974491351
12	***539486@qq.com	hjkkg520	827539486@qq.com	17854180339
36214469	151****7999	子豪90	350332905@qq.com	36214469
18933953288	189****3288	yvonne0753	 	18933953288;苹果客户端'''

# def evaluate(charge_account):
#     phone_res = re.findall('(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', charge_account)
#     #phone_res = re.findall('(\d{3}\*\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', charge_account)
#     return phone_res
# print(evaluate(test_str))
from odps.udf import annotate
import re
@annotate("string,string,string,string->string,string,string")
class fill_slot(object):
   def evaluate(charge_account, user_alipay_account_id, user_taobao_email, user_receiver_address):
       ## 解析用户手机号
       ## 手机号只可能存在于 charge_account 和 user_receiver_address
       charge_phone_list = re.findall('1[3,4,5,7,8,9]\d{9}', charge_account)
       charge_phone = charge_phone_list[0] if charge_phone_list else ''
       receiver_phone_list = re.findall('1[3,4,5,7,8,9]\d{9}', user_receiver_address)
       receiver_phone = receiver_phone_list[0] if receiver_phone_list else ''
       if len(charge_phone) == 11 and len(receiver_phone) == 11 and charge_phone == receiver_phone:
           user_phone = charge_phone
       elif len(charge_phone) == 11:
           user_phone = charge_phone
       elif len(receiver_phone) == 11:
           user_phone = receiver_phone
       else:
           user_phone = ''
       ## 解析用户支付宝账号
       ## 邮箱 user_alipay_account_id 和 user_taobao_email
       if '@' in user_alipay_account_id:
           # email
           alipay_email_pre = user_alipay_account_id.split('@')[0]
           alipay_email_suf = user_alipay_account_id.split('@')[1]
           if alipay_email_pre[:3] == '***' \
                   and len(user_taobao_email) > 0 \
                   and user_taobao_email.split('@')[0][3:] == alipay_email_pre[3:]:
               user_alipay_id = user_taobao_email
           elif alipay_email_pre[:3] == '***' \
                   and charge_account[3:] == alipay_email_pre[3:]:
               user_alipay_id = charge_account + '@' + alipay_email_suf
           elif alipay_email_pre[:3] == '***' \
                   and user_receiver_address[3:] == alipay_email_pre[3:]:
               user_alipay_id = user_receiver_address + '@' + alipay_email_suf
           else:
               user_alipay_id = user_alipay_account_id
       elif user_phone[:3] == user_alipay_account_id[:3] \
               and user_phone[7:] == user_alipay_account_id[7:] \
               and user_alipay_account_id[3:7] == '****':
           user_alipay_id = user_phone
       else:
           user_alipay_id = user_alipay_account_id

       ## 解析用户邮箱
       if '@' in user_alipay_id:
           user_email = user_alipay_id
       elif len(user_taobao_email) > 3:
           user_email = user_taobao_email
       else:
           user_email = ''
       return (user_phone, user_alipay_id, user_email)



import re
def fill_slot(charge_account, user_alipay_account_id, user_taobao_email, user_receiver_address):
    ## 解析用户手机号
    ## 手机号只可能存在于 charge_account 和 user_receiver_address
    charge_phone_list = re.findall('1[3,4,5,7,8,9]\d{9}', charge_account)
    charge_phone = charge_phone_list[0] if charge_phone_list else ''
    receiver_phone_list = re.findall('1[3,4,5,7,8,9]\d{9}', user_receiver_address)
    receiver_phone = receiver_phone_list[0] if receiver_phone_list else ''
    if len(charge_phone) == 11 and len(receiver_phone) == 11 and charge_phone == receiver_phone:
        user_phone = charge_phone
    elif len(charge_phone) == 11:
        user_phone = charge_phone
    elif len(receiver_phone) == 11:
        user_phone = receiver_phone
    else:
        user_phone = ''
    ## 解析用户支付宝账号
    ## 邮箱 user_alipay_account_id 和 user_taobao_email
    if '@' in user_alipay_account_id:
        # email
        alipay_email_pre = user_alipay_account_id.split('@')[0]
        alipay_email_suf = user_alipay_account_id.split('@')[1]
        if alipay_email_pre[:3] == '***' \
            and len(user_taobao_email) > 0 \
            and user_taobao_email.split('@')[0][3:] == alipay_email_pre[3:]:
            user_alipay_id = user_taobao_email
        elif alipay_email_pre[:3] == '***' \
            and charge_account[3:] == alipay_email_pre[3:]:
            user_alipay_id = charge_account + '@' + alipay_email_suf
        elif alipay_email_pre[:3] == '***' \
            and user_receiver_address[3:] == alipay_email_pre[3:]:
            user_alipay_id = user_receiver_address + '@' + alipay_email_suf
        else:
            user_alipay_id = user_alipay_account_id
    elif user_phone[:3] == user_alipay_account_id[:3] \
            and user_phone[7:] == user_alipay_account_id[7:] \
            and user_alipay_account_id[3:7] == '****':
            user_alipay_id = user_phone
    else:
        user_alipay_id = user_alipay_account_id

    ## 解析用户邮箱
    if '@' in user_alipay_id:
        user_email = user_alipay_id
    elif len(user_taobao_email) > 3:
        user_email = user_taobao_email
    else:
        user_email = ''
    return user_phone, user_alipay_id, user_email

    # 通过聚石塔数据完成支付宝账号清洗
    # 无法完成清洗的使用充值账号进行清洗
    # 提取手机号作为主键进行数据关联
    # 支付宝邮箱 阿里系
    # 腾讯信系账号
    # 统计各大平台账号类型 发现规律 将数据映射的可行性最大化
# 189****3288
# 1493111827436
# 19806785871
# 19806785871
# 012345678910
if __name__ == '__main__':
    data_list = [item.split('\t') for item in test_str.split('\n') if len(item) > 0]
    for row_data in data_list:
        print('################################################')
        print('init_data: ', row_data)
        print('analyse res: ', complete_slot(row_data[0], row_data[1], row_data[3], row_data[4]))


# '17688679089'
# re.findall('(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', '17688679089')
#
# re.findall('1[3,4,5,7,8]\d{9}', '17688679089')










