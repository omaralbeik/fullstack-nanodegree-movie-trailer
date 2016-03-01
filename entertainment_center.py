import fresh_tomatoes
import media

#Movies
up = media.Movie("UP",
"Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his home equipped with balloons, inadvertently taking a young stowaway.",
"https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
"https://www.youtube.com/watch?v=pkqzFUhGPJg",
"2009",
"1h 36min")

grown_ups = media.Movie("Grown Ups",
"After their high school basketball coach passes away, five good friends and former teammates reunite for a Fourth of July holiday weekend.",
"https://upload.wikimedia.org/wikipedia/en/f/fe/Grownupsmovie.jpg",
"https://www.youtube.com/watch?v=e01NVCveGkg",
"2010",
"1h 42min")

the_internship = media.Movie("The Internship",
"Two salesmen whose careers have been torpedoed by the digital age find their way into a coveted internship at Google, where they must compete with a group of young, tech-savvy geniuses for a shot at employment.",
"https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg",
"https://www.youtube.com/watch?v=cdnoqCViqUo",
"2013",
"1h 59min")


#TV Shows
breaking_bad = media.TVShow("Breaking Bad",
                            "A chemistry teacher diagnosed with terminal lung cancer teams up with his former student to cook and sell crystal meth.",
                            "https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png",
                            "https://www.youtube.com/watch?v=HhesaQXLuRY",
                            "2008–2013",
                            "5")

game_of_thrones = media.TVShow("Game of Thrones",
                            "While a civil war brews between several noble families in Westeros, the children of the former rulers of the land attempt to rise up to power. Meanwhile a forgotten race, bent on destruction, return after thousands of years in the North.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg",
                            "https://www.youtube.com/watch?v=IxI8aPISq8I",
                            "2011 -",
                            "6")


movies = [up, grown_ups, the_internship]
tv_shows = [breaking_bad, game_of_thrones]

fresh_tomatoes.open_movies_page(movies)
