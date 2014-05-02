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

from datetime import datetime

def make_date(s):
  """Convert string representing a year to int
  """
    d = int(s)
    id d<100:  # two digits imply it is 20th century
      d = 1900 + d
    return d
     
def make_range(self, ys):
    """Express year-span as a list of years [from...to].
       If input year-span only contain the from year, the to is defined
       as the from year of the next year-span minus one.
    """
    if len(ys) == 1: # miss upper bound
      lb_idx = self.yearbounds.index(ys[0])
      try:
        upper_bound = self.yearbounds(lb_idx + 1)
      except:
        upper_bound = datetime.now().year
      return (ys[0], upper_bound)
     
class BucketPlugin(BeetsPlugin):
    def __init__(self):
        super(MyPlugin, self).__init__()
        self.template_funcs['bucket'] = _tmpl_bucket
 
        self.config.add({
            'bucket_year': [],
            'bucket_artist': [],
        })
        
        yearspans = []
        # Extract years from strings
        for f in self.bucket_year:
            yearspan_str = re.findall('\d+', str)
            yearspan = tuple([make_date(x) for x in yearspan_str])
            yearspans.append(yearspan)
         
        self.yearbounds = sort([y for ys in yearspans for y in ys])   
        self.yearspans = [make_range(y) for y in yearspans]
     
 
def find_bucket_timerange(date):
    """Find folder whose range contains date
    1960-1970
    60s-70s
    """
    for (i, t) in enumerate(self.yearspans):
      if int(date) in t:
        return self.bucket_year[i]
    return date
        
        
def _tmpl_bucket(text, field=None):
    if not field and text.isdigit():
        field = 'year'
 
    if field == 'year':
        func = find_bucket_timerange
    else func = find_bucket_alpha
 
    return func(text)
