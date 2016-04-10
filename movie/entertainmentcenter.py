import fresh_tomatoes
import media

SWVII  = media.Movie("Star Wars Episode VII",
                     "The story begins thirty years after the events of Star Wars: Episode VI Return of the Jedi. The First Order has risen from the ashes of the Galactic Empire and is opposed by General Leia Organa and the Resistance, both of which seek to find the missing Jedi Master Luke Skywalker. In the midst of this search, new heroes rise in the form of Rey, a Force-sensitive scavenger from Jakku; Finn, a stormtrooper who defected from the First Order",
                     "http://vignette2.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_Awakens.jpg/revision/latest/scale-to-width-down/1000?cb=20151018162823",
                     "https://www.youtube.com/watch?v=sGbxmsDFVnE")


Revenant = media.Movie("The Revenent",
                       "A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team.",
                       "http://ia.media-imdb.com/images/M/MV5BMjU4NDExNDM1NF5BMl5BanBnXkFtZTgwMDIyMTgxNzE@._V1__SX1303_SY615_.jpg",
                       "https://www.youtube.com/watch?v=LoebZZ8K5N0")

Bm_vs_Sm = media.Movie("Batman Vs. Superman",
                       "Fearing that the actions of Superman are left unchecked, Batman takes on the Man of Steel, while the world wrestles with what kind of a hero it really needs.",
                       "https://s.yimg.com/ny/api/res/1.2/gyFqKB85n5rFl4e1SpvJDg--/YXBwaWQ9aGlnaGxhbmRlcjtzbT0xO3c9ODAwO2lsPXBsYW5l/http://l.yimg.com/cd/resizer/2.0/FIT_TO_WIDTH-w1280/08d16d4567f303c46f16a66041eca2f620352f4b.jpg",
                       "https://www.youtube.com/watch?v=xe1LrMqURuw")

#Bm_vs_Sm.show_trailer() 
                    
The_Martian = media.Movie("The Martian",
                          "Mark gets stuck on Mars, fights for survival, and is rescued by his former crewmates",
                          "http://www.bringhimhome.com/img/poster-full-page1.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")
#print(The_Martian.storyline)

Gravity = media.Movie("Gravity",
                      "A medical engineer and an astronaut work together to survive after an accident leaves them adrift in space.",
                      "http://cdn.collider.com/wp-content/uploads/gravity-poster.jpg",
                      "https://www.youtube.com/watch?v=xgGPTa7-vlE&nohtml5=False")
#print(Gravity.storyline)

Whiplash = media.Movie("Whiplash",
                       "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
                       "http://fanaru.com/whiplash/image/84241-whiplash-whiplash-poster-art.jpg",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo&nohtml5=False")
#print(Whiplash.storyline)

movies = [SWVII, Revenant, Bm_vs_Sm, The_Martian, Gravity, Whiplash]

fresh_tomatoes.open_movies_page(movies)


























                       
