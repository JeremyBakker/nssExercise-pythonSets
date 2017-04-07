songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('The Wood Brothers', 'Postcards from Hell'),
    ('John Coltrane', 'A Love Supreme'),
    ('The Black Keys', 'The Lengths')
}

non_nickelback_songs = [song[1] for song in songs if song[0] is not 'Nickelback']
print(non_nickelback_songs)