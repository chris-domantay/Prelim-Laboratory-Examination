class Song:
    def __init__(self, songId, songTitle, artist, duration):
        self.songId = songId
        self.songTitle = songTitle
        self.artist = artist
        self.duration = duration

    def display(self):
        print("Song ID :", self.songId)
        print("Song Title:", self.songTitle)
        print("Artist    :", self.artist)
        print("Duration  :", self.duration)


class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    # Add song at the beginning
    def insertFirst(self, song):
        newNode = Node(song)

        newNode.next = self.head
        self.head = newNode

        self.count += 1

    # Add song at the end
    def insertLast(self, song):
        newNode = Node(song)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = newNode

        self.count += 1

    def insertAt(self, song, position):
        if position < 0 or position > self.count:
            return False

        if position == 0:
            self.insertFirst(song)
            return True

        newNode = Node(song)
        current = self.head

        for i in range(position - 1):
            current = current.next

        newNode.next = current.next
        current.next = newNode

        self.count += 1

        return True

    def search(self, songId):
        current = self.head

        while current is not None:
            if current.song.songId == songId:
                return current.song

            current = current.next

        return None

    def delete(self, songId):
        if self.head is None:
            return False

        if self.head.song.songId == songId:
            self.head = self.head.next
            self.count -= 1
            return True

        current = self.head

        while current.next is not None:
            if current.next.song.songId == songId:
                current.next = current.next.next
                self.count -= 1
                return True

            current = current.next

        return False

    def display(self):
        if self.head is None:
            print("\nPlaylist is empty.")
            return

        current = self.head

        print("\n========== PLAYLIST ==========")

        while current is not None:
            current.song.display()
            print("------------------------------")

            current = current.next

        print("Total Songs:", self.count)

    def size(self):
        return self.count

    def isEmpty(self):
        return self.head is None


def main():
    playlist = LinkedList()

    while True:
        print("\n================================")
        print("       MUSIC PLAYLIST MANAGER")
        print("================================")
        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            songId = input("Enter Song ID: ")
            songTitle = input("Enter Song Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration: ")

            song = Song(songId, songTitle, artist, duration)
            playlist.insertFirst(song)

            print("Song added at the beginning.")

        elif choice == "2":
            songId = input("Enter Song ID: ")
            songTitle = input("Enter Song Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration: ")

            song = Song(songId, songTitle, artist, duration)
            playlist.insertLast(song)

            print("Song added at the end.")

        elif choice == "3":
            songId = input("Enter Song ID: ")
            songTitle = input("Enter Song Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration: ")

            position = int(input("Enter Position: "))

            song = Song(songId, songTitle, artist, duration)

            if playlist.insertAt(song, position):
                print("Song inserted successfully.")
            else:
                print("Invalid position.")

        elif choice == "4":
            playlist.display()

        elif choice == "5":
            songId = input("Enter Song ID: ")

            song = playlist.search(songId)

            if song is not None:
                print("\nSong found!")
                print("------------------------------")
                song.display()
            else:
                print("Song not found.")

        elif choice == "6":
            songId = input("Enter Song ID: ")

            if playlist.delete(songId):
                print("Song removed successfully.")
            else:
                print("Song not found.")

        elif choice == "7":
            print("\nPlaylist Size:", playlist.size())

        elif choice == "8":
            print("\nExiting Music Playlist Manager...")
            break

        else:
            print("Invalid choice.")


main()