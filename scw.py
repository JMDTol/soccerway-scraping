import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time
import re


LONGEST_WAIT_SEC = 60

start_page_url = "http://au.soccerway.com/national/australia/a-league/20162017/regular-season/r35455/matches/"
driver = webdriver.Chrome('/Users/ik/Codes/soccerway-scraping/chromedriver')
#driver = webdriver.PhantomJS()

driver.get(start_page_url)
driver.implicitly_wait(20)
# wait up to 10 seconds before throwing a TimeoutException (if there's still no "Previous" link)

def wait_and_click_by_link_text(txt):

	try:
		#ActionChains(driver)
		e = WebDriverWait(driver, 20).until(
		     EC.element_to_be_clickable((By.CSS_SELECTOR, "#page_competition_1_block_competition_matches_7_previous")))	
		#ActionChains(driver).move_to_element(e).perform()
		#print("trying to focus on","document.getElementsById('" + e.get_attribute("id") + "').focus()")	
		driver.execute_script("arguments[0].click()", e)
		#driver.execute_script("document.getElementsByClassName('" + e.get_attribute("id") + "').focus()");
		time.sleep(5)

		#e.click()
		print("clicked, moving on..",e.get_attribute("class"))
	# A finally clause is always executed before leaving the try statement, whether an exception has occurred or not
	except:
		print("waited but that element didn't become clickable anyway..")
	 		#driver.quit()
	
	time.sleep(3)

def is_pagination_possible(txt):

	try:
	    if re.search(r"\s*"+txt.lower()+"\s*$", WebDriverWait(driver, 20).until(
	        EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, txt))).get_attribute("class")):
	    	click_enabled = True
	    else:
	    	click_enabled = False
	# A finally clause is always executed before leaving the try statement, whether an exception has occurred or not
	except:
		print("waited but that element didn't become visible anyway..")
	 		#driver.quit()
	return click_enabled



wait_and_click_by_link_text("Previous")
print("is Next possible?",is_pagination_possible("Next") )
print("is Previous possible?",is_pagination_possible("Previous") )
wait_and_click_by_link_text("Next")

driver.quit()

# def is_another_page_before(dr):
	
# 	try:
# 		prev_link = WebDriverWait(driver, 20).until(
# 			EC.find_element_by_partial_link_text("Previous")
# 		)
# 	# A finally clause is always executed before leaving the try statement, whether an exception has occurred or not
# 	except:
# 		print("waited too long...")

# 	#prev_link_class_name = dr.find_element_by_class_name("nav_description").find_element_by_id("page_competition_1_block_competition_matches_7_previous").get_attribute("class")
# 	#time.sleep(3)
# 	print("looking for:", prev_link.get_attribute("class"))
# 	if re.search(r"\s*previous\s*$", prev_link.get_attribute("class")):
# 		is_last_page  = False
# 		print("there is another page bofore this one..")
# 	elif re.search(r"\s*previous\s+disabled\s*$", prev_link.get_attribute("class")):
# 		is_last_page = True
# 	else:
# 		print("note: unusual previous link",prev_link.get_attribute("class"))

# 	return not is_last_page

# def is_another_page_after(dr):
	
# 	next_link_class_name = dr.find_element_by_class_name("nav_description").find_element_by_id("page_competition_1_block_competition_matches_7_next").get_attribute("class")
# 	print("looking for",next_link_class_name)
# 	if re.search(r"\s*next\s*$", next_link_class_name):
# 		is_last_page  = False
# 	elif re.search(r"\s*next\s+disabled\s*$", next_link_class_name):
# 		is_last_page = True
# 	else:
# 		print("note: unusual next link",next_link_class_name)

# 	return not is_last_page

# def scrape_results_table(s):
# 	# first, go to the match table
# 	match_table = s.find("table", {"class": "matches"})
	
# 	all_rows = match_table.findAll("tr", {"class": True, "data-timestamp": True, "id": True, "data-competition": True})
# 	# look for table rows

# 	for table_row in all_rows:
# 		# and then start going through every table cell in this row
# 		week_day = table_row.find("td", {"class": "day no-repetition"}).text.strip()
# 		list_days.append(week_day)
# 		date = table_row.find("td",{"class": "date no-repetition"}).text.strip()
# 		list_dates.append(date)
	
# 		home_team = table_row.find("td",{"class": "team team-a "}).find("a")
	
# 		list_home_teams.append(home_team["title"].strip())
	
# 		away_team = table_row.find("td",{"class": "team team-b "}).find("a")
# 		list_away_teams.append(away_team["title"].strip())
	
# 		score = table_row.find("td",{"class": "score-time score"})

# 		print("getting score link..")
# 		score_link = score.a
# 		print("score link is",score_link["href"])
		
