from gtts import gTTS
from playsound import playsound
audio='speech.mp3'
sp=gTTS(text="Dolphins are regarded as the friendliest creatures in the sea and stories of them helping drowning sailors have been common since Roman times. The more we learn about dolphins, the more we realize that their society is more complex than people previously imagined. They look after other dolphins when they are ill, care for pregnant mothers and protect the weakest in the community, as we do. Some scientists have suggested that dolphins have a language but it is much more probable that they communicate with each other without needing words. Could any of these mammals be more intelligent than man? Certainly the most common argument in favor of man's superiority over them that we can kill them more easily than they can kill us is the least satisfactory. On the contrary, the more we discover about these remarkable creatures, the less we appear superior when we destroy them.")
sp.save(audio)
playsound(audio)
