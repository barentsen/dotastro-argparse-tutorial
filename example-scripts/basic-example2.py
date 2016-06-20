import argparse
parser = argparse.ArgumentParser(description='A tool that does nothing.')
parser.add_argument('name')
args = parser.parse_args()
print('Hello ' + args.name)

