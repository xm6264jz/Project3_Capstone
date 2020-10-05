
from database import Artist, Artwork





def add_artist(name, email):
    try:
        
      
        Artist(name = name, email = email).save()
       
        print("you added new name")
    #except IntegrityError as e:
        #raise ArtError('Error adding artist because' + str(e)) 
    except:
        print('not adding') 
        
def add_artwork(artist, artwork_name, price):
    try:
        artist_id = find_artist(artist)
        if artist_id:
            Artwork.create(artist = artist_id, artwork_name = artwork_name, price = price).save()
        
       
        print('art work added succesfully')
    #except IntegrityError as e:
       # raise ArtError('error adding artwork because' + str(e))
    except:
        print("art work not add")
      
def get_all_artwork_of_artist(name):

    """returns a list of all the ark work of an artist regardless of the availibility status

       """
    try:
        art_list = []
        for art in Artwork.select().join(Artist).where(Artist.name == name):
            art_list.append(art.artwork_name)

        return ', '.join(art_list)
    except:
        return 'No artwork found for this artist'    

def change_availability_status( artwork_available, id):

    """gets artwork by ID and updates it's availibility status. retuns 

    number of row updated """

    query = Artwork.update(available=artwork_available).where(Artwork.id == id)

    updated_rows = query.execute()

    return updated_rows

""" def display_avail_by_artist(artist,id):
    available_artwork = Artwork.select().where(Artwork.id == artist.id) and (Artwork.artwork_available)
    return list(available_artwork) """

def delete_artwork(artwork_name):
    rows_delete = Artwork.delete().where(Artwork.artwork_name==artwork_name).execute()
    if not rows_delete:
        print("art not deleted")
        

def show_all_artist():
    try:
        artists =Artist.select()
        return list(artists)
    except:
        return 'Error'


def artwork_search(name):
    artwork = Artwork.select().where(Artwork.artwork_name == name)
    return artwork

def find_artist(name):
    artist =Artist.get_or_none(Artist.name == name)
    if artist:
        return artist.id
