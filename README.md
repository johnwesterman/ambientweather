# AmbientWeather WS-1550-IP (version 4.5.8 firmware) HTML Scraping of Live Data HowTo Documentation

This repository holds code I've written to scrape the "Live Data" page data, put them in variables and allow you to uses these variables in your own code without using the API and ambientweater.net.

The output to this program looks like this:

{ "ambient1.ham.co" :  {"outHumi": "--", "RelPress": "30.09", "uvi": "--", "avgwind": "----", "rainofyearly": "0.04", "windir": "---", "eventrain": "0.02", "solarrad": "----.-", "inTemp": "75.6", "inHumi": "57", "rainofmonthly": "0.04", "rainofdaily": "0.00", "dailygust": "2.2", "rainofweekly": "0.00", "AbsPress": "29.59", "rainofhourly": "0.00", "uv": "---", "outTemp": "--.-", "outBattSta1": "- -", "CurrTime": "09:34 8/11/2019", "inBattSta": "Normal", "gustspeed": "----"} }

When you pretty up the JSON it'll look like this:

```text
{
	"ambient1.ham.co": {
		"outHumi": "--",
		"RelPress": "30.09",
		"uvi": "--",
		"avgwind": "----",
		"rainofyearly": "0.04",
		"windir": "---",
		"eventrain": "0.02",
		"solarrad": "----.-",
		"inTemp": "75.6",
		"inHumi": "57",
		"rainofmonthly": "0.04",
		"rainofdaily": "0.00",
		"dailygust": "2.2",
		"rainofweekly": "0.00",
		"AbsPress": "29.59",
		"rainofhourly": "0.00",
		"uv": "---",
		"outTemp": "--.-",
		"outBattSta1": "- -",
		"CurrTime": "09:34 8/11/2019",
		"inBattSta": "Normal",
		"gustspeed": "----"
	}
}
```

You can then use JSON to parse out the various fields you may want to interpret. I'm not interested in all the available fields so I parse out what I want with the Python code.

I do all of this becajuse one of my weather apps does not use the Internet so going to ambientweater.net is not an option for that application. This tool allows me to get updated weather data as often as I need without restriction.

I currently do not have any internet facing data to demo this so will add some screenshots when I can.

For the AmbientWeather API documentation go here:

https://github.com/ambient-weather/api-docs