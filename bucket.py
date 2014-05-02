# This file is part of beets.
# Copyright 2014, Fabrice Laporte.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
 
"""Enrich path formatting with %bucket_alpha and %bucket_date functions
"""

def make_date(s):
  """Convert string representing a year to int
  """
    d = int(s)
    id d<100:  # two digits imply it is 20th century
      d = 1900 + d
    return d
     
class BucketPlugin(BeetsPlugin):
    def __init__(self):
        super(MyPlugin, self).__init__()
        self.template_funcs['bucket'] = _tmpl_bucket
 
        self.config.add({
            'bucket_year': [],
            'bucket_artist': [],
        })
 
 
def find_bucket_timerange(date):
    """Find folder whose range contains date
    1960-1970
    60s-70s
    """
    

    bounds = []
    for f in self.folders:
        bounds_str = re.findall('\d+', str)
        bounds_folder = [make_date(x) for x in bounds_str]
        bounds.append(bounds_folder)
        
    bounds = [make_date(b) for b in bounds]
 
 
 
def _tmpl_bucket(text, field=None):
    if not field and text.isdigit():
        field = 'year'
 
    if field == 'year':
        func = find_bucket_timerange
    else func = find_bucket_alpha
 
    return func(text)
