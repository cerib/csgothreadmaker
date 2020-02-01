#link = "https://www.hltv.org/matches/2339092/faze-vs-nip-blast-premier-spring-series-2020"
link = "https://www.hltv.org/matches/2336334/natus-vincere-vs-vitality-dreamhack-masters-malm-2019"


from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()

page = http.request('GET', link)
soup = BeautifulSoup(page.data, "html.parser")

teamsHtml = soup.find_all("div", class_="teamName")

teamA = teamsHtml[0].getText()
teamB = teamsHtml[1].getText()
maps = []
vetoesHtml = soup.find_all("div", class_="standard-box veto-box")[1].find_all("div", class_="padding")
vetoesText = []

#printing overall match scores
teamBoxesHtml = soup.find_all("div", class_="standard-box teamsBox")[0].find_all("div", class_="team")
teamAScore = teamBoxesHtml[0].find_all("div", class_=["won", "lost", "tie"])[0].text
teamBScore = teamBoxesHtml[1].find_all("div", class_=["won", "lost", "tie"])[0].text
print("#" + teamA + " [](#" + teamA.lower() + "-logo) " + teamAScore + "-" + teamBScore +" [](#" + teamB.lower() + "-logo) " + teamB + "\n\n")

#printing each map team scores
scoresHtml = soup.find_all("div", class_="mapholder")
mapNames = []
for teamscores in scoresHtml:
  mapName = teamscores.find("div", class_="mapname").text
  mapNames.append(mapName)
  print("**" + mapName + "**: " + teamscores.find_all("div", class_="results-team-score")[0].text + " - " + teamscores.find_all("div", class_="results-team-score")[1].text + "\n")

#printing veto info
print("\n---\n")
print("&nbsp;\n")
print("|[](#" + teamA.lower() + "-logo)|**MAP**|[](#" + teamB.lower() + "-logo)|")
print("|:--:|:--:|:--:|")
i = 0
for veto in vetoesHtml[0].text.strip().split("\n"):
  #currentTeam = veto.split(" ")[1]
  test = " ".join(veto.replace("removed", "__").replace("picked", "__").split("__")[0].split(" ")[1:]).strip()
  currentTeam = test
  method = veto.split(" ")[-2]
  currentMap = veto.split(" ")[-1].lower()

  if currentMap == "over":
    currentMap = veto.split(" ")[1].lower()
  #fix for when team has spaces in it
  #if currentMap == "picked" or currentMap == "removed":
  #  print(veto.split(" "))
  if method == "removed":
    if currentTeam == teamA:
      print("|**X**|[](#map-" + currentMap + ")||")
    else:
      print("||[](#map-" + currentMap + ")|**X**|")
  elif method == "picked":
    maps.append(currentMap)
    if currentTeam == teamA:
      print("|**✔**|[](#map-" + currentMap + ")||")
    else:
      print("||[](#map-" + currentMap + ")|**✔**|")
  else:
    maps.append(currentMap)
    print("||[](#map-"+ currentMap + ")||")
  i += 1
print("\n&nbsp;\n")
print("---\n")





#printing map scores
statsHtml = soup.find_all("div", class_="stats-content")[1:]
resultsHalfScoreHtml = soup.find_all("div", class_="results-center-half-score")
map_n = 1
i = 0
for stats in statsHtml:
  teamACt = ""
  teamBCt = ""
  teamAT = ""
  teamBT = ""
  scoresHtml = resultsHalfScoreHtml[i].find_all("span", class_=["ct", "t"])
  if scoresHtml[0]["class"][0] == "ct":
    teamACt = scoresHtml[0].text
    teamBT = scoresHtml[1].text
    teamAT = scoresHtml[2].text
    teamBCt = scoresHtml[3].text
  else:
    teamAT = scoresHtml[0].text
    teamBCt = scoresHtml[1].text
    teamACt = scoresHtml[2].text
    teamBT = scoresHtml[3].text
  mapName = mapNames[i]
  teamATotal = int(teamACt)+int(teamAT)
  teamBTotal = int(teamBCt)+int(teamBT)
  print("\n###MAP "+ str(map_n) +"/3: " + mapName + "\n")
  print("|Team|CT|T|Total|\n|:--|:--:|:--:|:--:|")
  print("|[](#"+teamA.lower()+"-logo) **"+ teamA + "**|" + str(teamACt) + "|"+ str(teamAT) + "|**" + str(teamATotal) + "**|")
  print("||**T**|**CT**|")
  print("|[](#"+teamB.lower()+"-logo) **"+ teamB + "**|" + str(teamBT) + "|"+ str(teamBCt) + "|**" + str(teamBTotal) + "**|")

  print("\n&nbsp;\n")

  tableA = stats.find_all("table")[0]
  tableB = stats.find_all("table")[1]

  print("|[](#"+teamA.lower()+"-logo) **"+ teamA +"**|**K-D**|**ADR**|**HLTV**|\n|:--|:--:|:--:|:--:|:--:|")  
  for j in range(0, 5):
    #gtSmartphone-only statsPlayerName
    playerName = tableA.find_all("span", class_="player-nick")[j].text
    playerKD = tableA.find_all("td", class_="kd text-center")[j+1].text
    playerADR = tableA.find_all("td", class_="adr text-center")[j+1].text
    playerHLTV = tableA.find_all("td", class_="rating text-center")[j+1].text
    print("|"+playerName+"|"+playerKD+"|"+playerADR+"|"+playerHLTV+"|")

  print("|[](#"+teamB.lower()+"-logo) **"+ teamB +"**|**K-D**|**ADR**|**HLTV**|")
  for j in range(0, 5):
    playerName = tableB.find_all("span", class_="player-nick")[j].text
    playerKD = tableB.find_all("td", class_="kd text-center")[j+1].text
    playerADR = tableB.find_all("td", class_="adr text-center")[j+1].text
    playerHLTV = tableB.find_all("td", class_="rating text-center")[j+1].text
    print("|"+playerName+"|"+playerKD+"|"+playerADR+"|"+playerHLTV+"|")
  i += 1
  map_n += 1


print("---\n&nbsp;\n---\n [Check out the HLTV match page](" + link + ")")
print("\n[Made for r/GlobalOffensive with <3 Check out github by clicking here and help improve the project!](https://github.com/cerib/csgothreadmaker)")