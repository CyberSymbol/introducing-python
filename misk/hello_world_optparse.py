import optparse
def main():
    p = optparse.OptionParser()
    p.add_option('--sysadmin', '-s', default="B0FH")
    options, arguments = p.parse_args()
    print('Hello, %s' % options.sysadmin)
if __name__ == '__main__':
    main()