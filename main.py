# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from  moviepy.editor import *

def print_hi():


    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    video = VideoFileClip('C:\\Users\\cruda\\Videos\\Captures\\green_grass.mp4').subclip(30,70)
    text = (TextClip('BlueGrass',fontsize=50,color='white')
        .set_position('center')
        .set_duration(10))
    result = CompositeVideoClip([video,text])
    result.write_videofile('cut.webm',fps=25)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
