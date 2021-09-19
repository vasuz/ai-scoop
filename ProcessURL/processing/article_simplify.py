import json
import requests

url = "http://rewordify.com/rwprocess.php"

content = 'SAN FRANCISCO (AP) — The mayor of San Francisco was spotted dancing and singing along to live music without a mask at an indoor nightclub, despite a strict order by her public health department that requires wearing masks at indoor establishments unless someone is actively eating or drinking.Mayor London Breed, a Democrat, has promoted restrictive measures aimed at curbing the coronavirus, frustrating business owners who have had to shut down or limit customers.The San Francisco Chronicle reported the mayor was at the Black Cat nightclub Wednesday for an impromptu late night performance by two of the original three members of popular R&B act Tony! Toni! Toné!“The fact that we have not been able to enjoy live music in this way since the beginning of this pandemic made it even that much more special and extraordinary,” she told The Chronicle after the performance.San Francisco also requires proof of full vaccination for customers at indoor venues including restaurants, bars, gyms and other businesses.Breed told the Chronicle that she tests often for COVID-19 and she was reassured that the subterranean club was safe because people at the Black Cat need to show proof of vaccination to get in.Still, the August health order by San Francisco and other Bay Area counties requires people to wear “well-fitting mask indoors in public settings” regardless of vaccination status. The delta variant is so contagious that even inoculated people have been able to catch the virus and spread it to others.San Francisco and neighboring counties were the first to issue a stay-home order in March 2020, even before California Gov.Last year, Breed also was accused of hypocrisy when she attended a group dinner at the posh French Laundry restaurant in Napa in spite of strong recommendations by state and public health officials at the time to avoid gatherings with people outside the household.'

data= {
    's': content
}

request = json.loads(requests.post(url, data=data).content)["RewordifiedString"];
request = request.replace("%@", "");

print(request)
