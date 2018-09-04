# -*- coding: utf-8 -*-
###################################################################################################
#
# NFL Videos for Plex (by 41john)
#
###################################################################################################

NFL_URL						= 'http://www.nfl.com'
NFL_URL1					= 'http://a.video.nfl.com/'
BASE_URL					= 'http://www.nfl.com/feeds-rs/videos/byChannel/%s.json?limit=100&offset=0'
LATEST_VIDEOS				= 'http://www.nfl.com/feeds-rs/videos/byChannel/nfl-videos.json?limit=100&offset=0'
NFL_NETWORK_LIVE			= 'https://www.nflgamepass.com/api/en/content/v1/web/network/data'
NFL_REDZONE					= 'https://www.nflgamepass.com/api/en/content/v1/web/redzone/videos'
GAMEPASS_SCHEDULE_WEEK		= 'https://www.nflgamepass.com/api/en/content/v1/web/games/seasons'
GAMEPASS_SCHEDULE			= 'https://www.nflgamepass.com/api/en/content/v1/web/games/%s/%s/%s/list'
NFL_VIDEOS_JSON				= 'http://www.nfl.com/static/embeddablevideo/%s.json'
NFLNA_PROGRAMS				= 'https://www.nflgamepass.com/api/en/content/v1/web/network/programs'
NFLGAMEPASS_TEAMS			= 'https://www.nflgamepass.com/api/en/content/v1/web/teams/list'

TEAMS = {'arizona-cardinals': 'Arizona Cardinals', 'atlanta-falcons': 'Atlanta Falcons', 'baltimore-ravens': 'Baltimore Ravens', 'buffalo-bills': 'Buffalo Bills', 'carolina-panthers': 'Carolina Panthers', 'chicago-bears': 'Chicago Bears', 'cincinnati-bengals': 'Cincinnati Bengals', 'cleveland-browns': 'Cleveland Browns', 'dallas-cowboys': 'Dallas Cowboys', 'denver-broncos': 'Denver Broncos', 'detroit-lions': 'Detroit Lions', 'green-bay-packers': 'Green Bay Packers', 'houston-texans': 'Houston Texans', 'indianapolis-colts': 'Indianapolis Colts', 'jacksonville-jaguars': 'Jacksonville Jaguars', 'kansas-city-chiefs': 'Kansas City Chiefs', 'los-angeles-chargers': 'Los Angeles Chargers', 'los-angeles-rams': 'Los Angeles Rams', 'miami-dolphins': 'Miami Dolphins', 'minnesota-vikings': 'Minnesota Vikings', 'new-england-patriots': 'New England Patriots', 'new-orleans-saints': 'New Orleans Saints', 'new-york-giants': 'New York Giants', 'new-york-jets': 'New York Jets', 'oakland-raiders': 'Oakland Raiders', 'philadelphia-eagles': 'Philadelphia Eagles', 'pittsburgh-steelers': 'Pittsburgh Steelers', 'san-francisco-49ers': 'San Francisco 49ers', 'seattle-seahawks': 'Seattle Seahawks', 'tampa-bay-buccaneers': 'Tampa Bay Buccaneers', 'tennessee-titans': 'Tennessee Titans', 'washington-redskins': 'Washington Redskins', 'None': 'Set Team in Preferences'}
ORDERED_TEAMS = ['arizona-cardinals','atlanta-falcons','baltimore-ravens','buffalo-bills','carolina-panthers','chicago-bears','cincinnati-bengals','cleveland-browns','dallas-cowboys','denver-broncos','detroit-lions','green-bay-packers','houston-texans','indianapolis-colts','jacksonville-jaguars','kansas-city-chiefs', "los-angeles-chargers", 'los-angeles-rams', 'miami-dolphins','minnesota-vikings','new-england-patriots','new-orleans-saints','new-york-giants','new-york-jets','oakland-raiders','philadelphia-eagles','pittsburgh-steelers','san-francisco-49ers','seattle-seahawks','tampa-bay-buccaneers','tennessee-titans','washington-redskins','None']

