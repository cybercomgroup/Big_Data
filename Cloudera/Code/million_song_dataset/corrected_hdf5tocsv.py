"""
Alexis Greenstreet (October 4, 2015) University of Wisconsin-Madison

This code is designed to convert the HDF5 files of the Million Song Dataset
to a CSV by extracting various song properties.

The script writes to a "SongCSV.csv" in the directory containing this script.

Please note that in the current form, this code only extracts the following
information from the HDF5 files:
AlbumID, AlbumName, ArtistID, ArtistLatitude, ArtistLocation,
ArtistLongitude, ArtistName, Danceability, Duration, KeySignature,
KeySignatureConfidence, SongID, Tempo, TimeSignature,
TimeSignatureConfidence, Title, and Year.

This file also requires the use of "hdf5_getters.py", written by
Thierry Bertin-Mahieux (2010) at Columbia University

Credit:
This HDF5 to CSV code makes use of the following example code provided
at the Million Song Dataset website
(Home>Tutorial/Iterate Over All Songs,
http://labrosa.ee.columbia.edu/millionsong/pages/iterate-over-all-songs),
Which gives users the following code to get all song titles:

import os
import glob
import hdf5_getters
def get_all_titles(basedir,ext='.h5') :
    titles = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            titles.append( hdf5_getters.get_title(h5) )
            h5.close()
    return titles
"""

import sys
import os
import glob
import hdf5_getters
import re

class Song:
    songCount = 0
    # songDictionary = {}

    def __init__(self, songID):
        self.id = songID
        Song.songCount += 1
        # Song.songDictionary[songID] = se

        self.albumName = None
        self.albumID = None
        self.artistID = None
        self.artistLatitude = None
        self.artistLocation = None
        self.artistLongitude = None
        self.artistName = None
        self.danceability = None
        self.duration = None
        # self.genreList = []
        self.keySignature = None
        self.keySignatureConfidence = None
        self.lyrics = None
        self.popularity = None
        self.tempo = None
        self.timeSignature = None
        self.timeSignatureConfidence = None
        self.title = None
        self.year = None
        ##########Added by us!
        self.familiarity = None
        self.artist_mbid = None
        self.artist_playmeid = None
        self.artist_7digid = None
        self.hottness = None
        self.song_hottness = None
        self.digitalid7 = None
        #self.similar_artists = None
        #self.artist_terms = None
        #self.art_terms_freq = None
        #self.art_terms_weight = None
        self.a_sample_rate = None
        self.audio_md5 = None
        self.end_of_fade_in = None
        self.energy = None
        self.loudness = None
        self.mode = None
        self.mode_conf = None
        self.start_of_fade_out = None
        self.trackid = None
        #self.segm_start = None
        #self.segm_conf = None
        #self.segm_pitch = None
        #self.segm_timbre = None
        #self.segm_max_loud = None
        #self.segm_max_loud_time = None
        #self.segm_loud_start = None
        #self.sect_start = None
        #self.sect_conf = None
        #self.beats_start = None
        #self.beats_conf = None
        #self.bars_start = None
        #self.bars_conf = None
        #self.tatums_start = None
        #self.tatums_conf = None
        #self.artist_mbtags = None
        #self.artist_mbtags_count = None

    def displaySongCount(self):
        print ("Total Song Count %i" % Song.songCount)

    def displaySong(self):
        print ("ID: %s" % self.id)


