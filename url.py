from base64 import b64encode
from datetime import date

def create_fb_url(string, dt = date.today()):
	a_1 = "https://www.facebook.com/search/posts/?q="
	a_3 = "&filters="
	a_5 = "&epa=FILTERS"
	a_2 = convert_url(string)
	a_4 = b64encode(time_to_string(dt).encode()).decode()
	return a_1 + a_2 + a_3 + a_4[:-2] + a_5

def convert_url(string):
	result = ""
	for i in string:
		if i == ' ':
			result += "%20"
		else:
			result += i
	return result

def time_to_string(date):
	s = "{\"rp_creation_time\":\"{\\\"name\\\":\\\"creation_time\\\",\\\"args\\\":\"{\\\\\\\"start_year\\\\\\\":\\\\\\\""+str(date.year)+ "\\\\\\\",\\\\\\\"start_month\\\\\\\":\\\\\\\""+str(date.year)+"-"+str(date.month)+"\\\\\\\",\\\\\\\"end_year\\\\\\\":\\\\\\\""+str(date.year) + "\\\\\\\",\\\\\\\"end_month\\\\\\\":\\\\\\\"" +str(date.year)+ "-" + str(date.month)+ "\\\\\\\",\\\\\\\"start_day\\\\\\\":\\\\\\\"" + str(date.year)+ "-" + str(date.month)+ "-" +str(date.day -1) + "\\\\\\\",\\\\\\\"end_day\\\\\\\":\\\\\\\"" + str(date.year)+ "-" + str(date.month)+ "-"+str(date.day) + "\\\\\\\"}\"}\"}"
	return s


def add_url(string, new, dt = date.today(), days = 1):
	if string[0] == '#':
		new.write("<h1>"+string+"</h1>")
	else:
		new.write("<h3>"+string+"</h3>")
		new.write("<a href=\""+create_fb_url(string, dt)+"\">"+string+"</a>")
	return
	
if __name__=='__main__':
		#abrir archivo búsquedas
		queries = open("queries.txt", "r")
		#crear archivo + inicializar html
		new = open("fb_urls.html", "w")
		#bucle crear url + añadir al html
		new.write("<!DOCTYPE html><html><body>\n")
		for line in queries:
			add_url(line, new)
		#cerrar
		new.write("</body></html>")
		queries.close()
		new.close()
