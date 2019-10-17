from TestFw.web_driver_fw import *
from TestFw.helper_function import *


"""
This test the search field on rocketmiles.com by validating all the items found by entering all permutation 
of a two letter pattern.
Test 1: Validate the website is open successfully
Test 2: Validate search AA - ZZ permutation total search 676

"""

# Test chrome browser, to test other browser just pass in chrome, ie, firefox, safari
# for this exercise only supporting chrome
web_test = WebDriverFw('chrome')

# Open the browser under test and validate contents
web_test.open_website('https://www.rocketmiles.com/')

# TEST 1: validate web site is open by checking the title
# below gives an example of added feature to the framework
# provides the user case_sensitive option
web_test.validate_title("rocketmiles", False)
web_test.validate_title("Rocketmiles")

# close any pop up window
web_test.click_button_by_class_name("close")

# auto generate a-z list permutation by using helper function
helper_func = HelperFunction()
search_list = helper_func.auto_generate_two_letter_list('a')

# TEST 2: Execute a search based on search_list criteria by searching in upper case
result_dict_search_upper_case = {}
for location_begin_with in search_list:
    location_begin_with = location_begin_with.upper()
    search_hit_count = web_test.get_all_search_result('locationSearch', location_begin_with)
    result_dict_search_upper_case[location_begin_with] = search_hit_count
    print ("."),

# TEST 3: Execute a search base on search_list criteria by searching in lower case
result_dict_search_lower_case = {}
for location_begin_with in search_list:
    location_begin_with = location_begin_with.lower()
    search_hit_count = web_test.get_all_search_result('locationSearch', location_begin_with)
    result_dict_search_lower_case[location_begin_with] = search_hit_count
    print ("."),
web_test.close()
print ("\n")

# Add pass fail criteria based on expected value
# for this demo, i am validating base on upper case result should equal lower case result
for key, upper_case_val in result_dict_search_upper_case.iteritems():
    key_lc = key.lower()
    lower_case_val = result_dict_search_lower_case[key_lc]
    try:
        assert lower_case_val == upper_case_val, "FAIL: Expecting " + str(upper_case_val) + " got " + str(lower_case_val)
    except AssertionError as fail_log:
        print (fail_log)
    else:
        print ("PASS: expect " + str(upper_case_val) + " got " + str(lower_case_val))







