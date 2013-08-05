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
GAMEHIGHLIGHTS_URL			= 'http://www.nfl.com/videos/nfl-game-highlights'
NFL_NETWORK_LIVE			= 'http://gamepass.nfl.com/nflgp/console.jsp?nfln=true'
GAMEPASS_SCHEDULE			= 'https://gamepass.nfl.com/nflgp/secure/schedulechange'
NFL_VIDEOS_JSON				= 'http://www.nfl.com/static/embeddablevideo/%s.json'

TEAMS = {'arizona-cardinals': 'Arizona Cardinals', 'atlanta-falcons': 'Atlanta Falcons', 'baltimore-ravens': 'Baltimore Ravens', 'buffalo-bills': 'Buffalo Bills', 'carolina-panthers': 'Carolina Panthers', 'chicago-bears': 'Chicago Bears', 'cincinnati-bengals': 'Cincinnati Bengals', 'cleveland-browns': 'Cleveland Browns', 'dallas-cowboys': 'Dallas Cowboys', 'denver-broncos': 'Denver Broncos', 'detroit-lions': 'Detroit Lions', 'green-bay-packers': 'Green Bay Packers', 'houston-texans': 'Houston Texans', 'indianapolis-colts': 'Indianapolis Colts', 'jacksonville-jaguars': 'Jacksonville Jaguars', 'kansas-city-chiefs': 'Kansas City Chiefs', 'miami-dolphins': 'Miami Dolphins', 'minnesota-vikings': 'Minnesota Vikings', 'new-england-patriots': 'New England Patriots', 'new-orleans-saints': 'New Orleans Saints', 'new-york-giants': 'New York Giants', 'new-york-jets': 'New York Jets', 'oakland-raiders': 'Oakland Raiders', 'philadelphia-eagles': 'Philadelphia Eagles', 'pittsburgh-steelers': 'Pittsburgh Steelers', 'san-diego-chargers': 'San Diego Chargers', 'san-francisco-49ers': 'San Francisco 49ers', 'seattle-seahawks': 'Seattle Seahawks', 'st-louis-rams': 'St. Louis Rams', 'tampa-bay-buccaneers': 'Tampa Bay Buccaneers', 'tennessee-titans': 'Tennessee Titans', 'washington-redskins': 'Washington Redskins'}
ORDERED_TEAMS = ['arizona-cardinals','atlanta-falcons','baltimore-ravens','buffalo-bills','carolina-panthers','chicago-bears','cincinnati-bengals','cleveland-browns','dallas-cowboys','denver-broncos','detroit-lions','green-bay-packers','houston-texans','indianapolis-colts','jacksonville-jaguars','kansas-city-chiefs','miami-dolphins','minnesota-vikings','new-england-patriots','new-orleans-saints','new-york-giants','new-york-jets','oakland-raiders','philadelphia-eagles','pittsburgh-steelers','san-diego-chargers','san-francisco-49ers','seattle-seahawks','st-louis-rams','tampa-bay-buccaneers','tennessee-titans','washington-redskins']

