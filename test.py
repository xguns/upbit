import pyupbit

access = "FquAJLqb0vKTyui9xzsJrrBQqhRHThxBCLcPZOK4"          # 본인 값으로 변경
secret = "XLA6LeNxGOSwTdrEMJCJtCLMVMv5REUNeLv934y4"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
