class SystemAdmin:
    def __init__(self):  # file formats to store data written in front of attributes
        self.movie_lists = open("movie_lists.txt", 'a')  # movietitle,availableseats
        self.screens = open("screens.txt", 'a')  # screennumber
        self.timings = open("timings.txt", 'a')  # screennumber,timeslots

    def manage_movies(self, movie_title, available_seats):
        self.movie_lists.write(f"{movie_title},{available_seats}\n")

    def manage_screens(self, screen_number):
        self.screens.write(f"{screen_number}\n")

    def manage_timings(self, screen_number, timeslots):
        self.timings.write(f"{screen_number},{timeslots}\n")

    def save_files(self):
        self.movie_lists.close()
        self.screens.close()
        self.timings.close()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.booking_file = open(f"{username}_booking_receipt.txt", 'a+')  # a+ to open for read and append

    def select_movies(self, movie_title, date, screening_time):
        print(f"Selected movie: {movie_title}, Date: {date}, Time: {screening_time}")

    def choose_seats(self, number_of_seats):
        print(f"Selected seats: {number_of_seats}")

    def finalise_reservation(self):
        self.booking_file.seek(0)  # move pointer back to start of file
        print("Reservation Finalized!Here is the Booking receipt:")
        print(self.booking_file.read())  # print receipt
        self.booking_file.close()


class Movie:
    def __init__(self, title, available_seats):
        self.title = title
        self.available_seats = available_seats
        self.movie_booking_file = open(f"{self.title}_bookings", 'a')  # booking file for this specific movie

    def record_booking(self, booking_info):
        self.movie_booking_file.write(f"{booking_info}\n")
        print("Booking recorded!")


class Screen:
    def __init__(self, screen_number):
        self.screen_number = screen_number
        self.screen_timings_file = open(f"{screen_number}_timeslots.txt", 'a')

    def add_timeslot(self, timeslot):
        self.screen_timings_file.write(f"{timeslot}\n")
        print(f"Timeslot of {timeslot} added to Screen#{self.screen_number}!")


class Timeslot:
    def __init__(self, start_time, end_time):  # staring and ending time
        self.start = start_time
        self.end = end_time


class BookingDetails:
    def __init__(self, user, movie_name, screening_date, seats):
        self.user = user
        self.movie = movie_name
        self.date = screening_date
        self.seats = seats
        self.booking_id = ''

    def generate_booking_id(self, booking_id):
        self.booking_id = str(booking_id)


hamza = SystemAdmin()
hamza.manage_movies("fake movie 1", 20)
hamza.manage_screens(5)
hamza.manage_timings(5, "10:00-12:00")
hamza.save_files()

user = User("Hamza57", "abc123")
user.select_movies("fake movie 1", "10-05-2024", "10:00-12:00")
user.choose_seats(2)
user.finalise_reservation()

booking_details1 = BookingDetails(user.username, "fake movie 1", "10-05-2024", 2)
booking_details1.generate_booking_id(456321)

movie = Movie("fake movie 1", 20)
movie.record_booking("sample booking info 1")

screen = Screen(5)
screen.add_timeslot("10:00-12:00")