SHOWS = {'nfl-am': 'NFL AM', 'nfl-network-total-access': 'NFL Total Access', 'nfl-network-gameday': 'NFL GameDay', 'nfl-network-playbook': 'Playbook', 'nfl-films-sound-efx': 'Sound FX', 'nfl-top100-2014': 'Top 100 Players of 2014', 'nfl-top100-2013': 'Top 100 Players of 2013', 'nfl-network-path-to-the-draft': 'Path to the Draft', 'nfl-network-around-the-league': 'Around the League', 'nfl-fantasy': 'Fantasy', 'nfl-fantasy-team-by-team': 'Fantasy Team Previews', 'nfl-network-the-coaches': 'The Coaches', 'nfl-films-game-of-the-week': 'Game of the Week', 'nfl-films-americas-game': 'Americas Game', 'nfl-films-presents': 'NFL Films Presents', 'nfl-films-anatomy-of-a-play': 'Anatomy of a Play', 'nfl-network-hard-knocks': 'Hard Knocks', 'nfl-redzone-videos': 'NFL Redzone Top 5 Plays', 'a-football-life': 'A Football Life', 'nfl-network-top-ten': 'NFL Top Ten Plays'}
ORDERED_SHOWS = ['nfl-am', 'nfl-network-total-access', 'nfl-network-gameday', 'nfl-network-playbook', 'nfl-films-sound-efx', 'nfl-top100-2014', 'nfl-top100-2013', 'nfl-network-path-to-the-draft', 'nfl-network-around-the-league', 'nfl-fantasy', 'nfl-fantasy-team-by-team', 'nfl-network-the-coaches', 'nfl-films-game-of-the-week', 'nfl-films-americas-game', 'nfl-films-presents', 'nfl-films-anatomy-of-a-play', 'nfl-network-hard-knocks', 'nfl-redzone-videos', 'a-football-life', 'nfl-network-top-ten']

SPOTLIGHT = {'nfl-countdowns': 'Countdowns', 'nfl-cant-miss-plays': 'Cant Miss Plays', 'nfl-drive-of-the-week': 'Drive Of The Week', 'nfl-the-season': 'The Season', 'nfl-player-interviews': 'Player Interviews', 'nfl-game-previews': 'Game Previews'}
ORDERED_SPOTLIGHT = ['nfl-countdowns', 'nfl-cant-miss-plays', 'nfl-drive-of-the-week', 'nfl-the-season', 'nfl-player-interviews', 'nfl-game-previews']

EVENTS = {'nfl-draft': 'Draft', 'nfl-mini-camps': 'Minicamps', 'nfl-training-camps': 'Training Camps', 'nfl-super-bowl-commercials': 'Commercials', 'nfl-hall-of-fame': 'Hall of Fame', 'nfl-preseason': 'Preseason', 'nfl-kickoff': 'Kickoff', 'nfl-thanksgiving': 'Thanksgiving', 'nfl-playoffs': 'Playoffs', 'nfl-super-bowl': 'Super Bowl', 'nfl-pro-bowl': 'Pro Bowl', 'nfl-free-agency': 'Free Agency', 'nfl-combine': 'Combine', 'nfl-senior-bowl': 'Senior Bowl', 'nfl-international-series': 'International Series', 'nfl-rookie-symposium': 'Rookie Symposium', 'nfl-thursday-night-football': 'NFL Thursday Night Football', 'nfl-honors': 'NFL Honors'}
ORDERED_EVENTS = ['nfl-draft', 'nfl-mini-camps', 'nfl-training-camps', 'nfl-super-bowl-commercials', 'nfl-hall-of-fame', 'nfl-preseason', 'nfl-kickoff', 'nfl-thanksgiving', 'nfl-playoffs', 'nfl-super-bowl', 'nfl-pro-bowl', 'nfl-free-agency', 'nfl-combine', 'nfl-senior-bowl', 'nfl-international-series', 'nfl-rookie-symposium', 'nfl-thursday-night-football','nfl-honors']

NAME = 'NFL Network'
ART  = 'art-default.jpg'
ICON = 'icon-default.png'

####################################################################################################

