# SQLite dont' come with python but you can bring in the module
# it is a tricky because it can connet python with SQLite databased. 
# second after speaking about SQLite we ll pass on SPATIAL

import sqlite3
## attento a .... R lib..... py.... conn = sqlite3.Connection('C:/Users/baldo/OneDrive/Documenti/R/win-library/3.6/BH/include/boost/python/tompkins.sqlite')
conn = sqlite3.Connection('C:/training/python/tompkins.sqlite')

# I haven't the table parcels.. so you have to change in another folder/table. this is just to show how i can do this
answer = conn.execute('SELECT * FROM parcels LIMIT 3')
answer
for row in answer:
    print (row)

answer = conn.execute('SELECT asmt FROM parcels LIMIT 3')
for row in answer:
    print (row)

answer = conn.execute('SELECT parcelkey, asmt FROM parcels LIMIT 3')
for row in answer:
    print (row)

### to comunicate with the computer and user    
import sqlite3
pkey = input ('enter your parcel key: ')
conn = sqlite3.Connection('C:/training/python/tompkins.sqlite')
answer = conn.execute('SELECT parcelkey, asmt FROM parcels where parcelkey = \'' + pkey + '\'') ## '\' command to see the special signs.
for row in answer:
    print (row)

##
import sqlite3
pkey = input ('enter your parcel key: ')
conn = sqlite3.Connection('C:/training/python/tompkins.sqlite')
answer = conn.execute('SELECT AVG(asmt), propclass FROM parcels GROUP BY propclass')
for row in answer:
    print (row)
    print ("Property Class", row[1], " $", row[0])

# sum to the assessed values ordered
#import sqlite3
conn = sqlite3.Connection('C:/training/python/tompkins.sqlite')
answer = conn.execute('SELECT AVG(asmt) AS sumasmt, propclass FROM parcels GROUP BY propclass ORDER BY sumasmt')
for row in answer:
    print (row)
    print ("Property Class", row[1], " $", row[0])
    
############################################################
###################   SECOND PART    #######################

## to import mod_spatialite

import os
os.chdir("C:/OSGeo4W64/bin")

import sqlite3
#pkey = input ('enter your parcel key: ')
conn = sqlite3.Connection('C:/training/python/tompkins.sqlite')
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("C:/OSGeo4W64/bin/mod_spatialite")')

answer = conn.execute('''SELECT sum(asmt) AS sumasmt, propclass
                      FROM parcels, floodzones
                      WHERE ST_Intersects(parcels.geometry, floodzones.geom)
                      AND floodzones.zone = 'A'
                      GROUP BY propclass ORDER BY sumasmt''')
for row in answer:
    print ("property Class", row[1], "$", row[0])









