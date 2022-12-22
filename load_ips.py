def mac_to_vendor(mac):
  from mac_vendor_lookup import MacLookup
  if mac[0] == '-':
    return '-'
  try:
    return MacLookup().lookup(mac)
  except Exception:
    return '-'
  
def get_mac(ip):
  import subprocess  
  mac_info = subprocess.getoutput("arp -a "+ip)
  import re  
  result = re.findall(r'\S*', mac_info)
  if result[6][0] == 'e':
    result[6] = '-'
  return result[6]
  
with open('ip_list.txt') as f:
  lines = f.readlines()
    
for line in lines:
  print(line.rstrip() + ' ' + get_mac(line.rstrip()) + ' ' + mac_to_vendor(get_mac(line.rstrip())))