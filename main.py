import media1
import movie_trailer_treasure_chest


# Movie selections and their respective information

ex_machina = media1.Movie("Ex Machina",
                          "https://goo.gl/hN2oWW",
                          "https://www.youtube.com/watch?v=bggUmgeMCdc")

children_of_men = media1.Movie("Children of Men",
                               "https://goo.gl/zrzhZ3",
                               "https://www.youtube.com/watch?v=2VT2apoX90o")

the_shawshank_redemption = media1.Movie("The Shawshank Redemption",
                                        "https://goo.gl/jHBdV3",
                                        "https://www.youtube.com/watch?v=WawU4ouldxU")

gangs_of_new_york = media1.Movie("Gangs of New York",
                                 "https://goo.gl/fLjpE1",
                                 "https://www.youtube.com/watch?v=1bjh979vVG0")

the_ghost_and_the_darkness = media1.Movie("The Ghost and the Darkness",
                                          "https://goo.gl/TQAVP4",
                                          "https://www.youtube.com/watch?v=1M38HWM4CTY")

the_hunt_for_red_october = media1.Movie("The Hunt for Red October",
                                        "https://goo.gl/154KQ7",
                                        "https://www.youtube.com/watch?v=kxL8uBmdulY")

gotg = media1.Movie("Guardians of the Galaxy",
                    "https://goo.gl/WeFfmL",
                    "https://www.youtube.com/watch?v=2XltzyLcu0g")

ghost_busters = media1.Movie("GhostBusters",
                             "https://goo.gl/WxGh4Q",
                             "https://www.youtube.com/watch?v=eowrFdpcRbs")

rogue_one = media1.Movie("Rogue One",
                         "https://goo.gl/aEFPb1",
                         "https://www.youtube.com/watch?v=frdj1zb9sMY")

interstellar = media1.Movie("Interstellar",
                            "https://goo.gl/wyLwW7",
                            "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

top_gun = media1.Movie("Top Gun",
                       "https://goo.gl/CwE7bA",
                       "https://www.youtube.com/watch?v=ioWpe3hdFH0&t=22s")

the_dark_knight = media1.Movie("The Dark Knight",
                               "https://goo.gl/JMd4JP",
                               "https://www.youtube.com/watch?v=EXeTwQWrcwY")

# List of movies being added to page

movies = [ex_machina, children_of_men, the_shawshank_redemption,
          gangs_of_new_york, the_ghost_and_the_darkness,
          the_hunt_for_red_october, gotg, ghost_busters,
          rogue_one, interstellar, top_gun, the_dark_knight]

# Sending of program to display on browser

movie_trailer_treasure_chest.open_movies_page(movies)