def Start():

	ObjectContainer.title1 = NAME
	ObjectContainer.art = R(ART)
	DirectoryObject.thumb = R("nfl-network.png")
	DirectoryObject.art = R(ART)

	HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'

###################################################################################################

@handler('/video/nflvideos', NAME, thumb=ICON, art=ART)
def VideoMainMenu():
	
	oc = ObjectContainer()
	
	for category in ORDERED_TEAMS:
		if Prefs['team'] == category:
			sTitle = TEAMS[category]
		
	oc.add(DirectoryObject(key = Callback(NFLVideosMenu), title="NFL.com Videos", summary="Browse videos from NFL.com/Videos"))
	oc.add(DirectoryObject(key = Callback(PlayMenu, url=BASE_URL % Prefs['team']), title=sTitle, summary="Set your favourite team in Preferences and browse videos for that team here", thumb=R("%s.png" % Prefs['team'])))
	if Prefs['gamepasssub'] == "GamePass Europe":
		oc.add(DirectoryObject(key = Callback(GamepassMenu), title="NFL GamePass Europe", summary="NFL GamePass Europe subscribers only", thumb=R("gamepass.png")))
	oc.add(PrefsObject(title="Preferences", summary="Set My Team. Enter subscription details for Gamepass", thumb=R("icon-prefs.png")))
	return oc

###################################################################################################

@route('/video/nflvideos/nflvideosmenu')
def NFLVideosMenu():
	
	oc = ObjectContainer(title2="NFL.com Videos")
	
	oc.add(DirectoryObject(key = Callback(PlayMenu, url=LATEST_VIDEOS), title="Latest Videos", summary="Browse the latest videos"))
	oc.add(DirectoryObject(key = Callback(ShowsMenu), title="Shows", summary="Browse videos for different NFL shows"))
	oc.add(DirectoryObject(key = Callback(TeamsMenu), title="Teams", summary="Browse videos by team"))
	oc.add(DirectoryObject(key = Callback(SpotlightMenu), title="Channels", summary="Browse videos for different NFL channels"))
	oc.add(DirectoryObject(key = Callback(EventsMenu), title="Events", summary="Browse videos by Event"))
	return oc

###################################################################################################

@route('/video/nflvideos/shows')
def ShowsMenu():

	oc = ObjectContainer(title2="Shows")

	for category in ORDERED_SHOWS:
		oc.add(DirectoryObject(key=Callback(PlayMenu, url=BASE_URL % category), title=SHOWS[category], thumb=R("%s.png" % category)))

	return oc

###################################################################################################

@route('/video/nflvideos/teams')
def TeamsMenu():

	oc = ObjectContainer(title2="Teams")

	for category in ORDERED_TEAMS:
		oc.add(DirectoryObject(key=Callback(PlayMenu, url=BASE_URL % category), title=TEAMS[category], thumb=R("%s.png" % category)))

	return oc

###################################################################################################

@route('/video/nflvideos/spotlight')
def SpotlightMenu():

	oc = ObjectContainer(title2="Channels")

	for category in ORDERED_SPOTLIGHT:
		oc.add(DirectoryObject(key=Callback(PlayMenu, url=BASE_URL % category), title=SPOTLIGHT[category], thumb=R("%s.png" % category)))

	return oc

###################################################################################################

@route('/video/nflvideos/events')
def EventsMenu():

	oc = ObjectContainer(title2="Events")

	for category in ORDERED_EVENTS:
		oc.add(DirectoryObject(key=Callback(PlayMenu, url=BASE_URL % category), title=EVENTS[category], thumb=R("%s.png" % category)))

	return oc

###################################################################################################

@route('/video/nflvideos/playmenu')
def PlayMenu(url=None):

	oc = ObjectContainer(title2="NFL.com/Videos")
	list = JSON.ObjectFromURL(url)['videos']

	for stream in list:
		try:
			streamid = stream['id']
			sTitle = stream['briefHeadline']
			sSummary = stream['caption']
			sThumb = stream['largeImageUrl']
			sStreamURL = stream['videoBitRates'][-5]['videoPath'] + "#" + streamid
			if sStreamURL.startswith("http://video.nfl.com"):
				sStreamURL = sStreamURL.replace("http://video.nfl.com","http://a.video.nfl.com")
			oc.add(VideoClipObject(url=sStreamURL, title=sTitle, summary=sSummary, thumb=sThumb))
		except:
			Log("Error obtaining URLs, ignoring Video")

	return oc