SHOWS = {'nfl-am': 'NFL AM', 'nfl-network-total-access': 'NFL Total Access', 'nfl-network-gameday': 'NFL GameDay', 'nfl-network-playbook': 'Playbook', 'nfl-films-sound-efx': 'Sound FX', 'nfl-top100-2013': 'Top 100 Players of 2013', 'nfl-network-path-to-the-draft': 'Path to the Draft', 'nfl-network-around-the-league': 'Around the League', 'nfl-fantasy': 'Fantasy', 'nfl-fantasy-team-by-team': 'Fantasy Team Previews', 'nfl-network-the-coaches': 'The Coaches', 'nfl-films-game-of-the-week': 'Game of the Week', 'nfl-films-americas-game': 'Americas Game', 'nfl-films-presents': 'NFL Films Presents', 'nfl-films-anatomy-of-a-play': 'Anatomy of a Play', 'nfl-network-hard-knocks': 'Hard Knocks', 'nfl-redzone-videos': 'NFL Redzone Top 5 Plays', 'a-football-life': 'A Football Life', 'nfl-network-top-ten': 'NFL Top Ten Plays'}
ORDERED_SHOWS = ['nfl-am', 'nfl-network-total-access', 'nfl-network-gameday', 'nfl-network-playbook', 'nfl-films-sound-efx', 'nfl-top100-2013', 'nfl-network-path-to-the-draft', 'nfl-network-around-the-league', 'nfl-fantasy', 'nfl-fantasy-team-by-team', 'nfl-network-the-coaches', 'nfl-films-game-of-the-week', 'nfl-films-americas-game', 'nfl-films-presents', 'nfl-films-anatomy-of-a-play', 'nfl-network-hard-knocks', 'nfl-redzone-videos', 'a-football-life', 'nfl-network-top-ten']

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
	
	oc.add(DirectoryObject(key = Callback(PlayMenu, url=LATEST_VIDEOS), title="Latest Videos", summary="Browse the latest videos"))
	oc.add(DirectoryObject(key = Callback(PlayMenu, url=GAMEHIGHLIGHTS_URL), title="Game Highlights", summary="Browse game highlights"))
	oc.add(DirectoryObject(key = Callback(ShowsMenu), title="Shows", summary="Browse videos for different NFL shows"))
	oc.add(DirectoryObject(key = Callback(TeamsMenu), title="Teams", summary="Browse videos by team"))
	oc.add(DirectoryObject(key = Callback(PlayMenu, url="%s/%s" % (BASE_URL, Prefs['team'])), title="My Team", summary="Set your favourite team in Preferences and browse videos for that team here", thumb=R("%s.png" % Prefs['team'])))
	oc.add(DirectoryObject(key = Callback(SpotlightMenu), title="Channels", summary="Browse videos for different NFL channels"))
	oc.add(DirectoryObject(key = Callback(EventsMenu), title="Events", summary="Browse videos by Event"))
	oc.add(PrefsObject(title="Preferences", summary="Set My Team. Enter subscription details for Gamepass or NFL Network Live", thumb=R("icon-prefs.png")))
	oc.add(DirectoryObject(key = Callback(NflNetworkMenu), title="NFL Network Live", summary="Watch NFL Network Live", thumb=R("nfl-network-live.png")))
	oc.add(DirectoryObject(key = Callback(GamepassMenu), title="NFL GamePass", summary="NFL GamePass subscribers only", thumb=R("gamepass.png")))
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

	oc = ObjectContainer(title2="NFL Network")
	list = HTML.ElementFromURL(url, errors='ignore', cacheTime=1).xpath('//div[@id="videos-list"]/ul[@class="list-items"]/li')

	for stream in list:
		sTitle = stream.xpath('.//div[@class="content"]//a')[0].text
		sSummary = stream.xpath('.//p[last()]')[0].text
		sThumb = stream.xpath('.//div[@class="thumbnail"]//a/img')[0].get('src')
		sThumb = sThumb.replace("thumbnail_80_60.jpg","rhr_210.jpg")
		sStreamURL = NFL_URL + stream.xpath('.//div[@class="content"]//a')[0].get('href')
		oc.add(VideoClipObject(url=sStreamURL, title=sTitle, summary=sSummary, thumb=sThumb))

	return oc

###################################################################################################	

@route('/video/nflvideos/gamepass')
def GamepassMenu():

	oc = ObjectContainer(title2="NFL Game Pass")
	
	oc.add(DirectoryObject(key=Callback(GamepassSeason), title="Archive", thumb=R("gamepass.png"), summary="Archived games from this season back to 2012"))
	oc.add(DirectoryObject(key=Callback(GamepassPlayweek), title="Live / This week", thumb=R("gamepass-live.png"), summary="This weeks games, Live!"))
	
	return oc

###################################################################################################

