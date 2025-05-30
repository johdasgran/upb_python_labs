# 2. Transacciones Repetidas Cercanas

ip_addresses_arr = [
  "192.168.0.1",
  "192.168.1.100",
  "10.0.0.5",
  "172.16.254.3",
  "192.168.1.100",
  "192.168.1.100",
  "203.0.113.45",
  "8.8.8.8",
  "192.0.2.10",
  "10.1.1.1",
  "172.31.255.254",
  "192.168.1.100",
  "198.51.100.23",
  "192.168.10.10",
  "127.0.0.1"
  "8.8.8.8",
  "192.168.1.100",
  "8.8.8.8",
]

k = 8

ip_addresses_arr_by_k = ip_addresses_arr[:k]
ip_addresses_arr_repeated_by_k = []

for ip in ip_addresses_arr_by_k:
    found = False
    for ip_repeated in ip_addresses_arr_repeated_by_k:
      if ip_repeated['ip'] == ip:
         ip_repeated['count'] += 1
         found = True
         break
    if not found:
      ip_addresses_arr_repeated_by_k.append({
          "ip": ip,
          "count": 1
      })

for ip in ip_addresses_arr_repeated_by_k:
   print(f"La {ip['ip']} se ha repetido { ip['count']} veces")


