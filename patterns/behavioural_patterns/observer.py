# This design pattern is rather close to us, 
# we can can easily demonstrate it with our daily-life example.
# Take Youtube as an example, you are a user, and when you subscribe to a channel
# This action will let you recieve all kinds of notifications about new videos, new popular posts, etc.
# Which also means you are observe that channel to any updates.

class Subcriber:
    def __init__(self, name) -> None:
        self.name = name

    def on_new_video_added(self, message):
        # Notify user by sending mail to him/her, for instance
        print(message)


class Channel:
    def __init__(self, name) -> None:
        self.name = name
        self.subcribers = []
        self.videos = []

    def _notify_subcribers(self, action):
        for subcriber in self.subcribers:
            subcriber.on_new_video_added('{} has posted {}'.format(self.name, action))

    def add_subcriber(self, subcriber):
        self.subcribers.append(subcriber)

    def add_video(self, video):
        self.videos.append(video)
        self._notify_subcribers('NEW_VIDEO: {}'.format(video))
        

if __name__ == '__main__':
    subcriber = Subcriber('John')
    channel = Channel('DeveloperChannel')

    channel.add_subcriber(subcriber)

    channel.add_video('Python in 3000 hours') # DeveloperChannel has posted NEW_VIDEO: Python in 3000 hours
    channel.add_video('Design Pattern for dummy') # DeveloperChannel has posted NEW_VIDEO: Design Pattern for dummy
