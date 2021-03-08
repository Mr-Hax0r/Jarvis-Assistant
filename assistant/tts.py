import subprocess
#import config
 
 
def output_command(text):
    if text == None:
        text = ''

    cmd = ['flite', '-voice', './model-flitevox/model-us.flitevox',
        '-t', text, '--setf', 'duration_stretch=1']
    subprocess.run(cmd)


            


