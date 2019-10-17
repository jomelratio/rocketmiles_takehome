"""
This test the search field on rocketmiles.com by validating all the items
found by entering all permutation of a two letter pattern.
Test 1: Validate the website is open successfully
Test 2: Validate search AA - ZZ permutation total search 676
"""

from TestFw.web_driver_fw import WebDriverFw
from TestFw.helper_function import HelperFunction

# Test chrome browser, to test other browser just pass in chrome, ie, firefox, safari
# for this exercise only supporting chrome
WEB_TEST = WebDriverFw('chrome')

# Open the browser under test and validate contents
WEB_TEST.open_website('https://www.rocketmiles.com/')

# TEST 1: validate web site is open by checking the title
# below gives an example of added feature to the framework
# provides the user case_sensitive option
WEB_TEST.validate_title("rocketmiles", False)
WEB_TEST.validate_title("Rocketmiles")

# close any pop up window
WEB_TEST.click_button_by_class_name("close")

# auto generate a-z list permutation by using helper function
HELPER_FUNC = HelperFunction()
SEARCH_LIST = HELPER_FUNC.auto_generate_two_letter_list('a')

# TEST 2: Execute a search based on SEARCH_LIST criteria by searching in upper case
RESULT_DICT_SEARCH_UPPER_CASE = {}
for location_begin_with in SEARCH_LIST:
    location_begin_with = location_begin_with.upper()
    search_hit_count = WEB_TEST.get_all_search_result('locationSearch', location_begin_with)
    RESULT_DICT_SEARCH_UPPER_CASE[location_begin_with] = search_hit_count
    print("."),

# TEST 3: Execute a search base on SEARCH_LIST criteria by searching in lower case
RESULT_DICT_SEARCH_LOWER_CASE = {}
for location_begin_with in SEARCH_LIST:
    location_begin_with = location_begin_with.lower()
    search_hit_count = WEB_TEST.get_all_search_result('locationSearch', location_begin_with)
    RESULT_DICT_SEARCH_LOWER_CASE[location_begin_with] = search_hit_count
    print("."),
WEB_TEST.close()
print("\n")

# Add pass fail criteria based on expected value
# for this demo, i am validating base on upper case result should equal lower case result
FAIL_COUNTER = 0
PASS_COUNTER = 0
for key, upper_case_val in RESULT_DICT_SEARCH_UPPER_CASE.iteritems():
    key_lc = key.lower()
    lower_case_val = RESULT_DICT_SEARCH_LOWER_CASE[key_lc]
    try:
        assert lower_case_val == upper_case_val, "FAIL: %s %s NOT EQUAL %s %s" \
                                                 % (key, upper_case_val, key_lc, lower_case_val)
    except AssertionError as fail_log:
        print(fail_log)
        FAIL_COUNTER += 1
    else:
        print("PASS: %s %s EQUAL %s %s" % (key, upper_case_val, key_lc, lower_case_val))
        PASS_COUNTER += 1

print("Summary: Total PASS %s Total Fail %s" % (PASS_COUNTER, FAIL_COUNTER))