# 		try:
# 			st = "a[href*=" + score_link['href'] + "]"
# 			print(st)
# 			element_to_click = WebDriverWait(driver, LONGEST_WAIT_SEC).until(EC.element_to_be_clickable((By.CSS_SELECTOR())))
# 		finally:
# 			pass

# 		driver.execute_script("arguments[0].click()", element_to_click)

# 		if score:

# 			score_a = score.find("a")
			
# 			if "-" in score_a.text:

# 				sc_home, sc_away = score_a.text.split("-")
# 				list_home_team_scores.append(sc_home.strip())
# 				list_away_team_scores.append(sc_away.strip())

# 			elif score_a.text == "PSTP":

# 				list_home_team_scores.append(score_a.text)
# 				list_away_team_scores.append(score_a.text)
# 		else:
			
# 			list_home_team_scores.append(None)
# 			list_away_team_scores.append(None)

# 		# try:
# 		# 	element_to_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sc))
# 		# print("now clicking..")
# 		# driver.execute_script("arguments[0].click()", element_to_click)



# 	return zip(list_days, list_dates, list_home_teams, list_home_team_scores, list_away_teams, list_away_team_scores)

# # try:
# #     element = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.ID, "myDynamicElement"))
# #     )
# #  finally:

# # the starting page is assumed to be a valid page with the results table and all

# #
# # click "Previous" until end up on the very first page
# #
# #element_to_click = driver.find_element_by_id("page_competition_1_block_competition_matches_7_previous")
# clicks_to_first_page = 0

# while is_another_page_before(driver):
# 	print("page before?",is_another_page_before(driver))
# 	clicks_to_first_page += 1
# 	print("already clicked:",clicks_to_first_page)
# 	try:
# 		element_to_click = WebDriverWait(driver, 20).until(
# 		    EC.element_to_be_clickable((By.ID, "page_competition_1_block_competition_matches_7_previous"))
# 		)
# # A finally clause is always executed before leaving the try statement, whether an exception has occurred or not
# 	finally:
#  		print("waited but that element didn't show anyway..")
#  			#driver.quit()

# 	driver.execute_script("arguments[0].click()", element_to_click)

# print("got to the very first page; had to click 'Previous' {} times...".format(clicks_to_first_page))


# # create a soup object
# s = BeautifulSoup(driver.page_source, "lxml")

# list_days = []
# list_dates = []
# list_home_teams = []
# list_away_teams = []
# list_home_team_scores = []
# list_away_team_scores = []

# pp1 = scrape_results_table(s)

# # element = driver.find_element_by_id("page_competition_1_block_competition_matches_7_previous")
# # print("found elelent:",element.get_attribute('id'),"and",element.get_attribute('text'))
# # print("is there another page to see?",is_another_page_before(driver))
# # #rint("OLD PAGE:", driver.page_source)
# # print("now clicking..")
# # element.click()
# # time.sleep(10)
# # driver.execute_script("arguments[0].click()", element)
# # #element.click()
# # #selenium.FireEvent(element, 'click')
# # print("clicked. wait 30 seconds..")
# # time.sleep(30)
# #print("NEW PAGE:", driver.page_source)
# #print("current URL:",driver.current_url)
# #s1 = BeautifulSoup(driver.page_source, "lxml")
# #pp2 = scrape_results_table(s1)

# print("page1:",pp1)
# for zi in pp1:
#  	print(zi)
# print("page2:",pp2)
# for zi in pp2:
#  	print(zi)

# while True: 

	

# 	prev_page_element = driver.find_element_by_class_name("nav_description").find_element_by_tag_name("a")

# 	#print("prev_page_element=",prev_page_element)
	
# 	#
# 		score_to_click = driver.find_element_by_partial_link_text('matches')
# 		print('will click ',score_to_click)
# 		score_to_click.click()

# 		#print("game week:",driver.find_element_by_link_text("Game week").text)
	
# 		i
	
		# print(list_away_teams)
# 		# is there another page to scrape
# 	if is_another_page_before(driver):
		
# 		print("doing click...")
# 		what_to_click = driver.find_element_by_id("page_competition_1_block_competition_matches_7_previous")
# 		what_to_click.click()
# 		pc += 1
# 		print("current page:",pc)
# 		time.sleep(3)
# 	else:
# 		print("no more pages...")
# 		break

# print("scraped {} pages".format(pc))

"""
Finally, the browser window is closed. You can also call quit method instead of close. 
The quit will exit entire browser whereas close` will close one tab, but if just one tab was open, 
by default most browser will exit entirely
"""
# check if the driver title contains the word Australia (if it does, it's an indication that we're grabbing the right page)
#assert "Australia" in driver.title 
#print("title:",driver.title)

#driver.close()

