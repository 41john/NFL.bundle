# -*- coding: utf-8 -*-
###################################################################################################
#
# NFL Videos for Plex (by 41john)
#
###################################################################################################

NFL_URL						= 'http://www.nfl.com'
NFL_URL1					= 'http://a.video.nfl.com/'
BASE_URL					= 'http://www.nfl.com/videos'
LATEST_VIDEOS				= 'http://www.nfl.com/videos/nfl-videos'
NFL_NETWORK_LIVE			= 'http://gamepass.nfl.com/nflgp/console.jsp?nfln=true#Live'
NFL_REDZONE_LIVE			= 'http://gamepass.nfl.com/nflgp/console.jsp?nfln=true#RedzoneLive'
GAMEPASS_SCHEDULE			= 'https://gamepass.nfl.com/nflgp/secure/schedulechange'
GAMEREWIND_SCHEDULE			= 'https://gamerewind.nfl.com/nflgr/secure/schedulechange'
GAMEPASS_SCHEDULE_WEEK		= 'https://gamepass.nfl.com/nflgp/secure/schedule'
GAMEREWIND_SCHEDULE_WEEK	= 'https://gamerewind.nfl.com/nflgr/secure/schedule'
NFL_VIDEOS_JSON				= 'http://www.nfl.com/static/embeddablevideo/%s.json'
NFL_NETWORK_SCHEDULE		= 'http://www.locatetv.com/listings/nflnet'
NFLNAIMAGE 					= 'http://smb.cdn.neulion.com/u/nfl/nfl/thumbs/'