###################################################################################################	

@route('/video/nflvideos/gamepass')
def GamepassMenu():

	oc = ObjectContainer(title2="NFL Game Pass")
	
	oc.add(DirectoryObject(key=Callback(GamepassPlayweek), title="This Week's Games", thumb=R("gamepass-live.png"), summary="This Week's Games"))
	oc.add(DirectoryObject(key=Callback(GamepassSeason), title="Archived Games", thumb=R("gamepass.png"), summary="Archived games from this season back to 2013"))
	oc.add(DirectoryObject(key=Callback(GamepassTeamMenu), title="Team Games", summary="Watch Games for a team of your choice", thumb=R("gamepass.png")))
	oc.add(DirectoryObject(key=Callback(NflNetworkMenu), title="NFL Network Live", summary="Watch NFL Network Live", thumb=R("nfl-network-live.png")))
	oc.add(DirectoryObject(key=Callback(NflNetworkArchiveMenu), title="NFL Network Archive", summary="Watch NFL Network Archived Shows", thumb=R("nfl-network.png")))
	oc.add(DirectoryObject(key=Callback(NflRedzoneMenu), title="NFL Redzone Live", summary="Watch NFL Redzone Live", thumb=R("redzone-logo-live.png")))
	oc.add(DirectoryObject(key=Callback(NflRedzoneArchive), title="NFL Redzone Archive", thumb=R("redzone-logo.png"), summary="Archived Redzone channel Videos"))
	
	return oc

###################################################################################################

@route('/video/nflvideos/gamepassseason')
def GamepassSeason():

	oc = ObjectContainer(title2="NFL Game Pass")

	year = Datetime.Now().year if Datetime.Now().month < 7 else Datetime.Now().year+1

	for season in reversed(range(2013, year)):
		oc.add(DirectoryObject(key = Callback(GamepassWeek, season=str(season)), title=str(season), thumb=R("gamepass.png")))

	return oc

####################################################################################################

@route('/video/nflvideos/gamepassweek')
def GamepassWeek(season):

	oc = ObjectContainer(title2="NFL Game Pass")
	list = JSON.ObjectFromURL(GAMEPASS_SCHEDULE_WEEK, cacheTime=1)

	if season == '2018':
		seasonlist = list['modules']['mainMenu']['seasonStructureList'][0]
	if season == '2017':
		seasonlist = list['modules']['mainMenu']['seasonStructureList'][1]
	if season == '2016':
		seasonlist = list['modules']['mainMenu']['seasonStructureList'][2]
	if season == '2015':
		seasonlist = list['modules']['mainMenu']['seasonStructureList'][3]
	if season == '2014':
		seasonlist = list['modules']['mainMenu']['seasonStructureList'][4]
	if season == '2013':
		seasonlist = list['modules']['mainMenu']['seasonStructureList'][5]
		
	for seasontype in seasonlist['seasonTypes']:
		seasontypelist	= seasontype['weeks']
		for gameweek in seasontypelist:
			week = gameweek['_links'][0]['href']
			week = week.replace("https://nflgp-prd.akamaized.net","http://nflgamepass.com/api/en/content")
			week_title = gameweek['weekNameAbbr'] + str(gameweek['number'])
			week_title = week_title.replace("pro21","Pro Bowl").replace("hof0","Hall of Fame").replace("p","Preseason Week ").replace("week","Week ").replace("wc18","Wild Card Games").replace("div19","Divisional Games").replace("conf20","Conference Championship Games").replace("sb22","Super Bowl")
			oc.add(DirectoryObject(key = Callback(GamepassPlay, week=week, season=season, week_title=week_title), title = week_title, thumb=R("gamepass.png")))
	
	return oc
	
