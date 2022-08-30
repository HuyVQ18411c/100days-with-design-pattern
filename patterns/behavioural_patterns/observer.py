# This design pattern is rather close to us, 
# we can can easily demonstrate it with our daily-life example.
# Take Youtube as an example, you are a user, and when you subscribe to a channel
# This action will let you recieve all kinds of notifications about new videos, new popular posts, etc.
# Which also means you are observe that channel to any updates.

class Subcriber:
    def __init__(self, name) -> None:
        self.name = name

    def subscribe(self, channel):
        channel.add_subcriber(self)

    def unsubcribe(self, channel):
        channel.remove_subscriber(self)

    def on_new_video_added(self, message):
        # Notify user by sending mail to him/her, for instance
        print("Sending notification: {} to {}".format(message, self.name))


class Channel:
    def __init__(self, name) -> None:
        self.name = name
        self.subcribers = []
        self.videos = []

    def _notify_subcribers(self, action):
        for subcriber in self.subcribers:
            subcriber.on_new_video_added('{} has posted {}'.format(self.name, action))

    def add_subcriber(self, subcriber):
        if subcriber not in self.subcribers:
            self.subcribers.append(subcriber)

    def remove_subscriber(self, subcriber):
        if subcriber in self.subcribers:
            self.subcribers.remove(subcriber)

    def add_video(self, video):
        self.videos.append(video)
        self._notify_subcribers('NEW_VIDEO: {}'.format(video))
        

if __name__ == '__main__':
    subcriber_john = Subcriber('John')
    subcriber_lena = Subcriber('Lena')
    channel = Channel('DeveloperChannel')

    subcriber_john.subscribe(channel)
    subcriber_lena.subscribe(channel)

    channel.add_video('Python in 3000 hours') 
    # Sending notification: DeveloperChannel has posted NEW_VIDEO: Python in 3000 hours to John
    # Sending notification: DeveloperChannel has posted NEW_VIDEO: Python in 3000 hours to Lena
    
    subcriber_john.unsubcribe(channel) # Bye John :(

    channel.add_video('Design Pattern for dummy')
    # Sending notification: DeveloperChannel has posted NEW_VIDEO: Design Pattern for dummy to Lena