TEAMS = {'arizona-cardinals': 'Arizona Cardinals', 'atlanta-falcons': 'Atlanta Falcons', 'baltimore-ravens': 'Baltimore Ravens', 'buffalo-bills': 'Buffalo Bills', 'carolina-panthers': 'Carolina Panthers', 'chicago-bears': 'Chicago Bears', 'cincinnati-bengals': 'Cincinnati Bengals', 'cleveland-browns': 'Cleveland Browns', 'dallas-cowboys': 'Dallas Cowboys', 'denver-broncos': 'Denver Broncos', 'detroit-lions': 'Detroit Lions', 'green-bay-packers': 'Green Bay Packers', 'houston-texans': 'Houston Texans', 'indianapolis-colts': 'Indianapolis Colts', 'jacksonville-jaguars': 'Jacksonville Jaguars', 'kansas-city-chiefs': 'Kansas City Chiefs', 'miami-dolphins': 'Miami Dolphins', 'minnesota-vikings': 'Minnesota Vikings', 'new-england-patriots': 'New England Patriots', 'new-orleans-saints': 'New Orleans Saints', 'new-york-giants': 'New York Giants', 'new-york-jets': 'New York Jets', 'oakland-raiders': 'Oakland Raiders', 'philadelphia-eagles': 'Philadelphia Eagles', 'pittsburgh-steelers': 'Pittsburgh Steelers', 'san-diego-chargers': 'San Diego Chargers', 'san-francisco-49ers': 'San Francisco 49ers', 'seattle-seahawks': 'Seattle Seahawks', 'st-louis-rams': 'St. Louis Rams', 'tampa-bay-buccaneers': 'Tampa Bay Buccaneers', 'tennessee-titans': 'Tennessee Titans', 'washington-redskins': 'Washington Redskins'}
ORDERED_TEAMS = ['arizona-cardinals','atlanta-falcons','baltimore-ravens','buffalo-bills','carolina-panthers','chicago-bears','cincinnati-bengals','cleveland-browns','dallas-cowboys','denver-broncos','detroit-lions','green-bay-packers','houston-texans','indianapolis-colts','jacksonville-jaguars','kansas-city-chiefs','miami-dolphins','minnesota-vikings','new-england-patriots','new-orleans-saints','new-york-giants','new-york-jets','oakland-raiders','philadelphia-eagles','pittsburgh-steelers','san-diego-chargers','san-francisco-49ers','seattle-seahawks','st-louis-rams','tampa-bay-buccaneers','tennessee-titans','washington-redskins']

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

	HTTP.Headers['User-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:22.0) Gecko/20100101 Firefox/22.0'

###################################################################################################

@handler('/video/nflvideos', NAME, thumb=ICON, art=ART)
def VideoMainMenu():
	
	oc = ObjectContainer()
		
	oc.add(DirectoryObject(key = Callback(NFLVideosMenu), title="NFL.com Videos", summary="Browse videos from NFL.com/Videos"))
	oc.add(DirectoryObject(key = Callback(PlayMenu, url="%s/%s" % (BASE_URL, Prefs['team'])), title="My Team", summary="Set your favourite team in Preferences and browse videos for that team here", thumb=R("%s.png" % Prefs['team'])))
	oc.add(DirectoryObject(key = Callback(GamepassMenu), title="NFL GamePass", summary="NFL GamePass subscribers only", thumb=R("gamepass.png")))
	oc.add(DirectoryObject(key = Callback(GamerewindMenu), title="NFL Game Rewind", summary="NFL Game Rewind subscribers only", thumb=R("gamerewind.png")))
	oc.add(PrefsObject(title="Preferences", summary="Set My Team. Enter subscription details for Gamepass or NFL Network Live", thumb=R("icon-prefs.png")))
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
		oc.add(DirectoryObject(key=Callback(PlayMenu, url="%s/%s" % (BASE_URL, category)), title=SHOWS[category], thumb=R("%s.png" % category)))

	return oc

###################################################################################################

@route('/video/nflvideos/teams')
def TeamsMenu():

	oc = ObjectContainer(title2="Teams")

	for category in ORDERED_TEAMS:
		oc.add(DirectoryObject(key=Callback(PlayMenu, url="%s/%s" % (BASE_URL, category)), title=TEAMS[category], thumb=R("%s.png" % category)))

	return oc

###################################################################################################

@route('/video/nflvideos/spotlight')
def SpotlightMenu():

	oc = ObjectContainer(title2="Channels")

	for category in ORDERED_SPOTLIGHT:
		oc.add(DirectoryObject(key=Callback(PlayMenu, url="%s/%s" % (BASE_URL, category)), title=SPOTLIGHT[category], thumb=R("%s.png" % category)))

	return oc

###################################################################################################

@route('/video/nflvideos/events')
def EventsMenu():

	oc = ObjectContainer(title2="Events")

	for category in ORDERED_EVENTS:
		oc.add(DirectoryObject(key=Callback(PlayMenu, url="%s/%s" % (BASE_URL, category)), title=EVENTS[category], thumb=R("%s.png" % category)))

	return oc

###################################################################################################

@route('/video/nflvideos/playmenu')
def PlayMenu(url=None):

	oc = ObjectContainer(title2="NFL.com/Videos")
	list = HTML.ElementFromURL(url, errors='ignore', cacheTime=1).xpath('//div[@class="coverage-wrapper"]/div[@class="yui3-video-coverage-item "]')

	for stream in list:
		try:
			streamid = stream.xpath('./@data-contentid')[0]
			json = JSON.ObjectFromURL(NFL_VIDEOS_JSON % streamid)
			sTitle = json['briefHeadline']
			sSummary = json['caption']
			sThumb = json['imagePaths']['m']
			sStreamURL = NFL_URL1 + json['cdnData']['bitrateInfo'][-5]['path'] + "#" + streamid	
			oc.add(VideoClipObject(url=sStreamURL, title=sTitle, summary=sSummary, thumb=sThumb))
		except:
			Log("Error obtaining URLs, ignoring Video")

	return oc

###################################################################################################	

@route('/video/nflvideos/gamepass')
def GamepassMenu():

	oc = ObjectContainer(title2="NFL Game Pass")
	
	oc.add(DirectoryObject(key=Callback(GamepassPlayweek), title="Live Games", thumb=R("gamepass-live.png"), summary="This week's Live Games"))
	oc.add(DirectoryObject(key=Callback(GamepassSeason), title="Archived Games", thumb=R("gamepass.png"), summary="Archived games from this season back to 2012"))
	oc.add(DirectoryObject(key=Callback(NflNetworkMenu), title="NFL Network Live", summary="Watch NFL Network Live", thumb=R("nfl-network-live.png")))
	oc.add(DirectoryObject(key=Callback(NflNetworkArchiveMenu), title="NFL Network Archive", summary="Watch NFL Network Archived Shows", thumb=R("nfl-network.png")))
	oc.add(DirectoryObject(key=Callback(NflRedzoneMenu), title="NFL Redzone Live", summary="Watch NFL Redzone Live", thumb=R("redzone-logo-live.png")))
	oc.add(DirectoryObject(key=Callback(NflRedzoneArchive), title="NFL Redzone Archive", thumb=R("redzone-logo.png"), summary="Archived Redzone channel from this season back to 2012"))
	
	return oc

###################################################################################################

@route('/video/nflvideos/gamepassseason')
def GamepassSeason():

	oc = ObjectContainer(title2="NFL Game Pass")

	year = Datetime.Now().year if Datetime.Now().month < 7 else Datetime.Now().year+1

	for season in reversed(range(2012, year)):
		oc.add(DirectoryObject(key = Callback(GamepassWeek, season=str(season)), title=str(season), thumb=R("gamepass.png")))

	return oc

####################################################################################################

@route('/video/nflvideos/gamepassweek')
def GamepassWeek(season):

	oc = ObjectContainer(title2="NFL Game Pass")
	
	weeks = {'100': 'Hall Of Fame', '101': 'Preseason 1','102': 'Preseason 2','103': 'Preseason 3','104': 'Preseason 4', '201': 'Week 1', '202': 'Week 2', '203': 'Week 3', '204': 'Week 4', '205': 'Week 5', '206': 'Week 6', '207': 'Week 7', '208': 'Week 8', '209': 'Week 9', '210': 'Week 10', '211': 'Week 11', '212': 'Week 12', '213': 'Week 13', '214': 'Week 14', '215': 'Week 15', '216': 'Week 16', '217': 'Week 17', '218': 'Wild Card Round', '219': 'Divisional Round', '220': 'Championship Round', '221': 'Pro Bowl', '222': 'Super Bowl'}
	orderedWeeks = ['100', '101','102','103','104', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222']
	currentSeason = Datetime.Now().year -1 if Datetime.Now().month < 3 else Datetime.Now().year
	
	if str(currentSeason) == season:
		page = HTML.ElementFromURL(GAMEPASS_SCHEDULE_WEEK, errors='ignore', cacheTime=1)
		currentWeek = page.xpath("//select[@id = 'weekSelect']/option[@selected = 'true']")[0].get("value")
		oc.add(DirectoryObject(key = Callback(GamepassPlay, week=currentWeek, season=season, week_title=weeks[currentWeek]), title = "Current Week", thumb=R("gamepass.png")))
		
		try:
			if currentWeek[-1:] != "1":
				lastWeek = str(int(currentWeek) - 1)
				oc.add(DirectoryObject(key = Callback(GamepassPlay, week=lastWeek, season=season, week_title=weeks[lastWeek]), title = "Last Week", thumb=R("gamepass.png")))
		except:
			Log("Last weeks games not available")
		
	for week in orderedWeeks:
		week_title = weeks[week]	
		oc.add(DirectoryObject(key = Callback(GamepassPlay, week=week, season=season, week_title=week_title), title = week_title, thumb=R("gamepass.png")))
	
	return oc
	
###################################################################################################

@route('/video/nflvideos/gamepassplay')	
def GamepassPlay(week, season, week_title):

	oc = ObjectContainer(title2=week_title)
	
	list = HTML.ElementFromURL(GAMEPASS_SCHEDULE, errors='ignore', values={'week':week, 'season':season}, cacheTime=1)

	for stream in list.xpath('//td[@class="gameTile"]/*/parent::td'):
		sTeam1 = stream.xpath('./table/tr[2]/td[2]/text()')[0]
		sTeam2 = stream.xpath('./table/tr[3]/td[2]/text()')[0]
		sTitle = "%s @ %s" % (sTeam1,sTeam2)
		sStreamURL = stream.xpath('./table/tr[3]/td[3]/a')[0].get('href')
		sStreamURL = sStreamURL.replace("javascript:launchApp('","http://gamepass.nfl.com/nflgp/console.jsp?eid=").replace("')","")
		oc.add(VideoClipObject(url=sStreamURL + "#Condensed", title=sTitle + " - Condensed Game",  thumb=R("icon-gamepass.png")))
		oc.add(VideoClipObject(url=sStreamURL, title=sTitle + " - Full Length Game",  thumb=R("icon-gamepass.png")))
	return oc

###################################################################################################

@route('/video/nflvideos/gamepassplayweek')	
def GamepassPlayweek():

	oc = ObjectContainer(title2="NFL Game Pass")

	list = HTML.ElementFromURL(GAMEPASS_SCHEDULE, errors='ignore', cacheTime=1)

	for stream in list.xpath('//td[@class="gameTile"]/*/parent::td'):
		sTeam1 = stream.xpath('./table/tr[2]/td[2]/text()')[0]
		sTeam2 = stream.xpath('./table/tr[3]/td[2]/text()')[0]
		sTitle = "%s @ %s" % (sTeam1,sTeam2)
		try:
			sSummary = stream.xpath('./table/tr[2]/td[3]/span/text()')[0].strip()
		except:
			sSummary = "Game Has Finished"
		sStreamURL = stream.xpath('./table/tr[3]/td[3]/a')[0].get('href')
		sStreamURL = sStreamURL.replace("javascript:launchApp('","http://gamepass.nfl.com/nflgp/console.jsp?eid=").replace("')","")
		oc.add(VideoClipObject(url=sStreamURL + "#Live", title=sTitle, summary = sSummary, thumb=R("icon-gamepass-live.png")))

	return oc

###################################################################################################

@route('/video/nflvideos/nflnetwork')	
def NflNetworkMenu():

	oc = ObjectContainer(title2="NFL Network")
	
	page = HTML.ElementFromURL(NFL_NETWORK_SCHEDULE, errors='ignore', cacheTime=1)
	try:
		onnow = page.xpath('//ul[@class="nextOn clearFix"]/li[2]/div/a/text()')[0]
		timestarted = page.xpath('//ul[@class="nextOn clearFix"]/li[1]/text()')[0]
	except:
		onnow = ""
		timestarted = ""
		
	try:
		nextstarted = page.xpath('//ul[@class="schedule hoverable"]/li[3]/ul/li[1]/text()')[0]
		onnext = page.xpath('//ul[@class="schedule hoverable"]/li[3]/ul/li[2]/div/a/text()')[0]
	except:
		nextstarted = ""
		onnext = ""

	oc.add(VideoClipObject(url=NFL_NETWORK_LIVE, title="NFL Network Live", summary = "Started at " + timestarted + " " + onnow + "\n Next at " + nextstarted +" " + onnext, thumb=R("icon-nfl-network-live.png")))

	return oc

###################################################################################################	

@route('/video/nflvideos/nflredzone')	
def NflRedzoneMenu():

	oc = ObjectContainer(title2="NFL Redzone")

	oc.add(VideoClipObject(url=NFL_REDZONE_LIVE, title="NFL Redzone Live", summary="Watch NFL Redzone Live", thumb=R("icon-nfl-redzone-live.png")))

	return oc

###################################################################################################

@route('/video/nflvideos/nflredzonearchive')
def NflRedzoneArchive():

	oc = ObjectContainer(title2="NFL Redzone Archive")

	year = Datetime.Now().year if Datetime.Now().month < 8 else Datetime.Now().year+1

	for season in reversed(range(2012, year)):
		oc.add(DirectoryObject(key = Callback(NflRedzoneArchiveWeek, season=str(season)), title=str(season), thumb=R("redzone-logo.png")))

	return oc

###################################################################################################	

@route('/video/nflvideos/nflredzonearchiveweek')
def NflRedzoneArchiveWeek(season):

	oc = ObjectContainer(title2="NFL Redzone Archive")
	
	if season == "2012":	
		weeks = {'2012/09/09': '2012 Week 1', '2012/09/16': '2012 Week 2','2012/09/23': '2012 Week 3','2012/09/30': '2012 Week 4','2012/10/07': '2012 Week 5', '2012/10/14': '2012 Week 6', '2012/10/21': '2012 Week 7', '2012/10/28': '2012 Week 8', '2012/11/04': '2012 Week 9', '2012/11/11': '2012 Week 10', '2012/11/18': '2012 Week 11', '2012/11/25': '2012 Week 12', '2012/12/02': '2012 Week 13', '2012/12/09': '2012 Week 14', '2012/12/16': '2012 Week 15', '2012/12/23': '2012 Week 16', '2012/12/30': '2012 Week 17'}
		orderedWeeks = ['2012/09/09', '2012/09/16','2012/09/23','2012/09/30','2012/10/07', '2012/10/14', '2012/10/21', '2012/10/28', '2012/11/04', '2012/11/11', '2012/11/18', '2012/11/25', '2012/12/02', '2012/12/09', '2012/12/16', '2012/12/23', '2012/12/30']
	if season == "2013":
		weeks = {'2013/09/08': '2013 Week 1', '2013/09/15': '2013 Week 2','2013/09/22': '2013 Week 3','2013/09/29': '2013 Week 4','2013/10/06': '2013 Week 5', '2013/10/13': '2013 Week 6', '2013/10/20': '2013 Week 7', '2013/10/27': '2013 Week 8', '2013/11/03': '2013 Week 9', '2013/11/10': '2013 Week 10', '2013/11/17': '2013 Week 11', '2013/11/24': '2013 Week 12', '2013/12/01': '2013 Week 13', '2013/12/08': '2013 Week 14', '2013/12/15': '2013 Week 15', '2013/12/22': '2013 Week 16', '2013/12/29': '2013 Week 17'}
		orderedWeeks = ['2013/09/08', '2013/09/15','2013/09/22','2013/09/29','2013/10/06', '2013/10/13', '2013/10/20', '2013/10/27', '2013/11/03', '2013/11/10', '2013/11/17', '2013/11/24', '2013/12/01', '2013/12/08', '2013/12/15', '2013/12/22', '2013/12/29']
	
	for week in orderedWeeks:
		week_title = weeks[week]
		oc.add(VideoClipObject(url="http://gamepass.nfl.com/nflgp/console.jsp?rza=" + week, title=week_title, thumb=R("icon-nfl-redzone.png")))
		
	return oc
	
###################################################################################################el

@route('/video/nflvideos/nflnarchiveplay')	
def NFLNArchivePlay(cid, title):

	oc = ObjectContainer(title2=title)
		
	username = Prefs['username']
	password = Prefs['password']
	
	# seems to log in each time you go back to the gamepass menu. Will fix in later update
	
	login_url = "https://gamepass.nfl.com/nflgp/secure/schedule"
	
	authentication_url = "https://id.s.nfl.com/login"
	post_values = {
		'username' : username,
		'password' : password,
		'vendor_id' : 'nflptnrnln',
		'success_url' : 'https://network.nfl.com/nfln/secure/login?redirect=schedule',
		'error_url' : 'https://network.nfl.com/nfln/secure/login?redirect=schedule'
		}

	login = HTTP.Request(url=authentication_url, values=post_values, cacheTime=0).content
	
	cookie_values = HTTP.CookiesForURL(login_url)
	
	headers_value = {'Cookie' : cookie_values}

	program_url = "http://gamepass.nfl.com/nflgp/servlets/browse"
	post_values1 = {
	'cid' : cid,
	'ps' : '50',
	'pm' : '0',
	'pn' : '1',
	'isFlex' : 'true'
	}
	program_pagedata = HTTP.Request(url=program_url, values=post_values1, headers=headers_value).content
	program_page = XML.ElementFromString(program_pagedata).xpath('//programs/program')

	for stream in program_page:
		sTitle = stream.xpath('.//name')[0].text
		sThumb = NFLNAIMAGE + stream.xpath('.//image')[0].text
		sStreamURL = stream.xpath('.//publishPoint')[0].text
		sStreamURL = sStreamURL.replace("adaptive","http").replace(":443","")
		if sTitle == "NFL TOTAL ACCESS: (08/07/2014)":
			sStreamURL="http://nlds84.neulion.com/nlds_vod/nfl/vod/2014/08/07/140807/2_140807_t1_nfltv_2013_h_quickpick1_1_pc.mp4"
		sSummary = stream.xpath('.//runtime')[0].text + " Minutes"
		Log(sStreamURL)
		Log(sTitle)
		oc.add(VideoClipObject(url=sStreamURL+"#"+sTitle, title=sTitle, summary=sSummary, thumb=sThumb))
		
	return oc	
	
###################################################################################################

@route('/video/nflvideos/gamerewind')
def GamerewindMenu():

	oc = ObjectContainer(title2="NFL Game Rewind")
	
	oc.add(DirectoryObject(key=Callback(GamerewindSeason), title="Archive", thumb=R("gamerewind.png"), summary="Archived games from this season back to 2012"))
	
	return oc

###################################################################################################

@route('/video/nflvideos/gamerewindseason')
def GamerewindSeason():

	oc = ObjectContainer(title2="NFL Game Rewind")

	year = Datetime.Now().year if Datetime.Now().month < 7 else Datetime.Now().year+1

	for season in reversed(range(2012, year)):
		oc.add(DirectoryObject(key = Callback(GamerewindWeek, season=str(season)), title=str(season), thumb=R("gamerewind.png")))

	return oc

####################################################################################################

@route('/video/nflvideos/gamerewindweek')
def GamerewindWeek(season):

	oc = ObjectContainer(title2="NFL Game Rewind")
	
	weeks = {'201': 'Week 1', '202': 'Week 2', '203': 'Week 3', '204': 'Week 4', '205': 'Week 5', '206': 'Week 6', '207': 'Week 7', '208': 'Week 8', '209': 'Week 9', '210': 'Week 10', '211': 'Week 11', '212': 'Week 12', '213': 'Week 13', '214': 'Week 14', '215': 'Week 15', '216': 'Week 16', '217': 'Week 17', '218': 'Wild Card Round', '219': 'Divisional Round', '220': 'Championship Round', '221': 'Pro Bowl', '222': 'Super Bowl'}
	orderedWeeks = ['201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222']
	currentSeason = Datetime.Now().year -1 if Datetime.Now().month < 3 else Datetime.Now().year

	if str(currentSeason) == season:
		page = HTML.ElementFromURL(GAMEREWIND_SCHEDULE_WEEK, errors='ignore', cacheTime=1)
		currentWeek = page.xpath("//select[@id = 'weekSelect']/option[@selected = 'true']")[0].get("value")
		oc.add(DirectoryObject(key = Callback(GamerewindPlay, week=currentWeek, season=season, week_title=weeks[currentWeek]), title = "Current Week", thumb=R("gamerewind.png")))
	
		try:
			if currentWeek[-1:] != "1":
				lastWeek = str(int(currentWeek) - 1)
				oc.add(DirectoryObject(key = Callback(GamerewindPlay, week=lastWeek, season=season, week_title=weeks[lastWeek]), title = "Last Week", thumb=R("gamerewind.png")))
		except:
			Log("Last weeks games not available")

	for week in orderedWeeks:
		week_title = weeks[week]
		oc.add(DirectoryObject(key = Callback(GamerewindPlay, week=week, season=season, week_title=week_title), title = week_title, thumb=R("gamerewind.png")))
	
	return oc
	
###################################################################################################

@route('/video/nflvideos/gamerewindplay')	
def GamerewindPlay(week, season, week_title):

	oc = ObjectContainer(title2=week_title)
	
	list = HTML.ElementFromURL(GAMEREWIND_SCHEDULE, errors='ignore', values={'week':week, 'season':season}, cacheTime=1)

	for stream in list.xpath('//td[@class="gameTile"]/*/parent::td'):
		sTeam1 = stream.xpath('./table/tr[2]/td[2]/text()')[0]
		sTeam2 = stream.xpath('./table/tr[3]/td[2]/text()')[0]
		sTitle = "%s @ %s" % (sTeam1,sTeam2)
		try:
			sStreamURL = stream.xpath('./table/tr[3]/td[3]/a')[0].get('href')
			sStreamURL = sStreamURL.replace("javascript:launchApp('","http://gamerewind.nfl.com/nflgr/console.jsp?eid=").replace("')","")
		except:
			sStreamURL = "http://gamerewind.nfl.com/nflgr/console.jsp?eid=blahblah"
		oc.add(VideoClipObject(url=sStreamURL + "#Condensed", title=sTitle + " - Condensed Game",  thumb=R("icon-gamerewind.png")))
		oc.add(VideoClipObject(url=sStreamURL, title=sTitle + " - Full Length Game",  thumb=R("icon-gamerewind.png")))
	return oc
	
###################################################################################################	

@route('/video/nflvideos/nflnetworkarchivemenu')
def NflNetworkArchiveMenu():

	oc = ObjectContainer(title2="NFL Network Archive")

	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="214", title="Total Access 2014"), title="Total Access 2014", thumb=R("nfl-network.png"), summary="Total Access 2014"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="212", title="NFL Gameday 2014"), title="NFL Gameday 2014", thumb=R("nfl-network.png"), summary="NFL Gameday 2014"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="220", title="Hard Knocks 2014"), title="Hard Knocks 2014", thumb=R("nfl-network.png"), summary="Hard Knocks 2014"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="218", title="A Football Life 2014"), title="A Football Life 2014", thumb=R("nfl-network.png"), summary="A Football Life 2014"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="222", title="Hall of Fame 2014"), title="Hall of Fame 2014", thumb=R("nfl-network.png"), summary="Hall of Fame 2014"))	
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="219", title="NFL Films Presents 2014"), title="NFL Films Presents 2014", thumb=R("nfl-network.png"), summary="NFL Films Presents 2014"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="213", title="Playbook 2014"), title="Playbook 2014", thumb=R("nfl-network.png"), summary="Playbook 2014"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="215", title="Sound FX 2014"), title="Sound FX 2014", thumb=R("nfl-network.png"), summary="Sound FX 2014"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="217", title="Top 100 Players of 2014"), title="Top 100 Players of 2014", thumb=R("nfl-network.png"), summary="Top 100 Players of 2014"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="181", title="Total Access 2013"), title="Total Access 2013", thumb=R("nfl-network.png"), summary="Total Access 2013"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="186", title="A Football Life 2013"), title="A Football Life 2013", thumb=R("nfl-network.png"), summary="A Football Life 2013"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="187", title="NFL Films Presents 2013"), title="NFL Films Presents 2013", thumb=R("nfl-network.png"), summary="NFL Films Presents 2013"))	
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="179", title="NFL Gameday 2013"), title="NFL Gameday 2013", thumb=R("nfl-network.png"), summary="NFL Gameday 2013"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="180", title="Playbook 2013"), title="Playbook 2013", thumb=R("nfl-network.png"), summary="Playbook 2013"))
	oc.add(DirectoryObject(key=Callback(NFLNArchivePlay, cid="183", title="Sound FX 2013"), title="Sound FX 2013", thumb=R("nfl-network.png"), summary="Sound FX 2013"))
	
	return oc
	
###################################################################################################
# Notes about xpaths
# .// means any child/grandchild of the currently selected node, rather than anywhere in the document. Particularly important when dealing with loops.
# // = any child or grand-child ( you can use // so that you don't have to specify all the parents before it). Be careful to be specific enough to avoid confusion.
# / = direct child of the parent (for example of the entire page)