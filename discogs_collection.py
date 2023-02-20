from collections import OrderedDict
from rich.console import Console
from rich.table import Table
import creds
import discogs_client

CONSOLE = Console()
USER_TOKEN = creds.user_token


def get_user_auth():
    user_client = discogs_client.Client('collection/0.1',
                                        user_token=USER_TOKEN)

    return user_client.identity()


def get_record_collection(user):
    record_collection = {}
    table = Table(title="Album Collection")
    table.add_column("Artist", justify="left", style="cyan")
    table.add_column("Album", justify="left", style="green")
    table.add_column("Format", justify="left", style="red")
    for item in user.collection_folders[0].releases:
        if item.release.artists[0].name in record_collection:
            record_collection[item.release.artists[0].name].update({
                item.release.title: ({
                    'format': item.release.formats[0]['name'],
                })
            })
        else:
            record_collection.update({
                item.release.artists[0].name: ({
                    item.release.title: ({
                        'format': item.release.formats[0]['name'],
                    })
                })
            })

    record_collection = OrderedDict(sorted(record_collection.items()))

    for artist_name, album_values in record_collection.items():
        for album_name, rformat in album_values.items():
            table.add_row(artist_name,
                          album_name,
                          rformat['format'])

    CONSOLE.print(table)
    CONSOLE.print(user.collection_folders[0].count)


def main():
    user = get_user_auth()
    get_record_collection(user)


if __name__ == '__main__':
    main()
