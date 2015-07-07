import glob
import os

# print(os.getcwdu())
for fpath in glob.glob('u_ex*.log'):
    # print(f)
    print('start to read contents of ' + fpath)
    with open(fpath) as f:
        lines = f.readlines()
        print('{0} has {1} lines'.format(fpath, len(lines)))
        service_calls = [l for l in lines if '/service' in l]
        print('{0} has {1} service calls'.format(fpath, len(service_calls)))

        with open('parsed_' + fpath, 'w') as fwrite:
            fwrite.writelines(service_calls)