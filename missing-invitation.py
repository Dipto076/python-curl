import requests

input = open('input.txt', 'r')
success = open('success.txt', 'w')
fail = open('fail.txt', 'w')

url = 'http://10.10.10.10:8070/offer_v2/api/v1/internal/promo/activate'
headers = {'Content-Type': 'application/json'}

for row in input:
	row = row.rstrip('\n')
	a,b = row.split(',')
	accountId = a
	promo = b
	payload = '{\"accountId\": %s,\"promoCode\": %s}' % (accountId, promo)
	response = requests.post(url, data=payload, headers=headers)
	message = response.json()['message']

	result = "accountId : %s, promo : %s, message : %s\n" % (accountId, promo, message)

	print(result)
	
	if(message == 'Promo code activated'):
		success.write(result)
	else:
		fail.write(result)


