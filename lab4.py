#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

FEDERAL_SALES_TAX_RATE = 0.0025
PROVINCIAL_SALES_TAX_RATE = 0.05
TOTAL_TAX_RATE = FEDERAL_SALES_TAX_RATE+PROVINCIAL_SALES_TAX_RATE
TOTAL_SALES_MULTIPLIER = 1 + TOTAL_TAX_RATE

def bill_of_sale(purchase):

    with open("output txt","w")as file_result:
        file_result.write("Amount of purchase:{0:2f}\n".format(purchase))
        file_result.write("Federal tax:{0:2f}\n".format(purchase*FEDERAL_SALES_TAX_RATE))
        file_result.write("Provincial tax:{0:2f}\n".format(purchase*PROVINCIAL_SALES_TAX_RATE))
        file_result.write("Total tax:{0:2f}\n".format(purchase*TOTAL_TAX_RATE))
        file_result.write("Total sale:{0:2f}\n".format(purchase*TOTAL_SALES_MULTIPLIER))

bill_of_sale(100)