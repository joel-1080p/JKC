SCHTASKS /CREATE /SC DAILY /TN "get_JKC_price" /TR "'C:\Program Files (x86)\JKC\get_JKC_price.exe'" /ST 15:22 /RL HIGHEST /RU %username% /RP