###################################################################################################

@route('/video/nflvideos/gamepassplay')	
def GamepassPlay(week, season, week_title):

	oc = ObjectContainer(title2=week_title)
	list = JSON.ObjectFromURL(week, cacheTime=1)
	
	try:
		for stream in list['modules']['weekLiveGames']['content']:
			sTeam1 = stream['visitorNickName']
			sTeam2 = stream['homeNickName']
			sTitle = "Live - %s @ %s" % (sTeam1,sTeam2)
			sStreamURL = "https://www.nflgamepass.com/api/en/content/v1/web/games/" + season + "/" + str(stream['gameId']) + "/data"
			try:
				videoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['video']['videoId'])
			except:
				videoId = '0'
			oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId + "#Live", title=sTitle,  thumb=R("icon-gamepass.png")))
	except:
		Log("No Live Games")
	try:
		for stream in list['modules']['weekCompletedGames']['content']:
			sTeam1 = stream['visitorNickName']
			sTeam2 = stream['homeNickName']
			sTitle = "%s @ %s" % (sTeam1,sTeam2)
			sStreamURL = "https://www.nflgamepass.com/api/en/content/v1/web/games/" + season + "/" + str(stream['gameId']) + "/data"
			try:
				condensedVideoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['condensedVideo']['videoId'])
				oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + condensedVideoId + "#Condensed", title=sTitle + " - Condensed Game",  thumb=R("icon-gamepass.png")))
			except:
				Log("No Condensed Games")
			try:
				coachesVideoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['coachfilmVideo']['videoId'])
				oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + coachesVideoId + "#CoachesFilm", title=sTitle + " - Coaches Film",  thumb=R("icon-gamepass.png")))
			except:
				Log("No Coaches Film")
			try:
				videoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['video']['videoId'])
				oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId, title=sTitle + " - Full Length Game",  thumb=R("icon-gamepass.png")))
			except:
				Log("No Full Length Games")
	except:
		Log("No Completed Games")
	try:
		for stream in list['modules']['weekScheduledGames']['content']:
			sTeam1 = stream['visitorNickName']
			sTeam2 = stream['homeNickName']
			sTitle = "Scheduled - %s @ %s" % (sTeam1,sTeam2)
			sStreamURL = "https://www.nflgamepass.com/api/en/content/v1/web/games/" + season + "/" + str(stream['gameId']) + "/data"
			try:
				videoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['video']['videoId'])
			except:
				videoId = stream['homeNickName']
			oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId, title=sTitle,  thumb=R("icon-gamepass.png")))
	except:
		Log("No Scheduled Games")

	return oc

###################################################################################################

