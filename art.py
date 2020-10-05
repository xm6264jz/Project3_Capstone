import ui
from database import Artist, Artwork
import artstore


def add_artist():
    

    #Adds anew artist to the database
    name= ui.get_name('Enter the full name of the artist: ')
    name = name.title()
    email = ui.get_email(f'Enter email for {name}: ')
    try:
        artstore.add_artist(name,email)
    except:
        return('Error')
    
    

def add_artwork():
    #Adds anew artwork but checks for artist before adding
    artist_name = ui.get_name('Enter artist name: ')
    artstore.find_artist(artist_name)
    if artist_name:
        art_work = ui.get_name('Enter the artwork name: ')
        art_work =  art_work .title()
        price = ui.get_postive_float('Enter the price of the artwork: ')
    try:
        artstore.add_artwork(artist_name, art_work, price)
    except:
        return 'Error'    


def delete_art_work():
    #deletes artwork 
    name_of_artwork = ui.get_name('Enter the name of the artwork you want to delete: ')
    name_of_artwork = name_of_artwork.title()
    artstore.delete_artwork(name_of_artwork)


def show_all_artwork_by_one_artist():
    #this methods gets all artwork of one artist
    name = ui.get_non_empty_string('enter the name of artist the one you want to see his/her arts')
    artstore.get_all_artwork_of_artist(name)

def artwork_availability():
    #This method checks for artwork availability
    id = ui.get_artwork_id()
    
    art_available = ui.get_artwork_availability()
    artstore.change_availability_status(id, art_available)

def available_artwork_of_artist():
    name = ui.get_name('Enter artist name: ')
    art_available = ui.get_artwork_availability()
    artstore.get_artist_available_artwork(name, art_available)



   