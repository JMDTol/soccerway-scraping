import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re

start_page_url = "http://au.soccerway.com/national/australia/a-league/20162017/regular-season/r35455/matches/"

driver = webdriver.Chrome('/Users/ik/Codes/soccerway-scraping/chromedriver')
driver.set_window_size(1124, 850)
driver.get(start_page_url)
time.sleep(3)

# check if the driver title contains the word Australia (if it does, it's an indication that we're grabbing the right page)
assert "Australia" in driver.title 

def is_another_page(dr):
	
	prev_link_class_name = dr.find_element_by_class_name("nav_description").find_element_by_id("page_competition_1_block_competition_matches_7_previous").get_attribute("class")
	next_link_class_name = dr.find_element_by_class_name("nav_description").find_element_by_id("page_competition_1_block_competition_matches_7_next").get_attribute("class")

	if re.search(r"\s*previous\s*$", prev_link_class_name):
		is_last_page  = False
	elif re.search(r"\s*previous\s+disabled\s*$", prev_link_class_name):
		is_last_page = True
	else:
		print("note: unusual previous link",prev_link_class_name)

	return not is_last_page

def scrape_results_table(s):
	# first, go to the match table
	match_table = s.find("table", {"class": "matches"})
	# look for table rows
	for table_row in match_table.findAll("tr", {"class": True, "data-timestamp": True, "id": True, "data-competition": True}):
		# and then start going through every table cell in this row
		week_day = table_row.find("td", {"class": "day no-repetition"}).text.strip()
		list_days.append(week_day)
		date = table_row.find("td",{"class": "date no-repetition"}).text.strip()
		list_dates.append(date)
	
		home_team = table_row.find("td",{"class": "team team-a "}).find("a")
	
		list_home_teams.append(home_team["title"].strip())
	
		away_team = table_row.find("td",{"class": "team team-b "}).find("a")
		list_away_teams.append(away_team["title"].strip())
	
		score = table_row.find("td",{"class": "score-time score"})
		if score:

			score_a = score.find("a")
			
			if "-" in score_a.text:

				sc_home, sc_away = score_a.text.split("-")
				list_home_team_scores.append(sc_home.strip())
				list_away_team_scores.append(sc_away.strip())

			elif score_a.text == "PSTP":

				list_home_team_scores.append(score_a.text)
				list_away_team_scores.append(score_a.text)
		else:
			
			list_home_team_scores.append(None)
			list_away_team_scores.append(None)

	return zip(list_days, list_dates, list_home_teams, list_home_team_scores, list_away_teams, list_away_team_scores)

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
#  finally:

# the starting page is assumed to be a valid page with the results table and all

s = BeautifulSoup(driver.page_source, "lxml")

list_days = []
list_dates = []
list_home_teams = []
list_away_teams = []
list_home_team_scores = []
list_away_team_scores = []

pp1 = scrape_results_table(s)

element = driver.find_element_by_id("page_competition_1_block_competition_matches_7_previous")
print("found elelent:",element.get_attribute('id'),"and",element.get_attribute('text'))
print("is there another page to see?",is_another_page(driver))
#rint("OLD PAGE:", driver.page_source)
print("now clicking..")
element.click()
time.sleep(10)
driver.execute_script("arguments[0].click()", element)
#element.click()
#selenium.FireEvent(element, 'click')
print("clicked. wait 30 seconds..")
time.sleep(30)
#print("NEW PAGE:", driver.page_source)
#print("current URL:",driver.current_url)
#s1 = BeautifulSoup(driver.page_source, "lxml")
#pp2 = scrape_results_table(s1)

#print("page1:",pp1)
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
# 	if is_another_page(driver):
		
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

driver.close()

