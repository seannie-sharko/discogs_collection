#### This is a simple Python script that pulls your record collection from Discogs and displays it in a table using [python3-discogs-client](https://python3-discogs-client.readthedocs.io/en/latest/index.html#).

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━┓
┃ Artist                                                        ┃ Album                                                                                             ┃ Year ┃ Format    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━━━┩
│ ...And You Will Know Us By The Trail Of Dead                  │ Source Tags & Codes                                                                               │ 2017 │ Vinyl     │
│ A Perfect Circle                                              │ Mer De Noms                                                                                       │ 2020 │ Vinyl     │
│ Agoraphobic Nosebleed                                         │ Altered States Of America / ANBRX II Delta 9                                                      │ 2016 │ Vinyl     │
│ Alice In Chains                                               │ Dirt                                                                                              │ 2022 │ Vinyl     │
│ Anthony Green (6)                                             │ Pixie Queen                                                                                       │ 2016 │ Vinyl     │
│ Arcade Fire                                                   │ We                                                                                                │ 2022 │ Vinyl     │
│ Arcade Fire                                                   │ No Cars Go - Surf City Eastern Bloc                                                               │ 2007 │ Vinyl     │
│ Arcade Fire                                                   │ The Suburbs / Month Of May                                                                        │ 2010 │ Vinyl     │
│ Arcade Fire                                                   │ The Suburbs                                                                                       │ 2010 │ Vinyl     │
│ Arcade Fire                                                   │ Reflektor                                                                                         │ 2013 │ Vinyl     │
│ Arcade Fire                                                   │ Neon Bible                                                                                        │ 2017 │ Vinyl     │
│ Arcade Fire                                                   │ Her                                                                                               │ 2021 │ Vinyl     │
│ Arcade Fire                                                   │ Everything Now                                                                                    │ 2017 │ Vinyl     │
│ Arcade Fire                                                   │ Funeral                                                                                           │ 2017 │ Vinyl     │
│ Asobi Seksu                                                   │ Citrus                                                                                            │ 2009 │ Vinyl     │
│ At The Drive-In                                               │ in•ter a•li•a                                                                                     │ 2017 │ Vinyl     │
│ At The Drive-In                                               │ Relationship Of Command                                                                           │ 2013 │ Vinyl     │
│ Azure Ray                                                     │ Hold On Love                                                                                      │ 2003 │ Vinyl     │
│ Band Of Horses                                                │ Things Are Great                                                                                  │ 2022 │ Vinyl     │
│ Band Of Horses                                                │ Everything All The Time                                                                           │ 2006 │ Vinyl     │
│ Bat For Lashes                                                │ Lost Girls                                                                                        │ 2019 │ Vinyl     │
│ Beach House                                                   │ Devotion                                                                                          │ 2008 │ Vinyl     │
│ Beach House                                                   │ Once Twice Melody                                                                                 │ 2022 │ Vinyl     │
```
## Requirements:
- Discogs account
- Create an API token [here](https://www.discogs.com/settings/developers)
- pip install -r requirements.txt
```
pip install discogs_client
```
## Setup & Install:

```
- Create your token and replace it in creds.py
```
## Running:
```
cd discogs_collection
python discogs_collection.py
```
