from GovAnalytics.processors.JsonProcessor import JsonProcessor
from GovAnalytics.processors.SqlProcessor import SqlProcessor
from GovAnalytics.PathConstants import *


processor = SqlProcessor()

all_bills = JsonProcessor.get_all_bills(PathConstants.BILL_ROOT)

processor.load_counter("Bill", len(all_bills))

for bill in all_bills:
    processor.insert_bill(bill)

processor.report()
