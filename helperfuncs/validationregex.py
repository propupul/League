import regex

'''League of Legends Regular Expressions name check. This simple function allows you to avoid calling LoL's API by "rejecting inputs that don't match this regular expression (i.e., that contain any punctuation characters other than periods, underscores, and spaces)". Example if you enter: "immaqtpie@#$%" the name will be rejected and the function will return "None" Also please note that I'm using the "regex" module as opposed to using the "re", this is due to re's innability to support UNICODE options like "\p{L}"" there are ways around this using re but this IMHO is less of a hassle.'''


def pattern_check(user_name):
    pattern = regex.compile('^[0-9\p{L} _\.]+$')
    if pattern.match(user_name):
        print('Valid')
        return(user_name)
    else:
        return(None)

def region_check(region):
    ''' Enter the Region(Continent) '''
    # Future add
    pass

if __name__ == '__main__':
    main()
