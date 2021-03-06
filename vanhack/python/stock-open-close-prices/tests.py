from open_close_prices_on_particular_days import week_day, get_data_from_month, openAndClosePrices

# Test week_day
sun, mon, tue, wed, thu, fri, sat = range(7)

assert(week_day(26, 8, 2019) == mon)
assert(week_day(27, 8, 2019) == tue)
assert(week_day(28, 8, 2019) == wed)
assert(week_day(29, 8, 2019) == thu)
assert(week_day(30, 8, 2019) == fri)
assert(week_day(31, 8, 2019) == sat)
assert(week_day(1, 9, 2019) == sun)
assert(week_day(23, 4, 2000) == sun)
assert(week_day(22, 7, 2000) == sat)
assert(week_day(17, 6, 2001) == sun)
assert(week_day(21, 9, 2001) == fri)
assert(week_day(6, 12, 2001) == thu)
assert(week_day(16, 6, 2002) == sun)
assert(week_day(15, 3, 2003) == sat)
assert(week_day(21, 9, 2003) == sun)
assert(week_day(16, 5, 2004) == sun)
assert(week_day(14, 1, 2005) == fri)
assert(week_day(9, 4, 2005) == sat)
assert(week_day(22, 12, 2006) == fri)
assert(week_day(23, 11, 2008) == sun)
assert(week_day(20, 1, 2009) == tue)
assert(week_day(1, 7, 2009) == wed)
assert(week_day(20, 7, 2009) == mon)
assert(week_day(16, 10, 2009) == fri)
assert(week_day(12, 12, 2009) == sat)
assert(week_day(26, 1, 2010) == tue)
assert(week_day(1, 12, 2010) == wed)
assert(week_day(31, 10, 2011) == mon)
assert(week_day(8, 1, 2012) == sun)
assert(week_day(16, 4, 2012) == mon)
assert(week_day(29, 9, 2012) == sat)
assert(week_day(12, 6, 2013) == wed)


# print(get_data_from_month(None, 2000))
openAndClosePrices('1-January-2000', '22-February-2000', 'Monday')
# openAndClosePrices('1-January-2000', '22-February-201', 'Monday')
