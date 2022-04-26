import json
import urllib.parse
import urllib.request

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Cookie': 'BIDUPSID=1E7D99BBFC0F0A68E410AD60A4C1978A; PSTM=1639188800; H_WI'
              'SE_SIDS=107317_110085_127969_131862_174441_179347_184716_185268_'
              '185634_187605_189037_189087_189325_189755_190247_190791_191068_1'
              '91252_191287_192206_192384_192407_192958_193283_193560_194085_19'
              '4511_194520_195003_195016_195187_195328_195342_195631_196045_196'
              '425_196590_197003_197242_197470_197472_197479_197711_197783_1978'
              '28_197957_198262_198445_198515_198650_198665_199082_199305_19946'
              '7_199489_199567_199642_199753_199754_199778_199967_200037_200128'
              '_200434_200450_200541_200556_200743_200968_201054_201104_201191_'
              '201328_201536_201581_201625_201699_201934_201947_201979_201996_2'
              '02177_202554_202561_202911_202915_202969; BAIDUID=E45D091DBFC233'
              '2C826F69337034F124:FG=1; BDSFRCVID=_WkOJeC62l6ypaTDjH44usJH5xS_A'
              'G3TH6ao5bUjY3stbaPxsXJ7EG0P8U8g0KubzcDrogKK32OTH6KF_2uxOjjg8UtVJ'
              'eC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJIe_C-atC-3Hn7gMtTJq4FDhUn2etJyaR'
              '38bCbvWJ5TMCozht5kKtDnDfQAQ5ovK5Tz-t3tQP05ShPCb6bIMb8QQGJ4WUnla2'
              'tL-Rn13l02V-Oae-t2ynLV2xbRbtRMW20eoq7mWIQvsxA45J7cM4IseboJLfT-0b'
              'c4KKJxbnLWeIJIjjCKjjJ0ja_DtTn2aKn0WJ082R6oDn8k-PnVeT0BLtnZKxtqtD'
              'jL3qchKq-5V45S5jb-e-tW5U5n-5JnWncKWhoS-PJPMp5syUjoXKuAM-v405OT-a'
              'IO0KJcbRo0Hpb4hPJvyTJXXnO7tfnlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtI'
              'FtVD_atKKMMDDmePbob-FHbgT024RyK-o2WbCQJboM8pcNLTDKhqKg2h-f0poWBg'
              'otQhcd-KJKfxjd0lO1j4_eyt5I563IMH79LtQgL4LKqq5jDh0Kb6ksD-Rt5JT23T'
              'ry0hvctKocShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2b6QhDG_et60ttR'
              'PsL-35HJTVDn7nq4bohjPm3UR9BtQmJJrQ_tTMKxbUjlPmjbo5yxv02bbd3x-eQg'
              '-q3RAaKf58oDOR5-5H0bkyW-Cf0x-jLnbPVn0MW-5DJROeK4nJyUnyD4nnBT5i3H'
              '8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRh_CcJ-J8XMC_xejrP; BCLID_BFESS='
              '11432987379298397936; BDSFRCVID_BFESS=_WkOJeC62l6ypaTDjH44usJH5x'
              'S_AG3TH6ao5bUjY3stbaPxsXJ7EG0P8U8g0KubzcDrogKK32OTH6KF_2uxOjjg8U'
              'tVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJIe_C-atC-3Hn7gMtTJq4FDh'
              'Un2etJyaR38bCbvWJ5TMCozht5kKtDnDfQAQ5ovK5Tz-t3tQP05ShPCb6bIMb8QQ'
              'GJ4WUnla2tL-Rn13l02V-Oae-t2ynLV2xbRbtRMW20eoq7mWIQvsxA45J7cM4Ise'
              'boJLfT-0bc4KKJxbnLWeIJIjjCKjjJ0ja_DtTn2aKn0WJ082R6oDn8k-PnVeT0BL'
              'tnZKxtqtDjL3qchKq-5V45S5jb-e-tW5U5n-5JnWncKWhoS-PJPMp5syUjoXKuAM'
              '-v405OT-aIO0KJcbRo0Hpb4hPJvyTJXXnO7tfnlXbrtXp7_2J0WStbKy4oTjxL1D'
              'b3JKjvMtIFtVD_atKKMMDDmePbob-FHbgT024RyK-o2WbCQJboM8pcNLTDKhqKg2'
              'h-f0poWBgotQhcd-KJKfxjd0lO1j4_eyt5I563IMH79LtQgL4LKqq5jDh0Kb6ksD'
              '-Rt5JT23Try0hvctKocShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2b6QhD'
              'G_et60ttRPsL-35HJTVDn7nq4bohjPm3UR9BtQmJJrQ_tTMKxbUjlPmjbo5yxv02'
              'bbd3x-eQg-q3RAaKf58oDOR5-5H0bkyW-Cf0x-jLnbPVn0MW-5DJROeK4nJyUnyD'
              '4nnBT5i3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRh_CcJ-J8XMC_xejrP; H_P'
              'S_PSSID=36309_31660_34812_36165_34584_36120_35863_26350_36303_22'
              '158_36061; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS'
              '=E45D091DBFC2332C826F69337034F124:FG=1; delPer=0; PSINO=6; BA_HE'
              'CTOR=a421ag8h0la50h21q51h6difb0r; Hm_lvt_64ecd82404c51e03dc91cb9'
              'e8c025574=1650903534; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1'
              '650903534; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY'
              '_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': 'cb46c5d7bec7dac5e871e6c8505cccf0',
    'domain': 'common',
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)
