# Mirah Gordon
# Coding Challenge Submission 

# The following link defines On-Peak and Off-Peak hours used to price bulk electricity: https://help.misoenergy.org/knowledgebase/article/KA-01299/en-us.
# Note that these definitions are based on the “Hour Ending” time.
# For example, “Hour Ending 0100" refers to the hour from 12:00 through 1:00.

# Please define a function in Python which takes in an argument hour_starting of type datetime.datetime (see https://docs.python.org/3/library/datetime.html) and determines whether the 1-hour interval starting at time hour_starting is an On-Peak or Off-Peak hour. You may assume hour_starting is defined in EST. You may assume hour_starting is defined on the hour (i.e. hour_starting can be 1:00, but will not be 1:03). You may use third-party libraries. We are more concerned with your problem-solving approach than if your method works perfectly.

# imports
import datetime

# main function
def get_peak_status(hour_starting: datetime.datetime) -> str:
    """
    Determines whether the 1-hour interval starting at the given time is an On-Peak or Off-Peak hour

    Args:
        hour_starting (datetime.datetime): the starting time of the hour long interval defined on the hour, given in EST

    Returns:
        peak_status (str): a string of either 'On-Peak' or 'Off-Peak', representing the peak status of the interval 
    """

    # define the hour ending time based on the input time
    hour_ending = hour_starting + datetime.timedelta(hours=1)

    # check if the hour and day are contained in the definition of on-peak
    # on-peak : 0700 - 2200 hour ending time (inclusive), monday-friday 
    # off-peak : all times not defined as on-peak
    if 7 <= hour_ending.hour <= 22 and hour_ending.weekday() in (0, 1, 2, 3, 4):
        return 'On-Peak'
    
    return 'Off-Peak'

# unit tests to ensure that the correct peak status is returned 
# making sure to test edge cases 
import unittest

class TestPeakStatus(unittest.TestCase):
    # tests for on peak hours
    def test_on_peak(self):
        # create times to check
        on_peak_times = [
            datetime.datetime(2023, 6, 26, 7, 0, 0),  # Monday, 7:00 AM EST
            datetime.datetime(2023, 6, 27, 13, 0, 0),  # Tuesday, 1:00 PM EST
            datetime.datetime(2023, 6, 28, 21, 0, 0),  # Wednesday, 9:00 PM EST
            datetime.datetime(2023, 6, 29, 16, 0, 0),  # Thursday, 4:00 PM EST
            datetime.datetime(2023, 6, 30, 10, 0, 0)  # Friday, 10:00 AM EST
        ]

        # assert that they are on peak
        for time in on_peak_times:
            result = get_peak_status(time)
            self.assertEqual(result, 'On-Peak')


    # tests for off peak hours 
    def test_off_peak(self):
        off_peak_times = [
            datetime.datetime(2023, 6, 25, 8, 0, 0),  # Sunday, 8:00 AM EST
            datetime.datetime(2023, 6, 27, 22, 0, 0),  # Tuesday, 10:00 PM EST
            datetime.datetime(2023, 6, 30, 5, 0, 0)  # Friday, 5:00 AM EST
        ]

        for time in off_peak_times:
            result = get_peak_status(time)
            self.assertEqual(result, 'Off-Peak')


    # test for edge cases
    def test_edge_cases(self):
        start_time = datetime.datetime(2023, 6, 26, 6, 0, 0)  # Monday, 6:00 AM EST
        self.assertEqual(get_peak_status(start_time), 'On-Peak')

        start_time = datetime.datetime(2023, 6, 30, 22, 0, 0) # Friday, 10:00 PM EST
        self.assertEqual(get_peak_status(start_time), 'Off-Peak')

if __name__ == '__main__':
    unittest.main()
