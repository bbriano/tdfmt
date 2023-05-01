tdfmt
=====

tdfmt formats datetime.timedelta

Install
-------

	pip install tdfmt

Use
---

	from datetime import timedelta
	from tdfmt.tdfmt import tdfmt

	print(tdfmt(timedelta(hours=3, minutes=14, seconds=15, microseconds=926535)))  # 3h14m15.926535s
	print(tdfmt(timedelta(hours=4, minutes=20)))                                   # 4h20m0s
	print(tdfmt(timedelta(minutes=17, seconds=38)))                                # 17m38s
	print(tdfmt(timedelta(seconds=9)))                                             # 9s
	print(tdfmt(timedelta(minutes=1, milliseconds=300)))                           # 1m0.3s
	print(tdfmt(timedelta(microseconds=12340)))                                    # 12.34ms
	print(tdfmt(timedelta(microseconds=12)))                                       # 12µs