@route('/video/nflvideos/gamepassseason')
def GamepassSeason():

	oc = ObjectContainer(title2="NFL Game Pass")

	year = Datetime.Now().year if Datetime.Now().month < 8 else Datetime.Now().year+1

	for season in range(2012, year):
		oc.add(DirectoryObject(key = Callback(GamepassWeek, season=str(season)), title=str(season), thumb=R("gamepass.png")))

	return oc

####################################################################################################

@route('/video/nflvideos/gamepassweek')
def GamepassWeek(season):

	oc = ObjectContainer(title2="NFL Game Pass")
	
	weeks = {'100': 'Hall Of Fame', '101': 'Preseason 1','102': 'Preseason 2','103': 'Preseason 3','104': 'Preseason 4', '201': 'Week 1', '202': 'Week 2', '203': 'Week 3', '204': 'Week 4', '205': 'Week 5', '206': 'Week 6', '207': 'Week 7', '208': 'Week 8', '209': 'Week 9', '210': 'Week 10', '211': 'Week 11', '212': 'Week 12', '213': 'Week 13', '214': 'Week 14', '215': 'Week 15', '216': 'Week 16', '217': 'Week 17', '218': 'Wild Card Round', '219': 'Divisional Round', '220': 'Championship Round', '221': 'Pro Bowl', '222': 'Super Bowl'}
	orderedWeeks = ['100', '101','102','103','104', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222']
    
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
		sTeam1 = stream.xpath('./table/tr[1]/td[2]/text()')[0]
		sTeam2 = stream.xpath('./table/tr[2]/td[2]/text()')[0]
		sTitle = "%s @ %s" % (sTeam1,sTeam2)
		sStreamURL = stream.xpath('./table/tr[2]/td[3]/a')[0].get('href')
		sStreamURL = sStreamURL.replace("javascript:launchApp('","http://gamepass.nfl.com/nflgp/console.jsp?eid=").replace("')","")
		oc.add(VideoClipObject(url=sStreamURL + "#Condensed", title="Condensed Game - " + sTitle,  thumb=R("icon-gamepass.png")))
		oc.add(VideoClipObject(url=sStreamURL, title="Full Length Game - " + sTitle,  thumb=R("icon-gamepass.png")))
	return oc

###################################################################################################

@route('/video/nflvideos/gamepassplayweek')	
def GamepassPlayweek():

	oc = ObjectContainer(title2="NFL Game Pass")

	list = HTML.ElementFromURL(GAMEPASS_SCHEDULE, errors='ignore', cacheTime=1)

	for stream in list.xpath('//td[@class="gameTile"]/*/parent::td'):
		sTeam1 = stream.xpath('./table/tr[1]/td[2]/text()')[0]
		sTeam2 = stream.xpath('./table/tr[2]/td[2]/text()')[0]
		sTitle = "%s @ %s" % (sTeam1,sTeam2)
		sSummary = stream.xpath('./table/tr[1]/td[3]/span/text()')[0].strip()
		sStreamURL = stream.xpath('./table/tr[2]/td[3]/a')[0].get('href')
		sStreamURL = sStreamURL.replace("javascript:launchApp('","http://gamepass.nfl.com/nflgp/console.jsp?eid=").replace("')","")
		oc.add(VideoClipObject(url=sStreamURL + "#Live", title=sTitle, summary = sSummary, thumb=R("icon-gamepass-live.png")))

	return oc

###################################################################################################

@route('/video/nflvideos/nflnetwork')	
def NflNetworkMenu():

	oc = ObjectContainer(title2="NFL Network")

	oc.add(VideoClipObject(url=NFL_NETWORK_LIVE, title="NFL Network Live", summary="Watch NFL Network Live", thumb=R("icon-nfl-network-live.png")))

	return oc

###################################################################################################
# Notes about xpaths
# .// means any child/grandchild of the currently selected node, rather than anywhere in the document. Particularly important when dealing with loops.
# // = any child or grand-child ( you can use // so that you don't have to specify all the parents before it). Be careful to be specific enough to avoid confusion.
# / = direct child of the parent (for example of the entire page)