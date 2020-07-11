from subprocess import Popen

def main():

    videoFiles = '''
    bandicam 2020-01-10 10-45-13-679.mp4
    bandicam 2020-01-06 11-01-35-020.mp4
    bandicam 2020-01-06 11-05-11-334.mp4
    '''

    for line in [x for x in videoFiles.splitlines() if '-' in x]:
        in_file = line.strip()
        out_file = line.strip().split('.')[0]+'_modified.mp4'
        args = fr"ffmpeg -i '/Users/lyndon/Documents/白月黑羽python/调用程序/{in_file}' -af asetrate='44100*8.9/10',atempo=10/8.9 -c:v copy '/Users/lyndon/Documents/白月黑羽python/调用程序/{out_file}'"
        print(args)
        proc = Popen(
            args = args,
            shell=True
            )
    proc.communicate()

if __name__ == '__main__':
    main()