@route('/video/nflvideos/gamepassplayweek')	
def GamepassPlayweek():

	oc = ObjectContainer(title2="NFL Game Pass")

	list = JSON.ObjectFromURL(GAMEPASS_SCHEDULE_WEEK, errors='ignore', cacheTime=1)

	season = list['modules']['meta']['currentContext']['currentSeason']
	seasonType = list['modules']['meta']['currentContext']['currentSeasonType']
	week = list['modules']['meta']['currentContext']['currentWeek']

	gamelist = JSON.ObjectFromURL(GAMEPASS_SCHEDULE % (season, seasonType, week), cacheTime=1)
	
	try:
		for stream in gamelist['modules']['weekLiveGames']['content']:
			sTeam1 = stream['visitorNickName']
			sTeam2 = stream['homeNickName']
			sTitle = "Live - %s @ %s" % (sTeam1,sTeam2)
			sStreamURL = "https://www.nflgamepass.com/api/en/content/v1/web/games/" + season + "/" + str(stream['gameId']) + "/data"
			try:
				videoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['video']['videoId'])
			except:
				videoId = '0'
			oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId + "#Live", title=sTitle,  thumb=R("icon-gamepass.png")))
	except:
		Log("No Live Games")
	try:
		for stream in gamelist['modules']['weekCompletedGames']['content']:
			sTeam1 = stream['visitorNickName']
			sTeam2 = stream['homeNickName']
			sTitle = "%s @ %s" % (sTeam1,sTeam2)
			sStreamURL = "https://www.nflgamepass.com/api/en/content/v1/web/games/" + season + "/" + str(stream['gameId']) + "/data"
			try:
				condensedVideoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['condensedVideo']['videoId'])
				oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + condensedVideoId + "#Condensed", title=sTitle + " - Condensed Game",  thumb=R("icon-gamepass.png")))
			except:
				Log("No Condensed Games")
			try:
				coachesVideoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['coachfilmVideo']['videoId'])
				oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + coachesVideoId + "#CoachesFilm", title=sTitle + " - Coaches Film",  thumb=R("icon-gamepass.png")))
			except:
				Log("No Coaches Film")
			try:
				videoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['video']['videoId'])
				oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId, title=sTitle + " - Full Length Game",  thumb=R("icon-gamepass.png")))
			except:
				Log("No Full Length Games")
	except:
		Log("No Completed Games")
	try:
		for stream in gamelist['modules']['weekScheduledGames']['content']:
			sTeam1 = stream['visitorNickName']
			sTeam2 = stream['homeNickName']
			sTitle = "Scheduled - %s @ %s" % (sTeam1,sTeam2)
			sStreamURL = "https://www.nflgamepass.com/api/en/content/v1/web/games/" + season + "/" + str(stream['gameId']) + "/data"
			try:
				videoId = str(JSON.ObjectFromURL(sStreamURL)['modules']['singlegame']['content'][0]['video']['videoId'])
			except:
				videoId = stream['homeNickName']
			oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId, title=sTitle,  thumb=R("icon-gamepass.png")))
	except:
		Log("No Scheduled Games")

	return oc

###################################################################################################

@route('/video/nflvideos/nflnetwork')	
def NflNetworkMenu():

	oc = ObjectContainer(title2="NFL Network")
	
	list = JSON.ObjectFromURL(NFL_NETWORK_LIVE, errors='ignore', cacheTime=1)

	onnow = list['modules']['networkEpg']['liveProgram']['shortDescription'].replace('\"','')
	onnext = list['modules']['networkEpg']['futurePrograms'][0]['shortDescription'].replace('\"','')
	videoId = str(list['modules']['networkLiveVideo']['content'][0]['videoId'])
	
	oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId + "#NFLNL", title="NFL Network Live", summary = "Now: " + onnow + "\n Next: " + onnext, thumb=R("icon-nfl-network-live.png")))

	return oc

###################################################################################################	

@route('/video/nflvideos/nflredzone')	
def NflRedzoneMenu():

	oc = ObjectContainer(title2="NFL Redzone Live")
	
	list = JSON.ObjectFromURL(NFL_REDZONE, errors='ignore', cacheTime=1)

	videoId = str(list['modules']['redZoneLive']['content'][0]['videoId'])

	oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId + "#NFLRL", title="NFL Redzone Live", summary="Watch NFL Redzone Live", thumb=R("icon-nfl-redzone-live.png")))

	return oc

###################################################################################################

@route('/video/nflvideos/nflredzonearchive')
def NflRedzoneArchive():

	oc = ObjectContainer(title2="NFL Redzone Archive")

	list = JSON.ObjectFromURL(NFL_REDZONE, errors='ignore', cacheTime=1)
	
	for stream in list['modules']['redZoneVod']['content']:
		sTitle = stream['season'].replace("season-","") + " " + stream['title']
		videoId = stream['videoId']
		sSummary = sTitle
		oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId + "#NFLRA", title=sTitle, summary=sSummary, thumb=R("icon-nfl-redzone-live.png")))

	return oc
	
###################################################################################################el

@route('/video/nflvideos/nflnarchiveplay')
def NFLNArchivePlay(title, id, thumbs):

	oc = ObjectContainer(title2=title)
		
	list = JSON.ObjectFromURL(url="https://www.nflgamepass.com/api/en/content/v1/web/network/"+id+"/list", errors='ignore', cacheTime=1)

	for stream in list['modules']['archive']['content']:
		sTitle = stream['title']
		videoId = stream['videoId']
		sSummary = stream['description'].replace("<p>","").replace("</p>","")
		sThumb = thumbs
		oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId + "#NFLRL", title=sTitle, summary=sSummary, thumb=sThumb))

	return oc
	
