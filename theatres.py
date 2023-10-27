theatres = []
class Theatres:

    def __init__(self):
        self.theatres = theatres

    def display_theatres(self, movie):
        print("--------------------------------------------------------\n")
        for theatre in theatres:
            if movie in theatre.movies:
                print(theatre.theatre_id, '\t', theatre.theatre_name, '\t', theatre.location, '\t', theatre.rating)

    def select_theatre(self, selected_movie):
        self.display_theatres(selected_movie)
        theatre_id = int(input("\nEnter a theatre id:\n"))
        for theatre in self.theatres:
            if theatre.theatre_id == theatre_id and selected_movie in theatre.movies:
                return theatre.theatre_name
    
    def display_showtime(self, selected_theatre):
        print("--------------------------------------------------------\n")
        for theatre in self.theatres:
            if theatre.theatre_name == selected_theatre:
                [print(key, value) for key, value in theatre.show_time.items()]
        return [theatre.show_time for theatre in self.theatres if theatre.theatre_name == selected_theatre]

    def select_showtime(self, selected_theatre):
        show_time = self.display_showtime(selected_theatre)
        show_id = int(input("\nEnter the Show_id:\n"))
        print("--------------------------------------------------------\n")
        if show_id>0 and show_id<= 4: 
            return show_time[0][show_id]

         
            
class TheatresData:

    def __init__(self,theatre_id:int, theatre_name:str, location:str, rating:float, movies:list, show_time):
        self.theatre_id = theatre_id
        self.theatre_name = theatre_name
        self.location = location
        self.rating = rating
        self.movies = movies
        self.show_time = show_time

theatre1 = TheatresData(1, 'PVR Cinemas   ', 'Anna Nagar', 7.5, ['Leo       ', 'Por Thozhil', 'Good Night'], {1:'10:30AM',2:'02:00PM',3:'06:20PM',4:'10:15PM'})
theatre2 = TheatresData(2, 'AGS Cinemas   ', 'Villivakkam', 6.2, ['Leo       '], {1:'10:15AM',2:'01:45PM',3:'06:05PM',4:'09:45PM'})
theatre3 = TheatresData(3, 'Rohini Cinemas', 'Koyambedu', 6.8, ['Leo       ','Good Night'], {1:'10:45AM',2:'02:15PM',3:'06:00PM',4:'10:05PM'})

theatres.append(theatre1)
theatres.append(theatre2)
theatres.append(theatre3)