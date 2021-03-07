import imageio
import os

clip =os.path.abspath('./gif1.mp4')

def gif(inputpath ,target):
    outputPath = os.path.splitext(inputpath)[0]+target


    print(f'converting{inputpath}\n to {outputPath}')
    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath,fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frame {frames}')
    print ('done')
    writer.close()
gif(clip,'.gif')
