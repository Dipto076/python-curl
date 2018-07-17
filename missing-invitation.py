import requests,csv,sys

success = open('success.txt', 'w')
fail = open('fail.txt', 'w')

server = 'localhost'
port = '8070'

if(len(sys.argv)==3):
	server = sys.argv[1]
	port = sys.argv[2]

url = 'http://%s:%s/offer_v2/api/v1/internal/promo/activate' % (server, port)
headers = {'Content-Type': 'application/json'}

counter = 0
with open('valid_invitation_code_users_request.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		counter += 1
		accountId = row['data_accountID']
		promo = row['data_promoCode']
		# print(str(accountId) + ' ' + str(promo))
		payload = '{\"accountId\": %s,\"promoCode\": "%s"}' % (accountId, promo)
		print(payload)
		response = requests.post(url, data=payload, headers=headers)
		message = response.json()['message']

		result = "row: %s, accountId : %s, promo : %s, message : %s\n" % (counter, accountId, promo, message)

		print(result)
		
		if(message == 'Promo code activated'):
			success.write(result)
		else:
			fail.write(result)