def main():
    outputFile1 = open('SongCSV.csv', 'w')
    csvRowString = ""

    #################################################
    #if you want to prompt the user for the order of attributes in the csv,
    #leave the prompt boolean set to True
    #else, set 'prompt' to False and set the order of attributes in the 'else'
    #clause
    prompt = False
    #################################################
    if prompt == True:
        while prompt:

            prompt = False

            csvAttributeString = raw_input("\n\nIn what order would you like the colums of the CSV file?\n" +
                "Please delineate with commas. The options are: " +
                "AlbumName, AlbumID, ArtistID, ArtistLatitude, ArtistLocation, ArtistLongitude,"+
                " ArtistName, Danceability, Duration, KeySignature, KeySignatureConfidence, Tempo," +
                " SongID, TimeSignature, TimeSignatureConfidence, Title, and Year.\n\n" +
                "For example, you may write \"Title, Tempo, Duration\"...\n\n" +
                "...or exit by typing 'exit'.\n\n")

            csvAttributeList = re.split('\W+', csvAttributeString)
            for i, v in enumerate(csvAttributeList):
                csvAttributeList[i] = csvAttributeList[i].lower()

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"


                if attribute == 'AlbumID'.lower():
                    csvRowString += 'AlbumID'
                elif attribute == 'AlbumName'.lower():
                    csvRowString += 'AlbumName'
                elif attribute == 'ArtistID'.lower():
                    csvRowString += 'ArtistID'
                elif attribute == 'ArtistLatitude'.lower():
                    csvRowString += 'ArtistLatitude'
                elif attribute == 'ArtistLocation'.lower():
                    csvRowString += 'ArtistLocation'
                elif attribute == 'ArtistLongitude'.lower():
                    csvRowString += 'ArtistLongitude'
                elif attribute == 'ArtistName'.lower():
                    csvRowString += 'ArtistName'
                elif attribute == 'Danceability'.lower():
                    csvRowString += 'Danceability'
                elif attribute == 'Duration'.lower():
                    csvRowString += 'Duration'
                elif attribute == 'KeySignature'.lower():
                    csvRowString += 'KeySignature'
                elif attribute == 'KeySignatureConfidence'.lower():
                    csvRowString += 'KeySignatureConfidence'
                elif attribute == 'SongID'.lower():
                    csvRowString += "SongID"
                elif attribute == 'Tempo'.lower():
                    csvRowString += 'Tempo'
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += 'TimeSignature'
                elif attribute == 'TimeSignatureConfidence'.lower():
                    csvRowString += 'TimeSignatureConfidence'
                elif attribute == 'Title'.lower():
                    csvRowString += 'Title'
                elif attribute == 'Year'.lower():
                    csvRowString += 'Year'
                elif attribute == 'Familiarity'.lower():                        ####Added by us!
                    csvRowString += song.familiarity
                elif attribute == 'artist_mbid'.lower():
                    csvRowString += song.artist_mbid
                elif attribute == 'artist_playmeid'.lower():
                    csvRowString += song.artist_playmeid
                elif attribute == 'artist_7digid'.lower():
                    csvRowString += song.artist_7digid
                elif attribute == 'hottness'.lower():
                    csvRowString += song.hottness
                elif attribute == 'song_hottness'.lower():
                    csvRowString += song.song_hottness
                elif attribute == 'digitalid7'.lower():
                    csvRowString += song.digitalid7
                elif attribute == 'similar_artists'.lower():
                    csvRowString += song.similar_artists
                elif attribute == 'artist_terms'.lower():
                    csvRowString += song.artist_terms
                elif attribute == 'art_terms_freq'.lower():
                    csvRowString += song.art_terms_freq
                elif attribute == 'art_terms_weight'.lower():
                    csvRowString += song.art_terms_weight
                elif attribute == 'a_sample_rate'.lower():
                    csvRowString += song.a_sample_rate
                elif attribute == 'audio_md5'.lower():
                    csvRowString += song.audio_md5
                elif attribute == 'end_of_fade_in'.lower():
                    csvRowString += song.end_of_fade_in
                elif attribute == 'energy'.lower():
                    csvRowString += song.energy
                elif attribute == 'loudness'.lower():
                    csvRowString += song.loudness
                elif attribute == 'mode'.lower():
                    csvRowString += song.mode
                elif attribute == 'mode_conf'.lower():
                    csvRowString += song.mode_conf
                elif attribute == 'start_of_fade_out'.lower():
                    csvRowString += song.start_of_fade_out
                elif attribute == 'trackid'.lower():
                    csvRowString += song.trackid
                elif attribute == 'segm_start'.lower():
                    csvRowString += song.segm_start
                elif attribute == 'segm_conf'.lower():
                    csvRowString += song.segm_conf
                elif attribute == 'segm_pitch'.lower():
                    csvRowString += song.segm_pitch
                elif attribute == 'segm_timbre'.lower():
                    csvRowString += song.segm_timbre
                elif attribute == 'segm_max_loud'.lower():
                    csvRowString += song.segm_max_loud
                elif attribute == 'segm_max_loud_time'.lower():
                    csvRowString += song.segm_max_loud_time
                elif attribute == 'segm_loud_start'.lower():
                    csvRowString += song.segm_loud_start
                elif attribute == 'sect_start'.lower():
                    csvRowString += song.sect_start
                elif attribute == 'sect_conf'.lower():
                    csvRowString += song.sect_conf
                elif attribute == 'beats_start'.lower():
                    csvRowString += song.beats_start
                elif attribute == 'beats_conf'.lower():
                    csvRowString += song.beats_conf
                elif attribute == 'bars_start'.lower():
                    csvRowString += song.bars_start
                elif attribute == 'bars_conf'.lower():
                    csvRowString += song.bars_conf
                elif attribute == 'tatums_start'.lower():
                    csvRowString += song.tatums_start
                elif attribute == 'tatums_conf'.lower():
                    csvRowString += song.tatums_conf
                elif attribute == 'artist_mbtags'.lower():
                    csvRowString += song.artist_mbtags
                elif attribute == 'artist_mbtags_count'.lower():
                    csvRowString += song.artist_mbtags_count
                elif attribute == 'Exit'.lower():
                    sys.exit()
                else:
                    prompt = True
                    print( "==============")
                    print( "I believe there has been an error with the input.")
                    print( "==============")
                    break

                csvRowString += ","

            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString);
            csvRowString = ""
    #else, if you want to hard code the order of the csv file and not prompt
    #the user,
    else:
        #################################################
        #change the order of the csv file here
        #Default is to list all available attributes (in alphabetical order)
        csvRowString = "SongID,AlbumID,AlbumName,ArtistID,ArtistLatitude,ArtistLocation,ArtistLongitude,ArtistName,Danceability,Duration,KeySignature,KeySignatureConfidence,Tempo,TimeSignature,TimeSignatureConfidence,Title,Year,Familiarity,Artist_Mbid,Artist_PlaymeId,Artist_7didId,Hottness,Song_Hottness,7digitalid,A_Sample_Rate,Audio_Md5,End_Of_Fade_In,Energy,Loudness,Mode,Mode_Conf,Start_Of_Fade_Out,TrackId"
        #################################################

        csvAttributeList = re.split(',', csvRowString)
        for i, v in enumerate(csvAttributeList):
            csvAttributeList[i] = csvAttributeList[i].lower()
        csvRowString += "\n"
        outputFile1.write(csvRowString);
        csvRowString = ""

    #################################################


    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    basedir = "/home/bigdata/smalltest/" # "." As the default means the current directory
    ext = ".h5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    #FOR LOOP
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            print(f)

            songH5File = hdf5_getters.open_h5_file_read(f)
            song = Song(str(hdf5_getters.get_song_id(songH5File)))

            # testDanceability = hdf5_getters.get_danceability(songH5File)
            # print type(testDanceability)
            # print ("Here is the danceability: ") + str(testDanceability)

            song.artistID = str(hdf5_getters.get_artist_id(songH5File))
            song.albumID = str(hdf5_getters.get_release_7digitalid(songH5File))
            song.albumName = str(hdf5_getters.get_release(songH5File))
            song.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
            song.artistLocation = str(hdf5_getters.get_artist_location(songH5File))
            song.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File))
            song.artistName = str(hdf5_getters.get_artist_name(songH5File))
            song.danceability = str(hdf5_getters.get_danceability(songH5File))
            song.duration = str(hdf5_getters.get_duration(songH5File))
            # song.setGenreList()
            song.keySignature = str(hdf5_getters.get_key(songH5File))
            song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File))
            # song.lyrics = None
            # song.popularity = None
            song.tempo = str(hdf5_getters.get_tempo(songH5File))
            song.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
            song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
            song.title = str(hdf5_getters.get_title(songH5File))
            song.year = str(hdf5_getters.get_year(songH5File))

            #########Added by us!
            song.familiarity = str(hdf5_getters.get_artist_familiarity(songH5File))
            song.artist_mbid = str(hdf5_getters.get_artist_mbid(songH5File))
            song.artist_playmeid = str(hdf5_getters.get_artist_playmeid(songH5File))
            song.artist_7digid = str(hdf5_getters.get_artist_7digitalid(songH5File))
            song.hottness = str(hdf5_getters.get_artist_hotttnesss(songH5File))
            song.song_hottness = str(hdf5_getters.get_song_hotttnesss(songH5File))
            song.digitalid7 = str(hdf5_getters.get_track_7digitalid(songH5File))
            #song.similar_artists = str(hdf5_getters.get_similar_artists(songH5File))
            #song.artist_terms = str(hdf5_getters.get_artist_terms(songH5File))
            #song.art_terms_freq = str(hdf5_getters.get_artist_terms_freq(songH5File))
            #song.art_terms_weight = str(hdf5_getters.get_artist_terms_weight(songH5File))
            song.a_sample_rate = str(hdf5_getters.get_analysis_sample_rate(songH5File))
            song.audio_md5 = str(hdf5_getters.get_audio_md5(songH5File))
            song.end_of_fade_in = str(hdf5_getters.get_end_of_fade_in(songH5File))
            song.energy = str(hdf5_getters.get_energy(songH5File))
            song.loudness = str(hdf5_getters.get_loudness(songH5File))
            song.mode = str(hdf5_getters.get_mode(songH5File))
            song.mode_conf = str(hdf5_getters.get_mode_confidence(songH5File))
            song.start_of_fade_out = str(hdf5_getters.get_start_of_fade_out(songH5File))
            song.trackid = str(hdf5_getters.get_track_id(songH5File))
            #song.segm_start = str(hdf5_getters.get_segments_start(songH5File))
            #song.segm_conf = str(hdf5_getters.get_segments_confidence(songH5File))
            #song.segm_pitch = str(hdf5_getters.get_segments_pitches(songH5File))
            #song.segm_timbre = str(hdf5_getters.get_segments_timbre(songH5File))
            #song.segm_max_loud = str(hdf5_getters.get_segments_loudness_max(songH5File))
            #song.segm_max_loud_time = str(hdf5_getters.get_segments_loudness_max_time(songH5File))
            #song.segm_loud_start = str(hdf5_getters.get_segments_loudness_start(songH5File))
            #song.sect_start = str(hdf5_getters.get_sections_start(songH5File))
            #song.sect_conf = str(hdf5_getters.get_sections_confidence(songH5File))
            #song.beats_start = str(hdf5_getters.get_beats_start(songH5File))
            #song.beats_conf = str(hdf5_getters.get_beats_confidence(songH5File))
            #song.bars_start = str(hdf5_getters.get_bars_start(songH5File))
            #song.bars_conf = str(hdf5_getters.get_bars_confidence(songH5File))
            #song.tatums_start = str(hdf5_getters.get_tatums_start(songH5File))
            #song.tatums_conf = str(hdf5_getters.get_tatums_confidence(songH5File))
            #song.artist_mbtags = str(hdf5_getters.get_artist_mbtags(songH5File))
            #song.artist_mbtags_count = str(hdf5_getters.get_artist_mbtags_count(songH5File))

            #print song count
            #csvRowString += str(song.songCount) + ","

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"

                if attribute == 'AlbumID'.lower():
                    csvRowString += song.albumID
                elif attribute == 'AlbumName'.lower():
                    albumName = song.albumName
                    albumName = albumName.replace("b\"", "")
                    albumName = albumName.replace("\"", "")
                    albumName = albumName.replace(',',"")
                    csvRowString += "\"" + albumName + "\""
                elif attribute == 'ArtistID'.lower():
                    csvRowString += "\"" + song.artistID + "\""
                elif attribute == 'ArtistLatitude'.lower():
                    latitude = song.artistLatitude
                    if latitude == 'nan':
                        latitude = ''
                    csvRowString += latitude
                elif attribute == 'ArtistLocation'.lower():
                    location = song.artistLocation
                    location = location.replace(',','')
                    location = location.replace("b\"", "")
                    location = location.replace("\"", "")
                    csvRowString += "\"" + location + "\""
                elif attribute == 'ArtistLongitude'.lower():
                    longitude = song.artistLongitude
                    if longitude == 'nan':
                        longitude = ''
                    csvRowString += longitude
                elif attribute == 'ArtistName'.lower():
                    artistName = song.artistName
                    artistName = artistName.replace("b\"", "")
                    artistName = artistName.replace("\"", "")
                    csvRowString += "\"" + artistName + "\""
                elif attribute == 'Danceability'.lower():
                    csvRowString += song.danceability
                elif attribute == 'Duration'.lower():
                    csvRowString += song.duration
                elif attribute == 'KeySignature'.lower():
                    csvRowString += song.keySignature
                elif attribute == 'KeySignatureConfidence'.lower():
                    # print "key sig conf: " + song.timeSignatureConfidence
                    csvRowString += song.keySignatureConfidence
                elif attribute == 'SongID'.lower():
                    csvRowString += "\"" + song.id + "\""
                elif attribute == 'Tempo'.lower():
                    # print "Tempo: " + song.tempo
                    csvRowString += song.tempo
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += song.timeSignature
                elif attribute == 'TimeSignatureConfidence'.lower():
                    # print "time sig conf: " + song.timeSignatureConfidence
                    csvRowString += song.timeSignatureConfidence
                elif attribute == 'Title'.lower():
                    t = song.title
                    t = t.replace("b\"", "")
                    t = t.replace("\"", "")
                    csvRowString += "\"" + t + "\""
                elif attribute == 'Year'.lower():
                    csvRowString += song.year
                elif attribute == 'Familiarity'.lower():                        ####Added by us!
                    csvRowString += song.familiarity
                elif attribute == 'artist_mbid'.lower():
                    csvRowString += "\"" + song.artist_mbid + "\""
                elif attribute == 'artist_playmeid'.lower():
                    csvRowString += song.artist_playmeid
                elif attribute == 'artist_7digid'.lower():
                    csvRowString += song.artist_7digid
                elif attribute == 'hottness'.lower():
                    csvRowString += song.hottness
                elif attribute == 'song_hottness'.lower():
                    csvRowString += song.song_hottness
                elif attribute == 'digitalid7'.lower():
                    csvRowString += song.digitalid7
                elif attribute == 'similar_artists'.lower():
                    csvRowString += song.similar_artists
                elif attribute == 'artist_terms'.lower():
                    csvRowString += song.artist_terms
                elif attribute == 'art_terms_freq'.lower():
                    csvRowString += song.art_terms_freq
                elif attribute == 'art_terms_weight'.lower():
                    csvRowString += song.art_terms_weight
                elif attribute == 'a_sample_rate'.lower():
                    csvRowString += song.a_sample_rate
                elif attribute == 'audio_md5'.lower():
                    csvRowString += "\"" + song.audio_md5 + "\""
                elif attribute == 'end_of_fade_in'.lower():
                    csvRowString += song.end_of_fade_in
                elif attribute == 'energy'.lower():
                    csvRowString += song.energy
                elif attribute == 'loudness'.lower():
                    csvRowString += song.loudness
                elif attribute == 'mode'.lower():
                    csvRowString += song.mode
                elif attribute == 'mode_conf'.lower():
                    csvRowString += song.mode_conf
                elif attribute == 'start_of_fade_out'.lower():
                    csvRowString += song.start_of_fade_out
                elif attribute == 'trackid'.lower():
                    csvRowString += "\"" + song.trackid + "\""
                elif attribute == 'segm_start'.lower():
                    csvRowString += song.segm_start
                elif attribute == 'segm_conf'.lower():
                    csvRowString += song.segm_conf
                elif attribute == 'segm_pitch'.lower():
                    csvRowString += song.segm_pitch
                elif attribute == 'segm_timbre'.lower():
                    csvRowString += song.segm_timbre
                elif attribute == 'segm_max_loud'.lower():
                    csvRowString += song.segm_max_loud
                elif attribute == 'segm_max_loud_time'.lower():
                    csvRowString += song.segm_max_loud_time
                elif attribute == 'segm_loud_start'.lower():
                    csvRowString += song.segm_loud_start
                elif attribute == 'sect_start'.lower():
                    csvRowString += song.sect_start
                elif attribute == 'sect_conf'.lower():
                    csvRowString += song.sect_conf
                elif attribute == 'beats_start'.lower():
                    csvRowString += song.beats_start
                elif attribute == 'beats_conf'.lower():
                    csvRowString += song.beats_conf
                elif attribute == 'bars_start'.lower():
                    csvRowString += song.bars_start
                elif attribute == 'bars_conf'.lower():
                    csvRowString += song.bars_conf
                elif attribute == 'tatums_start'.lower():
                    csvRowString += song.tatums_start
                elif attribute == 'tatums_conf'.lower():
                    csvRowString += song.tatums_conf
                elif attribute == 'artist_mbtags'.lower():
                    csvRowString += song.artist_mbtags
                elif attribute == 'artist_mbtags_count'.lower():
                    csvRowString += song.artist_mbtags_count
                else:
                    csvRowString += "\"ERR\""

                csvRowString += ","

            #Remove the final comma from each row in the csv
            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""

            songH5File.close()

    outputFile1.close()

main()