###################################################################################################

@route('/video/nflvideos/nflnetworkarchivemenu')
def NflNetworkArchiveMenu():

	oc = ObjectContainer(title2="NFL Network Archive")
	
	list = JSON.ObjectFromURL(NFLNA_PROGRAMS, errors='ignore', cacheTime=1)
	
	for program in list['modules']['programs']:
		programTitle = program['title']
		programId = program['slug']
		seasonslist = program['seasons']
		sThumb = program['thumbnail']['templateUrl'].replace("{formatInstructions}","w_512,h_512,c_thumb,q_auto,f_jpg")
		
		if not seasonslist:
			oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, title=programTitle, id=programId, thumbs=sThumb), title=programTitle, thumb=sThumb, summary=programTitle))
		else:
			for seasons in seasonslist:
				seasonTitle = seasons['value']
				seasonId =  seasons['slug']
				oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, title=programTitle + " " + seasonTitle, id=seasonId + "/" + programId, thumbs=sThumb), title=programTitle + " " + seasonTitle, thumb=sThumb, summary=programTitle + " " + seasonTitle))
		
	return oc

###################################################################################################

@route('/video/nflvideos/gamepassteammenu')
def GamepassTeamMenu():

	oc = ObjectContainer(title2="NFL Gamepass Teams")
	
	list = JSON.ObjectFromURL(NFLGAMEPASS_TEAMS, errors='ignore', cacheTime=1)
	
	for team in list['modules']['teamListAFC']['content']:
		teamTitle = str(team['fullName'])
		teamId = team['seoname']
		sThumb = teamTitle.replace(" ","-").lower()
		oc.add(DirectoryObject(key=Callback(GamepassTeamPlay, title=teamTitle, id=teamId, thumbs=sThumb), title=teamTitle, thumb=R("%s.png" % sThumb), summary=teamTitle))
	for team in list['modules']['teamListNFC']['content']:
		teamTitle = team['fullName']
		teamId = team['seoname']
		sThumb = teamTitle.replace(" ","-").lower()
		oc.add(DirectoryObject(key=Callback(GamepassTeamPlay, title=teamTitle, id=teamId, thumbs=sThumb), title=teamTitle, thumb=R("%s.png" % sThumb), summary=teamTitle))

	return oc
	
###################################################################################################

@route('/video/nflvideos/gamepassteamplay')
def GamepassTeamPlay(title, id, thumbs):

	oc = ObjectContainer(title2=title)
	
	list = JSON.ObjectFromURL(url="https://www.nflgamepass.com/api/en/content/v1/web/teams/"+id+"/videos", errors='ignore', cacheTime=1)

	try:
		for stream in list['modules']['gamesCurrentSeason']['content']:
			sTitle = stream['video']['title'] + " " + str(stream['season']) + " " + stream['weekName']
			videoId = stream['video']['videoId']
			sThumb = thumbs
			oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoId + "#NFLTEAMS", title=sTitle, summary=sTitle, thumb=R("%s.png" % sThumb)))
			try:
				sTitlecon = stream['condensedVideo']['title'] + " " + str(stream['season']) + " " + stream['weekName']
				videoIdcon = stream['condensedVideo']['videoId']
				oc.add(VideoClipObject(url="https://www.nflgamepass.com/api/en/content/v1/diva/" + videoIdcon + "#NFLTEAMS", title=sTitlecon, summary=sTitlecon, thumb=R("%s.png" % sThumb)))
			except:
				Log("No Condensed Game")	
	except:
		Log("No Games in list")
		
	return oc

###################################################################################################
# Notes about xpaths
# .// means any child/grandchild of the currently selected node, rather than anywhere in the document. Particularly important when dealing with loops.
# // = any child or grand-child ( you can use // so that you don't have to specify all the parents before it). Be careful to be specific enough to avoid confusion.
# / = direct child of the parent (for example of the entire page)